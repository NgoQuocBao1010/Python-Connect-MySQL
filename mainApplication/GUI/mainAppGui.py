import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from tableGUI import TableGUI
import model

TITLE_FONT = ("Comic Sans MS", 10, "bold")

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
		self.root.geometry('1200x600')

		# Right side frame
		self.navFrame = tk.Frame(self.root, bg='#3F66DC')
		self.navFrame.place(relx=0, rely=0, relwidth=0.1, relheight=1)

		# Frame contains buttons
		tablesOptionsFr = tk.Frame(self.navFrame, bg='#3F66DC')
		tablesOptionsFr.place(relx=0, rely=0.085, relwidth=1, relheight=0.7)

		tbLb = tk.Label(tablesOptionsFr, fg='white', bg="#3F66DC")
		tbLb.place(relx=0, rely=0, relwidth=1, relheight=0.1)

		# ----- Button toggel between tables
		btn = tk.Button(tablesOptionsFr, text='Công Trình', bg='#1640C5', fg='white',font=TITLE_FONT, 
						command= lambda: self.changeTableView(TABLES.get(btn['text'])))
		btn.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.1)

		btn1 = tk.Button(tablesOptionsFr, text='Kiến Trúc Sư', bg='#1640C5', fg='white',font=TITLE_FONT, 
						command= lambda: self.changeTableView(TABLES.get(btn1['text'])))
		btn1.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.1)

		btn2 = tk.Button(tablesOptionsFr, text='Công Nhân', bg='#1640C5', fg='white',font=TITLE_FONT, 
						command= lambda: self.changeTableView(TABLES.get(btn2['text'])))
		btn2.place(relx=0.1, rely=0.50, relwidth=0.8, relheight=0.1)

		btn3 = tk.Button(tablesOptionsFr, text='Chủ Thầu', bg='#1640C5', fg='white',font=TITLE_FONT, 
						command= lambda: self.changeTableView(TABLES.get(btn3['text'])))
		btn3.place(relx=0.1, rely=0.65, relwidth=0.8, relheight=0.1)

		btn4 = tk.Button(tablesOptionsFr, text='Chủ Nhà', bg='#1640C5', fg='white',font=TITLE_FONT, 
						command= lambda: self.changeTableView(TABLES.get(btn4['text'])))
		btn4.place(relx=0.1, rely=0.80, relwidth=0.8, relheight=0.1)

		# ------
		self.exitBtn = tk.Button(
					self.navFrame, text='thoát', bg='#E94F37', fg='white',font=TITLE_FONT, 
					command = self.exit
					)
		self.exitBtn.place(relx=0.1, rely=0.9, relwidth=0.8, relheight=0.075)

		# Frame contains table
		self.contentFrame = tk.Frame(self.root)
		self.contentFrame.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)

		# Table gui
		self.table = TableGUI(self.contentFrame, model.Congtrinh, self)
		self.table.createGUI()
		self.table.configColumns(model.Congtrinh.colData)

		self.root.mainloop()

	# Toggels between tables
	def changeTableView(self, newTableModel):
		self.contentFrame.destroy()
		self.contentFrame = tk.Frame(self.root)
		self.contentFrame.place(relx=0.1, rely=0, relwidth=0.9, relheight=1)

		newTable = TableGUI(self.contentFrame, newTableModel, self)
		newTable.createGUI()
		newTable.configColumns(newTableModel.colData)

		self.table = newTable

	# Exit button
	def exit(self):
		msg = messagebox.askokcancel('Exit?', 'Do you want to exit the app?')
		
		if msg:
			self.root.destroy()
	

	def reborn(self):
		self.rebornApp = Application()




app = Application()