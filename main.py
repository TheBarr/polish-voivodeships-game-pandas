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
    try:
        answer_voivodeship = screen.textinput(title=f"Guess the voivodeship {len(guessed_voivodeships)}/16",
                                              prompt="What's another voivodeship name?").title()
    except AttributeError:
        break
    if answer_voivodeship == "Exit":
        voivodeships_to_learn = [voivodeship for voivodeship in all_voivodeships if
                                 voivodeship not in guessed_voivodeships]
        df = pandas.DataFrame(voivodeships_to_learn, columns=["To Learn"])
        df.to_csv('voivodeships_to_learn.csv', index=False)
        break
    elif answer_voivodeship in all_voivodeships:
        guessed_voivodeships.append(answer_voivodeship)
        voiv = data[data.voivodeship == answer_voivodeship]
        pointer = turtle.Turtle()
        pointer.hideturtle()
        pointer.penup()
        pointer.speed("fastest")
        pointer.setposition(voiv.x.iloc[0], voiv.y.iloc[0])
        pointer.write(voiv.voivodeship.item(), font=("Arial", 10, "bold"))
