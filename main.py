import turtle
import pandas

screen = turtle.Screen()
screen.title("Polish Voivodeships Game")
image = "Voivodeships_of_Poland.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("voivodeships.csv")
all_voivodeships = data.voivodeship.to_list()
guessed_voivodeships = []

while len(guessed_voivodeships) < 17:
    answer_voivodeship = screen.textinput(title=f"Guess the voivodeship {len(guessed_voivodeships)}/16",
                                          prompt="What's another voivodeship name?").title()
    if answer_voivodeship in all_voivodeships:
        guessed_voivodeships.append(answer_voivodeship)
        voiv = data[data.voivodeship == answer_voivodeship]
        voivodeship_name = voiv.voivodeship.item()

        pointer = turtle.Turtle()
        pointer.hideturtle()
        pointer.penup()
        pointer.speed("fastest")
        pointer.setposition(voiv.x.iloc[0], voiv.y.iloc[0])
        pointer.write(voivodeship_name, font=("Arial", 10, "bold"))

screen.exitonclick()
