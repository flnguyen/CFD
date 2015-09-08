import matplotlib.pyplot as plt
from pylab import *  # for plotting commands
import numpy as numpy
import math
#Felicia Nguyen
#This program solves a wave-like form of the Navier Stokes Equation under a set of assumptions.
#Equation details: -Incompressible form, newtonian fluid

c=0.5
nMax=20  #Number of time steps we want to tak
iMax=20 #This dictates the number of i's starting at 0

uTemp=[]
dt=.1
dx = (2.0-0) / (iMax) #since the index STARTS at 1, we dont need to add 1 to the denominator like usual
u = numpy.ones(iMax)   #Set some ones
#setting u = 2 between 0.5 and 1 because of the initial conditions
u[.5/dx : 1/dx+1]=2  

# for n in range(0, nMax, dt): #This for loop is moving forward in time
for n in range (nMax):
	uTemp=u
	print uTemp
	for i in range(1,iMax): 
		#Calculate and store values into list
		# u[i]= ( -uTemp[i] ) * ( dt/dx ) * ( uTemp[i] - uTemp[i-1] ) + uTemp[i]
		u[i]= ( -c ) * ( dt/dx ) * ( uTemp[i] - uTemp[i-1] ) + uTemp[i]
		print u
	plt.plot(linspace(0,2,iMax),u)
	plt.axis((0, 2 , 0, 2) )
	plt.show()





