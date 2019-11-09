from microbit import *
import radio
radio.on()
while True:
    if button_a.is_pressed() and button_b.is_pressed():
        radio.send("motor"+'#'+str(accelerometer.get_x())+'#'+str(accelerometer.get_y()))
        print ("motor")
    elif button_a.is_pressed():
        radio.send("LED"+'#'+str(accelerometer.get_y()))
        print ("LED")
    elif button_b.is_pressed():
        radio.send("Buzzer"+'#'+str(accelerometer.get_y()))
        print ("Buzzer")
    else:
        radio.send("Stop")