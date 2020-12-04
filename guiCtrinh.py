import tkinter as tk
from tkinter import ttk

from mysqlConnection import ConnectionToMySQl
from table import TableTkinter

HEIGHT = 500
WIDTH  = 1200

btnBGColor = 'green'

connection = ConnectionToMySQl()


def change():
	columns = {
		"stt": 'stt_ctr',
		"công trình": 'ten_ctr', 
		"địa chỉ": 'diachi_ctr',
		"tên chủ": 'ten_chu',
		"nhà thầu": 'ten_thau', 
		"tỉnh thành": 'tinh_thanh', 
		"kinh phí": 'kinh_phi', 
		"ngày bắt đầu": 'ngay_bd',
	}

	fT = columns.get(filterTopic.get())
	oT = columns.get(orderByTopic.get())
	inputData = filterEntry.get()

	statement = f"select * from cgtrinh where {fT} like '%{inputData}%'"

	if inputData == "":
		statement = "select * from cgtrinh"

	statement += " order by " + oT + " desc"
	data = generateData(connection.getQueryset(statement))
	table.insertData(data)


def generateData(querySet):
	data = []
	rowsData = []

	for row in querySet:
		stt = str(row[0])
		tCtr = row[1]
		dcctr = row[2]
		tthanh = row[3]
		kphi = str(row[4]) + ' trieu đ'
		tchu = row[5]
		nthau = row[6]
		nbdau = str(row[7])

		rowsData.append(stt)
		rowsData.append(tCtr)
		rowsData.append(dcctr)
		rowsData.append(tthanh)
		rowsData.append(kphi)
		rowsData.append(tchu)
		rowsData.append(nthau)
		rowsData.append(nbdau)

		data.append(rowsData)
		rowsData = []

	return data



root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

btn = tk.Button(canvas, bg='green', fg='white', command=change, text='Search')
btn.place(relx=0.05, rely=0.05, relwidth=0.1, relheight=0.05)

filterEntry = tk.Entry(canvas, font=("Gothic", 13), fg="#2019CC")
filterEntry.place(relx=0.15, rely=0.05, relwidth=0.4, relheight=0.05)

filterLb = tk.Label(canvas, bg='black', fg='white', text='Filter By')
filterLb.place(relx=0.58, rely=0.05, relwidth=0.075, relheight=0.05)

filterTopic = tk.StringVar()
filterTopic.set('công trình')
filterDropDown = tk.OptionMenu(canvas, filterTopic, 'công trình', 'tỉnh thành', 'nhà thầu')
filterDropDown.place(relx=0.65, rely=0.05, relwidth=0.12, relheight=0.05)

orderLb = tk.Label(canvas, bg='black', fg='white', text='Order By')
orderLb.place(relx=0.78, rely=0.05, relwidth=0.075, relheight=0.05)

orderByTopic = tk.StringVar()
orderByTopic.set('công trình')
orderDropdown = tk.OptionMenu(canvas, orderByTopic, 'công trình', 'tỉnh thành', 'nhà thầu', 'kinh phí', 'ngày bắt đầu')
orderDropdown.place(relx=0.85, rely=0.05, relwidth=0.12, relheight=0.05)


frame = tk.Frame(canvas)
frame.place(relx=0, rely=0.15, relwidth=1, relheight=1)

table = TableTkinter(frame, 0.05, 0.05, 0.9, 0.5)

colData = {
	'stt': ('STT', 10, 'e'),
	'tcrt': ('Cong Trinh', 100, 'e'),
	'diachi_ctr': ('Dia Chi', 100, 'e'),
	'tthanh': ('Tinh Thanh', 50, 'e'),
	'kphi': ('Kinh Phi', 25, 'e'),
	'tchu': ('Ten Chu', 100, 'e'),
	'nthau': ('Nha Thau', 100, 'e'),
	'ngaybd': ('Bat Dau', 50, 'e')
}

table.setColumns(colData)
data = generateData(connection.getQueryset("select * from cgtrinh"))
table.insertData(data)


root.mainloop()