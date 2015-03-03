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
    self.update()
    return True
  
  def update(self):
    pi.set_PWM_dutycycle(self.__pinR, self.__red)
    pi.set_PWM_dutycycle(self.__pinG, self.__green)
    pi.set_PWM_dutycycle(self.__pinB, self.__blue)
    return True

  def show(self, var1, var2, var3, var4):
    self.setColor(var1, var2, var3)
    self.update()
    time.sleep(var4)


led = LED(27, 22, 17)

led.show(255, 255, 255, 1)
led.show(0, 0, 0, 1)

led.show(0, 0, 2, 0.1)
led.show(0, 0, 2, 0.1)
led.show(0, 0, 3, 0.1)
led.show(0, 0, 4, 0.1)
led.show(0, 0, 5, 0.1)
led.show(0, 0, 7, 0.1)
led.show(0, 0, 9, 0.1)
led.show(0, 0, 12, 0.1)
led.show(0, 0, 15, 0.1)
led.show(0, 0, 18, 0.1)
led.show(0, 0, 22, 0.1)
led.show(0, 0, 26, 0.1)
led.show(0, 0, 31, 0.1)
led.show(0, 0, 36, 0.1)
led.show(0, 0, 41, 0.1)
led.show(0, 0, 47, 0.1)
led.show(0, 0, 53, 0.1)
led.show(0, 0, 60, 0.1)
led.show(0, 0, 67, 0.1)
led.show(0, 0, 74, 0.1)
led.show(0, 0, 82, 0.1)
led.show(0, 0, 90, 0.1)
led.show(0, 0, 99, 0.1)
led.show(0, 0, 108, 0.1)
led.show(0, 0, 117, 0.1)
led.show(0, 0, 127, 0.1)
led.show(0, 0, 137, 0.1)
led.show(0, 0, 148, 0.1)
led.show(0, 0, 159, 0.1)
led.show(0, 0, 170, 0.1)
led.show(0, 0, 182, 0.1)
led.show(0, 0, 194, 0.1)
led.show(0, 0, 207, 0.1)
led.show(0, 0, 220, 0.1)
led.show(0, 0, 233, 0.1)
led.show(0, 0, 247, 0.1)
led.show(0, 0, 255, 0.1)
led.off()
