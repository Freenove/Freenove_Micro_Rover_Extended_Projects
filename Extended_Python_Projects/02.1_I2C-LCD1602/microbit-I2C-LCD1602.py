from microbit import *
from I2C_LCD1602_Class import *
lcd = I2C_LCD1602(0x27)
hello='Hello'
counter=0
lcd.puts(hello, 0, 0)
lcd.puts(str(counter), 0, 1)
sleep(1000)
while True:
    for i in range(4):
        lcd.clear()
        counter+=1
        lcd.puts(hello, i+1, 0)
        lcd.puts(str(counter), i+1, 1)
        sleep(1000)
    for i in range(4):
        lcd.clear()
        counter+=1
        lcd.puts(hello, 3-i, 0)
        lcd.puts(str(counter), 3-i, 1)
        sleep(1000)