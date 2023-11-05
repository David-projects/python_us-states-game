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
data = pandas.read_csv(STATES_FILE)
states = data.state.to_list()
guessed_states = []
print(states)
# get answer to question
answer_state = screen.textinput(title="0/50 Guess the State", prompt="What's a state's name?").capitalize()

game_is_on = True
score = 0
loops = 0

while game_is_on:
    loops += 1
    if answer_state in states:
        guessed_states.append(answer_state)
        score += 1
        sam = turtle.Turtle()
        sam.color("black")
        sam.penup()
        sam.hideturtle()
        state_data = data[data.state == answer_state]
        sam.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        sam.write(arg=answer_state, move=False, align="Center", font=('Arial', 8, 'normal'))

    if loops >= len(states):
        game_is_on = False

    try:
        answer_state = screen.textinput(title=f"{score}/50 Guess the State",
                                        prompt="What's a state's name?").capitalize()
    except:
        game_is_on = False

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in  guessed_states]
        to_learn = pandas.DataFrame(missing_states)
        to_learn.to_csv("missing_states.txt")
        game_is_on = False


