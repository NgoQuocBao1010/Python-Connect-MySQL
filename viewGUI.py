import tkinter as tk
from tkinter import ttk

from mysqlConnection import ConnectionToMySQl
from table import TableTkinter

HEIGHT = 500
WIDTH  = 1200

fontHeadings = ('Times New Roman', 15,'bold')
fontName = ('Courier', 30,'bold')
fontName2 = ('Times New Roman', 15)

connection = ConnectionToMySQl()

data = {}

def generateData(columns, data):
	data = connection.getObject('cgtrinh', (columns, data))
	
	sttCtr = data.get('STT_CTR')
	statement = f'select hoten_kts from thietke where stt_ctr = {sttCtr}'

	architects = connection.getQueryset(statement)
	data.setdefault('kts', architects[0][0])

	statement = f'select hoten_cn from thamgia where stt_ctr = {sttCtr}'
	engineers = connection.getQueryset(statement)
	
	engineersList = []
	engineer = []

	for index in range(len(engineers)):
		engineer.append(index + 1)
		engineer.append(engineers[index][0])
		engineersList.append(engineer)
		engineer = []

	print(engineersList)
	data.setdefault('cntb', engineersList)



	return data

data = generateData('stt_ctr', 1)
root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

tCtrName = tk.Label(canvas, fg='black', text=data.get('TEN_CTR').upper(), font=fontName)
tCtrName.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)

detailFrame = tk.Frame(canvas)
detailFrame.place(relx=0.05, rely=0.2, relwidth=0.6, relheight=0.6)

constructFrame = tk.Frame(canvas)
constructFrame.place(relx=0.65, rely=0.2, relwidth=0.3, relheight=0.6)

row = 0
for col, info in data.items():
	if col.lower() in ('stt_ctr', 'ten_ctr', 'kts', 'cntb'):
		continue

	nameLb = tk.Label(detailFrame, fg='black', text=col + ':', font=fontName2, anchor='nw')
	nameLb.grid(row=row, column=1, ipadx=20, ipady=5, sticky='W')

	detailLb = tk.Label(detailFrame, fg='black', text=data.get(col), font=fontName2, anchor='nw')
	detailLb.grid(row=row, column=2, ipadx=250, ipady=5, sticky='W')
	row += 1

ktsLb = tk.Label(constructFrame, fg='black', text='Designed by: ', font=('Times New Roman', 11), anchor='nw')
ktsLb.place(relx=0, rely=0.0, relwidth=0.3, relheight=0.1)

ktsNameLb = tk.Label(constructFrame, fg='black', text=data.get('kts'), font=('Times New Roman', 15), anchor='nw')
ktsNameLb.place(relx=0.32, rely=0.0, relwidth=0.5, relheight=0.1)

cntbLb = tk.Label(constructFrame, fg='black', text='Cac cong nhan da lam viec: ', font=('Times New Roman', 11), anchor='nw')
cntbLb.place(relx=0, rely=0.28, relwidth=0.7, relheight=0.1)

tableCN = TableTkinter(constructFrame, 0, 0.4, 0.6, 0.4)
colData = {
	'stt': ('STT', 10, 'c'),
	'tcrt': ('Ten Cong Nhan', 100, 'w'),
}
tableCN.setColumns(colData)
tableCN.insertData(data.get('cntb'))
root.mainloop()

# from tkinter import Tk, font
# root = Tk()
# print(font.families())