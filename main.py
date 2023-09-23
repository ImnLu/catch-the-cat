import random
import time
import turtle

# importing cat image
turtle.register_shape("cat75x75.gif")

# creating screen
wn = turtle.Screen()
wn.bgcolor("light blue")
wn.title("Catch the Cat!")


# functions
def score_changer(score):  # score changer
    t_score.clear()
    t_score.penup()
    t_score.goto(0, turtle.window_height() // 2 - 40)
    t_score.write(f"Score: {score}", align="center", font=("Verdana", 20, "bold"))


def time_changer(rem_time):  # time changer
    t_time.clear()
    t_time.penup()
    t_time.goto(0, turtle.window_height() // 2 - 80)
    t_time.write(f"Time: {rem_time}", align="center", font=("Verdana", 20, "bold"))


def cat_move():  # moves the cat randomly
    x, y = random.randint(-turtle.window_width() // 2 + 50, turtle.window_width() // 2 - 50), random.randint(
        -turtle.window_height() // 2 + 50, turtle.window_height() // 2 - 120)
    t_cat.ht()
    t_cat.goto(x, y)
    t_cat.st()
    if game_time > 0:
        turtle.ontimer(cat_move, 1000)


def cat_clicked(x, y):  # clicking on the cat increases user score
    print(x, y)
    t_cat.ht()
    t_cat.goto(int(turtle.window_width()) + 100, int(turtle.window_height()) + 100)
    global user_score
    user_score += 1


def update_screen():  # updates the screen throughout the game duration
    global game_time
    score_changer(user_score)
    time_changer(game_time)
    game_time -= 1
    if game_time > 0:
        turtle.ontimer(update_screen, 1000)
    else:
        time_changer("Game Over!")


# creating turtles
t_score = turtle.Turtle(visible=False)
t_time = turtle.Turtle(visible=False)
t_cat = turtle.Turtle()

# game variables
game_time = 30
user_score = 0

# cat settings
t_cat.ht()
t_cat.shape("cat75x75.gif")
t_cat.penup()
t_cat.speed("fastest")
t_cat.onclick(cat_clicked)

# shows default score and remaining time
score_changer(user_score)
time_changer(game_time)
time.sleep(3)

# screen updates
cat_move()
update_screen()

turtle.mainloop()
