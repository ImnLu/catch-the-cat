import turtle

# turtle object
img_turtle = turtle.Turtle()

# registering the image
# as a new shape
turtle.register_shape('cat100x100.gif')

# setting the image as cursor
img_turtle.shape('cat100x100.gif')

turtle.mainloop()