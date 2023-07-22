import turtle

class Universe:
    
    planets = {}

    def __init__(self) -> None:
        self.pen = turtle.Turtle()
        self.planets = Universe.planets
        self.screen = turtle.Screen()
        self.screen.setup(width=700, height=700)
        self.screen.bgpic("assets/space.png")
        self.screen.title("Solar System 2D Animation: Turtle Graphics")
        
        