import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from mysqlConnection import ConnectionToMySQl
from multipleForm import MultipleFormsFrame
from model import *


# Fonts
TITLE_FONT = ("Comic Sans MS", 25, "bold")
LABEL_FONT = ("Sitka Banner", 15, "bold")
ENTRY_FONT = ("Sitka Banner", 20)

# Colors
LABEL_COLOR = 'Blue'


class Form():

	# special function with ability to change to another view
	class funcButton():
		def __init__(self, canvas, text, root, fModel, tModel, form=None, m2m=False, coordinate=(0, 0, 0, 0)):
			self.canvas = canvas
			self.text = text
			self.root = root
			self.fModel = fModel
			self.tModel = tModel
			self.form = form
			self.m2m = m2m
			self.coordinate = coordinate
			self.bg = 'black'
			self.fg = 'white'
			self.font = LABEL_FONT
			self.create()

		# create method
		def create(self):
			summit = tk.Button(	self.canvas, 
								text 	=	self.text, 
								bg   	=	self.bg, 
								fg   	=	self.fg, 
								font 	=	self.font,
								command	=	self.addNew)
			x, y, width, height = self.coordinate
			summit.place(relx=x, rely=y, relwidth=width, relheight=height)

		# New view
		def addNew(self):
			# change to form view
			if not self.m2m:
				values = self.form.getValues()
				self.form.contentFrame.pack_forget()
				form = Form(self.form.window, self.tModel, pFormInfo=(self.form, values))
				form.createGUI()
			else:
				msg = messagebox.askokcancel(
					'Tiếp tục?',
					'Dữ liệu sẽ được lưu trước khi cập nhật!'
					)

				# change to multipleForm view
				if msg:
					self.form.submit(True)

	def __init__(self, window, tableModel, app=None, edit=False, pFormInfo=None, values={}):
		self.window = window
		self.tableModel = tableModel
		self.app = app
		self.pFormInfo = pFormInfo
		self.values = values
		self.edit = edit
		self.contentFrame = tk.Frame(self.window)

	def createGUI(self):
		self.contentFrame.pack(fill='both', expand='yes')

		self.fieldInputs = {}

		# Form's Name
		titleLb = tk.Label(
			self.contentFrame, 
			fg='#FF2323', 
			text='Thêm ' + self.tableModel.tableName, 
			font=TITLE_FONT
			)
		titleLb.place(relx=0.2, rely=0.02, relwidth=0.6, relheight=0.1)

		fieldNames = self.tableModel.formsField().get('arribute')
		lbRely = 0.2
		for field in fieldNames:
			fieldLb = tk.Label(self.contentFrame, fg='#1640C5', text=field, font=LABEL_FONT, anchor='w')
			fieldLb.place(relx=0.02, rely=lbRely, relwidth=0.13, relheight=0.035)

			# Var to save input
			fieldVar = tk.StringVar()
			fieldVar.set('')
			fieldEnt = tk.Entry(self.contentFrame, fg='black', textvariable=fieldVar, font=ENTRY_FONT)
			fieldEnt.place(relx=0.02, rely=lbRely + 0.037, relwidth=0.4, relheight=0.07)

			lbRely += 0.12
			self.fieldInputs.setdefault(field, fieldVar)


		fkFields = self.tableModel.formsField().get("forgeinKey").keys()
		lbRely = 0.2
		for field in fkFields:
			fieldLb = tk.Label(self.contentFrame, fg='black', text=field, font=LABEL_FONT, bg='light gray')
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

			# change view button
			btn = self.funcButton(
				self.contentFrame, 
				'Thêm ' + field,
				self.window, 
				self.tableModel, 
				tModel,
				self, 
				coordinate=(0.82, lbRely + 0.1, 0.15, 0.07)
			)

			lbRely += 0.3
			conn.closeConnection()
		
		# many to many field handle
		m2mFields = self.tableModel.formsField().get("manyToMany")
		if m2mFields is not None:
			self.m2mText = 'Cập nhật '
			for field in m2mFields:
				self.m2mText += field.tableName + '  '

			# change to many to many form
			btn = self.funcButton(
				self.contentFrame, 
				self.m2mText,
				self.window, 
				self.tableModel, 
				tModel=None,
				form=self, 
				m2m=True,
				coordinate=(0.6, 0.8, 0.35, 0.07)
			)
		
		# Submit Button
		submitBtn = tk.Button(
						self.contentFrame, 
						fg='white', text='Lưu', 
						font=LABEL_FONT, bg='#1640C5', 
						command=self.submit
						)
		submitBtn.place(relx=0.85, rely=0.1, relwidth=0.1, relheight=0.07)

		# Back btn
		gobackBtn = tk.Button(self.contentFrame, bg='gray', fg='white', text='trở về',font=('Courier', 10), command=self.back)
		gobackBtn.place(relx=0, rely=0, relwidth=0.1, relheight=0.07)

		self.preFill()

	# get all input values
	def getValues(self):
		values = {}
		for field in self.fieldInputs.keys():
			entry = self.fieldInputs.get(field).get()
			values.setdefault(field, entry)

			if self.pFormInfo is not None:
				self.pFormInfo[1][field] = entry

		if self.edit:
			for field, data in self.values.items():
				values.setdefault(field, data)

		return values

	# function when hit the submit button
	# save data to databse ig the input is valid
	def submit(self, m2m=False):
		values = self.getValues()

		try:
			self.obj = self.tableModel.saveToDatabase(values, self.edit)
			messagebox.showinfo('Thành công!', 'Dữ liệu của bạn đã được lưu!')

			if m2m:
				if type(self.obj) is Congtrinh:
					mtf = MultipleFormsFrame(self.window, self.obj, Thietke, containInfo=(self.app, self.tableModel))
					mtf.createGui()
				else:
					mtf = MultipleFormsFrame(self.window, self.obj, None, containInfo=(self.app, self.tableModel))
					mtf.createGui()
			else:
				if self.app is not None:
					self.app.changeTableView(self.tableModel)

			self.back()

		except Exception as e:
			messagebox.showerror('Error!!!', str(e))

	# use when edit data or to preserve data when toggel betwween view
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

		if self.pFormInfo is not None:
			form = self.pFormInfo[0]
			form.values = self.pFormInfo[1]
			form.createGUI()



# root = tk.Tk()
# root.geometry('1200x600')
# f = Form(root, Congtrinh)
# f.createGUI()
# root.mainloop()