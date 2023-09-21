from turtle import *
import colorsys

speed(1000)
bgcolor("black")
h = 0

# Escribir el mensaje en letra blanca
penup()
goto(50, 180)  # Ajusta la posición en la que quieres escribir el mensaje
pendown()
color("white")
write(
      "Las flores amarillas llegaron antes, con colores adicionales blanco y rojo.\nNo siempre tienen que ser fisicas, hay más formas de hacerlo\nAprovecho mi profesión para hacerlo. Solo por guapa.\nEl aprecio y cariño que te tengo es gigante.\nA veces es dificil saber como demostrarlo.\nEspero tengas un buen día",
       align="right", 
       font=("Calibri", 10, "bold")
      )
penup()
goto(0, -100)
pendown()

penup()
goto(0, -100)
pendown()
color("green")
begin_fill()
rt(90)
fd(400)
lt(90)
fd(20)
lt(90)
fd(400)
lt(90)
fd(20)
end_fill()

penup()
goto(0,0)
pendown()

for i in range(22):
    for j in range(18):
        color("yellow")
        h += 0.005
        rt(90)
        circle(150 - i * 6, 90)
        lt(90)
        circle(150 - i * 6, 90)
        rt(100)
    # circle(40, 24)

penup()
goto(0, 40)
pendown()
color("#331213")
begin_fill()
circle(35)
end_fill()

done()