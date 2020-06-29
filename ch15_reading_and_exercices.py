class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):  # All we have done is renamed the method
        return "({0}, {1})".format(self.x, self.y)

    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def reflect_x(self):
        return self.x, -self.y

    def slope_from_origin(self):
        return self.y / self.x

    def get_line_to(self, target):
        slope = (target.y - self.y) / (target.x - self.x)
        intercept = self.y - (slope * self.x)
        return slope, intercept

    def midpoint_circle(self, target1):
        return ((self.x + target.x) / 2), ((self.y + target.y) / 2)


p = Point()  # Instantiate an object of type Point
q = Point()  # Make a second point
r = Point()
# print(p.x, q.y, r.x)
p.x = 3
p.y = 4


# print(p.x, p.y, q.x, q.y)       # Each point object has its own x and y\
#
#
# print("(x={0}, y={1})".format(p.x, p.y))
# distance_squared_from_origin = p.x * p.x + p.y * p.y


def print_point(pt):
    print("({0}, {1})".format(pt.x, pt.y))

    def midpoint(p1, p2):
        """ Return the midpoint of points p1 and p2 """
        mx = (p1.x + p2.x) / 2
        my = (p1.y + p2.y) / 2
        return Point(mx, my)


def distance(a, b):
    dx = b.x - a.x
    dy = b.y - a.y
    dsquared = dx * dx + dy * dy
    result = dsquared ** 0.5
    return result


p = Point(4, 3)
print(distance(Point(1, 1), Point(3, 3)))
print(Point(4, 11).get_line_to(Point(6, 15)))




