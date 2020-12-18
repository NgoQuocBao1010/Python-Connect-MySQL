import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import  PIL.Image

from test2 import *
from model import *
from mysqlConnection import ConnectionToMySQl

def checkList(tableModel, objectKey):
	def test(event):
		row = table.identify_row(event.y)
		tag = table.item(row, 'tags')[0]
		
		if tag == 'checked':
			table.item(row, tags='unchecked')
		else:
			table.item(row, tag='checked')


	def getChecked():
		values = []
		for rowId in table.get_children():
			row = table.item(rowId)
			itemsTag = row['tags'][0]

			if itemsTag == 'checked':
				values.append(row['values'][0])

		if type(objectKey) is Congtrinh:
			values = [values, objectKey]

		else:
			values = [objectKey, values]

		root.destroy()
		scrollFrame(values, tModel)



	root = tk.Tk()
	root.geometry('1000x400')

	mysqlConn = ConnectionToMySQl()
	model = tableModel.table
	modelName = tableModel.tableName
	field = tableModel.imptField
	colName = tableModel.sqlSyntax.get(field)

	if type(objectKey) is Congtrinh:
		tModel = Thamgia if model == 'congnhan' else Thietke

	else:
		tModel = Thamgia if type(objectKey) is Congnhan else Thietke
		# data = mysqlConn.getQueryset(f'select {field} from {tModel.table}')


	textLb = 'Chọn ' + modelName + ' cho ' + objectKey.tableName + ' ' + str(objectKey)
	nameLb = tk.Label(root, text=textLb)
	nameLb.place(relx=0.05, rely=0.05, relwidth=0.4, relheight=0.05)

	table = ttk.Treeview(root, columns=(1, ))
	table.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.7)

	vsb = ttk.Scrollbar(root, orient="vertical", command=table.yview)
	vsb.place(relx=0.95, rely=0.1, relwidth=0.02, relheight=0.7)
	table.configure(yscrollcommand=vsb.set)

	btn = tk.Button(root, text='submit', command=getChecked)
	btn.place(relx=0.75, rely=0.85, relwidth=0.05, relheight=0.05)

	imgChecked = ImageTk.PhotoImage(PIL.Image.open('checked(1).png'))
	imgUnchecked = ImageTk.PhotoImage(PIL.Image.open('unchecked(1).png'))

	# table["show"] = 'headings'

	style = ttk.Style(table)
	style.configure('Treeview', rowheight=30)
	# style.map('Treeview', background=[('selected', '#BFBFBF')])

	table.tag_configure('checked', image=imgChecked)
	table.tag_configure('unchecked', image=imgUnchecked)
	table.tag_configure('bg', background='yellow')

	table.heading(0, text='')
	table.heading(1, text=colName)

	rows = mysqlConn.getQueryset(f'select {field} from {model}')

	for data in rows:
		table.insert("", "end", values=data, tags='unchecked')


	table.bind('<Button 1>', test)

	root.mainloop()


v = {
	'STT': 8, 
	'Tên Công Trình': 'nha rieng cua bao', 
	'Địa Chỉ': 'hung phu', 
	'Tỉnh Thành': 'ha noi', 
	'Kinh Phí': 100, 
	'Tên Chủ': 'quoc bao', 
	'Tên Thầu': 'tran khai hoan', 
	'Ngày Bắt Đầu': '1994-09-06'
}

obj = Congtrinh(*v.values())
# print(type(obj) is Congtrinh)

a = {
	'Họ và tên': 'le quyet thang', 
	'Năm sinh': 54, 
	'Năm vào nghề': 74, 
	'Chuyên môn': 'son'
}

obj2 = Congnhan(*a.values())

ty = {
	'Họ và tên': 'nguyen thi anh thu', 
	'Năm sinh': 1970, 
	'Phái': 0, 
	'Nơi tốt nghiệp': 
	'new orlean usa', 
	'Địa chỉ': 'khu i dhct tp can tho'
	}

obj3 = Ktrucsu(*ty.values())


# checkList(Congtrinh, objectKey=obj2)
# checkList(Congnhan, objectKey=obj)
# checkList(Congtrinh, objectKey=obj3)