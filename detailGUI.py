import tkinter as tk
from tkinter import ttk

from mysqlConnection import ConnectionToMySQl
from table import TableTkinter
from model import *

HEIGHT = 500
WIDTH  = 1200

fontHeadings = ('Felix Titling', 30,'bold')
fontFields = ('Courier', 12,'bold')
fontData = ('Courier', 13, 'bold')


class Details():
	def __init__(self, window, tableModel, values={}):
		self.window = window
		self.tableModel = tableModel
		self.values = values
		self.contentFrame = tk.Frame(self.window)
	
	def createGui(self):
		self.contentFrame.pack(fill='both', expand='yes')
		
		typeOfDetail = self.tableModel.tableName
		name = self.values.get(self.tableModel.sqlSyntax.get(self.tableModel.imptField))
		title = typeOfDetail + ' ' + name.upper()
		# Main Label
		nameLb = tk.Label(
			self.contentFrame,
			text=title,
			font=fontHeadings,
			fg='black'
		)
		nameLb.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)

		startPos = 0.2
		for field, data in self.values.items():
			tk.Label(
				self.contentFrame,
				text=field,
				font=fontFields,
				fg='#3F66DC'
			).place(relx=0.02, rely=startPos, relwidth=0.15, relheight=0.075)

			if field == 'Kinh Phí':
				data = str(data)
				data += ' triệu đồng'
			tk.Label(
				self.contentFrame,
				text=data,
				font=fontData,
				fg='#FF2323',
				bg='white'
			).place(relx=0.17, rely=startPos, relwidth=0.4, relheight=0.075)

			startPos += 0.08
		
		if self.tableModel.formsField().get('manyToMany') is not None:
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


		gobackBtn = tk.Button(self.contentFrame, bg='gray', fg='white', text='trở về',font=('Courier', 10), command=self.back)
		gobackBtn.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)
	
	def back(self):
		self.contentFrame.destroy()






# root = tk.Tk()
# root.geometry('1200x600')
# d = Details(root, Congtrinh)
# f.createGUI()
# root.mainloop()