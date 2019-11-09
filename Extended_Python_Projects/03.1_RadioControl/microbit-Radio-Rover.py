import radio
from Freenove_Micro_Rover_2 import *
Rover = Micro_Rover()
radio.on()
while True:
    data = radio.receive()
    if data is not None:
        data=data.split("#")
        if "LED" in data:
            R,G,B=Rover.hsl_to_rgb(Rover.map(abs(Rover.constrain(int(data[1]),-800,800)),0,800,0,360))
            Rover.all_led_show(255,R,G,B)
        elif "Buzzer" in data:
            value = int(Rover.map(Rover.constrain(int(data[1]),-800,800),-800,800,2500,280))
            pin0.set_analog_period_microseconds(value)
            pin0.write_analog(600)
        elif "motor" in data:
            x=Rover.constrain(int(data[1]),-800,800)
            y=Rover.constrain(int(data[2]),-800,800)
            y=Rover.map(y,-800,800,255,-255)
            if y>0:
                if x<0:
                    x=Rover.map(x,0,-800,255,-255)
                    Rover.motor(x,y)
                elif x>0:
                    x=Rover.map(x,0,800,255,-255)
                    Rover.motor(y,x)
            elif y < 0:
                if x<0:
                    x=Rover.map(x,0,-800,-255,255)
                    Rover.motor(x,y)
                elif x>0:
                    x=Rover.map(x,0,800,-255,255)
                    Rover.motor(y,x)
        elif "Stop" in data:
            Rover.motor(0,0)
            pin0.write_analog(0)