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


def application():
	def changeTableView(tableName):
		global table
		table.tableFrame.destroy()

		newTableModel = TABLES.get(tableName)

		newTable = TableGUI(contentFrame, newTableModel)
		newTable.createGUI()
		newTable.configColumns(newTableModel.colData)	

		table = newTable


	root = tk.Tk()
	root.title('My Application')
	root.geometry('1400x600')


	navFrame = tk.Frame(root, bg='brown')
	navFrame.place(relx=0, rely=0, relwidth=0.1, relheight=1)

	tablesOptionsFr = tk.Frame(navFrame, bg='blue')
	tablesOptionsFr.place(relx=0, rely=0.1, relwidth=1, relheight=0.7)

	tbLb = tk.Label(tablesOptionsFr, fg='white', text='Choose Table', bg="#196BCC")
	tbLb.place(relx=0, rely=0, relwidth=1, relheight=0.1)

	btn = tk.Button(tablesOptionsFr, text='Công Trình', bg='black', fg='white', 
					command= lambda: changeTableView(btn['text']))
	btn.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

	btn1 = tk.Button(tablesOptionsFr, text='Kiến Trúc Sư', bg='black', fg='white', 
					command= lambda: changeTableView(btn1['text']))
	btn1.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.1)

	btn2 = tk.Button(tablesOptionsFr, text='Công Nhân', bg='black', fg='white', 
					command= lambda: changeTableView(btn2['text']))
	btn2.place(relx=0.1, rely=0.50, relwidth=0.8, relheight=0.1)

	btn3 = tk.Button(tablesOptionsFr, text='Chủ Thầu', bg='black', fg='white', 
					command= lambda: changeTableView(btn3['text']))
	btn3.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.1)

	btn4 = tk.Button(tablesOptionsFr, text='Chủ Nhà', bg='black', fg='white', 
					command= lambda: changeTableView(btn4['text']))
	btn4.place(relx=0.1, rely=0.80, relwidth=0.8, relheight=0.1)



	contentFrame = tk.Frame(root)
	contentFrame.place(relx=0.1, rely=0, relwidth=0.9, relheight=0.7)

	global table
	table = TableGUI(contentFrame, model.Congtrinh)
	table.createGUI()
	table.configColumns(model.Congtrinh.colData)

	root.mainloop()


app = application()