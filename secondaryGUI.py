import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from mysqlConnection import ConnectionToMySQl
from tableGUI import TableGUI
# from mainAppGui import application
import model

TITLE_FONT = ("Comic Sans MS", 25, "bold")
LABEL_FONT = ("Times New Roman", 14)


class funcButton():
	def __init__(self, root, text, fModel, tModel, coordinate=(0, 0, 0, 0)):
		self.root = root
		self.text = text
		self.fModel = fModel
		self.tModel = tModel
		self.coordinate = coordinate
		self.bg = 'black'
		self.fg = 'white'
		self.font = LABEL_FONT
		self.create()


	def create(self):
		summit = tk.Button(	self.root, 
							text 	=	self.text, 
							bg   	=	self.bg, 
							fg   	=	self.fg, 
							font 	=	self.font,
							command	=	lambda: self.addNew(self.tModel))
		x, y, width, height = self.coordinate
		summit.place(relx=x, rely=y, relwidth=width, relheight=height)

	def addNew(self, tModel):
		self.root.destroy()
		addElementGui(self.tModel)
		addElementGui(self.fModel)


def addElement(window, tableModel, pValues={}):
	def getValues():
		values = {}
		for field in fieldInputs.keys():
			entry = fieldInputs.get(field).get()
			values.setdefault(field, entry)
		print(values)
		return values

	def submit():
		values = getValues()

		for data in values.values():
			if len(data) == 0:
				messagebox.showerror('Error!!!', 'Invalid format on fields: ' + field)
				return

		try:
			tableModel.saveToDatabase(values)
			messagebox.showinfo('Succesful!!', 'Your Data has been saved!!')
			window.destroy()

		except Exception as e:
			messagebox.showerror('Error!!!', str(e))

	def preFill():
		print(pValues)
		for field in fieldInputs.keys():
			data = pValues.get(field)
			var = fieldInputs.get(field).set(data)


	fieldNames = tableModel.formsField().get('arribute')
	fieldInputs = {}

	titleLb = tk.Label(window, fg='black', text='Thêm ' + tableModel.tableName, font=TITLE_FONT)
	titleLb.place(relx=0.2, rely=0.02, relwidth=0.6, relheight=0.1)

	lbRely = 0.2
	for field in fieldNames:
		fieldLb = tk.Label(window, fg='black', text=field, font=LABEL_FONT, bg='gray')
		fieldLb.place(relx=0.02, rely=lbRely, relwidth=0.13, relheight=0.07)

		fieldVar = tk.StringVar()
		fieldVar.set('')
		fieldEnt = tk.Entry(window, fg='black', textvariable=fieldVar, font=LABEL_FONT)
		fieldEnt.place(relx=0.16, rely=lbRely, relwidth=0.25, relheight=0.07)

		lbRely += 0.12
		fieldInputs.setdefault(field, fieldVar)

	fkFields = tableModel.formsField().get("forgeinKey").keys()
	lbRely = 0.2
	for field in fkFields:
		fieldLb = tk.Label(window, fg='black', text=field, font=LABEL_FONT, bg='gray')
		fieldLb.place(relx=0.6, rely=lbRely, relwidth=0.13, relheight=0.07)

		tModel = tableModel.formsField().get("forgeinKey").get(field)
		conn = ConnectionToMySQl()
		statement = f'select {tModel.pk} from {tModel.tableName}'
		rs = conn.getQueryset(statement)
		
		options = []
		for name in rs:
			options.append(*name)

		fieldVar = tk.StringVar()
		fieldVar.set(options[0])
		dropdown = tk.OptionMenu(window, fieldVar, *options)
		dropdown.place(relx=0.6, rely=lbRely + 0.1, relwidth=0.2, relheight=0.07)
		fieldInputs.setdefault(field, fieldVar)
		btn = funcButton(window, 'Them ' + field, tableModel, tModel, (0.82, lbRely + 0.1, 0.15, 0.07))

		lbRely += 0.3

	

	submitBtn = tk.Button(window, fg='white', text='Save', font=LABEL_FONT, bg='green', command=submit)
	submitBtn.place(relx=0.85, rely=0.8, relwidth=0.1, relheight=0.07)

	if len(pValues) != 0:
		print('hello')
		preFill()


def addElementGui(tModel, values={}):
	root = tk.Tk()
	root.title('My Application')
	root.geometry('1400x600')

	addElement(root, tModel, values)

	root.mainloop()

values = {'Tên Công Trình': 'hello', 'Địa Chỉ': '123 d', 'Tỉnh Thành': 'ct', 'Kinh Phí (triệu đồng)': '100', 'Ngày Bắt Đầu': '1990-06-06', 'Tên Chủ': 'phan thanh liem', 'Tên Thầu': 'cty xd so 6'}
addElementGui(model.Congtrinh, values)