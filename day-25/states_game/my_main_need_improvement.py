import turtle as t
import pandas as pd


screen = t.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)


answer_state = screen.textinput(
    title="Guess the State", prompt="What's another state's name?"
)
# print(answer_state)
# answer_state = answer_state.capitalize()


"""This is what I got on my own, but I could not remember how to use Turtle properly. I will try to use the solution to understand how to use Turtle properly"""
# state_name = pd.read_csv("50_states.csv")
# score = 0
# answered_states = []
# if answer_state in state_name.values and answer_state not in answered_states:
#     print("Yes")
#     score += 1
#     answered_states.append(answer_state)
#     screen.title("U.S. States Game | Score: {score}")
# else:
#     print("No")
# t.mainloop()

data = pd.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_state = []
score = 0

while len(guessed_state) < 50:
    if answer_state in all_states:
        guessed_state.append(answer_state)
        # t = t.turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        score += 1
        screen.title("United States Game | Score: {score} out of 50 states")


screen.exitonclick()
