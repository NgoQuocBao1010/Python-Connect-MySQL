from tkinter import *
from tkinter import ttk

root = Tk()

wrapper1 = LabelFrame(root)
wrapper2 = LabelFrame(root)

mycanvas = Canvas(wrapper1)
mycanvas.place(relx=0, rely=0, relwidth=1, relheight=1)

ycrollbar = ttk.Scrollbar(wrapper1, orient='vertical', command=mycanvas.yview)
# ycrollbar.pack(side=RIGHT, fill='y')
ycrollbar.place(relx=0.9, rely=0, relwidth=0.02, relheight=1)

mycanvas.configure(yscrollcommand=ycrollbar.set)

mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox('all')))

myFrame = ttk.Frame(mycanvas)
myFrame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
# mycanvas.create_window((0, 0), window=myFrame, anchor='nw')

wrapper1.pack(fill='both', expand='yes', padx=10, pady=10)
wrapper2.pack(fill='both', expand='yes', padx=10, pady=10)

f = 0.1
for i in range(50):
	b = Button(myFrame, text=f'My Button - {i}')
	b.place(relx=0, rely=f, relwidth=0.5, relheight=0.1)
	# Frame(myFrame, bg='blue').place(relx=0, rely=f, relwidth=0.5, relheight=0.1)
	f += 0.2

root.geometry('500x500')
root.title('Myscrollbar')
root.mainloop()