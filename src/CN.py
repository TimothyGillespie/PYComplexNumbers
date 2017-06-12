import math

class CN:

#=================================================
# Attributes with Getters, Setters and Constructor
#=================================================

	#algebraic notation a + bi	__re = float(0) 	#real value a	__im = float(0)		#imginary value b

	#Constructor	def __init__(self, re = 0, im = 0):		self.setRe(re)		self.setIm(im)

	#+++++++
	# Getter
	#+++++++
			def getRe(self):		return self.__re
	def getIm(self):		return self.__im

	#++++++++
	# Setters
	#++++++++
			def setRe(self, value):		self.__re = float(value)
	def setIm(self, value):		self.__im = float(value)

		
		
#=======
# Prints
#=======

	#Print the algebraic notation of the form a + bi. Braces are optional. default they are with braces.	def prettyprint(self, braces = True):		if self.getIm() >= 0:			x = str(self.getRe()) + " + " + str(self.getIm()) + "i"		else:			x = str(self.getRe()) + " - " + str(-self.getIm()) + "i"					if braces:			x = "(" + x + ")"		print(x)

		
		
		
#==================
# Simple Operations	
#==================

	#Swaps signs of a and b. It equivalent to -z
	def signswap(self):
		x = CN()
		x.setRe(-self.getRe())
		x.setIm(-self.getIm())
		return x

	#Swaps the sign of b and therefore returns the conjugation of the complex number
	def conjugate(self):
		x = CN()
		x.setRe(self.getRe())
		x.setIm(-self.getIm())
		return x
		
	#Compares two complex numbers
	def eq(self, c2):
		return self.getRe() == c2.getRe() and self.getIm() == c2.getIm()
		
		
		

#==========
# Converter
#==========
		
	#Gives back the radius of the complex number
	def abs(self):
		return math.sqrt(self.getRe()**2 + self.getIm()**2)

	#Gives back the angle of the complex number
	def angle(self):
		preresult = math.acos(self.getRe()/self.abs())
	
		if self.getIm() >= 0:
			return preresult
		else:
			return -preresult
			
	#Returns the the complex number as an object of CNPolar	
	def topolar(self):
		return CNPolar(self.abs(), CN.phiInDegrees(self.angle()))
		

	#Gives back Phi in degrees. It is to modularize this part in the polar-oriented prints	
	@staticmethod
	def phiInDegrees(x):
		return math.degrees(x)
		
	#unkown curater - it takes x and sees if it is of the class CNPolar or a number and then transforms it to a CN object
	@staticmethod	
	def ucurate(x):
		if isinstance(x, CNPolar):
			x = x.toalg()
		elif not isinstance(x, CN):
			x = CN(x)
			
		return x
		

		
		
		
#=============================================
# Arithmetic Operations in Algebraic Notation
#=============================================
#These functions also allow to work with a complex number and a number of the real domain.	
	
	#Add to a complex number	def add(self, c2):		x = CN()
		c2 = CN.ucurate(c2)
				x.setRe(self.getRe() + c2.getRe())		x.setIm(self.getIm() + c2.getIm())		
				return x

	#Substract from a complex number	def sub(self, c2):		
		c2 = CN.ucurate(c2)		
		return self.add(c2.signswap())

	#Multiply a complex number	def mul(self, c2):		x = CN()
				c2 = CN.ucurate(c2)		
		x.setRe((self.getRe() * c2.getRe()) - (self.getIm() * c2.getIm()))		x.setIm((self.getRe() * c2.getIm()) + (self.getIm() * c2.getRe()))				return x

	#Divided a complex number	def div(self, c2):		x = CN()
		
		c2 = CN.ucurate(c2)
				x.setRe(((self.getRe() * c2.getRe()) + (self.getIm() * c2.getIm()))/(c2.getRe()**2 + c2.getIm()**2))		x.setIm(((self.getIm() * c2.getRe()) - (self.getRe() * c2.getIm()))/(c2.getRe()**2 + c2.getIm()**2))
			
					return x

		
		
		
		
#=============================
# Other Mathematial Operations
#=============================

	def power(self, n):
		
		if n == 1:
			return self
	
		result = self.mul(self)
		i = 2
		
		while i < n:
			result = result.mul(self)
			i = i + 1
			
		return result

	#Gives back a list of complex numbers with the results of the nth root of the complex number. The number of results is equal to n
	#The first element of the list (index 0) is the principal root
	def nroot(self, n):
		preresults = self.topolar().nroot(n)
		results = []
		
		for x in preresults :
			results = [x.toalg()] + results 
			
		return results





		

#======================================================================
# Another Class for Complex Numbers which Stores them in Polar Notation
#======================================================================

