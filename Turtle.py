from turtle import * # for importing the turtle library file

#square
pensize(10)#thickness of line
pencolor("green")
fillcolor("blue") # color to be filled inside the shape
begin_fill() #start filling the color
for i in range(4):
    forward(200) #move the turtle forward
    left(90) # turn left - 90
end_fill() #end the fill color

#triangle
penup()
goto(-300, -150)
pendown()
pencolor("pink")
speed(0) #speed of the turtle -- 0 is fastest
fillcolor("purple") # color to be filled inside the shape
begin_fill() #start filling the color
for i in range(3):
    forward(200) #move the turtle forward
    left(120) # turn left - 90
end_fill() #end the fill color

#flag
penup()
goto(-300, -150)
pendown()
pencolor("pink")
speed(0) #speed of the turtle -- 0 is fastest
fillcolor("purple") # color to be filled inside the shape
begin_fill() #start filling the color
for i in range(3):
    forward(200) #move the turtle forward
    left(120) # turn left - 90
end_fill() #end the fill color




mainloop() #keep the window open #this should be your last line of code in any programme
