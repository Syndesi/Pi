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