class CNPolar:
	

	
#=================================================
# Attributes with Getters, Setters and Constructor
#=================================================

	#polar components phi and r
	__r = float(0)		#The radius r
	__phi = float(0)	#The angle Phi in degrees

	#Constructor
	def __init__(self, r = 0, phi = 0):
		self.setR(r)
		self.setPhi(phi)

	#+++++++
	# Getter
	#+++++++
		
	def getR(self):
		return self.__r

	def getPhi(self):
		return self.__phi

	#++++++++
	# Setters
	#++++++++
		
	def setR(self, value):
		self.__r = float(value)

	def setPhi(self, value):
		self.__phi = float(value)
		
		

		
#================
# Print functions
#================
	
	#Prints both values phi and r seperately divided with an semicolon.	
	def printcomponents(self, deg = True):
		phi = self.getPhi()
		if deg:
			phi = str(phi) + "°"
		else:
			phi = str(math.radians(phi))
			
		r = str(self.getR())
		print("r = " + r + "; Phi = " + phi)

	#In the trigonometric form either with cis or with cos and sin * i. Default it is with cos and sin * i.
	def printtrig(self, deg = True, cis = False):
		phi = self.getPhi()
		if deg:
			phi = str(phi) + "°"
		else:
			phi = str(math.radians(phi))
			
		r = str(self.getR())
		
		if cis:
			print(r + " * cis( " + phi +" )")
		else:
			print(r + " * ( cos( " + phi +" ) + sin( " + phi + " ) i )")
			
					
	#Actually equivalent to the cis notation but with euler's number notated.
	def printeuler(self, deg = True):
		phi = self.getPhi()
		if deg:
			phi = str(phi) + "°"
		else:
			phi = str(math.radians(phi))
			
			
		r = str(self.getR())
		print(r + " * e^( " + phi + " i )")
		
	
		
#=================
# Simple Functions
#=================
	
	#will be called so that phi is in the domain of (-pi; pi]
	@staticmethod
	def curatePhi(x):
		x = x % 360
		if x > 180:
			x = x - 360
		elif x < -180:
			x = x + 360
			
		return x
		
	#Multiplies -1, the inverse element of the multiplication in complex numbers
	def signswap(self):
		return self.mul(-1)
		
#==========
# Converter
#==========

	#stands for "to algebraic notation"
	def toalg(self):
		phi = math.radians(self.getPhi())
		return CN(self.getR() * math.cos(phi), self.getR() * math.sin(phi))
	
	#unkown curater - it takes x and sees if it is of the class CN or a number and then transforms it to a CNPolar object
	@staticmethod	
	def ucurate(x):
		if isinstance(x, CN):
			x = x.topolar()
		elif not isinstance(x, CNPolar):
			x = CNPolar(x)
			
		return x
		
		
#========================================
# Arithmetic Operations in Polar Notation
#========================================
#These functions also allow to work with a complex number and a number of the real domain.	
	
	#Add to a complex number
	def add(self, c2):
		x = CNPolar()
			
		c2 = CNPolar.ucurate(c2)	
			
		r = self.getR()
		phi = math.radians(self.getPhi())
		
		s = c2.getR()
		psi = math.radians(c2.getPhi())
			
		t = math.sqrt(r*r + s*s + 2 * r * s * math.cos(phi-psi))
		chi = math.degrees(math.atan2(r * math.sin(phi) + s * math.sin(psi), r * math.cos(phi) + s * math.cos(psi)))
		
		x.setR(t)
		x.setPhi(chi)
		
		return x
		
	#Substract from a complex number
	def sub(self, c2):
		c2 = CNPolar.ucurate(c2)
		return self.add(c2.signswap())

	def mul(self, c2):
		x = CNPolar()
		
		c2 = CNPolar.ucurate(c2)
		
		x.setR(self.getR() * c2.getR())
		x.setPhi(self.getPhi() + c2.getPhi())
		
		return x
		
		
	def div(self, c2):
		x = CNPolar()
		
		c2 = CNPolar.ucurate(c2)
		
		x.setR(self.getR() / c2.getR())
		x.setPhi(self.getPhi() - c2.getPhi())
		
		return x
		
		
		
#========================
# Mathematical Operations
#========================

	#the nth power of a complex number
	def power(self, n):
		phi = CNPolar.curatePhi(self.getPhi() * n)
		r = self.getR() ** n
		return CNPolar(r, phi)

	#Gives back a list of complex numbers with the results of the nth root of the complex number. The number of results is equal to n
	#The first element of the list (index 0) is the principal root
	def nroot(self, n):
		r = self.getR() **(1/n)
		phi = self.getPhi()/n
		difference = 360/n
		
		results = []
		i = 0
		
		while i < n:
			results = results + [CNPolar(r, phi)]
			i = i + 1
			phi = CNPolar.curatePhi(phi + difference)
			
		aux = results[0]
		results[0] = results[n-1]
		results[n-1] = aux
			
			
		return results