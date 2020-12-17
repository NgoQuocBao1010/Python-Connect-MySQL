import tkinter as tk
from tkinter import ttk
from PIL import ImageTk
import  PIL.Image

from test2 import *
from mysqlConnection import ConnectionToMySQl

def checkList():
	def test(event):
		row = table.identify_row(event.y)
		tag = table.item(row, 'tags')[0]
		
		if tag == 'checked':
			table.item(row, tags='unchecked')
		else:
			table.item(row, tag='checked')


	def getChecked():
		for rowId in table.get_children():
			row = table.item(rowId)
			itemsTag = row['tags'][0]

			if itemsTag == 'checked':
				print(row)



	root = tk.Tk()
	root.geometry('1000x400')

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
	table.heading(1, text='Ho ten CN')

	mysqlConn = ConnectionToMySQl()
	rows = mysqlConn.getQueryset('select hoten_cn from congnhan')

	for data in rows:
		table.insert("", "end", values=data, tags='unchecked')


	table.bind('<Button 1>', test)

	root.mainloop()



checkList()