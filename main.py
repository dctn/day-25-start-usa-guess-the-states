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
# looping program
game_on = True
guessed_states = []
unguessed_states = []
while game_on:

    user_input_raw = screen.textinput(title="guess the states", prompt=f"you guessed {score}/50 states")
    user_input = str(user_input_raw).capitalize()

    if user_input == "Exit":
        game_on = False
        for i in states_name_list:
            if i not in guessed_states:
                unguessed_states.append(i)

        unguessed_states_dict = {
            "unguessed states": unguessed_states
        }
        unguessed_states_data = pandas.DataFrame(unguessed_states_dict)
        unguessed_states_data.to_csv("unguessed states.csv")



    if user_input in states_name_list:
        guessed_states.append(user_input)
        state_position(user_input)
        score += 1


