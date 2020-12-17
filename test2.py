from tkinter import *
from tkinter import ttk


def scrollFrame():
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

	for thing in range(10):
		Label(second_frame, text='Ho ten: ').grid(
								row=thing, 
								column=0, 
								pady=10, 
								padx=10, 
								ipadx=20,
								ipady=10
								)
		Entry(second_frame).grid(
								row=thing, 
								column=1, 
								pady=10,  
								ipadx=40,
								ipady=10
								)
		Label(second_frame, text='Ngay tham gia').grid(
														row=thing, 
														column=2, 
														pady=10, 
														padx=10,
														ipadx=20,
														ipady=10				
														)

		Entry(second_frame).grid(
								row=thing, 
								column=3, 
								pady=10, 
								ipadx=40,
								ipady=10
								)

		Label(second_frame, text='So ngay').grid(
														row=thing, 
														column=4, 
														pady=10, 
														padx=10,
														ipadx=20,
														ipady=10				
														)

		Entry(second_frame).grid(
								row=thing, 
								column=5, 
								pady=10, 
								ipadx=40,
								ipady=10
								)




	root.mainloop()


scrollFrame()