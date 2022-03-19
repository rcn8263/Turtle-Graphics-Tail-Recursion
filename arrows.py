"""
   Use turtle graphics to draw arrows using tail
   recursion and while loop

   assignment: Lab 3
   file: arrows.py
   author: Ryan Nowak
"""

# imports

import turtle as tt
import math
import random

# global Variables

MAX_FIGURES = 500
BOUNDING_BOX = 200
MAX_DISTANCE = 30
MAX_SIZE = 30
MAX_ANGLE = 30

# definitions


def draw_triangle(size):
    """
    draw_triangle draws a filled triangle of random color

    size - length of one side of triangle

    pre-condition - pen is up, facing same direction as
                               before function is called
    post-condition - pen is up, facing same direction
    """
    tt.down()
    tt.color(random.random(), random.random(), random.random())
    tt.begin_fill()
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.end_fill()
    tt.up()


def draw_figures_rec(depth, accum=0):
    """
    draw_figures_rec draws a given number of triangles of
        random size and distance that all stay within a box
        using tail recursion

    depth - how many triangles to draw
    accum - total area of all triangles

    returns accum - positive float value

    pre-condition - pen is up, facing right
    post-condition - pen is up, facing the angle of the last triangle drawn
    """
    if depth <= 0:
        return accum
    else:
        size = random.randint(1, MAX_SIZE)
        distance = random.randint(1, MAX_DISTANCE)
        angle = random.randint(-MAX_ANGLE, MAX_ANGLE)

        if not is_in_box(size, distance):
            tt.left(180)

        tt.forward(distance)
        draw_triangle(size)
        tt.left(angle)
        accum += eq_tri_area(size)

        return draw_figures_rec(depth - 1, accum)


def draw_figures_iter(depth):
    """
    draw_figures_iter draws a given number of triangles of
        random size and distance that all stay within a box
        using a while loop

    depth - how many triangles to draw

    returns accum - positive float value

    pre-condition - pen is up, facing right
    post-condition - pen is up, facing the angle of the last triangle drawn
    """
    accum = 0
    while depth > 0:
        size = random.randint(1, MAX_SIZE)
        distance = random.randint(1, MAX_DISTANCE)
        angle = random.randint(-MAX_ANGLE, MAX_ANGLE)

        if not is_in_box(size, distance):
            tt.left(180)

        tt.forward(distance)
        draw_triangle(size)
        tt.left(angle)
        accum += eq_tri_area(size)
        depth -= 1

    return accum


def draw_bounding_box():
    """
    draw_bounding_box draws a box with a radius given by the constant
        BOUNDING_BOX

    pre-condition - pen is up, facing right
    post-condition - pen is up, facing right
    """
    tt.up()
    tt.forward(BOUNDING_BOX)
    tt.left(90)
    tt.down()
    tt.pencolor('black')
    tt.fillcolor(0.8, 0.8, 0.8)
    tt.begin_fill()
    tt.forward(BOUNDING_BOX)
    tt.left(90)
    tt.forward(BOUNDING_BOX * 2)
    tt.left(90)
    tt.forward(BOUNDING_BOX * 2)
    tt.left(90)
    tt.forward(BOUNDING_BOX * 2)
    tt.left(90)
    tt.forward(BOUNDING_BOX)
    tt.end_fill()
    tt.up()
    tt.right(90)
    tt.back(BOUNDING_BOX)


def is_in_box(size, distance):
    """
    is_in_box checks if the next triangle will be contained within
        the box and return true if it is and false if not

    size - length of one side of triangle
    distance - distance between triangles

    pre-condition - pen is up, facing same direction as
                               before function is called
    post-condition - pen is up, facing same direction
    """
    in_box = True
    tt.forward(distance + size)
    if (abs(tt.xcor()) + size + distance > BOUNDING_BOX or
        abs(tt.ycor()) + size + distance > BOUNDING_BOX):
        in_box = False
    tt.back(distance + size)
    return in_box


def eq_tri_area(side):
    """
    eq_tri_area calculates the area of the equilateral triangle

    side - length of one side of triangle
    """
    return (math.sqrt(3) / 4) * pow(side, 2)


def main():
    num_of_arrows = int(input("Arrows (0-500): "))
    if num_of_arrows < 0 or num_of_arrows > 500:
        print("Arrows must be between 0 and 500 inclusive.")
        exit()

    tt.speed(0)
    tt.up()
    draw_bounding_box()
    total_area_painted = draw_figures_rec(num_of_arrows)
    print("The total area painted is ", total_area_painted, " units.")
    input("Hit enter to continue...")
    tt.reset()

    tt.speed(0)
    tt.up()
    draw_bounding_box()
    total_area_painted = draw_figures_iter(num_of_arrows)
    print("The total area painted is ", total_area_painted, " units.")
    tt.done()
    print("Close the canvas window to quit.")


if __name__ == '__main__':
    main()
