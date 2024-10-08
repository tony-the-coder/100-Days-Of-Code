import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(
        title=f"len(guessed_state)/50 States Correct",
        prompt="What's another state's name?",
    ).title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

# TODO1: Get a good way to mark if someone got an answer wrong.

# States to learn a CSV story
with open("states_to_learn.csv", "w") as file:
    file.write("state\n")
    for state in all_states:
        if state not in guessed_state:
            file.write(f"{state}\n")


screen.exitonclick()
