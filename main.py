import numpy as np
import matplotlib.pyplot as plt

#starting conditions
c = 1
d = 2

x10 = 0.1
x20 = 0.2

time_step = 0.01
t = np.arange(0.0,2.0, time_step) #timegrid

no_steps = len(t)

x1 = np.zeros(no_steps)
x2 = np.zeros(no_steps)

x1[0] = x10
x2[0] = x20

for i in range(0,no_steps -1):
  x1[i+1] = x1[i] + time_step*(c*x1[i] + c*x2[i]) 
  x2[i+1] = x2[i] + time_step*(d*x1[i] + c*x2[i]) 

plt.plot(t,x1) #blue
plt.plot(t,x2) #green
plt.show()
