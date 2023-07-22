from lib.Universe import Universe

class Star(Universe):

    def __init__(self, name, color, size, x, y) -> None:
        super().__init__()
        
        self.name = name
        self.color = color
        self.size = size
        self.x = x
        self.y = y

        self.pen.hideturtle()
        self.pen.speed(0) # Render asap

    def draw(self):
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.begin_fill()

        self.pen.fillcolor(self.color)

        self.pen.pendown()
        self.pen.circle(self.size)
        self.pen.end_fill()
        self.pen.penup()

        self.planets[self.name] = {
            "size": self.size, 
            "x": self.x,
            "y": self.y,
        }
        