# import turtle
# t=turtle.Turtle()
# t.speed(1)
# for culoare in ["red","green","yellow","blue"]:
#     t.color(culoare)
#     t.forward(175)
#     t.left(90)
# print("gata primul nostru patrat multicolor")
#
# n = int(input("n="))
# suma = 0
# while n!=0:
#     suma = suma + n%10 #adun ultima cifră
#     n = n // 10 #noul număr fără ea
# print("Suma este",suma)


# import turtle
# t=turtle.Turtle()
# n=int(input("Numarul de laturi"))
# u=360/n
# laturi=1
# while laturi<=n:
#     t.fd(50)
#     t.lt(u)
#     laturi=laturi+1


import turtle
t = turtle.Turtle()
raza = 5
while raza <= 75:
    t.circle(raza)
    t.left(20)
    raza += 5