from tkinter import *
from tkinter import ttk
from model import *


class MultipleForms():
	def __init__(self, window, coordinate=(0, 0), fields=[], values={}):
		self.window = window
		self.relx, self.rely = coordinate
		self.fields = fields
		self.values = values

	def createGui(self):
		marginx = 0
		for field in self.fields:
			Label(
				self.window,
				text=field,
				fg='#3F66DC'
			).place(relx=self.relx + marginx, rely=self.rely, relwidth=0.1, relheight=0.1)

			Entry(
				self.window,
			).place(relx=self.relx + 0.15 + marginx, rely=self.rely, relwidth=0.2, relheight=0.1)

			marginx += 0.32


class MultipleFormsFrame():
	def __init__(self, window, tableModel, savedTable, values={}):
		self.window = window
		self.tableModel = tableModel
		self.savedTable = savedTable
		self.values = values

		self.contentFrame = Frame(self.window)
	
	def createGui(self):
		self.contentFrame.pack(fill='both', expand='yes')

		fields = []
		for syntax, field in self.savedTable.sqlSyntax.items():
			if syntax != self.tableModel.pk:
				fields.append(field)
			
		mf = MultipleForms(self.window, (0.01, 0.1), fields)
		mf.createGui()

	
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
print(objCt.getKienTrucSu())
root = Tk()
root.geometry('600x600')
mft = MultipleFormsFrame(root, Congtrinh, Thietke)
mft.createGui()
root.mainloop()



	
