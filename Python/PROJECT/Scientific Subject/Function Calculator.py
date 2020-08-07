import numpy as np
import pylab as pl



x = [0,1,3,-2,]
y = []

for i in x:
	f = ((1/4) * (4/1))*(x[i]**3)
	y.append(f)

print(x,y)	 

pl.plot(x,y)
pl.show()




