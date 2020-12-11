import tkinter as tk
from tkinter import ttk

from mysqlConnection import ConnectionToMySQl
from tableGUI import TableGUI
import model

TABLES = {
	'Công Trình': model.Congtrinh,
	'Kiến Trúc Sư': model.Ktrucsu,
	'Công Nhân': model.Congnhan,
	'Chủ Thầu': model.Chuthau,
	'Chủ Nhà': model.Chunhan
}


class Application():
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('My Application')
		self.root.geometry('1400x600')

		self.navFrame = tk.Frame(self.root, bg='brown')
		self.navFrame.place(relx=0, rely=0, relwidth=0.1, relheight=1)

		tablesOptionsFr = tk.Frame(self.navFrame, bg='blue')
		tablesOptionsFr.place(relx=0, rely=0.1, relwidth=1, relheight=0.7)

		tbLb = tk.Label(tablesOptionsFr, fg='white', text='Choose Table', bg="#196BCC")
		tbLb.place(relx=0, rely=0, relwidth=1, relheight=0.1)

		btn = tk.Button(tablesOptionsFr, text='Công Trình', bg='black', fg='white', 
						command= lambda: self.changeTableView(TABLES.get(btn['text'])))
		btn.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

		btn1 = tk.Button(tablesOptionsFr, text='Kiến Trúc Sư', bg='black', fg='white', 
						command= lambda: self.changeTableView(TABLES.get(btn1['text'])))
		btn1.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.1)

		btn2 = tk.Button(tablesOptionsFr, text='Công Nhân', bg='black', fg='white', 
						command= lambda: self.changeTableView(TABLES.get(btn2['text'])))
		btn2.place(relx=0.1, rely=0.50, relwidth=0.8, relheight=0.1)

		btn3 = tk.Button(tablesOptionsFr, text='Chủ Thầu', bg='black', fg='white', 
						command= lambda: self.changeTableView(TABLES.get(btn3['text'])))
		btn3.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.1)

		btn4 = tk.Button(tablesOptionsFr, text='Chủ Nhà', bg='black', fg='white', 
						command= lambda: self.changeTableView(TABLES.get(btn4['text'])))
		btn4.place(relx=0.1, rely=0.80, relwidth=0.8, relheight=0.1)

		self.exitBtn = tk.Button(
					self.navFrame, text='Thoat', bg='black', fg='white', 
					command= lambda : self.root.destroy()
					)
		self.exitBtn.place(relx=0.01, rely=0.9, relwidth=0.8, relheight=0.075)

		self.contentFrame = tk.Frame(self.root)
		self.contentFrame.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)

		self.table = TableGUI(self.contentFrame, model.Congtrinh, self)
		self.table.createGUI()
		self.table.configColumns(model.Congtrinh.colData)

		self.root.mainloop()

	def changeTableView(self, newTableModel):
		self.contentFrame.destroy()
		self.contentFrame = tk.Frame(self.root)
		self.contentFrame.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)


		newTable = TableGUI(self.contentFrame, newTableModel, self)
		newTable.createGUI()
		newTable.configColumns(newTableModel.colData)

		self.table = newTable



# app = application()
app = Application()