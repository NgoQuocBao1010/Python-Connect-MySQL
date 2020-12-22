import tkinter as tk
from tkinter import ttk

from mysqlConnection import ConnectionToMySQl
from table import TableTkinter
from model import *

HEIGHT = 500
WIDTH  = 1200

fontHeadings = ('Mongolian Baiti', 30,'bold')
fontFields = ('Courier', 10,'bold')
fontData = ('Courier', 12)


class Details():
	def __init__(self, window, tableModel, values={}):
		self.window = window
		self.tableModel = tableModel
		self.values = values
		self.contentFrame = tk.Frame(self.window)
	
	def createGui(self):
		self.contentFrame.pack(fill='both', expand='yes')
		
		# Main Label
		nameLb = tk.Label(
			self.contentFrame,
			text='Ten Cong Trinh',
			font=fontHeadings,
			fg='red',
			bg='gray'
		)
		nameLb.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)

		startPos = 0.2
		for field, data in self.values.items():
			tk.Label(
				self.contentFrame,
				text=field,
				font=fontFields,
				fg='blue',
				bg='gray'
			).place(relx=0.05, rely=startPos, relwidth=0.1, relheight=0.075)

			tk.Label(
				self.contentFrame,
				text=data,
				font=fontData,
				fg='blue',
				bg='gray'
			).place(relx=0.17, rely=startPos, relwidth=0.4, relheight=0.075)

			startPos += 0.08
		
		startPos = 0.2
		for field in self.tableModel.formsField().get('manyToMany'):
			tableCN = TableTkinter(self.contentFrame, 0.6, startPos, 0.3, 0.2)
			colData = {
				field.tableName: (field.tableName, 100, 'w'),
			}
			tableCN.setColumns(colData)

			if field is Congnhan:
				obj = Congtrinh(*self.values.values())
				dataField = obj.getCongNhan()
			
			if field is Ktrucsu:
				obj = Congtrinh(*self.values.values())
				dataField = obj.getKienTrucSu()
			
			if field is Congtrinh:
				obj = self.tableModel(*self.values.values())
				dataField = obj.getCongTrinh()
			
			tableCN.insertData(dataField)

			startPos += 0.3


		gobackBtn = tk.Button(self.contentFrame, bg='red', fg='white', text='Back', command=self.back)
		gobackBtn.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)
	
	def back(self):
		self.contentFrame.destroy()






# root = tk.Tk()
# root.geometry('1200x600')
# d = Details(root, Congtrinh)
# f.createGUI()
# root.mainloop()