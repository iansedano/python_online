import math

class Point:
    """represents a point in 2-D space."""

blank = Point()
print(Point)
print(blank)


# /// ATTRIBUTES
print('\n\n/////ATTRIBUTES////')
blank.x = 3.0
blank.y = 4.0

print(blank.y)

print('(%g, %g)' % (blank.x, blank.y))

distance = math.sqrt(blank.x**2 + blank.y**2)

print(distance)

def print_point(p):
    print('(%g, %g)' % (p.x, p.y))

print_point(blank)

# /// RECTANGLES
print('\n\n/////RECTANGLES////')

class Rectangle:
    """represents a rectangle.

    attributes: width, height, corner.
    """

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

# /// INSTANCES AS RETURN VALUES
print('\n\n/////INSTANCES AS RETURN VALUES////')

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p

center = find_center(box)
print_point(center)

# /// OBJECTS ARE MUTABLE
print('\n\n/////OBJECTS ARE MUTABLE////')

box.width = box.width + 50
box.height = box.height + 100

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

print(box.width, box.height)
grow_rectangle(box, 50, 100)
print(box.width, box.height)


