#use arrows or WASD to change directions
#you can customize the below values

size=20 #Size of the board. A size over 100 gets ridiculous. 300+ you become blind. 500+ crashes
num_food=5 #Number of food in rotation, each one after the first increasing in power. Also increases the time between food spawns
delay=0.2 #Limit to the max speed of ticks in the game in seconds. Lower numbers are faster unless your computer can't keep up

import simplegui
import time
import random
gameover=2
def draw(canvas):
    global t, alt,gameover,food,size
    if gameover==0:
        alt*=-1
        if alt==1:
            while (time.time()-t)<0.2:
                wait=1
            for i in range(num_food):
                if (food[str(i)+"timer"]==0):
                    food[str(i)+"x"]=random.randint(0,size-1)
                    food[str(i)+"y"]=random.randint(0,size-1)
                    while (level[food[str(i)+"x"]][food[str(i)+"y"]]!=0):
                        food[str(i)+"x"]=random.randint(0,size-1)
                        food[str(i)+"y"]=random.randint(0,size-1)
                    level[food[str(i)+"x"]][food[str(i)+"y"]]=-1*(i+1)
                food[str(i)+"timer"]-=1
        else:
            t=time.time()
            global facing,length,x,y,press
            level[x][y]=2
            if (facing==1 and y>0): #up
                if not(level[x][y-1]>0):
                    if (level[x][y-1]!=0):
                        eat(level[x][y-1])
                    level[x][y-1]=1
                    y=y-1
                else:
                    gameover=1
            elif (facing==2 and x<size-1): #right
                if not(level[x+1][y]>0):
                    if (level[x+1][y]!=0):
                        eat(level[x+1][y])
                    level[x+1][y]=1
                    x=x+1
                else:
                    gameover=1
            elif (facing==3 and y<size-1): #down
                if not(level[x][y+1]>0):
                    if (level[x][y+1]!=0):
                        eat(level[x][y+1])
                    level[x][y+1]=1
                    y=y+1
                else:
                    gameover=1
            elif (facing==4 and x>0): #left
                if not(level[x-1][y]>0):
                    if (level[x-1][y]!=0):
                        eat(level[x-1][y])
                    level[x-1][y]=1
                    x=x-1
                else:
                    gameover=1
            else:
                gameover=1
            press=0
        for i in range(size):
            for o in range(size):
                if level[i][o]>(length):
                    level[i][o]=0
                if level[i][o]==1:
                    canvas.draw_line((i*500/size+0.5,(o+0.5)*500/size),((i+1)*500/size-0.5,(o+0.5)*500/size),500/size-1,"white")
                elif level[i][o]>1:
                    if (alt==1):
                        level[i][o]+=1
                    canvas.draw_line((i*500/size+0.5,(o+0.5)*500/size),((i+1)*500/size-0.5,(o+0.5)*500/size),500/size-1,"white")
                if level[i][o]<0:
                    canvas.draw_circle(((i+0.5)*500/size+0.5,(o+0.5)*500/size),250/size,0.5,"black","rgb("+str(level[i][o]*-255/num_food)+","+str(level[i][o]*-255/num_food)+","+str(285-level[i][o]*-255/num_food)+")")
    elif (gameover==1):
        canvas.draw_text("Gameover",(50,300),50,"white")
        canvas.draw_text("click to restart",(50,400),50,"white")
    else:
        canvas.draw_text("Click to start",(50,300),50,"white")
#def actual_draw():
#    global size
#    for i in range(size):
#        for o in range(size):
#            if level[i][o]==1:
#                canvas.draw_line((i*500/size+0.5,(o+0.5)*500/size),((i+1)*500/size-0.5,(o+0.5)*500/size),500/size-1,"white")
def key(k):
    global facing,t,press
    if (press==0):
        if (k==73 or k==38 or k==87) and facing!=3 and facing!=1: #up
            facing=1
            press=1
        elif (k==74 or k==37 or k==65) and facing!=2 and facing!=4: #left
            facing=4
            press=1
        elif (k==75 or k==40 or k==83) and facing!=1 and facing!=3: #down
            facing=3
            press=1
        elif (k==76 or k==39 or k==68) and facing!=4 and facing!=2: #right
            facing=2
            press=1
def click(c):
    global gameover,t,level,length,facing,alt,press,x,y,food,num_food
    if gameover!=0:
        gameover=0
        t=time.time()
        level=[]
        length=3
        facing=2
        alt=-1
        press=0
        for i in range(size):
            level.append([])
            for o in range(size):
                level[i].append(0)
        level[int(size/2)][int(size/2)]=1
        x=int(size/2)
        y=int(size/2)
        food={}
        for i in range(num_food):
            food[str(i)+"x"]=0
            food[str(i)+"y"]=0
            food[str(i)+"timer"]=4*num_food*i
def eat(f):
    global food,length,num_food
    food[str((f*-1)-1)+"timer"]=4*num_food*(f*-1)-4*num_food
    length+=(f*-1)
    long.set_text('Length: '+str(length))
#class food:
#    def __init__(self,l,px,py):
#        self.lev=l
#        self.posx=px
#        self.posy=py
#        self.active=False
#    def eat(self):
        
frame = simplegui.create_frame("Snake", 500, 500)
frame.set_keydown_handler(key)
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
long = frame.add_label('Length: 3')
long.set_text('Length: 3')
#score = frame.add_label('Score: 0')
#score.set_text('Score: 0')
frame.start()
