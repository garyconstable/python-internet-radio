
#  __________           __   .__                         _____               .___.__           __________ .__                                 
#  \______   \ ___.__._/  |_ |  |__    ____    ____     /     \    ____    __| _/|__|_____     \______   \|  |  _____   ___.__.  ____ _______ 
#   |     ___/<   |  |\   __\|  |  \  /  _ \  /    \   /  \ /  \ _/ __ \  / __ | |  |\__  \     |     ___/|  |  \__  \ <   |  |_/ __ \\_  __ \
#   |    |     \___  | |  |  |   Y  \(  <_> )|   |  \ /    Y    \\  ___/ / /_/ | |  | / __ \_   |    |    |  |__ / __ \_\___  |\  ___/ |  | \/
#   |____|     / ____| |__|  |___|  / \____/ |___|  / \____|__  / \___  >\____ | |__|(____  /   |____|    |____/(____  // ____| \___  >|__|   
#              \/                 \/              \/          \/      \/      \/          \/                         \/ \/          \/        


# --> imports
from Tkinter import *
import PIL
from PIL import ImageTk
import subprocess
from subprocess import *
import threading
from time import sleep

# ---> vars
maxWidth  	 = "320"
maxHeight 	 = "240"
imgFile   	 = "images/skin.jpg"
volume    	 = 0
volume_mute	 = 0
root		 = 0
songText     = "Most relationships seem so transitory"
canvas       = ''
current_song = ''

# ---> functions
def play():
	print "----> play"
	subprocess.check_output("mpc play", shell=True)

def pause():
	print "----> pause"
	subprocess.check_output("mpc pause", shell=True)

def mute():
	print "----> mute"
	global volume
	global volume_mute
	if volume == 0:
		subprocess.check_output("mpc volume " + str(volume_mute), shell=True)
	else:
		volume_mute = volume
		volume = 0
		subprocess.check_output("mpc volume " + str(volume), shell=True)
		
def volume_up():
	print "----> volume up"
	global volume
	if volume != 100:
		volume += 10
		subprocess.check_output("mpc volume " + str(volume), shell=True)

def volume_down():	
	print "----> volume down"
	global volume
	if volume != 0:
		volume -= 10
		subprocess.check_output("mpc volume " + str(volume), shell=True)

def get_current_song():
	global songText
	global canvas
	global current_song
	songText = subprocess.check_output("mpc current", shell=True)
	canvas.delete(current_song)
	current_song = canvas.create_text(30, 20, width=250, anchor="nw", fill="white", font="Purisa",text=songText)
	

def prev():
	print "----> prev"

def next():
	print "----> next"

def exit():
	closeApp()

def between(p, p1, p2):
	if p >= p1 and p <= p2:
		return True
	return False

def callback(event):
	if between(event.x, 16 , 75) and between(event.y, 122, 172):
		play()
	elif between(event.x, 91 , 150) and between(event.y, 122, 172):
		pause()
	elif between(event.x, 169 , 228) and between(event.y, 122, 172):
		volume_up()
	elif between(event.x, 245 , 303) and between(event.y, 122, 172):
		mute()	
	elif between(event.x, 16 , 75) and between(event.y, 185, 229):
		prev()
	elif between(event.x, 91 , 150) and between(event.y, 185, 229):
		next()
	elif between(event.x, 169 , 228) and between(event.y, 185, 229):
		volume_down()
	elif between(event.x, 245, 303) and between(event.y, 185, 229):
		exit()	
	else:
		print "---->", event.x, event.y
	
def closeApp():
	print "----> exit"
	global root
	subprocess.check_output("mpc stop", shell=True)
	root.destroy()

def check_thread():
	get_current_song()
	sleep(2.00)
	check_thread()

def updateGUI():
    t = threading.Thread(target=check_thread, args=() )
    t.daemon = True
    t.start()


def init():
	global volume
	global volume_mute
	global root
	global songText
	global canvas
	global current_song

	volume = 50
	volume_mute = volume

	try:
		subprocess.check_output("mpc volume " + str(volume), shell=True)
	except (RuntimeError, TypeError, NameError):
		pass

	try:
		subprocess.check_output("mpc stop", shell=True)
	except (RuntimeError, TypeError, NameError):
		pass

	root = Tk()
	root.title("MediaPlayer")
	root.resizable(width=FALSE, height=FALSE)
	root.geometry(maxWidth+'x'+maxHeight)
	root.protocol('WM_DELETE_WINDOW', closeApp)

	image  = ImageTk.PhotoImage(file=imgFile) 

	canvas = Canvas(root, bg="black", width=maxWidth, height=maxHeight)
	canvas.create_image(160, 120, image=image)
	canvas.bind('<ButtonPress-1>', callback )
	

	updateGUI()

	
	canvas.pack()
	root.mainloop()


# ---> play
init()


