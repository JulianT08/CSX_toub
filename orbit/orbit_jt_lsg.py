"""
FLOWER BOX
- Author: Julian Toub & Linnea Shah-Gustafsson
- Description:
    - Simulates the orbit of a planet around a stationary host
    - Initial position and velocity of planet can be altered in the instantiation of the planet, as well as host mass
    - Plots the orbit of the planet 
    - Plots an arrow displaying the direction and relative magnitude of centripetal acceleration
    - Plots a velocity vs. time graph
- Log:
    - 2/21/26, 1 PM - Base program completed (Julian)
        - Included all functionality and a working display
    - 2/21/26, 6 PM - Removed redundancies & fixed style (Linnea)
        - Converted program to object oriented programming
        - Reduced # of global variables to 1
        - Removed try...except from display function
        - Removed redundancies in code that generates the acceleration arrow
        - Updated variable names to be more consistent
        - Documented code
- Bugs:
    - No known bugs
- Credits:
    - All work was done by us alone without use of AI
"""

import matplotlib.pyplot as plt

g = 6.67e-11 # defines global variable g, the gravitational constant, which will never change

class Planet:
    # Planet: a class for a planet orbiting a host of a certain mass 

    def __init__(self, initial_x, initial_y, initial_vx, initial_vy, host_mass):
        self.ax = [-1*g*host_mass*initial_x/(initial_x**2 + initial_y**2)**1.5] # initializes x acceleration array
        self.ay = [-1*g*host_mass*initial_y/(initial_x**2 + initial_y**2)**1.5] # initializes y acceleration array
        self.vx = [initial_vx] # initializes x velocity array
        self.vy = [initial_vy] # initializes y velocity array
        self.v = [(initial_vx**2 + initial_vy**2)**0.5] # initializes net velocity array
        self.x = [initial_x] # initializes x position array
        self.y = [initial_y] # initializes y position array
        self.host_mass = host_mass # the mass of the planet's host

    def step(self, dt):
        # method: updates all the position, velocity, and acceleration arrays after some time dt
        # dt: the amount of time in seconds between steps
        self.x.append(self.x[-1]+self.vx[-1]*dt) # updates x position using current x velocity
        self.y.append(self.y[-1]+self.vy[-1]*dt) # updates y position using current y velocity
        self.ax.append(-1*g*self.host_mass*self.x[-1]/(self.x[-1]**2 + self.y[-1]**2)**1.5) # updates x acceleration via universal gravitation
        self.ay.append(-1*g*self.host_mass*self.y[-1]/(self.x[-1]**2 + self.y[-1]**2)**1.5) # updates y acceleration via universal gravitation
        self.vx.append(self.vx[-1]+self.ax[-1]*dt) # updates x velocity using current x acceleration
        self.vy.append(self.vy[-1]+self.ay[-1]*dt) # updates y velocity using current y acceleration
        self.v.append((self.vx[-1]**2 + self.vy[-1]**2)**0.5) # updates net velocity with magnitude of velocity vector

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_vx(self):
        return self.vx
    
    def get_vy(self):
        return self.vy
    
    def get_v(self):
        return self.v
    
    def get_ax(self):
        return self.ax
    
    def get_ay(self):
        return self.ay


class Simulation:

    def __init__(self):
        time = [10*i for i in range(1000)] # an array containing every time step the program will step through
        self.earth = Planet(4e+6,0,0,8e+3,5e+24) # initializes earth using its distance from the sun, its velocity, and the mass of the sun
        self.simulate(time)
        self.display(time)
        pass

    def simulate(self, time):
        # method: calls the earth object's step method repeatedly to generate all its positions, velocities, and accelerations. equivalent to populating the spreadsheet down
        # time: see __init__
        for i in range(len(time)):
            self.earth.step(10)

    def display(self, time):
        # method: using all the earth's previous positions/velocities/accelerations, displays the motion of its orbit
        # time: see __init__
        show_velocity = True # toggles the velocity graph on or off
        plt.ion() # makes the graph interactive (plots continuously as time goes on)
        fig, ax_plot = plt.subplots() # build the graph and the container for the graph
        if show_velocity:
            fig2, ax2_plot = plt.subplots() # build the velo graph and the container for the graph
        for i in range(1, len(time)):
            # Plot a new point and trace it
            ax_plot.clear()
            ax_plot.plot(self.earth.get_x()[:i], self.earth.get_y()[:i], 'b-') # make a blue line for the tracing
            ax_plot.plot(self.earth.get_x()[i], self.earth.get_y()[i], 'ro') # make a red dot for the current position
            ax_plot.plot(0, 0, 'go', markersize=15) # create and plot the host planet 
            ax_plot.set_title('Orbit') # set the title of graph 1 to 'Orbit'
            # Force arrow pointing to host
            ux = self.earth.get_ax()[i] * 1e5  # grab the acceleration value and scale it up
            uy = self.earth.get_ay()[i] * 1e5  # grab the acceleration value and scale it up
            ax_plot.quiver(self.earth.get_x()[i], self.earth.get_y()[i], ux, uy, angles='xy', scale_units='xy', scale=1, color='orange') # display orange arrow pointing towards host, proportional to the magnitude of the force
            if show_velocity:
                ax2_plot.clear()
                ax2_plot.plot(time[1:i+1], self.earth.get_v()[:i], 'b-') # make a blue line for the tracing
                ax2_plot.plot(time[i], self.earth.get_v()[i], 'ro') # make a red dot for the current position
                ax2_plot.set_title('Velocity KPH') # set the title of graph 1 to 'Velocity KPH'
            plt.pause(0.01) # pause for .01 seconds before plotting next point
        plt.ioff() # turn off interactive mode
        plt.show() # keep the window open

orbit_simulation = Simulation()

