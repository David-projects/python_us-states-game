import turtle
import pandas

IMAGE = "blank_states_img.gif"
STATES_FILE = "50_states.csv"
screen = turtle.Screen()
screen.title("U.S. States Game")

# set back ground image
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# load states file
states = pandas.read_csv(STATES_FILE)

# get answer to question
answer_state = screen.textinput(title="0/50 Guess the State", prompt="What's a state's name?").capitalize()

game_is_on = True
score = 0

while game_is_on:
    state = states[states['state'] == answer_state]

    if not len(state) == 0:
        score += 1
        sam = turtle.Turtle()
        sam.color("black")
        sam.penup()
        sam.hideturtle()
        sam.goto(int(state['x'].iloc[0]), int(state['y'].iloc[0]))
        sam.write(arg=answer_state, move=False, align="Center", font=('Arial', 8, 'normal'))

    if score >= len(states):
        game_is_on = False

    try:
        answer_state = screen.textinput(title=f"{score}/50 Guess the State",
                                        prompt="What's a state's name?").capitalize()
    except:
        game_is_on = False

screen.exitonclick()
