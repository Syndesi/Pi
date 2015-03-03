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
  
  def addColor(self, var1, var2):
    self.__red += var1.__red * var2
    self.__green += var1.__green * var2
    self.__blue += var1.__blue * var2
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
