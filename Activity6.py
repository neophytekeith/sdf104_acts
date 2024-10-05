from turtle import Turtle,Screen

my_screen = Screen()
my_screen.bgcolor("gray")
keith = Turtle()
keith.color("pink")
keith.color()
keith.turtlesize(3)
keith.pensize(5)

for i in range(10):
    keith.begin_fill()
    keith.fillcolor("dark red")
    keith.speed(4)
    keith.right(90)
    keith.forward(100)
    keith.right(90)
    keith.forward(100)
    keith.right(90)
    keith.forward(100)
    keith.right(90)
    keith.forward(100)
    keith.end_fill()

my_screen.exitonclick()
