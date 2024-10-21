from turtle import *

bgcolor("#d7f4f5")
penup()
pencolor("black")
fillcolor("#005cbf")
begin_fill() 
goto(-150, 0 )
pendown()
for i in range(2):
    forward(400) 
    left(90) 
    forward(200)
    left(90)

    
end_fill() 

penup()
goto(-150, 100)

fillcolor("#ffc720")
begin_fill()
for i in range (2) :
    forward(400)
    left(90)
    forward(30)
    left(90)
end_fill()

penup()
goto(-50, 0)

fillcolor("#ffc720")
begin_fill()
for i in range (2) :
    forward(30)
    left(90)
    forward(200)
    left(90)
end_fill()
penup()

goto(50, -100)

pendown()

write("SWEDISH KING ALEXANDER ISAK 👑", align='center', font=('Helvetica', 25, 'bold'))

# Hide the turtle and finish

hideturtle()

mainloop()