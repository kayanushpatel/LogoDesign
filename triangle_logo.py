"""This program creates a triangle concept logo
using the turtle module in python.

Author: Kayanush Patel
Date Created: 08/31/2014
"""

import turtle

def triangle():
    #Creates first triangle
    turtle.hideturtle()
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)
    turtle.left(120)
    turtle.forward(200)

def turn_n_go():
    """Turns 10 degrees to the right and continues with
    pattern from main function below.
    """
    turtle.right(10)
    triangle()
    triangle()
    triangle()

def main():
    input("Press return to start drawing.")
    triangle()
    #input("Press return to continue.")
    triangle()
    triangle()

    turn_n_go()
    turn_n_go()
    turn_n_go()
    turn_n_go()
    turn_n_go()
    #stopper
    turn_n_go()
    turn_n_go()
    turn_n_go()
    turn_n_go()
    #stopper
    turn_n_go()
    turn_n_go()

    input("Press return to terminate program.")
    turtle.bye()

main()