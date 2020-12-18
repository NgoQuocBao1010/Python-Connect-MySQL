from tkinter import *
from tkinter import ttk


def scrollFrame(values, dValues, tableModel):
	# print(values, tableModel.table)

	def save():
		values = {}

		for key, item in fDict.items():
			inputDictGet = {}
			for field, inputF in item.items():
				inputDictGet.setdefault(field, inputF.get())
			values.setdefault(key, inputDictGet)
		
		print(obj.getPk())
		print(values)


	root = Tk()
	root.title('Learn To Code at Codemy.com')
	root.geometry("1000x400")

	# Create A Main Frame
	main_frame = Frame(root)
	main_frame.pack(fill=BOTH, expand=1)

	# Create A Canvas
	my_canvas = Canvas(main_frame)
	my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

	# Add A Scrollbar To The Canvas
	my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
	my_scrollbar.pack(side=RIGHT, fill=Y)

	# Configure The Canvas
	my_canvas.configure(yscrollcommand=my_scrollbar.set)
	my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

	# Create ANOTHER Frame INSIDE the Canvas
	second_frame = Frame(my_canvas)

	# Add that New frame To a Window In The Canvas
	my_canvas.create_window((0,0), window=second_frame, anchor="nw")

	fields = list(tableModel.formsField().get('arribute'))
	
	data = values[0] if type(values[0]) is list else values[1]
	obj = values[1] if type(values[0]) is list else values[0]
	startField = 0 if type(values[0]) is list else 1

	textLb = 'Điền thông tin cho ' + str(obj)
	Label(second_frame, text=textLb, bg='gray').grid(
		row=0, 
		column=0, 
		pady=10, 
		padx=2, 
		ipadx=20,
		ipady=10
		)

	Button(second_frame, text='Save', bg='gray', command=save).grid(
		row=0, 
		column=5, 
		pady=10, 
		padx=2, 
		ipadx=20,
		ipady=10
		)

	row = 2
	fDict = {}
	for d in data:
		Label(second_frame, text=fields[startField], bg='gray').grid(
								row=row, 
								column=0, 
								pady=10, 
								padx=2, 
								ipadx=20,
								ipady=10
								)
		Label(second_frame, text=d).grid(
								row=row, 
								column=1, 
								pady=10,  
								ipadx=20,
								ipady=10
								)


		col = 2
		inputsDict = {}
		for i in range(2, len(fields)):
			Label(second_frame, text=fields[i]).grid(
				row=row, 
				column=col, 
				pady=10, 
				padx=2,
				ipadx=20,
				ipady=10				
				)

			fieldVar = StringVar()
			fieldVar.set('')
			Entry(second_frame, textvariable=fieldVar).grid(
				row=row, 
				column=col + 1, 
				pady=2, 
				ipadx=20,
				ipady=10
				)
			col += 2
			inputsDict.setdefault(fields[i], fieldVar)
		
		fDict.setdefault(d, inputsDict)

		row += 1




	root.mainloop()


# scrollFrame()