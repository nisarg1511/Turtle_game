from turtle import Turtle, Screen
from random import Random
ran = Random()
colors = ["red","green","yellow","blue","red","purple"]
y_index = [-150,-100,-50,0,50,100]
turtles = []
for x in range(0,6):
    turtles.append(Turtle("turtle"))
    turtles[x].penup()
    turtles[x].goto(-250,y_index[x])
    turtles[x].color(colors[x])

scr = Screen()
user_input = scr.textinput("Make a bet","Which turtle do you think would win ?")
scr.setup(width=600,height=300)
is_race_on = False
if user_input:
    is_race_on = True
while is_race_on:
    for turtle in  turtles:
        turtle.forward(ran.randint(a=0,b=10))
        position = turtle.pos()
        if  position[0] >= 250:
            is_race_on = False
            if user_input == turtle.color()[0]:
                print(f"{turtle.color()[0]} won the race. You won the bet.")
            else:
                print(f"{turtle.color()[0]} has won the race.You lost the bet."
                      f"")
scr.listen()
scr.exitonclick()
