# 3. ülesanne
# Metshein 05.12.24

#3.1
nimi ="Imre" #sõne, string, str
vanus = 20 #int, integer, täisarv
keskmine_hinne = 6.5 #komarv, float
#plussiga saan stringid kokku
print(nimi+", "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine_hinne))
#komaga saan mitu asja printida
print(nimi,",",vanus,"aastat vana ja keskmine hinne on",keskmine_hinne)
#lause vormindamine lünkadega
print(f"{nimi}, {vanus} aastat vana ja keskmine hinne on {keskmine_hinne}!")

#3.7

import turtle


kylje_pikkus = 100
nurk = 120
varv = "red"

turtle.speed(5)
turtle.color(varv)
#kolmnurk
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)


turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()

#kolnurk 2

turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)


turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()

#kolmnurk 3

turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)
turtle.forward(kylje_pikkus)
turtle.left(nurk)







turtle.done()

