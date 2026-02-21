import matplotlib.pyplot as plt
import math

# Initializing variables, setting things equal to Earth and a hypothetical orbiting object. Storing values in lists
dt = 10
g = 6.67*10**-11
m_host = 5.00*10**+24
initial_x = 4.00*10**+6
inital_y = 0
vx_initial = 0
vy_initial = 8.00*10**+3
vx = []
vy = []
velo = []
accelx = []
ay = []
x_pos = [initial_x]
y_pos = [inital_y]
time = [10*i for i in range(1000)]


count = 0
for i in range(len(time)):
    if count == 0: # The first time around, it should use the initial numbers
        accelx.append(-1*g*m_host*initial_x/(initial_x**2 + inital_y**2)**1.5)
        ay.append(-1*g*m_host*inital_y/(initial_x**2 + inital_y**2)**1.5)
        vx.append(vx_initial+accelx[-1]*dt)
        vy.append(vy_initial+ay[-1]*dt)
        count += 1
    else: # After the first time, it can reference previously calculated values
        x_pos.append(x_pos[-1]+vx[-1]*dt)
        y_pos.append(y_pos[-1]+vy[-1]*dt)
        accelx.append(-1*g*m_host*x_pos[-1]/(x_pos[-1]**2 + y_pos[-1]**2)**1.5)
        ay.append(-1*g*m_host*y_pos[-1]/(x_pos[-1]**2 + y_pos[-1]**2)**1.5)
        vx.append(vx[-1]+accelx[-1]*dt)
        vy.append(vy[-1]+ay[-1]*dt)
        velo.append(math.sqrt(vx[-1]**2 + vy[-1]**2))
        count += 1

plt.ion() # Makes the graph interactive and update
fig, ax_plot = plt.subplots()
show = True # True or False will either show or not show the velocity graph. Make sure that the velocity and orbit graphs don't overlap each other. 
if show:
    fig2, ax2 = plt.subplots() # This is the velocity graph
for i in range(1, len(time)):
    try: # Plot a new point and trace it
        ax_plot.clear()
        ax_plot.plot(x_pos[:i], y_pos[:i], 'b-')
        ax_plot.plot(x_pos[i], y_pos[i], 'ro')
        ax_plot.plot(0, 0, 'go', markersize=15)
        ax_plot.set_title('Orbit')
# Force arrow pointing to host
        r = math.sqrt(x_pos[i]**2 + y_pos[i]**2)
        a_mag = math.sqrt(accelx[i]**2 + ay[i]**2)
        arrow_len = a_mag * 1e5  # Arrow length scaled by acceleration magnitude — longer when closer to host
        ux = (accelx[i] / a_mag) * arrow_len  # Unit vector x, scaled
        uy = (ay[i] / a_mag) * arrow_len      # Unit vector y, scaled
        ax_plot.quiver(x_pos[i], y_pos[i], ux, uy, angles='xy', scale_units='xy', scale=1, color='orange')
        if show:
            ax2.clear()
            ax2.plot(time[1:i+1], velo[:i], 'b-')
            ax2.plot(time[i], velo[i], 'ro')
            ax2.set_title('Velocity KPH')
        plt.pause(0.01)
    except IndexError: # If the list "time" has run out, then break
        break
plt.ioff()
plt.show()







