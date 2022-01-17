import numpy as np
import matplotlib.pyplot as plt
import math
g=9.81
v0=10
a=math.radians(30)
s=math.sin(a)
tmax=2*v0*s/g
ymax=v0**2*s**2/(2*g)
xmax=v0**2*math.sin(2*a)/g
print(tmax,xmax,ymax)
t = np.arange(0.01, tmax, 0.01)
vy=(v0*s)-(g*t)
vx=v0
y=v0*t*s-(g/2*t**2)
x=v0*math.cos(a)*t
fig, (a1, b, c1) = plt.subplots(3, 1, sharey=True)

color = 'tab:blue'
a1.set_xlabel('t [s]')
a1.set_ylabel('y [m]', color=color)
a1.plot(t, y, color=color)
a1.tick_params(axis='y', labelcolor=color)

a2 = a1.twinx()

color = 'tab:red'
a2.set_ylabel('x [m]', color=color)
a2.plot(t, x, color=color)
a2.tick_params(axis='y', labelcolor=color)

color = 'tab:green'
b.set_ylabel('y [m]', color=color)
b.set_xlabel('x [m]')
b.plot(x, y, color=color)
b.tick_params(axis='y', labelcolor=color)

color = 'tab:blue'
c1.set_xlabel('t [s]')
c1.set_ylabel('Vy [m]', color=color)
c1.plot(t, vy, color=color)
c1.tick_params(axis='y', labelcolor=color)

c2 = c1.twinx()

color = 'tab:red'
c2.set_ylabel('Vh [m]', color=color)
c2.plot(t, vx*np.ones_like(t), color=color)
c2.tick_params(axis='y', labelcolor=color)


fig.tight_layout()
plt.show()