import turtle
import pandas

screen = turtle.Screen()
screen.title("Polish Voivodeships Game")
image = "Voivodeships_of_Poland.gif"
screen.addshape(image)
turtle.shape(image)

pointer = turtle.Turtle()
pointer.hideturtle()
pointer.penup()
pointer.speed("fastest")

data = pandas.read_csv("voivodeships.csv")

for i in range(16):
    answer_voivodeship = screen.textinput(title=f"Guess the voivodeship {i}/16",
                                          prompt="What's another voivodeship name?")
    if answer_voivodeship in data.voivodeship.to_string() and answer_voivodeship != "":
        voiv = data[data.voivodeship.str.lower() == answer_voivodeship.lower()]
        voivodeship_name = voiv.voivodeship.to_string(index=False)
        x, y = float(voiv.x.to_string(index=False)), float(voiv.y.to_string(index=False))
        pointer.setposition(x, y)
        pointer.write(voivodeship_name, font=("Arial", 10, "bold"))
        i += 1
    else:
        continue

screen.mainloop()
