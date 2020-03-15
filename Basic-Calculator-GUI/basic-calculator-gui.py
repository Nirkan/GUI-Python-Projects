from tkinter import *

class Calculator:
	def __init__(self, master):
		self.master = master
		master.title("Basic Calculator")

	        # Creating screen widget
		self.screen = Text(master, state='disabled', width=30, height=3, background = 'yellow', foreground='blue')


	        # Positioning screen in window
		self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
		self.screen.configure(state='normal')

	        # initializing screen value as empty
		self.equation = ' '


                # Creating buttons using method createButton
		b1 = self.createButton(7)
		b2 = self.createButton(8)
		b3 = self.createButton(9)
		b4 = self.createButton(u"\u232B",None)
		b5 = self.createButton(4)
		b6 = self.createButton(5)
		b7 = self.createButton(6)
		b8 = self.createButton(u"\u00F7")
		b9 = self.createButton(1)
		b10 = self.createButton(2)
		b11 = self.createButton(3)
		b12 = self.createButton('*')
		b13 = self.createButton('.')
		b14 = self.createButton(0)
		b15 = self.createButton('+')
		b16 = self.createButton('-')
		b17 = self.createButton('=',None,34)
		

		#buttons stored in list
		buttons  = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17]


		# initializing counter
		count = 0

		# arranging buttons with grid manager

		for row in range(1,5):
			for column in range(4):
				buttons[count].grid(row=row, column=column)
				count += 1

		# arrange last button '=' at the bottom
		
		buttons[16].grid(row=5, column=0, columnspan=4)


	# Create a function createButton which will return and create a Button in tkinter. createButton function has been called above.

	def createButton(self, val, write=True, width=7):
			return Button(self.master, text=val, command=lambda: self.click(val, write), width=width)


	# Create a function click that handles what happens when you click.

	def click(self, text, write):
		if write == None:
			if text == '=' and self.equation:
				self.equation = re.sub(u"\u00F7", '/', self.equation)  # change the unicode u"\u00F7" to '/'
				print(self.equation)
				answer = str(eval(self.equation))
				self.clear_screen()
				self.insert_screen(answer, newline = True)
			elif text == u"\u232B":
				self.clear_screen()
		else:
			self.insert_screen(text)  # adding text on the screen if write is not None.


	def clear_screen(self):			# clear the screen
		self.equation = ''
		self.screen.configure(state = 'normal')
		self.screen.delete('1.0', END)

	def insert_screen(self, value, newline = False):    # recording every value inserted on the screen
		self.screen.configure(state = 'normal')
		self.screen.insert(END, value)
		self.equation += str(value)
		self.screen.configure(state = 'disabled')


root = Tk()
my_gui = Calculator(root)
root.mainloop()
