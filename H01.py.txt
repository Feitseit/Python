# 01. ülesane
# Kleeman 05.12.24


# see impordib kilpkonna mooduli
import turtle

# kolmnurk

# reguleeri 1-9
turtle.speed(0)
# tõstab pliiasti ülesse
turtle.penup()
# liigub asukohale 
turtle.goto(-500,300)
# paneb pliiatsi kirjutamis valmis
turtle.pendown()

# liigutab konna edasi 200 pikslit ja joonistab vasakule liigutedes kolmnurga
turtle.forward(200)
turtle.left(120)
turtle.forward(200)
turtle.left(120)
turtle.forward(200)


# süda

turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.left(120)
turtle.fd(100)
turtle.circle(50,180)
turtle.right(90)
turtle.circle(50,180)
turtle.fd(100)



# lõpetab konna, et ei jookseks kokku.
turtle.done()