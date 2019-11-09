import microbit
from microbit import *
import math,ustruct
from time import sleep_us,ticks_us
class Micro_Rover(object):
    def __init__(self):
        self.address = 0x43
        microbit.i2c.write(self.address, bytearray([0x00, 0x00]))
        self.set_all_pwm(0, 0)
        microbit.i2c.write(self.address, bytearray([0x01, 0x04]))
        microbit.i2c.write(self.address, bytearray([0x00, 0x01]))
        sleep(5)
        microbit.i2c.write(self.address, bytearray([0x00]))
        mode1 = microbit.i2c.read(self.address, 1)
        mode1 = ustruct.unpack('<H', mode1)[0]
        mode1 = mode1 & ~0x10
        microbit.i2c.write(self.address, bytearray([0x00, mode1]))
        sleep(5)
    def set_pwm(self, channel, on, off):
        if on is None or off is None:
            microbit.i2c.writ(self.address, bytearray([0x06+4*channel]))
            data = microbit.i2c.read(self.address, 4)
            return ustruct.unpack('<HH', data)
        microbit.i2c.write(self.address, bytearray([0x06+4*channel, on & 0xFF]))
        microbit.i2c.write(self.address, bytearray([0x07+4*channel, on >> 8]))
        microbit.i2c.write(self.address, bytearray([0x08+4*channel, off & 0xFF]))
        microbit.i2c.write(self.address, bytearray([0x09+4*channel, off >> 8]))
    def set_all_pwm(self, on, off):
        microbit.i2c.write(self.address, bytearray([0xFA, on & 0xFF]))
        microbit.i2c.write(self.address, bytearray([0xFB, on >> 8]))
        microbit.i2c.write(self.address, bytearray([0xFC, off & 0xFF]))
        microbit.i2c.write(self.address, bytearray([0xFD, off >> 8]))
    def map(self,value,fromLow,fromHigh,toLow,toHigh):
        return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow) + toLow
    def constrain(self,Value,Low,High):
        if Value <= Low:
            return Low
        elif Value >= High:
            return High
        else:
            return Value
    def all_led_show(self,brightness,R,G,B):
        brightness=self.map(brightness,0,255,0,1)
        R=int(self.map(R,0,255,0,4095)*brightness)
        G=int(self.map(G,0,255,0,4095)*brightness)
        B=int(self.map(B,0,255,0,4095)*brightness)
        for i in range(4):
            self.set_pwm(5+3*i,0,R)
            self.set_pwm(6+3*i,0,G)
            self.set_pwm(4+3*i,0,B)
    def led_show(self,index,R,G,B):
        R=int(self.map(R,0,255,0,4095))
        G=int(self.map(G,0,255,0,4095))
        B=int(self.map(B,0,255,0,4095))
        for i in range(4):
            if index>>i & 0x01:
                if i==0:
                    self.set_pwm(14,0,R)
                    self.set_pwm(15,0,G)
                    self.set_pwm(13,0,B)
                else:
                    self.set_pwm(5+3*(i-1),0,R)
                    self.set_pwm(6+3*(i-1),0,G)
                    self.set_pwm(4+3*(i-1),0,B)
    def hsl_to_rgb(self,degree):
        degree=degree/360*255
        if degree < 85:
            red = 255 - degree * 3
            green = degree * 3
            blue = 0
        elif degree < 170:
            degree = degree - 85
            red = 0
            green = 255 - degree * 3
            blue = degree * 3
        else:
            degree = degree - 170
            red = degree * 3
            green = 0
            blue = 255 - degree * 3
        return int(red),int(green),int(blue)
    def motor(self,left,right):
        left=int(self.map(left,-255,255,-4095,4095))
        right=int(self.map(right,-255,255,-4095,4095))
        if left > 0:
            self.set_pwm(0,0,left)
            self.set_pwm(1,0,0)
        elif left < 0:
            self.set_pwm(0,0,0)
            self.set_pwm(1,0,abs(left))
        else:
            self.set_pwm(0,0,0)
            self.set_pwm(1,0,0)
        if right > 0:
            self.set_pwm(2,0,right)
            self.set_pwm(3,0,0)
        elif right < 0:
            self.set_pwm(2,0,0)
            self.set_pwm(3,0,abs(right))
        else:
            self.set_pwm(2,0,0)
            self.set_pwm(3,0,0)
