import tkinter as tk
from tkinter import ttk

from mysqlConnection import ConnectionToMySQl
from table import TableTkinter
from model import *


class TableGUI():
	def __init__(self, window, model):
		style = ttk.Style()
		style.configure("mystyle.Treeview", 
						highlightthickness=3, 
						bd=1, font=('Calibri', 11), 
						foreground='blue', 
						rowheight=40
		)
		style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 12,'bold'))

		self.model = model
		self.window = window

		self.defaultStatement = f'select * from {self.model.tableName}'

		# Label frames to hold component
		self.tableFrame = tk.LabelFrame(self.window, text=self.model.tableName)

		# Table and its crollbar component
		self.trv = ttk.Treeview(self.tableFrame, show="headings", height="7", style="mystyle.Treeview")
		self.vsb = ttk.Scrollbar(self.tableFrame, orient="vertical", command=self.trv.yview)

		self.updateData(self.defaultStatement)

		# Searchbar
		self.searchBtn = tk.Button(self.tableFrame, bg='green', fg='white', text='Search', command=self.search)
		self.searchInput = tk.Entry(self.tableFrame)
		self.searchTopic = tk.StringVar()
		self.searchTopic.set(self.columns[1])
		self.filterDropDown = tk.OptionMenu(self.tableFrame, self.searchTopic, *self.columns)

		# order by topic
		self.orderLb = tk.Label(self.tableFrame, bg='black', fg='white', text='Order By')
		# self.orderLb.place(relx=0.78, rely=0.05, relwidth=0.075, relheight=0.05)

		self.orderByTopic = tk.StringVar()
		self.orderByTopic.set(self.columns[1])
		self.orderDropdown = tk.OptionMenu(self.tableFrame, self.orderByTopic, *self.columns)
		# self.orderDropdown.place(relx=0.85, rely=0.05, relwidth=0.12, relheight=0.05)


	def updateData(self, statement):
		self.trv.delete(*self.trv.get_children())

		mysqlConn = ConnectionToMySQl()
		self.rows = mysqlConn.getQueryset(statement)
		self.columns = mysqlConn.cursor.column_names

		for data in self.rows:
			self.trv.insert('', 'end', values=data)

	def createGUI(self):
		self.tableFrame.pack(fill='both', expand='yes', padx=20, pady=10)

		self.trv.pack(side='top', padx=10)


		self.vsb.place(relx=0.97, rely=0, relwidth=0.02, relheight=0.7)
		self.trv.configure(yscrollcommand=self.vsb.set)

		self.searchBtn.place(relx=0.05, rely=0.9, relwidth=0.1, relheight=0.05)
		self.searchInput.place(relx=0.16, rely=0.9, relwidth=0.25, relheight=0.05)
		self.filterDropDown.place(relx=0.33, rely=0.9, relwidth=0.1, relheight=0.05)

		self.orderLb.place(relx=0.45, rely=0.9, relwidth=0.1, relheight=0.05)
		self.orderDropdown.place(relx=0.55, rely=0.9, relwidth=0.1, relheight=0.05)


		self.trv['columns'] = tuple(range(1, len(self.columns) + 1))
		for column in range(1, len(self.columns) + 1):
			self.trv.heading(column, text=self.columns[column - 1])


	def configColumns(self, colData={}):
		for col in colData.keys():
			defaultWidth = self.trv.column(1)['width']
			defaultAnchor = 'w'
			
			newWidth = colData.get(col).get("width")
			newAnchor = colData.get(col).get("anchor")

			width = newWidth if newWidth is not None else defaultWidth
			anchor = newAnchor if newAnchor is not None else defaultAnchor

			self.trv.column(col, width=width, anchor=anchor)


	def search(self):
		searchInput = self.searchInput.get()
		condition = "" if searchInput == "" else f" where {self.searchTopic.get()} like '%{searchInput}%'"

		orderCondition = " order by " + self.orderByTopic.get() + " desc"

		statement = self.defaultStatement + condition + orderCondition
		print(statement)
		self.updateData(statement)








# root = tk.Tk()
# root.title('My Application')
# root.geometry('1200x500')

# table = TableGUI(window=root, model=Ktrucsu, tableName='Bang Kien Truc Su')
# table.createGUI()

# colData = {
# 	1 : {
# 		'width': 80,
# 		'anchor': 'c'
# 	},
# 	2 : {
# 		'width': 150,
# 		'anchor': 'c'
# 	},
# 	3 : {
# 		'width': 150,
# 		'anchor': 'c'
# 	},
# 	4 : {
# 		'width': 150,
# 		'anchor': 'c'
# 	},
# 	5 : {
# 		'width': 150,
# 		'anchor': 'c'
# 	},
# 	6 : {
# 		'width': 150,
# 		'anchor': 'c'
# 	},
# 	7 : {
# 		'width': 120,
# 		'anchor': 'c'
# 	},
# 	8 : {
# 		'width': 100,
# 		'anchor': 'c'
# 	},
# }
# table.configColumns(colData)



# root.mainloop()