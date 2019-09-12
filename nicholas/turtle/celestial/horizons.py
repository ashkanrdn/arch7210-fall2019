import re
from astropy import units
from astropy.time import Time
from astropy.coordinates import CartesianRepresentation
from astroquery.jplhorizons import Horizons
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
            kg = float(f'{m}e{n}')
            return kg * units.kilogram
        return None

    def vectorData(self, columnName):
        if self.vectors is None:
            self.vectors = self.obj.vectors()
        return self.vectors[columnName].quantity[0]
    
    def position(self):
        return CartesianRepresentation(self.vectorData('x'), self.vectorData('y'), self.vectorData('z'))

    def velocity(self):
        return CartesianRepresentation(self.vectorData('vx'), self.vectorData('vy'), self.vectorData('vz'))
    
    def assignTo(self, celestialTurtle):
        celestialTurtle.mass = self.mass()
        celestialTurtle.setposition(self.position())
        celestialTurtle.setvelocity(self.velocity())
