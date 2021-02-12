#Shows the time based off your system clock and is adjusted to be in the time zone -5 from central
#You can change the theme color through the color menu represented by the color wheel
#Typically you want the menu toggled off as it causes lag
import simplegui
import math
import time
timezone=-5
color=[255,255,255]
showColor=False
r=0
b=0
def draw(canvas):
    global r,showColor,b
    if (b==1):
        b=0
        frame.set_canvas_background("rgb("+str(color[0])+","+str(color[1])+","+str(color[2])+")")
    main="rgb("+str(color[0]*-1+255)+","+str(color[1]*-1+255)+","+str(color[2]*-1+255)+")"
    canvas.draw_line((650,0),(650,500),300,"Black")
    canvas.draw_circle((250,250),5,15,main)
    if (showColor==True):
        canvas.draw_line((521.5,29),(778.5,29),11,"white")
        canvas.draw_line((521.5,200),(778.5,200),257,"white")
        for i in range(128):
            canvas.draw_line((522+i*2,29),(524+i*2,29),10,"rgb("+str(i*2)+",0,0)")
            for o in range(128):
                canvas.draw_line((522+i*2,73+o*2),(524+i*2,73+o*2),2,"rgb("+str(r)+","+str(i*2)+","+str(o*2)+")")
    for i in range(360):
        canvas.draw_line((525,475),(525+math.cos(i*math.pi/180)*20,475+math.sin(i*math.pi/180)*20),1,"rgb("+str(-math.sin(i*math.pi/180)*128+128)+","+str(-math.cos(i*math.pi/180)*128+128)+","+str(math.sin(i*math.pi/180)*128+128)+")")
    canvas.draw_line((250+3*math.sin((time.time()/3600)*math.pi*2),250-3*math.cos((time.time()/3600)*math.pi*2)),(250+200*math.sin((time.time()/3600)*math.pi*2),250-200*math.cos((time.time()/3600)*math.pi*2)),5,main)
    canvas.draw_line((250+3*math.sin((time.time()/60)*math.pi*2),250-3*math.cos((time.time()/60)*math.pi*2)),(250+210*math.sin((time.time()/60)*math.pi*2),250-210*math.cos((time.time()/60)*math.pi*2)),3,main)
    canvas.draw_line((250+3*math.sin(((time.time()/43200))*math.pi*2+timezone*math.pi/6),250-3*math.cos(((time.time()/43200))*math.pi*2+timezone*math.pi/6)),(250+100*math.sin(((time.time()/43200))*math.pi*2+timezone*math.pi/6),250-100*math.cos(((time.time()/43200))*math.pi*2+timezone*math.pi/6)),7,main)
def mouse_handler(pos):
    global color,showColor,r,b
    x=pos[0]
    y=pos[1]
    if (20>=math.sqrt((x-525)**2+(y-475)**2)):
        showColor=not(showColor)
    elif (x>=522 and x<=778 and showColor==True):
        if (y>=24 and y<=34):
            r=x-522
        elif (y>=73 and y<=328):
            color=[r,x-522,y-73]
            b=1
frame = simplegui.create_frame("Clock", 800, 500)
frame.set_canvas_background("White")
frame.set_mouseclick_handler(mouse_handler)
frame.set_draw_handler(draw)
frame.start()
