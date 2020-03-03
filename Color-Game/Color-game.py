from tkinter import * 
import random

# Making a list of possible colours.

colours = ['Brown', 'Purple', 'White', 'Orange', 'Yellow', 'Black', 'Pink', 'Green', 'Blue', 'Red']

score = 0

# We give intial value of time to be 30 seconds to take in account for the time left

time = 30

# Creating a function to  initate the game.

def beginGame(event):

	if time == 30:

		# starting the countdown timer
		countdown()

	# Running the function to chose the next color
	nextcolor()


def nextcolor():
	
	global score
	global time

	# if a game is in play
	if time > 0:

		# making the text entry box active 
		colour_entry.focus_set()

		if colour_entry.get().lower() == colours[1].lower():

			score += 1

		# Clearing the entry in the box
		
		colour_entry.delete(0, END)

		random.shuffle(colours)

		# Change the colour to type, by changing the text and the colour to a random colour value

		colour.config(fg = str(colours[1]), text = str(colours[0]))

		# Updating the score.
		scoreLabel.config(text = 'Score: ' + str(score))


# Countdown Timer Function

def countdown():

	global time 

	# If the game is played 

	if time > 0 :

		# Decrement the value

		time -= 1

		# Updating the time left label

		timeLabel.config(text = 'Time left : ' + str(time))

		# Running the function again after 1 second
	
		timeLabel.after(1000, countdown)


# Driver code 

""" The following __name__ = main implies the following code only runs for this .py file and will run if 
we import modules from the functions above into another python code. """ 


if __name__ == '__main__':      
	
	root = Tk()

	# Setting the title
	root.title('Color Game')

	# Setting the geometry of the window
	root.geometry('375x200')

	# Setting an instruction label
	instructions = Label(root, text = 'Type in the clour of the words, Do not type text colour! ', font = ('Helvetica', 12))
	instructions.pack()

	# Creating a score label
	scoreLabel = Label(root, text = 'score : '+ str(score), font = ('Helvetica', 12))
	scoreLabel.pack()

	# Creating a Time Label
	timeLabel = Label(root, text = 'Time Left : ' + str(time), font = ('Helvetica', 12))
	timeLabel.pack()

	# Creating a colour label
	colour = Label(root, font = ('Helvetica', 12))
	colour.pack()

	# Entry box for the input from user
	colour_entry = Entry(root)


	colour_entry  = Entry(root)
	
	colour_entry.focus_set()
	root.bind('<Return>', beginGame)

	colour_entry.pack()


	root.mainloop()





















