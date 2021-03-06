import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from mysqlConnection import ConnectionToMySQl
from formsGui import Form
from detailGUI import Details

LABEL_FONT = ("Sitka Banner", 13)
TITLE_FONT = ("Comic Sans MS", 19, "bold")
TITLE_FONT2 = ("Comic Sans MS", 15, "bold")

# Show mysql table in tkinter with functionality such as add, delete, edit and search 
class TableGUI():
	def __init__(self, window, model, app=None):
		style = ttk.Style()
		style.configure("mystyle.Treeview", 
						highlightthickness=3, 
						bd=1, font=('Calibri', 11), 
						foreground='blue', 
						rowheight=40
		)
		style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 12,'bold'))
		style.configure("TMenubutton", background="#CAD2E9")

		self.model = model
		self.window = window
		self.app = app

		# sql statement runs each time table's created
		self.defaultStatement = f'select * from {self.model.table}'

		# Label frames to hold component
		self.tableFrame = tk.LabelFrame(self.window, font=TITLE_FONT, text=self.model.tableName)
		self.searchFrame = tk.LabelFrame(self.window, text='Tìm Kiếm',font=TITLE_FONT2)
		self.infoFrame = tk.LabelFrame(self.window, text='Thông tin về bảng',font=TITLE_FONT2)

		# Table and its crollbar component
		self.trv = ttk.Treeview(self.tableFrame, show="headings", height="10", style="mystyle.Treeview")
		self.vsb = ttk.Scrollbar(self.tableFrame, orient="vertical", command=self.trv.yview)
		self.hsb = ttk.Scrollbar(self.tableFrame, orient="horizontal", command=self.trv.xview)

		# update data in table
		self.updateData(self.defaultStatement)

		# Searchbar
		self.searchBtn = tk.Button(
			self.searchFrame, 
			bg='#CAD2E9', fg='#1640C5', 
			text='Tìm Kiếm',
			font=LABEL_FONT, 
			command=self.search,
			compound = 'left'
			)
		self.searchInput = tk.Entry(self.searchFrame)
		self.searchTopic = tk.StringVar()
		self.searchTopic.set(self.model.imptField)
		self.filterDropDown = ttk.OptionMenu(
			self.searchFrame, 
			self.searchTopic, 
			self.model.imptField,
			*self.columnSyntaxs
			)

		# order by topic
		self.orderLb = tk.Label(self.searchFrame, bg='#8C8C8C', fg='black', text='Sắp Xếp')

		self.orderByTopic = tk.StringVar()
		self.orderByTopic.set(self.model.imptField)
		self.orderDropdown = ttk.OptionMenu(
			self.searchFrame, 
			self.orderByTopic, 
			self.model.imptField,
			*self.columnSyntaxs
			)

		# 
		self.addBtn = tk.Button(
			self.searchFrame,
			bg='#CAD2E9', 
			fg='#1640C5', 
			text='Thêm', 
			font=LABEL_FONT,
			command=self.addData
			)
		self.editBtn = tk.Button(
			self.searchFrame,
			bg='#CAD2E9', 
			fg='#1640C5', 
			text='Sửa', 
			font=LABEL_FONT,
			command=self.editData)
		self.delBtn = tk.Button(
			self.searchFrame,
			bg='red', 
			fg='white', 
			text='Xóa', 
			font=LABEL_FONT,
			command=self.deleteData
			)


	# update data from database
	def updateData(self, statement):
		# delete old data
		self.trv.delete(*self.trv.get_children())

		mysqlConn = ConnectionToMySQl()
		self.rows = mysqlConn.getQueryset(statement)

		# insert data into rows
		self.columnSyntaxs = mysqlConn.cursor.column_names

		self.columns = []
		for syn in self.columnSyntaxs:
			self.columns.append(self.model.sqlSyntax.get(syn.lower()))

		for data in self.rows:
			self.trv.insert('', 'end', values=data)
		
		mysqlConn.closeConnection()

		try:
			self.info = self.model.information()
		except Exception:
			self.info = []
		# print(self.info)

	# create graphic user interface
	def createGUI(self):
		self.tableFrame.place(relx=0, rely=0, relwidth=0.75, relheight=0.7)
		self.searchFrame.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.7)
		self.infoFrame.place(relx=0, rely=0.7, relwidth=1, relheight=0.3)

		self.trv.pack(side='top')

		# ---- table Frame component --- #
		self.vsb.place(relx=0.98, rely=0.05, relwidth=0.02, relheight=0.9)
		self.hsb.place(relx=0, rely=0.95, relwidth=1, relheight=0.05)
		self.trv.configure(xscrollcommand=self.hsb.set)
		self.trv.configure(yscrollcommand=self.vsb.set)

		self.searchBtn.place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.1)
		self.searchInput.place(relx=0.36, rely=0.05, relwidth=0.64, relheight=0.1)
		self.filterDropDown.place(relx=0.05, rely=0.15, relwidth=0.94, relheight=0.15)

		self.orderLb.place(relx=0.05, rely=0.32, relwidth=0.3, relheight=0.1)
		self.orderDropdown.place(relx=0.35, rely=0.32, relwidth=0.64, relheight=0.1)


		# ---- searcg Frame component --- #
		self.addBtn.place(relx=0.05, rely=0.65, relwidth=0.9, relheight=0.1)
		self.editBtn.place(relx=0.05, rely=0.75, relwidth=0.9, relheight=0.1)
		self.delBtn.place(relx=0.05, rely=0.85, relwidth=0.9, relheight=0.1)

		# ---- info Frame component --- #
		row = 0
		for info in self.info:
			textLb = str(row + 1) + ' .' + info 
			tk.Label(
				self.infoFrame,
				text=textLb,
				font=LABEL_FONT,
			).grid(column=0, row=row, pady=5, sticky='w')
			row += 1
		
		if len(self.info) == 0:
			textLb = 'Không có thông tin'
			tk.Label(
				self.infoFrame,
				text=textLb,
				font=LABEL_FONT,
			).grid(column=0, row=0, pady=5, sticky='w')


		self.trv['columns'] = tuple(range(1, len(self.columns) + 1))
		for column in range(1, len(self.columns) + 1):
			self.trv.heading(column, text=self.columns[column - 1])

		self.bindings()

	# set props for columns
	def configColumns(self, colData={}):
		for col in colData.keys():
			defaultWidth = self.trv.column(1)['width']
			defaultAnchor = 'w'
			
			newWidth = colData.get(col).get("width")
			newAnchor = colData.get(col).get("anchor")

			width = newWidth if newWidth is not None else defaultWidth
			anchor = newAnchor if newAnchor is not None else defaultAnchor

			self.trv.column(col, width=width, anchor=anchor)

	# search function
	def search(self):
		searchInput = self.searchInput.get()
		condition = "" if searchInput == "" else f" where {self.searchTopic.get()} like '%{searchInput}%'"

		orderCondition = " order by " + self.orderByTopic.get() + " desc"

		statement = self.defaultStatement + condition + orderCondition
		self.updateData(statement)

	# add data to mysql
	def addData(self):
		form = Form(self.window, self.model, self.app)
		form.createGUI()

	# edit data
	def editData(self):
		selected = self.trv.focus()
		if len(selected) == 0:
			messagebox.showwarning('Warning', 'Please choose a item you want to edit!')
			return

		selectedVal = self.trv.item(selected)['values']
		obj = dict(zip(self.model.sqlSyntax.values(), selectedVal))
		
		form = Form(self.window, self.model, app=self.app, edit=True, values=obj)
		form.createGUI()

	# delete data
	def deleteData(self):
		selected = self.trv.focus()
		if len(selected) == 0:
			messagebox.showwarning('Warning', 'Please choose a item you want to delete!')
			return

		selectedVal = self.trv.item(selected)['values']
		obj = dict(zip(self.model.sqlSyntax.values(), selectedVal))

		confirmMsg = messagebox.askokcancel(
			'Delete', 
			'Are you sure to permantly remove this item from database?'
			)
		if confirmMsg:
			self.model.deleteFromDb(obj)

			if self.app is not None:
				self.app.changeTableView(self.model)

	# bindings event
	def bindings(self):
		self.trv.bind("<Double-1>", self.toDetail)

	# double right click functions
	# show details of an selected item
	def toDetail(self, event):
		selected = self.trv.focus()
		if len(selected) == 0:
			messagebox.showwarning('Warning', 'Please choose a item you want to view!')
			return
		
		selectedVal = self.trv.item(selected)['values']
		obj = dict(zip(self.model.sqlSyntax.values(), selectedVal))
		print(obj)
		detail = Details(self.window, self.model, obj)
		detail.createGui()