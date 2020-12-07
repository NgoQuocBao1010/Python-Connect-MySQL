import tkinter as tk
from tkinter import ttk

from mysqlConnection import ConnectionToMySQl
from tableGUI import TableGUI
import model

TITLE_FONT = ("Comic Sans MS", 25, "bold")
LABEL_FONT = ("Times New Roman", 14)


def addElement(window, tableModel):
	def submit():
		for field in fieldNames:
			entry = fieldInputs.get(field).get()
			print(field, entry)


	fieldNames = tableModel.detailsField().get('arribute')
	fieldInputs = {}

	titleLb = tk.Label(window, fg='black', text='Thêm ' + tableModel.tableName, font=TITLE_FONT)
	titleLb.place(relx=0.2, rely=0.02, relwidth=0.6, relheight=0.1)

	lbRely = 0.2
	for field in fieldNames:
		fieldLb = tk.Label(window, fg='black', text=field, font=LABEL_FONT, bg='gray')
		fieldLb.place(relx=0.02, rely=lbRely, relwidth=0.13, relheight=0.07)

		fieldEnt = tk.Entry(window, fg='black', text=field, font=LABEL_FONT)
		fieldEnt.place(relx=0.16, rely=lbRely, relwidth=0.25, relheight=0.07)

		lbRely += 0.12
		fieldInputs.setdefault(field, fieldEnt)

	fkFields = tableModel.detailsField().get("forgeinKey").keys()

	lbRely = 0.2
	for field in fkFields:
		fieldLb = tk.Label(window, fg='black', text=field, font=LABEL_FONT, bg='gray')
		fieldLb.place(relx=0.6, rely=lbRely, relwidth=0.13, relheight=0.07)

		tModel = tableModel.detailsField().get("forgeinKey").get(field)
		conn = ConnectionToMySQl()
		statement = f'select {tModel.pk} from {tModel.tableName}'
		rs = conn.getQueryset(statement)
		print(rs)
		# fieldVar = tk.StringVar()
		# dropdown = tk.OptionMenu(window)

		lbRely += 0.3

	

	submitBtn = tk.Button(window, fg='black', text='Submit', font=LABEL_FONT, bg='gray', command=submit)
	submitBtn.place(relx=0.85, rely=0.8, relwidth=0.1, relheight=0.07)








root = tk.Tk()
root.title('My Application')
root.geometry('1400x600')

addElement(root, model.Congtrinh)

root.mainloop()