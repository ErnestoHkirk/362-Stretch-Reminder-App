# sandfly.py
# Dimitra Doiphode, Austin Sohn, Zakee Khattak, Ernesto Hooghkirk, Savannah Bauer
# TODO:
# Phase 1 -
# - Add clock GUI
# - Add way to display motivational quote
# - Add set interval for stretches with names of each stretch and description
# - Add stretch notifcation window
# - Auto-randomize new stretches with button
# Phase 2
# - Image accompanying each stretch to demonstrate how to do it
# - Dark mode -CHECK
# - Sound/alarm
# - Similar stretch button? (see similar stretches)
# - Point System
# Phase 3
# - Account System
# - LeaderBoard
# - Favorite(s) Stretch
# - Text to Speech
# - Music selector

import random
from time import strftime
import json
import tkinter
from PIL import Image, ImageTk # for JPG support
# importing strftime function to
# retrieve system's time
from tkinter import messagebox
import pygame
import pyttsx3


# creating tkinter window
fontName = 'Georgia'
root = tkinter.Tk()
root.title("Project Sandfly: Stretch Reminder")
root.configure(bg='#E19669')


engine = pyttsx3.init() 

""" RATE"""
engine.setProperty('rate', 150)
rate = engine.getProperty('rate')
engine.runAndWait()
engine.stop()


"""VOLUME"""
volume = engine.getProperty('volume')   
engine.setProperty('volume',1)   

"""VOICE"""
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) 



