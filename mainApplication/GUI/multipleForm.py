from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from model import *
# from collections import OrderedDict

from mysqlConnection import ConnectionToMySQl

SUB_TITLE = ("Sitka Banner", 13)
TITLE_FONT = ("Comic Sans MS", 15, "bold")
LABLE_FONT = ("Sitka Banner", 13, "bold")

# forms
class MultipleForms():
	def __init__(self, window, keyModel, coordinate=(0, 0), fields=[], values={}):
		self.window = window
		self.keyModel = keyModel
		self.relx, self.rely = coordinate
		self.fields = fields
		self.values = values

	def createGui(self):
		self.contentFrame = Frame(self.window)
		self.contentFrame.place(relx=self.relx, rely=self.rely, relwidth=1, relheight=0.12)

		marginx = 0
		self.getKeyOptions()
		self.inputs = []
		for field in self.fields:
			Label(
				self.contentFrame,
				text=field,
				bg='#3F66DC',
				font=LABLE_FONT
			).place(relx=0.01 + marginx, rely=0, relwidth=0.2, relheight=0.4)

			initText = self.values.get(field) if len(self.values) != 0 else ''
			textVar = StringVar()
			textVar.set(initText)

			if field == 'Họ và tên' or field == 'Tên Công Trình':
				ttk.OptionMenu(
					self.contentFrame,
					textVar,
					initText,
					*self.options
				).place(relx=0.01 + marginx, rely=0.5, relwidth=0.25, relheight=0.45)
			else:
				Entry(
					self.contentFrame,
					textvariable=textVar
				).place(relx=0.01 + marginx, rely=0.5, relwidth=0.25, relheight=0.45)
			marginx += 0.28
			self.inputs.append(textVar)

		self.variable = BooleanVar()
		self.variable.set(True)
		self.checkBox = Checkbutton(
			self.contentFrame,
			variable=self.variable,
		)
		self.checkBox.place(relx=0.9, rely=0.2, relwidth=0.1, relheight=0.5)
		
	# get options for dropdown
	def getKeyOptions(self):
		defaultStatement = f'select {self.keyModel.imptField} from {self.keyModel.table}'
		conn = ConnectionToMySQl()
		rs = conn.getQueryset(defaultStatement)
			
		self.options = []
		for name in rs:
			self.options.append(*name)
		conn.closeConnection()
	
	# get all input values
	def getValue(self):
		values = []
		for inputVar in self.inputs:
			value = inputVar.get()
			values.append(value)

		return values, self.variable.get()


