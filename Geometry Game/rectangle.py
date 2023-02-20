from random import randint


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rect):
        if rect.point1.x < self.x < rect.point2.x and \
                rect.point1.y < self.y < rect.point2.y:
            return True
        else:
            return False

    def set_point(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def get_point(self):
        return self.x, self.y


class Rectangle:
    def __init__(self, point1, point2, point3, point4):
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.point4 = point4
        self.breadth = self.get_length(self.point1, self.point2)
        self.height = self.get_length(self.point1, self.point4)

    @staticmethod
    def distance_between_two_points(point1, point2):
        return ((point2.x - point1.x) ** 2 + (point2.y - point1.y) ** 2) ** 0.5

    def get_length(self, point1, point2):
        return self.distance_between_two_points(point1, point2)

    def area(self):
        return self.breadth * self.height


class GUIRectangle(Rectangle):

    def draw(self, canvas):
        canvas.penup()
        canvas.ht()
        canvas.goto(0, 0)
        canvas.st()
        canvas.pendown()
        for i in range(0, 2):
            canvas.forward(self.breadth)
            canvas.left(90)
            canvas.forward(self.height)
            canvas.left(90)


def create_points():
    x = Point(randint(10, 100), randint(20, 200)).x
    y = Point(randint(20, 100), randint(20, 200)).y

    return x, y


# print(create_points())
def create_points_2(**kwargs) -> object:
    """

    :rtype: object
    """
    point1 = Point()
    point2 = Point()
    point3 = Point()
    point4 = Point()
    for i in range(1, 10 ** 3):
        x, y = create_points()
        k, l = create_points()
        if (x > k and (x - k) > 5) and (y == l):
            point1.set_point(x, y)
            point2.set_point(k, l)

            break

    for i in range(1, 10 ** 3):
        a, b = create_points()
        c, d = create_points()
        if (a > c and (a - c) > 5) and (b == d):
            point3.set_point(a, b)
            point4.set_point(c, d)

            break

    return point1, point2, point3, point4
