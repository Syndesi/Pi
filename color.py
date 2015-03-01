class Color(object):
  def __init__(self, var1, var2, var3):
    self.__red = var1
    self.__green = var2
    self.__blue = var3
  
  def setColor(self, var1, var2, var3):
    self.__red = var1
    self.__green = var2
    self.__blue = var3
    return True

  def getRed(self):
    return self.__red
  
  def getGreen(self):
    return self.__green
  
  def getBlue(self):
    return self.__blue
  
  def setRed(self, var1):
    self.__red = var1
    return True
  
  def setGreen(self, var1):
    self.__green = var1
    return True
  
  def setBlue(self, var1):
    self.__blue = var1
    return True

white = Color(255, 255, 255)
red = Color(255, 0, 0)
blue = Color(0, 0, 255)
yellow = Color(255, 255, 0)
green = Color(0, 255, 0)
black = Color(0, 0, 0)  # black is transparent, because the LED is off
purple = Color(255, 0, 255)
cyan = Color(0, 255, 255)
orange = Color(128, 255, 0)
