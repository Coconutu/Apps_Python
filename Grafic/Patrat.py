import turtle #importăm modulul
t = turtle.Turtle() #reținem țestoasa în t
t.color("red") #culoarea de desenare
t.forward(75) #înainte 75 de pixeli
t.left(90) #rotim 90 de grade
#repetăm mișcarea de încă 3 ori
t.forward(75) #prescurtat, fd
t.left(90) #prescurtat, lt
t.forward(75)
t.left(90)
t.forward(75)
t.left(90)
print("Gata primul nostru pătrat roșu!")