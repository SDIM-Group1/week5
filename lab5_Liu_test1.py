#!/usr/bin//env python
# -*- coding:utf-8 -*-
import smbus
import time
import scipy.io.wavfile as wavf
import numpy as np


import RPi.GPIO as GPIO     
from time import sleep
#from scipy.io import wavfile
    
                   
GPIO.cleanup() 
LedPin = 25   
freq =100                    
dc = 0          

GPIO.setmode(GPIO.BCM)               
GPIO.setup(LedPin, GPIO.OUT)     

pwm = GPIO.PWM(LedPin, freq)     
pwm.start(dc)


 
address = 0x48
A0 = 0x40
A1 = 0x41
A2 = 0x42
A3 = 0x43
bus = smbus.SMBus(1)
samples=np.random.randn(24000)

i=0
while i<24000:
    bus.write_byte(address,A3)  
    value = bus.read_byte(address)
    #print("AOUT:%1.3f  " %(value))
    #value= value **2 /100
    
    if value >100:
        value = 100
    elif value<0:
        value=2
        
    pwm.ChangeDutyCycle(value)
    
#    time.sleep(0.000125)
    samples[i]=value
    i=i+1
#     pwm.ChangeDutyCycle(0)
    
    #samples = np.random.randn(8000)
fs=8000
print('1')
out_f = '120out.wav'
wavf.write(out_f,fs,samples)
