import rhinoscriptsyntax as rs
from System.Drawing import Color

class Turtle:
    def __init__(self):
        self._weight = 0
        self._heading = None # can hold string values including: s, u, d, r, l ,b
        self._penDown = False
        self._position = [0, 0, 0]
        self._color = Color.FromArgb(250, 0, 0)
        
    def position(self):
        return self._position
        
    def weight(self):
        return self._weight
        
    def heading(self):
        return self._heading
        
    def color(self):
        return self._color
        
    def penUp(self):
        self._penDown = False
        
    def penDown(self):
        self._penDown = True
        
    def setPosition(self, x, y, z):
        self._position = [x, y, z]
    
    def setWeight(self, wt):
        self._weight = wt
        
    def setHeading(self, hd):
        self._heading = hd
    
    def isPenDown(self):
        if self._penDown is False:
            return False
        else:
            return True
            
    def setColor(self, r, g, b):
        self._color = Color.FromArgb(r, g, b)

    def set_spcf(self, obj):
        rs.ObjectColor(obj, self.color())
        rs.ObjectPrintColor(obj, self.color())
        rs.ObjectPrintWidth(obj, self.weight())
        
    def forward(self, hd, s):
        new_pos = [0, 0, 0]
        new_pos[0] = self.position()[0]
        new_pos[1] = self.position()[1]
        new_pos[2] = self.position()[2]
        self.setHeading(hd)

        if not self.isPenDown():
            print "Pen is up!"
            return
        
        if self.heading() == "s":
            new_pos[0] += s
            line = rs.AddLine(self.position(), new_pos)
            self.set_spcf(line)
        elif self.heading() == "b":
            new_pos[0] -= s
            line = rs.AddLine(self.position(), new_pos)
            self.set_spcf(line)
        elif self.heading() == "r":
            new_pos[1] -= s
            line = rs.AddLine(self.position(), new_pos)
            self.set_spcf(line)
        elif self.heading() == "l":
            new_pos[1] += s
            line = rs.AddLine(self.position(), new_pos)
            self.set_spcf(line)
        elif self.heading() == "u":
            new_pos[2] += s
            line = rs.AddLine(self.position(), new_pos)
            self.set_spcf(line)
        elif self.heading() == "d":
            new_pos[2] -= s
            line = rs.AddLine(self.position(), new_pos)
            self.set_spcf(line)
        else:
            print "None of them!!!!"
            
        self.setPosition(new_pos[0], new_pos[1], new_pos[2])
        

rs.DeleteObjects(rs.AllObjects(select=True))


t = Turtle()


t.penDown()
t.setColor(100, 100, 200)


for i in range(0, 102):
    t.forward("s", 10)
    t.setPosition(0, -i/10, 10)
    t.forward("s", 10)
    t.setPosition(0, -i/10, 0)
    rs.Redraw()

t.setPosition(0, 0, 0)
t.setColor(100, 200, 100)
for i in range(0, 102):
    t.forward("u", 10)
    t.setPosition(0, -i/10, 0)
    rs.Redraw()

t.setPosition(10, 0, 0)
for i in range(0, 102):
    t.forward("u", 10)
    t.setPosition(10, -i/10, 0)
    rs.Redraw()

t.setPosition(0, 0, 0)
t.setColor(200, 100, 100)
for i in range(0, 102):
    t.forward("s", 10)
    t.setPosition(0, 0, i/10)
    rs.Redraw()

t.setPosition(0, -10, 0)
for i in range(0, 102):
    t.forward("s", 10)
    t.setPosition(0, -10, i/10)
    rs.Redraw()
    
