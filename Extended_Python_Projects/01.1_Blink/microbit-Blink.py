from microbit import *
from time import sleep_us
while True:
    for i in range(4):
        pin8.write_digital(0)
        sleep(500)
        pin8.write_digital(1)
        sleep(500)
    for j in range(4):
        for k in range(2046):
            pin8.write_analog(abs(k-1023))
            sleep_us(500)