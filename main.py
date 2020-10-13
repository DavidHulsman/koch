__author__ = 'David'

import turtle
from enum import Enum

FORWARDS = 'F'
LEFTWARDS = 'L'
RIGHTWARDS = 'R'


def generatedmoves(depth: int) -> str:
    """Recursively generates a list of commands for the turtle to follow"""

    if depth == 0:
        return FORWARDS

    result = generatedmoves(depth-1)

    return result + LEFTWARDS + result + RIGHTWARDS + result + LEFTWARDS + result


def drawKochSide(depth):
    turtle.speed(0)  # fastest speed
    moves = generatedmoves(depth)
    for move in moves:
        if move == FORWARDS:
            turtle.forward(300/3**depth)
        if move == LEFTWARDS:
            turtle.lt(60)
        if move == RIGHTWARDS:
            turtle.rt(120)
    return turtle


def main():
    sides = 3
    depth = 3		# how often the drawing should recurse
    rotation = 360 / sides  # rotation after drawing a side

    for n in range(sides):
        turtle = drawKochSide(depth)
        turtle.rt(rotation)

    turtle.done()


main()