# This function is used to
# display time on the label
def time():
    string = strftime('%I:%M %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Styling the label widget so that clock
# will look more attractive
lbl = tkinter.Label(root, font=(fontName, 40))
lbl.configure(bg='#E19669')

# Placing clock at the centre
# of the tkinter window
lbl.pack(anchor='center')
time()

quotes = [
    '\n"The key to success is to start before \nyou are ready." \n- Marie Forleo\n',
    '\n"Challenges are what make life interesting. \nOvercoming them is what makes life meaningful." \n- Joshua J. Marine\n',
    '\n"If people are doubting how far you can go, \ngo so far that you can\'t hear them anymore." \n- Michele Ruiz\n',
    '\n"If you are always trying to be normal, \nyou will never know how amazing you can be." \n- Maya Angelou\n',
    '\n"If you\'re going through hell, keep going."\n - Winston Churchill\n'
]
move = tkinter.Label(text=random.choice(
    quotes), font=(fontName, 17), relief="solid")
move.configure(bg='#D67540')
move.pack(padx=20, pady=6)

stretch = [
    'Lunges (Leg):\n\nStand with one foot forward and one leg back. \nBend the forward knee into a right angle, and hold for five seconds.',
    'Modified hurdler stretch (Leg):\n\nRemaining seated on the floor, extend one leg outward. \nReach towards your toes. \nHold for 10 to 30 seconds. \nRepeat on the other side.',
    'Arm windmill (Shoulder):\n\nSlowly swing your arm in a circle stretching out as far as you can.',
    'Shoulder shrug (Shoulder):\n\nLift your shoulders towards your ears and hold for 1 to 2 seconds.\nThen roll your shoulders back as you relax down. Repeat a few times.',
    'Child\'s pose (Back):\n\nBegin at table top position. \nSlowly extend your arms in front of you and \ntry to put your face on the floor. \nHold for 20 to 30 seconds.',
    'Prone back extension (Back):\n\nLay face down on the floor, put your elbows below your shoulders and begin to push your upper body up with your arms.\n',
    'Top forearm stretch (Arm): \n\nExtend one arm out with your palm facing towards you, point your fingers to the floor. Use your other hand to gently pull the fingers towards yourself. Hold for 10 to 30 seconds. Repeat on the other hand.',
    'Under forearm stretch (Arm):\n\nExtend one arm out and have your palm face forward with the fingers pointed down. Use your other hands and gently pull your fingers towards yourself. Hold for 10 to 30 seconds. Repeat on the other hand.',
    'Neck side flexion (Neck): \n\nGently pull your head toward each shoulder \nuntil a light stretch is felt. \nHold pose for 10 to 15 seconds. \nAlternate once on each side.',
    'Forward/Backward tilt(Neck):\n\nStart with your head up and slowly lower your chin towards your chest and hold for 10 to 30 seconds. Slowly lift your head back up to neutral and then tilt your chin towards the ceiling and hold for 10 seconds. Repeat for a few reps.'
]

stretch_imgs = [  # THESE CORRESPOND TO THE STRETCHES IN stretch, DO NOT MIX EM UP
    ImageTk.PhotoImage(Image.open("./images/lunge-stretch.jpg")),
    ImageTk.PhotoImage(Image.open("./images/fowardfold-stretch.jpg")),
    ImageTk.PhotoImage(Image.open("./images/windmill-stretch.jpg")),
    ImageTk.PhotoImage(Image.open("./images/shrug-stretch.jpg")),
    ImageTk.PhotoImage(Image.open("./images/childspose-stretch.jpg")),
    ImageTk.PhotoImage(Image.open("./images/prone-back-extension.jpg")),
    ImageTk.PhotoImage(Image.open("./images/forearm-stretch.jpg")),
    ImageTk.PhotoImage(Image.open("./images/underforearm-stretch.jpg")),
    ImageTk.PhotoImage(Image.open("./images/neck-stretch.jpg")),
    ImageTk.PhotoImage(Image.open("./images/necktilt-stretch.jpg")),
]

username = "User"
username_string_var = tkinter.StringVar(value = "Username: User")
username_label = tkinter.Label(root, textvariable = username_string_var, font = (fontName, 15))
username_label.configure(bg='#E19669')
username_label.pack()

def change_username_window():
    new_window = tkinter.Toplevel(root)
    new_window.title = "Change Username"

    label = tkinter.Label(new_window, text = "What's your name?")
    label.pack()

    username_entry = tkinter.Entry(new_window)
    username_entry.pack()

    def done_button_cmd():
        change_username(username_entry.get())
        new_window.destroy()
    done_button = tkinter.Button(new_window, text = "Done", command = done_button_cmd)
    done_button.pack()

change_username_btn = tkinter.Button(root, text = "Not you?", command = change_username_window)
change_username_btn.configure(bg='#CF6024')
change_username_btn.pack()

_leaderboard = []

_favorites = {}

def write_data():
    data_to_write = {
        "username": username,
        "leaderboard": _leaderboard,
        "favorites": _favorites
    }

    with open("data.json", "w") as file:
        json.dump(data_to_write, file)

def read_data():
    data = None
    with open("data.json") as file:
        data = json.load(file)

    if data is not None:
        global _leaderboard
        global _favorites
        _leaderboard = data["leaderboard"]
        _favorites = data["favorites"]
        username = data["username"]
        username_string_var.set("Username: " + data["username"])

read_data()

def update_leaderboard(name, score):
    prev_entry_index = None
    for entry in _leaderboard:
        if entry[0] == name:
            prev_entry_index = _leaderboard.index(entry)
            break

    if prev_entry_index is not None:
        _leaderboard[prev_entry_index] = (name, score)
    else:
        _leaderboard.append((name, score))
    _leaderboard.sort(key = lambda x: x[1], reverse = True)
    if len(_leaderboard) > 5:
        _leaderboard.pop()

    write_data()

counter = 0
_score = 0 # DON'T DIRECTLY REFERENCE THIS, USE update_score
score_string_var = tkinter.StringVar(value="Score: ") # backs the score label
def update_score(delta):
    global _score
    _score += delta
    score_string_var.set("Score: " + str(_score))
    update_leaderboard(username, _score)

stretch_label_string_var = tkinter.StringVar() # backs the stretch text label
def display_stretch(index):
    new_window = tkinter.Toplevel(root)
    new_window.title = "Time to Stretch!"


    label = tkinter.Label(new_window, textvariable = stretch_label_string_var)
    label.pack()

    stretch_label_string_var.set(stretch[index])

    def done_with_stretch():
        new_window.destroy()
        update_score(10)
    btn = tkinter.Button(new_window, text="Done", command=done_with_stretch)
    btn.pack()

    def add_to_favorites():
        favs_list = _favorites.get(username, None)
        if favs_list is None:
            _favorites[username] = [index]
            return

        if index not in favs_list:
            favs_list.append(index)

        _favorites[username] = favs_list
        refresh_favorites()
        write_data()

    add_to_favorites_btn = tkinter.Button(new_window, text = "Add to Favorites", command = add_to_favorites)
    add_to_favorites_btn.pack()

    def text_to_speech_func():
        engine.say(stretch[index])
        engine.runAndWait()
        engine.stop()
        
    text_to_speech_btn = tkinter.Button(new_window, text = "Text to Speech", command = text_to_speech_func)
    text_to_speech_btn.pack()

    stretch_img_label = tkinter.Label(new_window, image=stretch_imgs[index])
    stretch_img_label.pack()

    new_window.bell()

def display_random_stretch():
    choice = random.randrange(0, len(stretch))
    display_stretch(choice)

def update_label():
    global counter
    getTime = float(eb1.get())
    if getTime < 1:
        return
    millisec = int(getTime * 60000)  # convert minutes to miliseconds
    print(getTime)  # delete later
    lbl.configure()
    counter += 1
    if counter > 1:
        display_random_stretch()

    # after 30 sec, executes update_label() func
    root.after(millisec, update_label)


# root.after(10000, update_label) # stops from running the first time

scoreLabel = tkinter.Label(root, textvariable = score_string_var, font=(fontName, 15))
scoreLabel.configure(bg='#E19669')
scoreLabel.pack()

def show_leaderboard():
    new_window = tkinter.Toplevel(root)

    for entry in _leaderboard:
        label = tkinter.Label(new_window, text = entry[0] + ": " + str(entry[1]))
        label.pack()
leaderboard_button = tkinter.Button(root, text = "Leaderboard", command = show_leaderboard)
leaderboard_button.configure(bg='#CF6024')
leaderboard_button.pack()

timeLabel = tkinter.Label(
    root, text="Enter time interval (minutes): ", font=(fontName, 15))
timeLabel.configure(bg='#E19669')
timeLabel.pack(anchor='w')
eb1 = tkinter.Entry(root)
eb1.pack(padx=20, pady=6, anchor='nw')
bt1 = tkinter.Button(padx=10, pady=10, text="Enter", command=update_label)
bt1.configure(bg='#CF6024')
bt1.pack(padx=20, pady=6, anchor='nw')


loadNewStretch = tkinter.Label(
    root, text="Get New Stretch", font=(fontName, 15))
loadNewStretch.configure(bg='#E19669')
loadNewStretch.pack(anchor='w')

bt2 = tkinter.Button(padx=10, pady=10, text="Enter", command=display_random_stretch)
bt2.pack(padx=20, pady=6, anchor='w')
bt2.configure(bg='#CF6024')

# Menu of stretches
stretch_menu_label = tkinter.Label(root, text = "Or pick a specific stretch: ", font = (fontName, 15))
stretch_menu_label.configure(bg = '#E19669')
stretch_menu_label.pack(anchor = 'w')

stretches_short = [
    'Lunges',
    'Modified hurdler stretch',
    'Arm windmill',
    'Shoulder shrug',
    'Child\'s pose',
    'Prone back extension',
    'Top forearm stretch',
    'Under forearm stretch',
    'Neck side flexion',
    'Forward/Backward tilt',
]
stretch_menu_string_var = tkinter.StringVar(value = stretches_short[0])
def choose_stretch_from_menu(choice):
    index = stretches_short.index(choice)
    display_stretch(index)
stretch_menu = tkinter.OptionMenu(root, stretch_menu_string_var, *stretches_short,
                                  command = choose_stretch_from_menu)
stretch_menu.configure(padx=10, pady=10, bg = '#CF6024')
stretch_menu.pack(padx=20, pady=6, anchor='w')


favorites_menu_button = tkinter.Menubutton(root, text = "Your Favorites", relief = tkinter.RAISED)
favorites_menu_button.configure(bg = '#CF6024')
favorites_menu = tkinter.Menu(favorites_menu_button, tearoff = 0)
favorites_menu_button["menu"] = favorites_menu
def refresh_favorites():
    favorites_menu.delete(0, 10) # this is terrible

    favs_list = _favorites.get(username, [])
    if favs_list == []:
        favorites_menu.add_command(label = "You don't have any favorites!")
    else:
        for item in favs_list:
            def open_favorite_stretch(index = item): # kludge - we use this to get an early binding on item
                display_stretch(index)
            favorites_menu.add_command(label = stretches_short[item], command = open_favorite_stretch)
refresh_favorites()

favorites_menu_button.pack(padx = 20, anchor = 'w')

def change_username(name):
    global username
    username = name
    username_string_var.set("Username: " + name)

    write_data()
    refresh_favorites()

# Start of Music Dependencies and Functionality

pygame.mixer.init()# initialise the pygame

def play(choice):
    print(choice)
    pygame.mixer.music.load(song_selector_file_path[choice])
    pygame.mixer.music.play()

# play_button = tkinter.Button(root, text="Play Song", font=("Helvetica", 32), command=play)
# play_button.pack(pady=20)

# Music drop-down label
song_menu_label = tkinter.Label(root, text = "Song selector: ", font = (fontName, 15))
song_menu_label.configure(bg = '#E19669')
song_menu_label.pack(anchor = 'w')

song_selector = [
    'Awakening',
    'Cali',
    'Cancion Triste',
    'Dreamy Piano',
    'Modular Ambient',
    'Nightlife',
]

song_selector_file_path = [
    "music/awakening-instrumental.mp3",
    "music/cali.mp3",
    "music/cancion-triste.mp3",
    "music/dreamy-piano-soft-sound-ambient-background.mp3",
    "music/modular-ambient.mp3",
    "music/nightlife-michael-kobrin.mp3",
]

song_menu_string_var = tkinter.StringVar(value = song_selector[0])
def choose_song_from_menu(choice):
    index = song_selector.index(choice)
    play(index)

song_menu = tkinter.OptionMenu(root, song_menu_string_var, *song_selector,
                                  command = choose_song_from_menu)
                                  
song_menu.configure(padx=10, pady=10, bg = '#CF6024')
song_menu.pack(padx=20, pady=6, anchor='w')

# End of Music Dependencies and Functionality

def dark_mode():
    print("Dark Mode")
    root.configure(bg='#008890')
    move.configure(bg='#005D62', fg="#E2E5DE")
    lbl.configure(bg='#008890', fg="#E2E5DE")
    timeLabel.configure(bg='#008890', fg="#E2E5DE")
    loadNewStretch.configure(bg='#008890', fg="#E2E5DE")
    bt1.configure(bg='#005D62', fg="#E2E5DE")
    bt2.configure(bg='#005D62', fg="#E2E5DE")
    bt3.configure(bg='#005D62', fg="#E2E5DE")
    stretch_menu_label.configure(bg='#008890', fg="#E2E5DE")
    song_menu_label.configure(bg='#008890', fg="#E2E5DE")
    stretch_menu.configure(bg='#005D62', fg="#E2E5DE")
    song_menu.configure(bg='#005D62', fg="#E2E5DE")
    username_label.configure(bg='#008890', fg="#E2E5DE")
    scoreLabel.configure(bg='#008890', fg="#E2E5DE")
    leaderboard_button.configure(bg='#005D62', fg="#E2E5DE")
    favorites_menu_button.configure(bg='#005D62', fg="#E2E5DE")
    change_username_btn.configure(bg='#005D62', fg="#E2E5DE")

bt3 = tkinter.Button(
    padx=20, pady=6, text="Switch to Dark/Night Mode", command=dark_mode)
bt3.configure(bg='#CF6024')
bt3.pack(padx=20, pady=20, anchor='e')

# photo = tkinter.PhotoImage(file="download.png")
# photo = photo.subsample(20, 20)
# myimage = tkinter.Label(image=photo)
# myimage.pack()


root.mainloop()  # leave at end of program
