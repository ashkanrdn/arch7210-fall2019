import re
from turtle import Vec2D
from astropy.time import Time
from astroquery.jplhorizons import Horizons
from MotionVector import MotionVector
from CelestialTurtle import CelestialTurtle

_massPattern = re.compile('Mass,?\s*x?10\^([0-9]+)\s*\(?kg\)?\s*=\s*~?([.0-9]+)')

class HorizonsLookup:

    vectors = None
    elements = None

    def __init__(self, objectId, relativeTo, time=Time.now()):
        self.obj = Horizons(id=objectId, id_type='majorbody', location=relativeTo, epochs=time.jd)

    def mass(self):
        if self.elements is None:
            self.elements = self.obj.elements(get_raw_response=True)

        match = _massPattern.search(self.elements)
        if match:
            n, m = match.group(1), match.group(2)
            return float(f'{m}e{n}')
        return None

    def vectorData(self, columnName, units):
        if self.vectors is None:
            self.vectors = self.obj.vectors()
        return self.vectors[columnName].to(units)[0].value
    
    def position(self):
        return Vec2D(self.vectorData('x', 'm'), self.vectorData('y', 'm'))

    def velocity(self):
        return MotionVector(self.vectorData('vx', 'm/s'), self.vectorData('vy', 'm/s'))
    
    def assignTo(self, celestialTurtle):
        celestialTurtle.mass = self.mass()
        celestialTurtle.setposition(self.position())
        celestialTurtle.setvelocity(self.velocity())
