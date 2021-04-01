# sandfly.py
# Dimitra Doiphode, Austin Sohn, Zakee Khattak, Ernesto Hooghkirk, Savannah Bauer
# TODO: 
# Phase 1 -
# Complete! :) 
# Phase 2 
# - Image accompanying each stretch to demonstrate how to do it
# - Dark mode -CHECK
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
root.title("Project Sandfly: Stretch Reminder")
root.configure(bg='#E19669')

# This function is used to 
# display time on the label 
def time(): 
	string = strftime('%I:%M %p') 
	lbl.config(text = string) 
	lbl.after(1000, time) 

# Styling the label widget so that clock 
# will look more attractive 
lbl = tkinter.Label(root, font = (fontName, 40)) 
lbl.configure(bg='#E19669')

# Placing clock at the centre 
# of the tkinter window 
lbl.pack(anchor = 'center') 
time()

quotes = [
	'\n"The key to success is to start before \nyou are ready." \n- Marie Forleo\n',
    '\n"Challenges are what make life interesting. \nOvercoming them is what makes life meaningful." \n- Joshua J. Marine\n',
    '\n"If people are doubting how far you can go, \ngo so far that you can\'t hear them anymore." \n- Michele Ruiz\n',
	'\n"If you are always trying to be normal, \nyou will never know how amazing you can be." \n- Maya Angelou\n',
	'\n"If you\'re going through hell, keep going."\n - Winston Churchill\n'
]
move = tkinter.Label(text = random.choice(quotes), font = (fontName, 17), relief = "solid")
move.configure(bg='#D67540')
move.pack(padx = 20, pady=6)

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

timeLabel = tkinter.Label(root, text = "Enter time interval (minutes): ", font = (fontName, 15))
timeLabel.configure(bg='#E19669')
timeLabel.pack(anchor = 'w')
eb1 = tkinter.Entry(root)
eb1.pack(padx = 20, pady=6, anchor = 'nw')
bt1 = tkinter.Button(padx = 10, pady=10,text= "Enter", command = update_label)
bt1.configure(bg='#CF6024')
bt1.pack(padx = 20, pady=6, anchor = 'nw')

def display_stretch():
	print("hello there")
	messagebox.showinfo(title = "Time to Stretch!", message = random.choice(stretch))
	pass

loadNewStretch = tkinter.Label(root, text = "Get New Stretch", font = (fontName, 15))
loadNewStretch.configure(bg='#E19669')
loadNewStretch.pack(anchor = 'w')

bt2 = tkinter.Button(padx = 10, pady=10, text= "Enter", command = display_stretch)
bt2.pack(padx = 20, pady=6,anchor = 'w')
bt2.configure(bg='#CF6024')

def dark_mode():
	print("Dark Mode")
	root.configure(bg='#008890')
	move.configure(bg='#005D62',fg="#E2E5DE")
	lbl.configure(bg='#008890',fg="#E2E5DE")
	timeLabel.configure(bg='#008890',fg="#E2E5DE")
	loadNewStretch.configure(bg='#008890',fg="#E2E5DE")
	bt1.configure(bg='#005D62',fg="#E2E5DE")
	bt2.configure(bg='#005D62',fg="#E2E5DE")
	bt3.configure(bg='#005D62',fg="#E2E5DE")
	pass

bt3 = tkinter.Button(padx = 20, pady=6, text="Switch to Dark/Night Mode", command = dark_mode)
bt3.configure(bg='#CF6024')
bt3.pack(padx = 20, pady=20, anchor = 'e')

photo = tkinter.PhotoImage(file="download.png")
photo = photo.subsample(20, 20)
myimage = tkinter.Label(image=photo)
myimage.pack()

root.mainloop()  # leave at end of program