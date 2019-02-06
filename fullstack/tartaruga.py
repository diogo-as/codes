import turtle

window = turtle.Screen()
window.title("My first python drawing")
window.bgcolor("gray")

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("black", "black")
    brad.speed(1)
    brad.fill(True)
    for i in range(4):
        brad.forward(200)
        brad.left(90)
    brad.end_fill()


def draw_circle():
    angel = turtle.Turtle()
    angel.shape("circle")
    angel.color("red")
    angel.right(180)
    angel.circle(100)


def draw_triangle():
    chapie = turtle.Turtle()
    chapie.shape("triangle")
    chapie.color("green")
    chapie.left(120)
    for i in range(3):
        chapie.forward(200)
        chapie.left(120)

draw_square()
draw_circle()
draw_triangle()

window.exitonclick()
