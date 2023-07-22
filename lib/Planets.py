import math
from lib.Universe import Universe

class Orbit(Universe):
    
    def __init__(self, star_name, distance, color, velocity) -> None:
        super().__init__()

        self.distance = distance
        self.color = color
        self.velocity = velocity

        planet:dict = self.planets.get(star_name)

        self.x = planet.get("x")
        self.y = planet.get("y")
        self.star_size = planet.get("size")
        self.radius = self.star_size + distance

        self.trajectory_step = -1

        self.calculate_trajectory()
        self.draw()


    def calculate_trajectory(self):
        """ STEPS PER FRAME (FPS) """

        self.trajectory_steps = []
        start_angle_radians = math.radians(0)
        end_angle_radians = math.radians(360)
        step_radians = math.radians(self.velocity)

        # ___ Calculate planet position for one orbit ____
        while start_angle_radians <= end_angle_radians:
            x = self.x + self.radius * math.cos(start_angle_radians)
            y = self.y + self.radius * math.sin(start_angle_radians) 
            start_angle_radians += step_radians
            self.trajectory_steps.append( (x, y + self.star_size) )


    def draw(self):
        """ RENDERING """

        self.pen.speed(0)
        self.pen.shape("circle")
        self.pen.color(self.color)
        self.pen.penup()
        self.pen.goto(self.x, self.y - self.distance)
        self.pen.pendown()
        
        # ___ Draw orbit ____
        self.pen.circle(self.radius)
        self.pen.penup()
        

    def refresh(self):
        """ REFRESH FRAME """

        # ___ Reached full orbit - Reset ____
        if self.trajectory_step == len(self.trajectory_steps)-1:
            self.trajectory_step = 0

        else:
            self.trajectory_step += 1

        x, y = self.trajectory_steps[self.trajectory_step]
        self.pen.goto(x, y)
    