import tkinter as tk
from tkinter import ttk
import tkinter.tix as tix


class TableTkinter():
	def __init__(self, window, x, y, width, height):
		self.window = window
		self.relx = x
		self.rely = y
		self.height = height
		self.width = width
		self.create()


	def create(self):
		style = ttk.Style()
		style.configure("mystyle.Treeview", 
						highlightthickness=3, 
						bd=1, font=('Calibri', 11), 
						foreground='blue', 
						rowheight=40
		) # Modify the font of the body
		style.configure("mystyle.Treeview.Heading", font=('Times New Roman', 12,'bold'))

		self.table = ttk.Treeview(self.window, selectmode='browse', style="mystyle.Treeview")
		self.table.place(relx=self.relx, rely=self.rely, relwidth=self.width, relheight=self.height)

		self.vsb = ttk.Scrollbar(self.window, orient="vertical", command=self.table.yview)
		self.vsb.place(relx=self.relx+self.width+0.015, rely=self.rely, relwidth=0.05, relheight=self.height)

		self.table.configure(yscrollcommand=self.vsb.set)

	def setColumns(self, colData={}):
		columnNames = tuple(colData.keys())

		self.table["columns"] = columnNames
		self.table["show"] = 'headings'

		for name in columnNames:
			colWidth = colData.get(name)[1]
			colAnchor = colData.get(name)[2]
			colHeading = colData.get(name)[0]
			self.table.column(name, width=colWidth, anchor=colAnchor)
			self.table.heading(name, text=colHeading)


		# print(columnNames)

	def insertData(self, data):
		self.table.delete(*self.table.get_children())
		for row in data:
			self.table.insert("", 'end', values=row)


# root = tk.Tk()
# root.geometry('1000x400')

# table = TableTkinter(root, 0.05, 0.05, 0.9, 0.7)

# root.mainloop()
