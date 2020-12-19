import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from mysqlConnection import ConnectionToMySQl
from checkList import *
from model import *

TITLE_FONT = ("Comic Sans MS", 25, "bold")
LABEL_FONT = ("Times New Roman", 14)


class Form():
	class funcButton():
		def __init__(self, canvas, text, root, fModel, tModel, form=None, coordinate=(0, 0, 0, 0)):
			self.canvas = canvas
			self.text = text
			self.root = root
			self.fModel = fModel
			self.tModel = tModel
			self.form = form
			self.coordinate = coordinate
			self.bg = 'black'
			self.fg = 'white'
			self.font = LABEL_FONT
			self.create()


		def create(self):
			summit = tk.Button(	self.canvas, 
								text 	=	self.text, 
								bg   	=	self.bg, 
								fg   	=	self.fg, 
								font 	=	self.font,
								command	=	self.addNew)
			x, y, width, height = self.coordinate
			summit.place(relx=x, rely=y, relwidth=width, relheight=height)

		def addNew(self):
			values = self.form.getValues()
			self.form.contentFrame.pack_forget()
			form = Form(self.form.window, self.tModel, pFormInfo=(self.form, values))
			form.createGUI()



	def __init__(self, window, tableModel, app=None, edit=False, pFormInfo=None, values={}):
		self.window = window
		self.tableModel = tableModel
		self.app = app
		self.pFormInfo = pFormInfo
		self.values = values
		self.edit = edit
		self.contentFrame = tk.Frame(self.window)

	def createGUI(self):
		self.contentFrame.pack(fill='both', expand='yes', padx=10, pady=10)
		fieldNames = self.tableModel.formsField().get('arribute')
		self.fieldInputs = {}

		titleLb = tk.Label(
			self.contentFrame, 
			fg='black', text='Thêm ' + 
			self.tableModel.tableName, 
			font=TITLE_FONT
			)
		titleLb.place(relx=0.2, rely=0.02, relwidth=0.6, relheight=0.1)

		lbRely = 0.2
		for field in fieldNames:
			fieldLb = tk.Label(self.contentFrame, fg='black', text=field, font=LABEL_FONT, bg='gray')
			fieldLb.place(relx=0.02, rely=lbRely, relwidth=0.13, relheight=0.07)

			fieldVar = tk.StringVar()
			fieldVar.set('')
			fieldEnt = tk.Entry(self.contentFrame, fg='black', textvariable=fieldVar, font=LABEL_FONT)
			fieldEnt.place(relx=0.16, rely=lbRely, relwidth=0.25, relheight=0.07)

			lbRely += 0.12
			self.fieldInputs.setdefault(field, fieldVar)

		fkFields = self.tableModel.formsField().get("forgeinKey").keys()
		lbRely = 0.2
		for field in fkFields:
			fieldLb = tk.Label(self.contentFrame, fg='black', text=field, font=LABEL_FONT, bg='gray')
			fieldLb.place(relx=0.6, rely=lbRely, relwidth=0.13, relheight=0.07)

			tModel = self.tableModel.formsField().get("forgeinKey").get(field)
			conn = ConnectionToMySQl()
			statement = f'select {tModel.pk} from {tModel.table}'
			rs = conn.getQueryset(statement)
			
			options = []
			for name in rs:
				options.append(*name)

			fieldVar = tk.StringVar()
			fieldVar.set(options[0])
			dropdown = tk.OptionMenu(self.contentFrame, fieldVar, *options)
			dropdown.place(relx=0.6, rely=lbRely + 0.1, relwidth=0.2, relheight=0.07)
			self.fieldInputs.setdefault(field, fieldVar)
			btn = self.funcButton(
				self.contentFrame, 
				'Them ' + field,
				self.window, 
				self.tableModel, 
				tModel,
				self, 
				coordinate=(0.82, lbRely + 0.1, 0.15, 0.07)
			)

			lbRely += 0.3
		

		submitBtn = tk.Button(
						self.contentFrame, 
						fg='white', text='Save', 
						font=LABEL_FONT, bg='green', 
						command=self.submit
						)
		submitBtn.place(relx=0.85, rely=0.8, relwidth=0.1, relheight=0.07)

		gobackBtn = tk.Button(self.contentFrame, bg='red', fg='white', text='Back', command=self.back)
		gobackBtn.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)

		self.preFill()

	def getValues(self):
		values = {}
		for field in self.fieldInputs.keys():
			entry = self.fieldInputs.get(field).get()
			values.setdefault(field, entry)

			if self.pFormInfo is not None:
				self.pFormInfo[1][field] = entry
		
		# print(values)
		# self.obj = self.tableModel.createObject(values)

		if self.edit:
			for field, data in self.values.items():
				values.setdefault(field, data)

		return values

	def submit(self):
		values = self.getValues()

		try:
			self.obj = self.tableModel.saveToDatabase(values, self.edit)
			messagebox.showinfo('Succesful!!', 'Your Data has been saved!!')

			if self.app is not None:
				self.app.changeTableView(self.tableModel)

			self.back()

		except Exception as e:
			messagebox.showerror('Error!!!', str(e))

	# prefill all the forms for edit data
	def preFill(self):
		if len(self.values) != 0:
			for field in self.fieldInputs.keys():
				data = self.values.get(field)
				var = self.fieldInputs.get(field).set(data)

			# Get old primary key's data before making changes
			oldPk = list(self.tableModel.sqlSyntax.values())[0]
			oldData = self.values.get(oldPk)
			self.values.setdefault('oldPk', oldData)

	# Return button 
	def back(self):
		self.contentFrame.destroy()

		# Futher Info
		if self.tableModel is Congtrinh:
			msg = messagebox.askokcancel(
				'Them Cong Nhan', 
				'Ban co muon them thong tin cong nhan lam viec?'
				)
				
			if msg:
				self.app.root.destroy()
				checkList(Congnhan, self.obj)
				self.app.reborn()
		
		elif self.tableModel is Congnhan or self.tableModel is Ktrucsu:
			msg = messagebox.askokcancel(
				'Them Cong Trinh', 
				'Ban co muon them thong tin cong trinh doi tuong dang lam viec?'
				)
				
			if msg:
				self.app.root.destroy()
				checkList(Congtrinh, self.obj)
				self.app.reborn()

		# prefill previous form if there is one
		if self.pFormInfo is not None:
			form = self.pFormInfo[0]
			form.values = self.pFormInfo[1]
			form.createGUI()
