"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Zachary Juday.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
mike = rg.SimpleTurtle('classic')
mike.pen = rg.Pen('violet', 0.5)
mike.speed = 50
window.tracer(200)
for k in range(100):
    mike.forward(60+k)
    mike.left(130)
    mike.forward(60+k)
    mike.right(90)
    mike.backward(60+k)
    mike.right(60)
    mike.pen_up()
    mike.right(90)
    mike.forward(5)
    mike.left(90)
    mike.pen_down()
sally = rg.SimpleTurtle('classic')
sally.pen = rg.Pen('pink',1)
sally.speed = 50
for k in range(230):
    sally.forward(30+k)
    sally.left(90)
    sally.forward(30+k)
    sally.left(90)
    sally.forward(30 + k)
    sally.left(90)
    sally.forward(30 + k)
    sally.left(90)
    sally.pen_up()
    sally.right(60 + k)
    sally.forward(5)
    sally.left(60 + k)
    sally.pen_down()
window.close_on_mouse_click()