# frame to contains all forms
class MultipleFormsFrame():
	def __init__(self, window, keyObject, savedTable, containInfo=None):
		self.window = window
		self.keyObject = keyObject
		self.tableModel = type(self.keyObject)
		self.savedTable = savedTable
		self.containInfo = containInfo

		self.contentFrame = Frame(self.window)
	
	def createGui(self):
		self.getData()
		self.contentFrame.pack(fill='both', expand='yes') 

		# title label
		firstText = 'Thêm ' + self.keyModel.tableName + ' cho ' + self.keyObject.tableName + ' '
		Label(
			self.contentFrame,
			text=firstText,
			font=SUB_TITLE
		).place(relx=0.01, rely=0.01, relwidth=0.4, relheight=0.1)


		Label(
			self.contentFrame,
			text=str(self.keyObject),
			anchor='w',
			font=TITLE_FONT
		).place(relx=0.45, rely=0.01, relwidth=0.33, relheight=0.1)

		# Add button
		Button(
			self.contentFrame,
			text='Thêm',
			bg='#3F66DC',
			fg='white',
			font=LABLE_FONT,
			command=self.addMoreForm
		).place(relx=0.9, rely=0.01, relwidth=0.09, relheight=0.07)

		# Submit Button
		Button(
			self.contentFrame,
			text='Save',
			bg='#3F66DC',
			fg='white',
			font=LABLE_FONT,
			command=self.getValues
		).place(relx=0.9, rely=0.9, relwidth=0.09, relheight=0.07)

		self.fields = []
		
		for syntax, field in self.savedTable.sqlSyntax.items():
			if syntax != self.tableModel.pk:
				self.fields.append(field)
		
		if type(self.keyObject) is not Congtrinh:
			self.fields[0] = 'Tên Công Trình'
		
		self.forms = []
		self.marginy = 0
		for data in self.data:
			values = dict(zip(self.fields, data))
			mf = MultipleForms(
				self.contentFrame, 
				self.keyModel,
				(0.01, 0.2 + self.marginy), 
				fields=self.fields, 
				values=values
				)
			mf.createGui()
			self.forms.append(mf)

			self.marginy += 0.18
	
	# get necessary data to create forms
	def getData(self):
		if self.tableModel is Congtrinh:
			self.keyModel = Congnhan if self.savedTable is Thamgia else Ktrucsu
			self.data = self.keyObject.getCongNhan() if self.savedTable is Thamgia else self.keyObject.getKienTrucSu()
		else:
			self.keyModel = Congtrinh
			self.data = self.keyObject.getCongTrinh()
			self.savedTable = Thamgia if type(self.keyObject) is Congnhan else Thietke

	# Add another form
	def addMoreForm(self):
		if len(self.forms) >= 4:
			messagebox.showerror('Vượt số hạn!', f'Không được thêm quá 4 {self.keyModel.tableName}')
			return
		
		mf = MultipleForms(
			self.contentFrame, 
			self.keyModel,
			(0.01, 0.2 + self.marginy), 
			fields=self.fields
			)
		mf.createGui()
		self.forms.append(mf)
		self.marginy += 0.15
	
	# refresh app to view info
	def refreshApp(self):
		self.app, self.tableModel = self.containInfo
		self.app.changeTableView(self.tableModel)
	
	# get all input values
	def getValues(self):
		values = {}
		aValues = [] # contains submit values
		for form in self.forms:
			value, checked = form.getValue()
			if checked:
				for v in value:
					if len(v) == 0:
						messagebox.showerror('Dữ liệu không đúng', 'Điền thiếu thông tin!!')
						return
				if value[0] not in aValues:
					aValues.append(value[0])
				else:
					messagebox.showerror('Dữ liệu không đúng', 'Các trường bị trùng lặp!!!')
					return

				values.setdefault(value[0],tuple(value))
		
		fValues = [] # first values
		for data in self.data:
			fValues.append(data[0])
		
		try:
			for value in aValues:
				if value in fValues:
					if type(self.keyObject) is Congtrinh:
						args = [value, str(self.keyObject)]
						for v in values.get(value):
							if v not in args:
								args.append(v)
					else:
						args = [str(self.keyObject), value]
						for v in values.get(value):
							if v not in args:
								args.append(v)
					print('Update', args)
					self.savedTable.saveToDatabase(args, edit=True)
				
				else:
					if type(self.keyObject) is Congtrinh:
						args = [value, str(self.keyObject)]
						for v in values.get(value):
							if v not in args:
								args.append(v)
					else:
						args = [str(self.keyObject), value]
						for v in values.get(value):
							if v not in args:
								args.append(v)
					
					print('Add', args)
					self.savedTable.saveToDatabase(args)
			
			for value in fValues:
				if value not in aValues:
					if type(self.keyObject) is Congtrinh:
						args = [value, str(self.keyObject)]
					else:
						args = [str(self.keyObject), value]
					print('Delete', value)
					self.savedTable.deleteFromDB(args)
			messagebox.showinfo('Thành công!', 'Dữ liệu của bạn đã được lưu!')
		except Exception as e:
			messagebox.showerror('Đã xảy ra lỗi!!!', str(e))
		self.contentFrame.destroy()
		
		if type(self.keyObject) is Congtrinh:
			if self.savedTable is Thietke:
				mft = MultipleFormsFrame(self.window, self.keyObject, Thamgia, containInfo=self.containInfo)
				mft.createGui()
			else:
				self.refreshApp()
		else:
			self.refreshApp()
