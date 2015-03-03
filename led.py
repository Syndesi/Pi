import pigpio
import time

pi = pigpio.pi()

class LED(object):
  def __init__(self, pinR, pinG, pinB):
    self.__pinR = pinR
    self.__pinG = pinG
    self.__pinB = pinB
    self.__red = 0
    self.__green = 0
    self.__blue = 0
  
  def setColor(self, var1, var2, var3):
    self.__red = var1
    self.__green = var2
    self.__blue = var3
    if self.__red >= 255:
      self.__red = 255
    elif self.__red <= 0:
      self.__red = 0
    if self.__green >= 255:
      self.__green = 255
    elif self.__green <= 0:
      self.__green = 0
    if self.__blue >= 255:
      self.__blue = 255
    elif self.__blue <= 0:
      self.__blue = 0
    return True
  
  def getRed(self):
    return self.__red
  
  def getGreen(self):
    return self.__green
  
  def getBlue(self):
    return self.__blue
  
  def off(self):
    self.setColor(0, 0, 0)
    return True
  
  def update(self):
    pi.set_PWM_dutycycle(self.__pinR, self.__red)
    pi.set_PWM_dutycycle(self.__pinG, self.__green)
    pi.set_PWM_dutycycle(self.__pinB, self.__blue)
    return True

  def show(self, var1, var2, var3, var4):
    self.setColor(self, var1, var2, var3)
    self.update()
    time.sleep(var4)


led = LED(27, 22, 17)

led.show(255, 255, 255, 1)
led.show(0, 0, 0, 1)
led.show(0, 0, 255, 1)
led.show(0, 0, 2, 1)
led.off()
