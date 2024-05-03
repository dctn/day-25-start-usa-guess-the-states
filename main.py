import turtle as t
import pandas

# data analysis program
data = pandas.read_csv("50_states.csv")

states_names = data.state
states_name_list = states_names.to_list()

# screen and turtle program
turtle = t.Turtle()
screen = t.Screen()
screen.title(titlestring="U.S.A states", )
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)


def states_names(x_pos, y_pos):
    name = t.Turtle()
    name.penup()
    name.goto(x=x_pos, y=y_pos)
    name.hideturtle()
    name.write(arg=user_input, align="center", font=("Arial", 8, "normal"))


def state_position(user_input):
    guess_row = data[data.state == user_input]
    x_cor_raw = guess_row.x
    x_cor_list = x_cor_raw.to_list()
    x_cor = x_cor_list[0]

    y_cor_raw = guess_row.y
    y_cor_list = y_cor_raw.to_list()
    y_cor = y_cor_list[0]
    states_names(x_pos=x_cor, y_pos=y_cor)


score = 0


# def score_func(score_parameter):
#     score_parameter += 1
    # return score
#

# looping program
game_on = True
while game_on:

    user_input_raw = screen.textinput(title="guess the states", prompt=f"you guessed {score}/50 states")
    user_input = str(user_input_raw).capitalize()

    if user_input in states_name_list:
        state_position(user_input)
        score += 1

        # score_func(score)

        # guess_row = data[data.state == user_input]
        # x_cor_raw = guess_row.x
        # x_cor_list = x_cor_raw.to_list()
        # x_cor = x_cor_list[0]
        #
        # y_cor_raw = guess_row.y
        # y_cor_list = y_cor_raw.to_list()
        # y_cor = y_cor_list[0]
        #
        # name = t.Turtle()
        # name.penup()
        # name.goto(x=x_cor, y=y_cor)
        # name.hideturtle()
        # name.write(arg=user_input, align="center", font=("Arial", 8, "normal"))

screen.exitonclick()
