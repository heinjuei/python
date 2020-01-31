for friend in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hello ", friend, "  Please come to my party on saturday!")

# Iteration or repetition white turtle

import turtle            # cria alex
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0,1,2,3]:      # repita 4 vezes
    alex.forward(50)
    alex.left(90)

wn.exitonclick()

""" import turtle            # cria alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:  # repita 4 vezes
    alex.forward(50)
    alex.left(90)

# com cores

wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]: # repita 4 vezes
   alex.color(aColor)
   alex.forward(50)
   alex.left(90)

wn.exitonclick() """