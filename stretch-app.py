# sandfly.py
# Dimitra Doiphode, Austin Sohn, Zakee Khattak, Ernesto Hooghkirk, Savannah Bauer
# TODO: 
# Phase 1 -
# Complete! :) 
# Phase 2 
# - Image accompanying each stretch to demonstrate how to do it
# - Dark mode
# - Sound/alarm
# - Similar stretch button? (see similar stretches)
# -
# Phase 3 
# - gif accompanying each stretch to demonstrate how to do it
# - reward system?
# -
# -
# -

# importing whole module 
import tkinter
import random
# importing strftime function to 
# retrieve system's time 
from time import strftime 
from tkinter import messagebox

# creating tkinter window 
fontName = 'Georgia'
root = tkinter.Tk() 
root.title("Project: Sandfly")

# This function is used to 
# display time on the label 
def time(): 
	string = strftime('%I:%M %p') 
	lbl.config(text = string) 
	lbl.after(1000, time) 

# Styling the label widget so that clock 
# will look more attractive 
lbl = tkinter.Label(root, font = (fontName, 40)) 

# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center') 
time()

quotes = [
	'"The key to success is to start before \nyou are ready." \n- Marie Forleo',
    '"Challenges are what make life interesting. \nOvercoming them is what makes life meaningful." \n- Joshua J. Marine',
    '"If people are doubting how far you can go, \ngo so far that you can\'t hear them anymore." \n- Michele Ruiz',
	'"If you are always trying to be normal, \nyou will never know how amazing you can be." \n- Maya Angelou',
	'"If you\'re going through hell, keep going."\n - Winston Churchill'
]
move = tkinter.Label(text = random.choice(quotes), font = (fontName, 15))
move.pack()

stretch = [
	'5 leg lunges on each leg. \n\nStand with one foot forward and one leg back. \nBend the forward knee into a right angle, and hold for five seconds.',
    'Torso Stretch. \n\nKeep your feet firmly on the ground, facing forward. \nTwist your upper body in the direction of your arms resting on the back of the chair. \nHold for 10 to 30 seconds. \nRepeat on the other side.',
    'Start with cartwheels for 30 seconds \n\nThen complete 30 seconds of windmills for each arm',
	'Child\'s pose. \n\nBegin at table top position. \nSlowly extend your arms in front of you and \ntry to put your face on the floor. \nHold for 20 to 30 seconds',
	'Upper Body Arm Stretch. \n\nLock your fingers and raise them above your head. \nKeep them up there for thirty seconds. \nRaise the roof, baby.',
	'Hamstring Stretch. \n\nRemaining seated, extend one leg outward. \nReach towards your toes. \nHold for 10 to 30 seconds. \nRepeat on the other side.',
	'Neck Stretch. \n\nGently pull your head toward each shoulder \nuntil a light stretch is felt. \nHold pose for 10 to 15 seconds. \nAlternate once on each side.'
]


counter = 0
def update_label(): 
	global counter
	getTime = float(eb1.get())
	millisec = int(getTime * 60000) # convert minutes to miliseconds
	print(getTime) # delete later
	lbl.configure()
	counter += 1
	if(counter > 1):
		messagebox.showinfo(title = "Time to Stretch!", message = random.choice(stretch))

	root.after(millisec, update_label) # after 30 sec, executes update_label() func 


#root.after(10000, update_label) # stops from running the first time

timeLabel = tkinter.Label(root, text = "\nEnter time interval (minutes): ")
timeLabel.pack(anchor = 'w')
eb1 = tkinter.Entry(root)
eb1.pack(anchor = 'nw')
bt1 = tkinter.Button(text= "Enter", command = update_label)
bt1.pack(anchor = 'w')

def display_stretch():
	print("hello there")
	messagebox.showinfo(title = "Time to Stretch!", message = random.choice(stretch))
	pass

loadNewStretch = tkinter.Label(root, text = "Get New Stretch")
loadNewStretch.pack(anchor = 'w')
bt1 = tkinter.Button(text= "Enter", command = display_stretch)
bt1.pack(anchor = 'w')

root.mainloop()  # leave at end of program