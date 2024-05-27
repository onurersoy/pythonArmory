# It's about importing modules
# import turtle
# from turtle import forward, right, done

done = "Well done, you have finished your drawing"

from turtle import *

forward(150)
right(250)
forward(150)
circle(75)

done()
print(done)  # notice that you don't get the string message but instead the function address of turtle.done() method

# You should avoid this way of importing because you actually have no idea what is being imported, so an imported name
# can hide one of your objects, or you can hide one of the imported names that you need. F.e. check the string above
# called 'done' and run the program to see the problem.

# Now if you change the lines 5 and 7, you will get a different behaviour also a type error on a different line
# comparing the current one as this time; 'done' string will go over the import and done method will act like the
# string one, but it's not a callable object, so that's why you will get a type error.
