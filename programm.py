# This script need pigpio for operating.

import pigpio
import color
import time

pi = pigpio.pi()


class LED(object):
  def __init__(self, pinR, pinG, pinB):
    self.__color = color.Color(0, 0, 0)
    self.__pinR = pinR
    self.__pinG = pinG
    self.__pinB = pinB
  
  def color(self, var1):
    self.__color = var1
    return True
  
  def addColor(self, var1, var2):
    self.__color.addColor(var1, var2)
    return True
  
  def update(self):
    pi.set_PWM_dutycycle(self.__pinR, self.__color.getRed())
    pi.set_PWM_dutycycle(self.__pinG, self.__color.getGreen())
    pi.set_PWM_dutycycle(self.__pinB, self.__color.getBlue())
    return True
  
  def getRed(self):
    return self.__color.getRed()
  
  def getGreen(self):
    return self.__color.getGreen()
  
  def getBlue(self):
    return self.__color.getBlue()
  
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

while True:
  led.color(color.black)
  led.update()
  time.sleep(0.5)
  led.addColor(color.white, 0.3)
