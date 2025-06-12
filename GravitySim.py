#You can only edit when you pause
#Add element button creates a default circle at (0,0)
#Clicking on an element will select it and show information about its position, size, mass, speed, and angle
#Once you select an element, you can select a piece of information to change and then use "input value" to change it
#Click on the fps and G_mult to then change their values in the input

#Visually shows 5 decimal points for position, speed, and angle but in reality stores it to about 14 or 15 decimal points
#Delete element button deletes the selected element
#Zoom will zoom in or out by a factor of 25%
#ShowInfo button will draw velocity vectors on every element
#Save/load: enter a code to load a specific setup. Enter in nothing to print out a code for your current setup
#Start/Pause: Toggles whether or not the simulation is running. Pause to edit values
fps=30 #Amount of frames that need to be processed by the computer before one second passes in the simulation (speed is in m/s)
#increase in fps is an increase in precision
G=6.674*10**(-11)
G_mult=11
Wait=False #if True, the code waits to run "x" frames per second. If False, simulation runs at max speed (more fps=slower speed)
import simplegui
import math
import time
e=[[50,50,40,10.2,0,0,"000000"]] #elements
#[x,y,size,mass,speed,angle,color(rrggbb)]
hx={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,
    0:"0",1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F",}
run=False
info=False
zoom=1.0
z=0
select=-1
infoSelect=-1
x=0
y=0
c=0
def draw(canvas):
    global Wait
    if (Wait==True):
        t=time.time()
    global e,run,zoom,select,x,y,infoSelect,hx,fps,G,c,G_mult
    canvas.draw_line((250,0),(250,500),1,"black")
    canvas.draw_line((0,250),(500,250),1,"black")
    for i in range(len(e)):
        canvas.draw_circle([(e[i][0])*zoom+250,(e[i][1])*zoom+250],(e[i][2])*zoom,1,"#"+hx[hx[e[i][6][0]]*-1+15]+e[i][6][1]+hx[hx[e[i][6][2]]*-1+15]+e[i][6][3]+hx[hx[e[i][6][4]]*-1+15]+e[i][6][5],"#"+e[i][6][0]+e[i][6][1]+e[i][6][2]+e[i][6][3]+e[i][6][4]+e[i][6][5])
    if info:
        for i in range(len(e)):
            canvas.draw_polygon([((e[i][0])*zoom+250+zoom*1*math.cos(3.141592653589793*(e[i][5]+90)/180),(e[i][1])*zoom+250+zoom*1*math.sin(3.141592653589793*(e[i][5]+90)/180)),((e[i][0])*zoom+250+zoom*8*e[i][4]*math.cos(3.141592653589793*e[i][5]/180)+zoom*5*math.cos(3.141592653589793*(e[i][5]+90)/180),(e[i][1])*zoom+250+zoom*8*e[i][4]*math.sin(3.141592653589793*e[i][5]/180)+zoom*5*math.sin(3.141592653589793*(e[i][5]+90)/180)),((e[i][0])*zoom+250+zoom*8*e[i][4]*math.cos(3.141592653589793*e[i][5]/180)+zoom*e[i][4]*math.cos(3.141592653589793*(e[i][5]+90)/180)+zoom*5*math.cos(3.141592653589793*(e[i][5]+90)/180),(e[i][1])*zoom+250+zoom*8*e[i][4]*math.sin(3.141592653589793*e[i][5]/180)+zoom*e[i][4]*math.sin(3.141592653589793*(e[i][5]+90)/180)+zoom*5*math.sin(3.141592653589793*(e[i][5]+90)/180)),((e[i][0])*zoom+250+zoom*10*e[i][4]*math.cos(3.141592653589793*e[i][5]/180),(e[i][1])*zoom+250+zoom*10*e[i][4]*math.sin(3.141592653589793*e[i][5]/180)),((e[i][0])*zoom+250+zoom*8*e[i][4]*math.cos(3.141592653589793*e[i][5]/180)+zoom*e[i][4]*math.cos(3.141592653589793*(e[i][5]-90)/180)+zoom*5*math.cos(3.141592653589793*(e[i][5]-90)/180),(e[i][1])*zoom+250+zoom*8*e[i][4]*math.sin(3.141592653589793*e[i][5]/180)+zoom*e[i][4]*math.sin(3.141592653589793*(e[i][5]-90)/180)+zoom*5*math.sin(3.141592653589793*(e[i][5]-90)/180)),((e[i][0])*zoom+250+zoom*8*e[i][4]*math.cos(3.141592653589793*e[i][5]/180)+zoom*5*math.cos(3.141592653589793*(e[i][5]-90)/180),(e[i][1])*zoom+250+zoom*8*e[i][4]*math.sin(3.141592653589793*e[i][5]/180)+zoom*5*math.sin(3.141592653589793*(e[i][5]-90)/180)),((e[i][0])*zoom+250+zoom*1*math.cos(3.141592653589793*(e[i][5]-90)/180),(e[i][1])*zoom+250+zoom*1*math.sin(3.141592653589793*(e[i][5]-90)/180))],0.4,"#"+e[i][6][0]+e[i][6][1]+e[i][6][2]+e[i][6][3]+e[i][6][4]+e[i][6][5],"#"+hx[hx[e[i][6][0]]*-1+15]+e[i][6][1]+hx[hx[e[i][6][2]]*-1+15]+e[i][6][3]+hx[hx[e[i][6][4]]*-1+15]+e[i][6][5])
    if (select!=-1):
        canvas.draw_polygon([(e[select][2]*zoom+(e[select][0])*zoom+250,e[select][2]*zoom+(e[select][1])*zoom+250),(e[select][2]*zoom+(e[select][0])*zoom+250,-e[select][2]*zoom+(e[select][1])*zoom+250),(-e[select][2]*zoom+(e[select][0])*zoom+250,-e[select][2]*zoom+(e[select][1])*zoom+250),(-e[select][2]*zoom+(e[select][0])*zoom+250,e[select][2]*zoom+(e[select][1])*zoom+250)],10,"rgba(255,255,0,0.7)")
    canvas.draw_line((600,0),(600,500),200,"black")
    canvas.draw_text("Click pos: "+str(round((x-250)/zoom,7))+", "+str((y-250)/zoom),(505,495),13,"white")
    canvas.draw_text("fps: "+str(fps),(505,475),13,"white")
    canvas.draw_text("G mult: 10^"+str(G_mult),(605,475),13,"white")
    if (select!=-1):
        canvas.draw_text("x: "+str(round(e[select][0],5)),(510,25),20,"white")
        canvas.draw_text("y: "+str(round(e[select][1],5)),(510,50),20,"white")
        canvas.draw_text("Size: "+str(e[select][2]),(510,75),20,"white")
        canvas.draw_text("Mass: "+str(e[select][3]),(510,100),20,"white")
        canvas.draw_text("Speed: "+str(round(e[select][4],5)),(510,125),20,"white")
        canvas.draw_text("Angle: "+str(round(e[select][5]%360,5)),(510,150),20,"white")
        precolor=(hx[e[select][6][0]]*16+hx[e[select][6][1]],hx[e[select][6][2]]*16+hx[e[select][6][3]],hx[e[select][6][4]]*16+hx[e[select][6][5]])
        canvas.draw_line((550,269.5),(550,334.5),21,"white")
        canvas.draw_line((600,269.5),(600,334.5),21,"white")
        canvas.draw_line((650,269.5),(650,334.5),21,"white")
        for i in range(64):
            canvas.draw_line((550,i+270),(550,i+271),20,"rgb("+str(4*i)+","+str(precolor[1])+","+str(precolor[2])+")")
            canvas.draw_line((600,i+270),(600,i+271),20,"rgb("+str(precolor[0])+","+str(4*i)+","+str(precolor[2])+")")
            canvas.draw_line((650,i+270),(650,i+271),20,"rgb("+str(precolor[0])+","+str(precolor[1])+","+str(4*i)+")")
        if (infoSelect!=-1 and infoSelect<10):
            canvas.draw_line((502.5,infoSelect*25-8),(697.5,infoSelect*25-8),20,"rgba(255,255,0,0.7)")
    if (infoSelect>=10):
        canvas.draw_line(((infoSelect-10)*100+551.25,460),((infoSelect-10)*100+551.25,480),95,"rgba(255,255,0,0.7)")
    if run:
        #print (3.1415926535897932384626433)
        for i in range(len(e)):
            ax=0
            ay=0
            for o in range(len(e)):
                if (i!=o):
                    a=G*(10**G_mult)*e[o][3]/((e[i][0]-e[o][0])**2+(e[i][1]-e[o][1])**2)*(1/fps)
                    aa=0
                    if ((e[i][0]-e[o][0])!=0):
                        aa=math.atan2(e[i][1]-e[o][1],e[i][0]-e[o][0])
                    elif ((e[i][1]-e[o][1])!=0):
                        aa=3.141592653589793/2*(abs(e[i][1]-e[o][1])/(e[i][1]-e[o][1]))
                    ax+=a*math.cos(aa)
                    ay+=a*math.sin(aa)
            s=e[i][4]/fps
            ox=s*math.cos(3.141592653589793*e[i][5]/180)-ax/fps
            oy=s*math.sin(3.141592653589793*e[i][5]/180)-ay/fps
            #if (c%fps==0):
            #    print ("ox: "+str(ox)+" ax: "+str(ax/fps))
            #    print ("oy: "+str(oy)+" ay: "+str(ay/fps))
            #    print ("")
            #c+=1
            e[i][0]=round(e[i][0]+ox,14)
            e[i][1]=round(e[i][1]+oy,14)
            e[i][4]=math.sqrt((ox*fps)**2+(oy*fps)**2)
            if (ox!=0):
                #print(oy*fps)
                #print(ox*fps)
                #print("")
                e[i][5]=math.atan2(oy*fps,ox*fps)*180/3.141592653589793
            elif (oy!=0):
                e[i][5]=90*(abs(oy)/oy)
                #print("noooooooooooo")
        if (Wait==True):
            wait=0
            while (time.time()-t<1/fps):
                wait=1
def click(pos):
    global e,select,zoom,x,y,infoSelect,hx
    if (pos[0]<500):
        x=pos[0]
        y=pos[1]
        select=-1
        for i in range(len(e)-1,-1,-1):
            if ((x-e[i][0]*zoom-250)**2+(y-e[i][1]*zoom-250)**2<(e[i][2]*zoom)**2):
                select=i
                break
    else:
        if (pos[1]<150):
            infoSelect=int((pos[1]-8)/25)+1
        elif (pos[0]>=540 and pos[0]<=560 and pos[1]>=270 and pos[1]<334):
            e[select][6]=hx[int((pos[1]-270)/4)]+hx[(pos[1]-270)*4%16]+e[select][6][2]+e[select][6][3]+e[select][6][4]+e[select][6][5]
        elif (pos[0]>=590 and pos[0]<=610 and pos[1]>=270 and pos[1]<334):
            e[select][6]=e[select][6][0]+e[select][6][1]+hx[int((pos[1]-270)/4)]+hx[(pos[1]-270)*4%16]+e[select][6][4]+e[select][6][5]
        elif (pos[0]>=640 and pos[0]<=660 and pos[1]>=270 and pos[1]<334):
            e[select][6]=e[select][6][0]+e[select][6][1]+e[select][6][2]+e[select][6][3]+hx[int((pos[1]-270)/4)]+hx[(pos[1]-270)*4%16]
        elif (pos[0]>=500 and pos[0]<600 and pos[1]>=460 and pos[1]<485):
            infoSelect=10
        elif (pos[0]>=600 and pos[0]<=700 and pos[1]>=460 and pos[1]<485):
            infoSelect=11
def InVal(val):
    global e,select,infoSelect,run,fps,G_mult
    if (run==False):
        f=0
        d=0
        if (select!=-1 and infoSelect!=-1 and infoSelect<10):
            for i in range(len(val)):
                if not(i==0 and val[0]=="-"):
                    if not(val[i]=="0" or val[i]=="1" or val[i]=="2" or val[i]=="3" or val[i]=="4" or val[i]=="5" or val[i]=="6" or val[i]=="7" or val[i]=="8" or val[i]=="9" or val[i]=="."):
                        f=1
                    if (val[i]=="."):
                        d=d+1
            if (f==0 and d==0):
                e[select][infoSelect-1]=int(val)
            if (f==0 and d==1):
                e[select][infoSelect-1]=float(val)
        elif (infoSelect==10):
            for i in range(len(val)):
                if not(i==0 and val[0]=="-"):
                    if not(val[i]=="0" or val[i]=="1" or val[i]=="2" or val[i]=="3" or val[i]=="4" or val[i]=="5" or val[i]=="6" or val[i]=="7" or val[i]=="8" or val[i]=="9" or val[i]=="."):
                        f=1
                    if (val[i]=="."):
                        d=d+1
            if (f==0 and d==0 and int(val)!=0):
                fps=int(val)
            if (f==0 and d==1 and float(val)!=0):
                fps=float(val)
        elif (infoSelect==11):
            for i in range(len(val)):
                if not(i==0 and val[0]=="-"):
                    if not(val[i]=="0" or val[i]=="1" or val[i]=="2" or val[i]=="3" or val[i]=="4" or val[i]=="5" or val[i]=="6" or val[i]=="7" or val[i]=="8" or val[i]=="9" or val[i]=="."):
                        f=1
                    if (val[i]=="."):
                        d=d+1
            if (f==0 and d==0):
                G_mult=int(val)
            if (f==0 and d==1):
                G_mult=float(val)
def add():
    global e,run
    if (run==False):
        e.append([0,0,20,10,0,0,"000000"])
def delete():
    global e,select,run
    if (run==False and select!=-1):
        e.pop(select)
        select=-1
def Zin():
    global zoom,z
    zoom=zoom*1.25
    z+=1
def Zout():
    global zoom,z
    zoom=zoom/1.25
    z-=1
def showInfo():
    global e,info
    info=not(info)
def code(inp):
    global e,run,z,zoom
    if (len(inp)>3):
        if (run==False):
            e=[]
            c=-1
            l=-1
            s=-1
            k=1
            z=inp[0]
            while (inp[k]!="|"):
                z=z+inp[k]
                k+=1
            z=int(z)
            zoom=1.25**z
            for x in range(k+1,len(inp)):
                if (inp[x]=="-"):
                    s=s+1
                    e[c][l]+="-"
                elif (inp[x]=="."):
                    s=s+1
                    e[c][l]+="."
                elif (inp[x]=="'"):
                    s=-1
                    l=l+1
                    e[c].append("")
                elif (inp[x]==","):
                    l=-1
                    c=c+1
                    e.append([])
                else:
                    if (ord(inp[x])>=68):
                        e[c][l]+=hx[ord(inp[x])-69]
                    else:
                        e[c][l]+=str(ord(inp[x])-48)
            for i in range(len(e)):
                for o in range(6):
                    strf=0
                    for j in range(len(e[i][o])):
                        if (e[i][o][j]=="."):
                            strf=1
                    if (strf==0):
                        e[i][o]=int(e[i][o])
                    else:
                        e[i][o]=float(e[i][o])
    else:
        #print(e)
        print (str(z),end="|")
        for i in range(len(e)):
            print (",",end="")
            for o in range(7):
                print ("'",end="")
                tem=str(e[i][o])
                for j in range(len(tem)):
                    
                    if (o<6):
                        if (tem[j]=="."):
                            print (".",end="")
                        elif (tem[j]=="-"):
                            print ("-",end="")
                        else:
                            print (chr(int(tem[j])+48),end="")
                    elif (j<6):
                        print (chr(hx[e[i][6][j]]+69),end="")
        print ("")
        print ("")
def start():
    global run
    run=not(run)
def key_handler(key):
    global e,zoom
    #38 = up   |   40 = down   |   39 = right   |   37 = left   |   32 = space   |   82 = r   |   90 = z   |   67 = c
    #87 = W   |   65 = A   |   83 = S   |   68 = D
    if (key==38 or key==87):#up
        for i in range(len(e)):
            e[i][1]+=10/zoom
    if (key==37 or key==65):#left
        for i in range(len(e)):
            e[i][0]+=10/zoom
    if (key==40 or key==83):#down
        for i in range(len(e)):
            e[i][1]+=-10/zoom
    if (key==39 or key==68):#right
        for i in range(len(e)):
            e[i][0]+=-10/zoom
frame = simplegui.create_frame("Gravity Sim", 700, 500)
frame.set_canvas_background("white")
frame.set_mouseclick_handler(click)
frame.add_input("Input Value", InVal,125)
frame.add_button("Add element", add,125)
frame.add_button("Delete element", delete,125)
frame.add_button("Zoom in", Zin,100)
frame.add_button("Zoom out", Zout,100)
frame.add_button("Show Info", showInfo,125)
frame.add_input("Load/Save", code,125)
frame.add_button("Start/Pause", start,125)
frame.set_keydown_handler(key_handler)
frame.set_draw_handler(draw)
frame.start()
