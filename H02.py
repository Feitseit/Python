# 2. ülesanne
# 05.12.24
import turtle
"""
    Loo värvilised olümpiarõngad vastavalt nõutele
    Loo aken, mille nimi on “Olümpiarõngad ja sinu nimi”
    Akna suurus 500×400
    Loo värvilised 50px olümpiarõngad (sinine, must, punane, kollane, roheline)
    Joone paksus 6
    Kiirus 0
"""

# sinine ring
turtle.speed(0)
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
turtle.color("blue")
turtle.pensize(5)
turtle.circle(50,360)
# must ring
turtle.speed(0)
turtle.penup()
turtle.goto(-90,100)
turtle.pendown()
turtle.color("black")
turtle.pensize(5)
turtle.circle(50,360)
# punane ring
turtle.speed(0)
turtle.penup()
turtle.goto(20,100)
turtle.pendown()
turtle.color("red")
turtle.pensize(5)
turtle.circle(50,360)
# yellow ring
turtle.speed(0)
turtle.penup()
turtle.goto(-145,50)
turtle.pendown()
turtle.color("yellow")
turtle.pensize(5)
turtle.circle(50,360)
# roheline ring
turtle.speed(0)
turtle.penup()
turtle.goto(-35,50)
turtle.pendown()
turtle.color("green")
turtle.pensize(5)
turtle.circle(50,360)



"""
    Loo sinilill vastavalt nõuetele
    Loo aken 500×500
    Akna nimi Sinilill ja sinu nimi
    Joone paksus 10
    Kiirus “fastest“
    Vars ja leht rohelised
    Lille kroonlehed tumesinise äärega ja sisu helesinine
    Südamik kollane
"""

turtle.penup()
turtle.pensize(10)
turtle.color("blue")
turtle.goto(300,100)
turtle.pendown()
turtle.circle(50,360)
turtle.fillcolor("lightblue")
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

turtle.penup()
turtle.goto(300,100)
turtle.pendown()
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.end_fill()



