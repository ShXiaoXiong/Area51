from random import choice

class Randomwalk():
    def __init__(self,points=5000):
       self.points=points
       self.x=[0]
       self.y=[0]

    def walk(self):
        while len(self.x) < self.points:

            x_direction=choice([-1,1])
            x_distance=choice([0,1,2,3,4,5])
            x_step=x_distance*x_direction
            
            y_direction=choice([-1,1])
            y_distance=choice([0,1,2,3,4,5])
            y_step=y_distance*y_direction
            
            if y_step==0 and x_step==0:
                continue
           
            x_next=self.x[-1]+x_step
            y_next=self.y[-1]+y_step
            
            self.x.append(x_next)
            self.y.append(y_next)

rw=Randomwalk()
rw.walk()

import matplotlib.pyplot
matplotlib.pyplot.scatter(rw.x,rw.y,s=3,c=range(0,rw.points),cmap=matplotlib.pyplot.cm.Reds)
matplotlib.pyplot.show()
