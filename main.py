from lib.Stars import Star
from lib.Planets import Orbit
import tkinter as tk


class Loop:

    def __init__(self) -> None:
        """ Prepare planets objects (Orbit) """

        self.planets = []

        Star("Sun", "yellow", 40, 0, -50).draw()

        self.mercury = Orbit("Sun", 20, "purple", 8)
        self.venus = Orbit("Sun", 50, "orange", 7)
        self.earth = Orbit("Sun", 80, "blue", 6)
        self.mars = Orbit("Sun", 115, "brown", 5)
        self.jupiter = Orbit("Sun", 155, "red", 4)
        self.saturn = Orbit("Sun", 185, "yellow", 3)
        self.uranus = Orbit("Sun", 225, "violet", 2)
        self.neptune = Orbit("Sun", 255, "dark blue", 1)

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
        """ Start/Stop animation - individual planets """
        
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
    
    btn = tk.Button(root, text="START ANIMATION", command=loop.start)
    stop_btn = tk.Button(root, text="STOP ANIMATION", command=loop.stop)
    earth_trig = tk.Button(root, text="ENABLE/DISABLE EARTH", command = lambda: loop.trigger(loop.earth))
    
    btn.pack()
    stop_btn.pack()
    earth_trig.pack()

    root.mainloop()
