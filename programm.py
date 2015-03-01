# This script need pigpio for operating.

import pigpio
import time

pi = pigpio.pi()


class LED(object):
  def __init__(self, pinR, pinG, pinB):
    self.__red = 0
    self.__green = 0
    self.__blue = 0
    self.__pinR = pinR
    self.__pinG = pinG
    self.__pinB = pinB
  
  def color(self, var1, var2, var3):
    self.__red = var1
    self.__green = var2
    self.__blue = var3
    return True
  
  def update(self):
    pi.set_PWM_dutycycle(self.__pinR, self.__red)
    pi.set_PWM_dutycycle(self.__pinG, self.__green)
    pi.set_PWM_dutycycle(self.__pinB, self.__blue)
    return True
  
  def getRed(self):
    return self.__red
  
  def getGreen(self):
    return self.__green
  
  def getBlue(self):
    return self.__Blue
  
  def getPinR(self):
    return self.__pinR
  
  def getPinG(self):
    return self.__pinG
  
  def getPinB(self):
    return self.__pinB
  
  def setPins(self, var1, var2, var3):
    self.__pinR = var1
    self.__pinG = var2
    self.__pinB = var3
    return True

led = LED(27, 22, 17)
led.color(0, 0, 255)
led.update()

while True:
  led.color(255, 255, 255)
  led.update()
  time.sleep(0.1)
  led.color(0, 0, 0)
  led.update()
  time.sleep(0.1)
