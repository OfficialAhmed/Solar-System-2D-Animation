from lib.Stars import Star
from lib.Planets import Orbit
import tkinter as tk


class Loop:

    def __init__(self) -> None:
        """ Prepare planets objects (Orbit) """

        self.planets = []

        Star("Sun", "yellow", 40, 0, -50).draw()

        self.mercury = Orbit("Mercury", "Sun", 20, "purple", 8)
        self.venus = Orbit("Venus", "Sun", 50, "orange", 7)
        self.earth = Orbit("Earth", "Sun", 80, "blue", 6)
        self.mars = Orbit("Mars", "Sun", 115, "brown", 5)
        self.jupiter = Orbit("Jupiter", "Sun", 155, "red", 4)
        self.saturn = Orbit("Saturn", "Sun", 185, "yellow", 3)
        self.uranus = Orbit("Uranus", "Sun", 225, "violet", 2)
        self.neptune = Orbit("Neptune", "Sun", 255, "dark blue", 1)

    def start(self):
        """ Start animation - All planets """
        self.planets = [
            self.mercury,
            self.venus,
            self.earth,
            self.mars,
            self.jupiter,
            self.saturn,
            self.uranus,
            self.neptune
        ]

        orbits = 10
        for _ in range(360 * orbits):
            for planet in self.planets:
                planet.refresh()

    def stop(self):

        self.planets = []

    def trigger(self, planet):
        """ Start/Stop animation - individual planet """
        
        if len(self.planets) == 0:
            return 0
        
        if planet not in self.planets:
            self.planets.append(planet)
        else:
            self.planets.remove(planet)



if __name__ == "__main__":

    loop = Loop()
    
    root = tk.Tk()
    root.title("Solar System Console")
    
    btn = tk.Button(root, text="START ANIMATION", command=loop.start).pack()
    stop_btn = tk.Button(root, text="STOP ANIMATION", command=loop.stop).pack()

    mercury_trig = tk.Button(root, text="ENABLE/DISABLE MERCURY", command = lambda: loop.trigger(loop.mercury)).pack()
    venus_trig = tk.Button(root, text="ENABLE/DISABLE VENUS", command = lambda: loop.trigger(loop.venus)).pack()
    earth_trig = tk.Button(root, text="ENABLE/DISABLE EARTH", command = lambda: loop.trigger(loop.earth)).pack()
    mars_trig = tk.Button(root, text="ENABLE/DISABLE MARS", command = lambda: loop.trigger(loop.mars)).pack()
    jupiter_trig = tk.Button(root, text="ENABLE/DISABLE JUPITAR", command = lambda: loop.trigger(loop.jupiter)).pack()
    saturn_trig = tk.Button(root, text="ENABLE/DISABLE SATURN", command = lambda: loop.trigger(loop.saturn)).pack()
    uranus_trig = tk.Button(root, text="ENABLE/DISABLE URANUS", command = lambda: loop.trigger(loop.uranus)).pack()
    neptune_trig = tk.Button(root, text="ENABLE/DISABLE NEPTUNE", command = lambda: loop.trigger(loop.neptune)).pack()
    
    root.mainloop()
