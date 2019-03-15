import os
import subprocess
import time
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from subprocess import call

disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)

##################################################################
#
#	func	print_on_screen
#
#	param	1 line
#	param	2 line
#	param	3 line
##################################################################

def print_on_screen(line_1,line_2,line_3):

	font = ImageFont.load_default()
	image = Image.new('1', (disp.width, disp.height))
	draw = ImageDraw.Draw(image)

	# Draw a black filled box to clear the image.
	draw.rectangle((0,0,disp.width,disp.height), outline=0, fill=0)

	#draw.text((0, -2),      "nombre",  font=font, fill=255)
	draw.text((0, -2),     line_1,  font=font, fill=255)
	draw.text((0, -2+8),     line_2, font=font, fill=255)
	draw.text((0, -2+16),    line_3,  font=font, fill=255)
	#draw.text((0, -2+25),    line_4,  font=font, fill=255)

	# Display image.
	disp.image(image)
	disp.display()
	time.sleep(.1)

##################################################################
#
#	init_HMI
#
#################################################################

def init_HMI():

	init_disp() 
	init_gpio()


def init_disp(): 
    
    	disp.begin()
    	disp.clear()
	disp.display()

def init_gpio():

	GPIO.setmode(GPIO.BCM)
	button= 18
	led_green = 14
	led_red = 15

	GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(led_green, GPIO.OUT)
	GPIO.setup(led_red , GPIO.OUT)
	
	#GPIO.setup(button_up, GPIO.IN, pull_up_down=GPIO.PUD_UP)	# Top (Pin 16)


	#GPIO.add_event_detect(button_up, GPIO.FALLING, callback=button_pushed)



#################################################################
#button_state(): 
#	func	display_result
#
#	brief	set leds and print message on screen
#
#	param	0 : NOK / 1 : OK
#	
#
#################################################################
def display_result(carte_state):

	if (carte_state == 1):
		GPIO.output(14, GPIO.HIGH)
		sleep(2)
		GPIO.output(14, GPIO.LOW)
          
	else: 	
		GPIO.output(15, GPIO.HIGH)
		sleep(2)
		GPIO.output(15, GPIO.LOW)


################################################################
#	func 	display_student_numbers()
#
#	brief	display the number of students
#
#	param	nb_student	
#	param	nb_total
#################################################################

def display_student_numbers(nb_total,nb_student): 

	font = ImageFont.load_default()
	image = Image.new('1', (disp.width, disp.height))
	draw = ImageDraw.Draw(image)

	# Draw a black filled box to clear the image.
	draw.rectangle((0,0,disp.width,disp.height), outline=0, fill=0)

	line_1 = "nombre etud  : " + str(nb_total)
	line_2 = "etud present : " + str(nb_student) + "/" + str(nb_total)

	draw.text((0, -2),      line_1,  font=font, fill=255)
	draw.text((0, -2+8),    line_2, font=font, fill=255)

	# Display image.
	disp.image(image)
	disp.display()
	time.sleep(.1)


################################################################
#	func button_state
#
#	return	0 : nothing / 1 : pushed
#################################################################

def button_state(): 

	while True:
    
		if (GPIO.input(18) == GPIO.LOW):

			print_on_screen("Button was pushed")
	                time.sleep(1)
			print("Button was pushed") 
			return 1 
		else: 
			return 0 
	
	

################################################################
#	func hp_signal ()
#
#	param 0: ok : 
#################################
def hp_signal (sound_code):

	if (sound_code == 0):
		os.system("mpg123 carte_ok.mp3")
	elif (sound_code == 1):
		os.system("mpg123 carte_not_ok.mp3")
	elif (sound_code == 2):
		os.system("mpg123 second_time.mp3")


############################################################################

if __name__ == "__main__":

	init_HMI()

        hp_signal (0)
        print_on_screen("raed","amri","test")
	display_result(0)
	display_result(1)
        ok = button_state()
        print (ok)
	display_student_numbers(20,5) 
	hp_signal (1)
	hp_signal (2)
