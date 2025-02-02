import turtle
t=turtle.Turtle()
t.color("red")
t.pensize(2)
t.speed(0)

def copac(lungime):
    if lungime<5:
        t.fd(lungime)
        t.bk(lungime)
        return
    t.fd(lungime/3)
    t.lt(30);copac(lungime*2/3);t.rt(30)
    t.fd(lungime/6)
    t.lt(30);copac(lungime/2);t.rt(30)
    t.fd(lungime / 3)
    t.lt(30);copac(lungime /2);t.rt(30)
    t.fd(lungime / 6)
    t.bk(lungime)
t.lt(90)
copac(140)


