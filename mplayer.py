
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
from subprocess import call

# ---> vars
maxWidth  	= "320"
maxHeight 	= "240"
imgFile   	= "images/skin.jpg"
volume    	= 0
volume_mute	= 0
root		= 0

# ---> functions
def play():
	print "----> play"
	call(["mpc", "play"])

def pause():
	print "----> pause"
	call(["mpc", "pause"])

def mute():
	print "----> mute"
	global volume
	global volume_mute
	if volume == 0:
		call(["mpc", "volume", str(volume_mute)])
	else:
		volume_mute = volume
		volume = 0
		call(["mpc", "volume", str(volume)])
		
def volume_up():
	print "----> volume up"
	global volume
	if volume != 100:
		volume += 10
		call(["mpc", "volume", str(volume)])

def volume_down():	
	print "----> volume down"
	global volume
	if volume != 0:
		volume -= 10
		call(["mpc", "volume", str(volume)])

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
	call(["mpc", "stop"])
	root.destroy()

def init():
	global volume
	global volume_mute
	global root
	volume = 50
	volume_mute = volume

	call(["mpc", "volume", str(volume)])
	call(["mpc", "stop"])

	root = Tk()
	root.title("MediaPlayer")
	root.resizable(width=FALSE, height=FALSE)
	root.geometry(maxWidth+'x'+maxHeight)
	root.protocol('WM_DELETE_WINDOW', closeApp)

	frame = Frame(root)
	frame.pack()

	canvas = Canvas(frame, bg="black", width=maxWidth, height=maxHeight)
	canvas.pack()
	canvas.bind('<ButtonPress-1>', callback )

	#image  = Image.open(imgFile) 
	image  = ImageTk.PhotoImage(file=imgFile) 
	canvas.create_image(160, 120, image=image)
	canvas.image = image
	root.mainloop()


# ---> play
init()


