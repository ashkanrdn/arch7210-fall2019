### Solution 3 - Practical ######

# Import tools %%%%%%%%%%
import turtle
import csv


class draw_xy():
    # Definition of a class %%%%%%%%%%
    class PlanPoint:
        name = ''
        x = 0
        y = 0
        connections = []  # array

    # Dictionary %%%%%%%%%%

    def __init__(self,point_csv_file_dir,start_pos=(0,0),scale=1):
        self.allpoints = {}  # dictionary
        self.dir_points = point_csv_file_dir
        self.read_csv_()

        self.start_pos = start_pos
        self.scale =scale

        # Window Setup %%%%%%%%%%
        self.window = turtle.Screen()
        self.window.title("Drawing a plan ")
        turtle.bgcolor("green")
        turtle.color("black")

        # Turtle %%%%%%%%%%
        self.elsa = turtle.Turtle()
        turtle.Screen().bgcolor("orange")
        self.elsa.color("black")
        self.elsa.speed(1)
        self.elsa.penup()



    def read_csv_(self):
        with open(self.dir_points) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[1] == 'X':  # Eliminating the first row (name, x , y, connections)
                    continue
                p = draw_xy.PlanPoint()
                p.name = row[0]  # Columns separation
                p.x = float(row[1])
                p.y = float(row[2])
                p.connections = str.split(row[3], ',')
                self.allpoints[p.name] = p  # Creation of all points

    def set_start_pos(self,start_pos):
        self.start_pos = start_pos

    def set_scale(self,scale):
        self.scale = scale

    def start_draw(self):
        temp_point ={}
        for pn in self.allpoints:
            p = self.allpoints[pn]
            p.x += self.start_pos[0]
            p.y += self.start_pos[1]
            temp_point[pn] = p

        # Finding each points and their connections %%%%%%%%%%
        for pn in temp_point:  # Finding each points from dictionary
            p = temp_point[pn]
            # turtle draws dot for p
            self.elsa.goto(p.x*self.scale, p.y*self.scale)
            self.elsa.dot(5, "red")
            self.elsa.write(p.name)
            for c in p.connections:
                q = temp_point[c]
                # turtle draws line form p to q
                self.elsa.goto(p.x*self.scale, p.y*self.scale)
                self.elsa.pendown()
                self.elsa.goto(q.x*self.scale, q.y*self.scale)
                self.elsa.penup()

p = draw_xy("Sample Plan.csv",start_pos=(-680,-280),scale=0.5)
p.set_scale(2)
p.set_start_pos((-500,-200))
p.start_draw()



pass




########################################################################
### Solution 4 - Practical ######

# Import tools %%%%%%%%%%
import turtle
import csv


class draw_xy(turtle.Turtle):
    import copy
    # Definition of a class %%%%%%%%%%
    class PlanPoint:
        name = ''
        x = 0
        y = 0
        connections = []  # array

    # Dictionary %%%%%%%%%%

    def __init__(self,point_csv_file_dir,window,start_pos=(0,0),scale=1,):
        super().__init__()
        self.max_x = -2000
        self.min_x = 2000
        self.max_y = -2000
        self.min_y = 2000


        self.allpoints = {}  # dictionary
        self.dir_points = point_csv_file_dir
        self.read_csv_()

        self.start_pos = list(start_pos)
        self.scale =scale

        # Window Setup %%%%%%%%%%
        self.window = window
        self.window.title("Drawing a plan ")
        turtle.bgcolor("green")
        turtle.color("black")
        # self.hideturtle()
        self.window.screensize()
        self.window.setup(width=1.0, height=1.0, startx=0, starty=0)

        # Turtle %%%%%%%%%%

        turtle.Screen().bgcolor("orange")
        self.color("black")
        self.speed(0.1)
        self.penup()



    def read_csv_(self):

        with open(self.dir_points) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if row[1] == 'X':  # Eliminating the first row (name, x , y, connections)
                    continue
                p = draw_xy.PlanPoint()
                p.name = row[0]  # Columns separation
                p.x = float(row[1])
                p.y = float(row[2])
                p.connections = str.split(row[3], ',')
                self.allpoints[p.name] = p  # Creation of all points



    def set_start_pos(self,start_pos):
        self.start_pos = list(start_pos)

    def set_scale(self,scale):
        self.scale = scale

    def start_draw(self):
        print(self.window.window_width(),self.window.window_height())

        temp_point ={}
        while True:
            print(self.scale)
            print(self.start_pos)
            min_x = 20000
            min_y = 20000
            max_x = -20000
            max_y = -20000

            temp_point = self.copy.deepcopy(self.allpoints)
            for pn in temp_point:
                p = temp_point[pn]
                p.x *= self.scale
                p.y *= self.scale
                p.x += self.start_pos[0]
                p.y += self.start_pos[1]


                min_x = min(min_x, p.x)
                min_y = min(min_y, p.y)
                max_x = max(max_x, p.x)
                max_y = max(max_y, p.y)


                temp_point[pn] = p


            print(max_x,min_x,max_y,min_y)
            if ((max_x-min_x) > self.window.window_width() or (max_y-min_y)>self.window.window_height()):
                self.scale *= 0.9
                continue

            if max_x > self.window.window_width()/2:
                self.start_pos[0] = (max_x - self.window.window_width())
                continue
            elif min_x < -self.window.window_width()/2:
                self.start_pos[0] = (min_x - self.window.window_width())
                continue

            if max_y > self.window.window_height()/2:
                self.start_pos[1] = (max_y - self.window.window_height())
                continue
            elif min_y <-self.window.window_height()/2:
                self.start_pos[1] = (min_y - self.window.window_height())
                continue

            break


        # Finding each points and their connections %%%%%%%%%%
        for pn in temp_point:  # Finding each points from dictionary
            p = temp_point[pn]
            # turtle draws dot for p
            self.goto(p.x, p.y)
            self.dot(5, "red")
            self.write(p.name)
            for c in p.connections:
                q = temp_point[c]
                # turtle draws line form p to q
                self.goto(p.x, p.y)
                self.pendown()
                self.goto(q.x, q.y)
                self.penup()

window = turtle.Screen()

p = draw_xy("Sample Plan.csv",window,start_pos=(-680,-280),scale=0.5)
p.set_scale(3)
p.set_start_pos((100,1000))
p.start_draw()

window.mainloop()






