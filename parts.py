from turtle import setheading, color, begin_fill, left, forward, right, end_fill, circle, fillcolor
from helpers import restore_state_when_finished

import math

def ngon(num_sides, size):
    '''
    This function draw a regular polygon with 
    `num_sides` sides, each with length of `size`. 
    '''
    for i in range(num_sides):
        forward(size)
        right(360/num_sides)

def draw_triangle(side_len, color_name):
    '''
    This function draws an equilateral triangle with
    side lengths `side_len` and color `color_name`.
    '''
    with restore_state_when_finished():
        color(color_name)
        begin_fill()
        for i in range(3):
            forward(side_len)
            right(120)
        end_fill()

def customized_circle(size, color_name):
    '''
    This function draws a circle with radius `size`
    and color `color_name`.
    '''
    color(color_name)
    begin_fill()
    circle(size)
    end_fill()

def petal(size, color_name):
    '''
    This function draws a single petal of a flower
    with size determined by `size` and of color `color_name`.
    '''
    color("white")
    fillcolor(color_name)
    begin_fill()
    for i in range(int(size/2)):
        forward(i)
        right(360/size/2)
    right(90)
    for i in range(int(size/2)):
        forward(i)
        right(360/size/2)
    end_fill()

def flower(size, num_petals, color_name, rotation):
    '''
    This function draws a full flower with `num_petals` petals,
    each with size determined by `size` and color determined by `color_name`.
    `rotation` in a number of degrees that the flower should be rotated
    from 0 degrees (right).
    '''
    for i in range(num_petals):
        setheading(rotation + (360/num_petals * i))
        petal(size, color_name)