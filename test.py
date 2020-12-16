import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def test(event):
	row = table.identify_row(event.y)
	tag = table.item(row, 'tags')[0]
	
	if tag == 'checked':
		table.item(row, tags='unchecked')
	else:
		table.item(row, tag='checked')



root = tk.Tk()
root.geometry('1000x400')

table = ttk.Treeview(root, columns=(1, 2, 3))
table.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.7)

vsb = ttk.Scrollbar(root, orient="vertical", command=table.yview)
vsb.place(relx=0.95, rely=0.1, relwidth=0.02, relheight=0.7)
table.configure(yscrollcommand=vsb.set)

imgChecked = ImageTk.PhotoImage(Image.open('checked(1).png'))
imgUnchecked = ImageTk.PhotoImage(Image.open('unchecked(1).png'))

# table["show"] = 'headings'

style = ttk.Style(table)
style.configure('Treeview', rowheight=30)
# style.map('Treeview', background=[('selected', '#BFBFBF')])

table.tag_configure('checked', image=imgChecked)
table.tag_configure('unchecked', image=imgUnchecked)
table.tag_configure('bg', background='yellow')

table.heading(0, text='')
table.heading(1, text='gg')
table.heading(2, text='gg2')
table.heading(3, text='gg3')


for i in range(20):
	table.insert("", "end", values=('haha', i, i+5), tags='unchecked')

table.bind('<Button 1>', test)

root.mainloop()