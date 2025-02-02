import turtle
t=turtle.Turtle()
t.color("red")
t.pensize(2)
t.speed(0)

def Koch(lungime):
    if lungime<=2:
        t.forward(lungime)
        return
    Koch(lungime/3)
    t.left(60)
    Koch(lungime/3)
    t.right(120)
    Koch(lungime/3)
    t.left(60)
    Koch(lungime/3)


Koch(300)


