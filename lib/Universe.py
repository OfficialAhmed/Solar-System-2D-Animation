import turtle

class Universe:
    
    planets = {}

    def __init__(self) -> None:
        self.pen = turtle.Turtle()
        self.planets = Universe.planets
        screen = turtle.Screen()
        screen.setup(width=700, height=700)
        screen.bgpic("assets/space.png")
        screen.title("Solar System 2D Animation: Turtle Graphics")
