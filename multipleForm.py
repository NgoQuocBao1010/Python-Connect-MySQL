from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from model import *
from collections import OrderedDict

from mysqlConnection import ConnectionToMySQl


class MultipleForms():
	def __init__(self, window, keyModel, coordinate=(0, 0), fields=[], values={}):
		self.window = window
		self.keyModel = keyModel
		self.relx, self.rely = coordinate
		self.fields = fields
		self.values = values

	def createGui(self):
		self.contentFrame = Frame(self.window)
		self.contentFrame.place(relx=self.relx, rely=self.rely, relwidth=1, relheight=0.15)

		marginx = 0
		self.getKeyOptions()
		self.inputs = []
		for field in self.fields:
			Label(
				self.contentFrame,
				text=field,
				bg='#3F66DC'
			).place(relx=0.01 + marginx, rely=0, relwidth=0.2, relheight=0.25)

			initText = self.values.get(field) if len(self.values) != 0 else ''
			textVar = StringVar()
			textVar.set(initText)

			if field == 'Họ và tên' or field == 'Tên Công Trình':
				ttk.OptionMenu(
					self.contentFrame,
					textVar,
					initText,
					*self.options
				).place(relx=0.01 + marginx, rely=0.31, relwidth=0.25, relheight=0.6)
			else:
				Entry(
					self.contentFrame,
					textvariable=textVar
				).place(relx=0.01 + marginx, rely=0.31, relwidth=0.25, relheight=0.6)
			marginx += 0.28
			self.inputs.append(textVar)

		self.variable = BooleanVar()
		self.variable.set(True)
		self.checkBox = Checkbutton(
			self.contentFrame,
			variable=self.variable,
		)
		self.checkBox.place(relx=0.9, rely=0.2, relwidth=0.05, relheight=0.3)
		
	
	def getKeyOptions(self):
		defaultStatement = f'select {self.keyModel.imptField} from {self.keyModel.table}'
		conn = ConnectionToMySQl()
		rs = conn.getQueryset(defaultStatement)
			
		self.options = []
		for name in rs:
			self.options.append(*name)
	
	
	def getValue(self):
		values = []
		for inputVar in self.inputs:
			value = inputVar.get()
			values.append(value)

		return values, self.variable.get()
	
		


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

		firstText = 'Thêm ' + self.keyModel.tableName + ' cho '
		Label(
			self.contentFrame,
			text=firstText,
			bg='#3F66DC'
		).place(relx=0.01, rely=0.01, relwidth=0.3, relheight=0.1)


		Label(
			self.contentFrame,
			text=str(self.keyObject),
			bg='#3F66DC'
		).place(relx=0.31, rely=0.01, relwidth=0.5, relheight=0.1)

		# Add button
		Button(
			self.contentFrame,
			text='Add',
			bg='#3F66DC',
			fg='red',
			command=self.addMoreForm
		).place(relx=0.9, rely=0.01, relwidth=0.09, relheight=0.07)

		# Submit Button
		Button(
			self.contentFrame,
			text='Save',
			bg='#3F66DC',
			fg='white',
			command=self.getValues
		).place(relx=0.9, rely=0.9, relwidth=0.09, relheight=0.07)

		self.fields = []
		for syntax, field in self.savedTable.sqlSyntax.items():
			if syntax != self.tableModel.pk:
				self.fields.append(field)
		
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
		mf = MultipleForms(
			self.contentFrame, 
			self.keyModel,
			(0.01, 0.2 + self.marginy), 
			fields=self.fields
			)
		mf.createGui()
		self.forms.append(mf)
		self.marginy += 0.15

	def refreshApp(self):
		self.app, self.tableModel = self.containInfo
		self.app.changeTableView(self.tableModel)
	
	def getValues(self):
		values = {}
		aValues = [] # contains submit values
		for form in self.forms:
			value, checked = form.getValue()
			if checked:
				if value[0] not in aValues:
					aValues.append(value[0])
				else:
					messagebox.showerror('Invalid Input', 'Cannot choose the same value twice')
					return

				values.setdefault(value[0],tuple(value))
		
		fValues = [] # first values
		for data in self.data:
			fValues.append(data[0])
		

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

		# print(self.savedTable)
		self.contentFrame.destroy()
		
		if type(self.keyObject) is Congtrinh:
			if self.savedTable is Thietke:
				mft = MultipleFormsFrame(self.window, self.keyObject, Thamgia, containInfo=self.containInfo)
				mft.createGui()
			else:
				self.refreshApp()
		


		

		# print(values)

	
obj = {
	'STT': 10, 
	'Tên Công Trình': 'cong trinh moi', 
	'Địa Chỉ': 'Hung Loi', 
	'Tỉnh Thành': 'sai gon', 
	'Kinh Phí': 100, 
	'Tên Chủ': 'NCHM', 
	'Tên Thầu': 'le van son', 
	'Ngày Bắt Đầu': '2020-10-10'
	}
objCt = Congtrinh(*obj.values())

# print(objCt.getKienTrucSu())
# root = Tk()
# root.geometry('600x600')
# mft = MultipleFormsFrame(root, objCt, Thietke)
# mft.createGui()
# root.mainloop()



	
