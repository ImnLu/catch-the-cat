import turtle

# importing cat image
turtle.register_shape("cat100x100.gif")

# creating screen
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Catch the Cat!")

# creating cat
t = turtle.Turtle()
t.shape("cat100x100.gif")

turtle.mainloop()
