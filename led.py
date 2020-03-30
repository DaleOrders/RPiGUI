import time
import RPi.GPIO as GPIO
from Tkinter import *
import tkFont

#open window and set myFont
window = Tk()
window.geometry("300x350")
window.title("Turn on an LED light")
myFont = tkFont.Font(family = 'Helvetica', size = 14, weight = "bold")

red = StringVar()
blue = StringVar()
green = StringVar()


red.set("A")
blue.set("B")
green.set("C")


red_LED = 21
blue_LED = 23
green_LED = 24

#setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([red_LED, blue_LED, green_LED], GPIO.OUT)

#toggles of each colour
def RedToggle():
	GPIO.output(red_LED, 1)
	GPIO.output(green_LED, 0)
	GPIO.output(blue_LED, 0)
	green.set("r")
	blue.set("r")
	
def BlueToggle():
	GPIO.output(blue_LED, 1)
	GPIO.output(green_LED, 0)
	GPIO.output(red_LED, 0)
	red.set("b")
	green.set("b")

def GreenToggle():
	GPIO.output(green_LED, 1)
	GPIO.output(blue_LED, 0)
	GPIO.output(red_LED, 0)
	red.set("g")
	blue.set("g")

def Exit_Window():
	RPi.GPIO.cleanup()
    
	

#RADIO WIDGET
blue_RADIO= Radiobutton(window, text="Blue Light", font=myFont, variable=blue, value="b", command=BlueToggle)
red_RADIO = Radiobutton(window, text="Red Light", font=myFont, variable=red, value="r", command=RedToggle)
green_RADIO = Radiobutton(window, text="Green Light", font=myFont, variable=green, value="g", command=GreenToggle)


exit = Button(window, text="exit now", font=myFont, command=Exit_Window)


blue_RADIO.pack(anchor=W)
red_RADIO.pack(anchor=W)
green_RADIO.pack(anchor=W)

exit.pack()


window.mainloop()
