import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import  PIL.Image

from multipleForm import *
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
		dValues = []
		uValues = []

		for rowId in table.get_children():
			row = table.item(rowId)
			itemsTag = row['tags'][0]

			if itemsTag == 'checked':
				values.append(row['values'][0])
		
		for v in prefillValues:
			if v[0] not in values:
				dValues.append(v[0])
			
			if v[0] in values:
				uValues.append(v[0])
		
		# print(values)
		# print(dValues)
		# print(uValues)

		if len(values) == 0:
			root.destroy()
			return

		if type(objectKey) is Congtrinh:
			values = [values, objectKey]

		else:
			values = [objectKey, values]

		root.destroy()
		scrollFrame(values, uValues, dValues, tModel)



	root = tk.Tk()
	root.title('Check list')
	root.geometry('1000x400')

	mysqlConn = ConnectionToMySQl()
	model = tableModel.table
	modelName = tableModel.tableName
	field = tableModel.imptField
	colName = tableModel.sqlSyntax.get(field)

	if type(objectKey) is Congtrinh:
		tModel = Thamgia if model == 'congnhan' else Thietke
		prefillValues = objectKey.getCongNhan() if model == 'congnhan' else objectKey.getKienTrucSu()
	else:
		tModel = Thamgia if type(objectKey) is Congnhan else Thietke
		prefillValues = objectKey.getCongTrinh()
		


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

	table.tag_configure('checked', image=imgChecked)
	table.tag_configure('unchecked', image=imgUnchecked)
	table.tag_configure('bg', background='yellow')

	table.heading(0, text='')
	table.heading(1, text=colName)

	rows = mysqlConn.getQueryset(f'select {field} from {model}')

	for data in rows:
		tags = 'checked' if data in prefillValues else 'unchecked'
		table.insert("", "end", values=data, tags=tags)


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
	'Họ và tên': 'le thanh tung', 
	'Năm sinh': 1956, 
	'Phái': 1, 
	'Nơi tốt nghiệp': 'tp hcm', 
	'Địa chỉ': '25 duong 3/2 tp bien hoa'
	}

obj3 = Ktrucsu(*ty.values())


# checkList(Congtrinh, 	objectKey=obj2)
# checkList(Congnhan, 	objectKey=obj)
# checkList(Congtrinh, 	objectKey=obj3)