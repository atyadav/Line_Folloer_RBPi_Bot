#!/usr/bin/python
from gpiozero import LED
from gpiozero import Button
from time import sleep

IR_1 = Button(12)
IR_2 = Button(16)

M1_C = LED(5)
M2_C = LED(6)

M1_A = LED(19)
M2_A = LED(26)

while True:
	if IR_1.is_pressed:
#		print("M1 OFF")
		M1_C.off()
	else:
		M1_C.on()
#		print("M1 ON")
	
	if IR_2.is_pressed:
#		print("M2 OFF")
		M2_C.off()
	else:
#		print ("M2 ON")
		M2_C.on()
	#sleep(0.5)
