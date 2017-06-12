#importing the complex number class
from CN import *
import sys

#w will be used for objects of CNPolar
#z will be used for objectzs of CN
#zn will be equal to wn

#================
#Creating Objects
#================

#A constructor without parameters will generate (0 + 0i)
z1 = CN()

sys.stdout.write("z1 is ")
z1.prettyprint()

print() #empty line

#Same goes for CNPolar with Phi = 0 und r = 0
w1 = CNPolar()

print("w1 is:")
#CNPolar has different print methods
w1.printcomponents() 		# phi and r 
w1.printtrig() 				# cos and sin
w1.printtrig(True, True) 	# cis
w1.printeuler() 			# Euler's function

print()

#When only one parameter is given it will only fill in the real value and therefore the number is also in the set of - at least - the real numbers
z2 = CN(3)
sys.stdout.write("z2 is ")
z2.prettyprint()


w2 = CNPolar(3)
sys.stdout.write("w2 is ")
w2.printcomponents()


#When all 2 paramters are filled in we actually get a complex number which is not in the set of the real numbers

z3 = CN(5, 3)
sys.stdout.write("z3 is ")
z3.prettyprint()

print()

#topolar() converts the CN class to the same number in CNPolar class. Inaccuracies are to be expected
w3 = z3.topolar() 
print("w3 is:")
#CNPolar with radians or degrees. What is used depends on the boolean value. Default is True for degrees
w3.printcomponents(True)
w3.printcomponents(False)
w3.printtrig(True)
w3.printtrig(False)


print()


#===============
#Small Functions
#===============

w4 = CNPolar(23, -70)
z4 = w4.toalg() #toalg() is the conversion from CNPolar to CN


sys.stdout.write("z4 is ")
z4.prettyprint()

sys.stdout.write("w4 is ")
w4.printcomponents()

print()

#Conjugate which is just a swapped sign for b
sys.stdout.write("The conjugation of z3 is ")
z3.conjugate().prettyprint()

#Swapped sign for a and b
sys.stdout.write("Negation of z3 is ")
z3.signswap().prettyprint()

sys.stdout.write("Negation of w3 is ")
w3.signswap().printcomponents()

print()

#====================
#Algebraic Operations
#====================

#Addition
sys.stdout.write("z3 + z4 = ")
z3.add(z4).prettyprint()

sys.stdout.write("w3 + w4 = ")
w3.add(w4).printcomponents()
print()

#Subtraction
sys.stdout.write("z3 - z4 = ")
z3.sub(z4).prettyprint()

sys.stdout.write("w3 - w4 = ")
w3.sub(w4).printcomponents()
print()

#Multiplication
sys.stdout.write("z3 * z4 = ")
z3.mul(z4).prettyprint()

sys.stdout.write("w3 * w4 = ")
w3.mul(w4).printcomponents()
print()

#Division
sys.stdout.write("z3 / z4 = ")
z3.div(z4).prettyprint()

sys.stdout.write("w3 / w4 = ")
w3.div(w4).printcomponents()
print()


#=======================
#Mathematical Operations
#=======================

#Power

sys.stdout.write("z3^4 = ")
z3.power(4).prettyprint()

sys.stdout.write("w3^4 = ")
w3.power(4).printcomponents()

print()

#Roots
print("The 5th roots of z4: ")
results1 = z4.nroot(5)
#The first result is the prinicpal root
for x in results1:
	x.prettyprint()
	
print()	
	
print("The 5th roots of w4: ")	
results2 = w4.nroot(5)
for x in results2:
	x.printcomponents()

print()	

#Comparing with eq()	
sys.stdout.write("z3 and z4 are equal: ")
print(z3.eq(z4))

sys.stdout.write("z4 and z4 are equal: ")
print(z4.eq(z4))

sys.stdout.write("z4 and w4 are equal: ")
print(z4.eq(w4.toalg())) # with a conversion to alg

sys.stdout.write("z3 and w3 are equal: ")
print(z3.eq(w3.toalg())) # here we have an accuracy issue with the conversion

#The input function is used here so that the programm will not close immediately (depending on how it is opened)
input("")