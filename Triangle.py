from tkinter import *
import random

running = False

#the fixed points to move to within the triangle
x1 = 250       
y1 = 40
x2 = 40
y2 = 460
x3 = 460
y3 = 460

#the starting point to move from
xS = 0
yS = 0

#draw the fixed/starting points on the canvas
def mainPoints():  
    point1=canvas.create_rectangle(245,35,255,45, fill="Blue")
    point2=canvas.create_rectangle(35,455,45,465, fill="Blue")
    point3=canvas.create_rectangle(455,455,465,465, fill="Blue")
    startPoint=canvas.create_rectangle(0,0,0,0, fill="Red")

#create new points based on the random number
def createPoints(xCord,yCord):
    global xS
    global yS
    x = xCord - xS
    y = yCord - yS
    xx = xS + (x / 2)
    yy= yS +(y / 2)
    canvas.create_rectangle(xx,yy,xx,yy)
    xS = xx
    yS = yy
    root.update()

#test to see if the running is true and generate 
#numbers and call createPoints()
def scanning():
    if running == True:
        RN=random.randint(1,3)
        if RN == 1:
            createPoints(x1,y1)
        if RN == 2:
            createPoints(x2,y2)
        if RN == 3:
            createPoints(x3,y3)
    if running == True:
        root.update()
    root.after(1, scanning)

#start command
def start():
    global running
    running = True
    
#stop command
def stop():
    global running
    running = False

#create a start and stop button
def buttons_start_call():
    startButton = Button(root, width=12, height=1, text="Start", command=start)
    stopButton = Button(root, width=12, height=1, text="Stop", command=stop)
    startButton.grid(row = 0, sticky = W)
    stopButton.grid(row = 1, sticky = W)

#create the canvas to draw on
root=Tk()
root.title("Sierpinski's Triangle")
root.configure(background="White")
buttons_start_call()
canvas=Canvas(root, width=500, height=500, bg="White")
canvas.grid()

#call mainPoints() and scanning()
mainPoints()
scanning()

#update the canvas and keep it running
root.update()
root.mainloop()
