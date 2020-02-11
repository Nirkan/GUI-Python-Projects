
# Creating a GUI window using tkinter

from tkinter import * 

window  = Tk()

window.title("Welcome to GUI app")

lbl = Label(window, text = "Hello", font=("Arial Bold", 50))

lbl.grid(column=0, row= 0)

txt = Entry(window, width = 10)

txt.grid(column=2, row=0)

def clicked():

	res = "Welcome to " + 	txt.get()

	lbl.configure(text = "Button was clicked !!")

btn = Button(window, text= "Click Me", bg = "Yellow", fg = 'red', command = clicked)

btn.grid(column=1, row= 0)

window.mainloop()

window.geometry('450x300')


# Adding a combobox widget

from tkinter.ttk import *

from tkinter.ttk import *

window  = Tk()

window.title("Welcome to GUI app")

window.geometry('500x400')

combo = Combobox(window)

combo['values'] = (1, 2, 3, 4, 5, "Text")

combo.current(1)  # set the selected item

combo.grid(column=0, row=0)

window.mainloop()

combo.get()


# Add a Checkbutton widget(Tkinter checkbox)

from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to GUI app")

window.geometry('500x400')

chk_state = BooleanVar()

chk_state.set(True) #set check state

chk = Checkbutton(window, text="Choose", var=chk_state)

chk.grid(column=0, row=0)

chk_state = IntVar()

chk_state.set(0)

window.mainloop()

# Add radio buttons widgets (Get radio button value)

from tkinter import *

from tkinter.ttk import *

window = Tk()

window.title("Welcome to GUI app")

window.geometry('500x500')

selected = IntVar()

rad1 = Radiobutton(window, text = 'First', value = 1, variable = selected)

rad2 = Radiobutton(window, text = 'Second', value = 2, variable = selected)

rad3 = Radiobutton(window, text= 'Third', value = 3, variable = selected)

def clicked():
      print(selected.get())

btn = Button(window, text='Click Me', command = clicked)

rad1.grid(column= 0, row = 0)

rad2.grid(column= 1, row = 0)

rad3.grid(column= 2, row = 0)

btn.grid(column = 3, row = 0)

window.mainloop()


# Add a ScrolledText widget(Tkinter textarea)


from tkinter import scrolledtext

from tkinter import scrolledtext

window = Tk()

window.title('Welcome to GUI app')

window.geometry('500x500')

txt = scrolledtext.ScrolledText(window, width = 40, height = 10)

txt.grid(column = 0, row = 0)

window.mainloop()


# Creating a MessageBox

from tkinter import *

from tkinter import messagebox

window = Tk()

window.title('Welcome to GUI app')

window.geometry('500x400')

def clicked():
     messagebox.showinfo('Important Message', 'Hello There. Whats up!')

btn = Button(window, text = 'Click here', command = clicked)

btn.grid(column = 0, row = 0)

window.mainloop()


# Adding a SpinBox(numbers widget)

from tkinter import *

window = Tk()

window.title("Welcome to GUI app")

window.geometry("500x400")

spin = Spinbox(window, from_= 0, to = 100, width = 5)

spin.grid(column = 0, row = 0)

window.mainloop()


# Adding a Progressbar widget

from tkinter import *

from tkinter.ttk import Progressbar

from tkinter import ttk

window = Tk()

window.title('Welcome to GUI app')

window.geometry('450x400')

style = ttk.Style()

style.theme_use('default')

style.configure('black.Horizontal.TProgressbar', background = 'Green')

bar = Progressbar(window, length = 200, style = 'black.Horizontal.TProgressbar')

bar['value'] = 70

bar.grid(column = 0, row = 0)

window.mainloop()


# Adding a Menu bar

from tkinter import *

from tkinter import Menu

window = Tk()

window.title("Welcome to GUI app")

menu = Menu(window)

new_item = Menu(menu)

new_item.add_command(label = 'New')

new_item.add_separator()

new_item.add_command(label = 'Edit')

new_item.add_separator()

new_item.add_command(label = 'save')

menu.add_cascade(label = 'File', menu = new_item)

window.config(menu = menu)

window.mainloop()



# Adding widgets to Notebooks (tab control)

from tkinter import *

from tkinter import ttk

window = Tk()

window.title("Welcome to GUI app")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)

tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text = 'First')

tab_control.add(tab2, text = 'Second')

lbl1 = Label(tab1, text = 'label1')

lbl1.grid(column = 0, row = 0)

lbl2 = Label(tab2, text = 'lable2')

lbl2.grid(column = 0, row = 0)

tab_control.pack(expand = 1, fill = 'both')

window.geometry('450x300')

window.mainloop()
