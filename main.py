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


# functions
def score_changer(score):
    t_score.clear()
    t_score.penup()
    t_score.goto(0, turtle.window_height() // 2 - 40)
    t_score.write(f"Score: {score}", align="center", font=("Verdana", 20, "bold"))


def time_changer(rem_time):
    t_time.clear()
    t_time.penup()
    t_time.goto(0, turtle.window_height() // 2 - 80)
    t_time.write(f"Time: {rem_time}", align="center", font=("Verdana", 20, "bold"))


# creating texts
t_score = turtle.Turtle(visible=False)
t_time = turtle.Turtle(visible=False)

game_time = 30
user_score = 0

score_changer(user_score)
time_changer(game_time)

while game_time > 0:
    break

turtle.mainloop()
