import math

class CN:

 __re = float(0)
 __im = float(0)

 def __init__(self, re = 0, im = 0):
  self.setRe(re)
  self.setIm(im)

 def getRe(self):
  return self.__re

 def getIm(self):
  return self.__im

 def setRe(self, value):
  self.__re = float(value)

 def setIm(self, value):
  self.__im = float(value)



 def prettyprint(self, braces = True):
  if self.getIm() >= 0:
   x = str(self.getRe()) + " + " + str(self.getIm()) + "i"
  else:
   x = str(self.getRe()) + " - " + str(-self.getIm()) + "i"
   
  if braces:
   x = "(" + x + ")"
  print(x)

 def signswap(self):
  x = CN()
  x.setRe(-self.getRe())
  x.setIm(-self.getIm())
  return x

 def conjugate(self):
  x = CN()
  x.setRe(self.getRe())
  x.setIm(-self.getIm())
  return x

 def abs(self):
  return math.sqrt(self.getRe()**2 + self.getIm()**2)

 def deg(self):
  pass

 def add(self, c2):
  x = CN()
  try:
   x.setRe(self.getRe() + c2.getRe())
   x.setIm(self.getIm() + c2.getIm())
  except:
   x.setRe(self.getRe() + c2)
   x.setIm(self.getIm())
  return x

 def sub(self, c2):
  try:
   return self.add(-c2)
  except:
   return self.add(c2.signswap())

 def mul(self, c2):
  x = CN()
  try:
   x.setRe((self.getRe() * c2.getRe()) - (self.getIm() * c2.getIm()))
   x.setIm((self.getRe() * c2.getIm()) + (self.getIm() * c2.getRe()))
  except:
   h = CN(c2)
   x.setRe((self.getRe() * h.getRe()) - (self.getIm() * h.getIm()))
   x.setIm((self.getRe() * h.getIm()) + (self.getIm() * h.getRe()))

  return x

 def div(self, c2):
  x = CN()
  try:
   x.setRe(((self.getRe() * c2.getRe()) + (self.getIm() * c2.getIm()))/(c2.getRe()**2 + c2.getIm()**2))
   x.setIm(((self.getIm() * c2.getRe()) - (self.getRe() * c2.getIm()))/(c2.getRe()**2 + c2.getIm()**2))
  except:
   h = CN(c2)
   x.setRe(((self.getRe() * h.getRe()) + (self.getIm() * h.getIm()))/(h.getRe()**2 + h.getIm()**2))
   x.setIm(((self.getIm() * h.getRe()) - (self.getRe() * h.getIm()))/(h.getRe()**2 + h.getIm()**2))
  return x
