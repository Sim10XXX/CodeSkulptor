import simplegui
import math
towers=[]
#[name,x,y,angle,cooldown,target]
t_list=("arrow","null","null","null","null","null","null","null","null")
stats={"arrow":(1,2,40,10,5,100,20,200),"null":(0,0,0,0,0,1,20,0),
      1:(10.4,1.5),2:(11.8,2),3:(13.2,2.5),4:(14.6,3),5:(16.0,3.5)}
#(damage,pierce,rate,p_speed,p_size,range,hitbox,base price) or  layer:(size,speed)
hold=["",0,0]
#[name,x,y]
h_a=False
valid=True
select=-1
path=[(100,-10),(100,150),(300,250,200,200,math.atan2(-50,-100),math.atan2(50,100),True),(400,350,300,350,-1*math.pi/2,0,False),(400,-10)]
#(x,y) or (end x, end y, center x, center y, start angle, end angle, clockwise?)
pathlength=0
pathsegment=[0]
for i in range(1,len(path)):
    if len(path[i])<3:
        pathlength+=math.sqrt((path[i][0]-path[i-1][0])**2+(path[i][1]-path[i-1][1])**2)
        pathsegment.append(pathlength)
    else:
        c=0
        if path[i][6]:
            if (path[i][4]-path[i][5]>=0):
                c=2*math.pi
            ca=abs(path[i][4]-path[i][5]-c)
        else:
            if (path[i][5]-path[i][4]>=0):
                c=2*math.pi
            ca=abs(path[i][5]-path[i][4]-c)
        pathlength+=math.sqrt((path[i][1]-path[i][3])**2+(path[i][0]-path[i][2])**2)*math.pi*2*(ca/(2*math.pi))
        pathsegment.append(pathlength)
#print (pathlength)
#print (pathsegment)
wave=0
waveend=True
waves=( #((layers,amount,spacing,initial delay))		#(2,5,20,50),(3,5,20,100),(4,5,20,150),(5,5,20,200)
    ((1,20,20,0),),
    ((1,30,15,0),),
    ((1,10,20,0),(2,10,20,220)),
    ((1,20,20,0),(2,10,10,400),(1,10,15,500)),
    ((2,30,20,0),),
    ((1,15,20,500),(2,20,20,100),(3,4,20,0)),
    ((1,10,20,0),(2,15,20,200),(3,6,20,500)),
    ((2,25,50,0),(1,15,15,100),(3,8,15,500)),
    ((3,25,30,0),(3,10,30,465)),
    ((2,50,30,0),(2,30,30,615),(2,20,10,1500)),#10
)
enemy=[]
#[layer,x,y,distance crossed,[hit values]]
ecount=0
proj=[]
#[type,x,y,angle,speed,size,pierce,life,[hit values]]
hit_value=0
money=650
lives=200
gameover=False
def draw(canvas):
    def sprite(n,x,y,a):
        if n=="arrow":
            canvas.draw_circle((x,y),10,20,"red")
            canvas.draw_line((x,y),(x+13*math.cos(a),y+13*math.sin(a)),4,"black")
        elif n=="":
            canvas.draw_circle((x,y),10,20,"grey")
        elif n=="":
            canvas.draw_circle((x,y),10,20,"grey")
        elif n=="":
            canvas.draw_circle((x,y),10,20,"grey")
        elif n=="":
            canvas.draw_circle((x,y),10,20,"grey")
        elif n=="":
            canvas.draw_circle((x,y),10,20,"grey")
        elif n=="":
            canvas.draw_circle((x,y),10,20,"grey")
        elif n=="":
            canvas.draw_circle((x,y),10,20,"grey")
        elif n=="null":
            canvas.draw_circle((x,y),10,20,"grey")
        elif n=="p:arrow":
            canvas.draw_line((x,y),(x-13*math.cos(a),y-13*math.sin(a)),2,"black")
            canvas.draw_circle((x,y),1.5,3,"rgba(255,0,0,0.5)")
        elif n==1:
            c="red"
        elif n==2:
            c="blue"
        elif n==3:
            c="green"
        elif n==4:
            c="yellow"
        elif n==5:
            c="pink"
        if type(n)==int and n<6:
            m=0.7*n+0.5
            canvas.draw_circle((x,y),4+m,8+2*m,c)
            canvas.draw_line((x-3-m,y+4-0.2*m-3),(x+3+m,y+4+0.8*m+3+m),(6+m+m)*math.sqrt(2),c)
    global towers,hold,path,pathsegment,pathlength,wave,waveend,waves,enemy,proj,hit_value,ecount,money,lives,gameover,select
    for i in range(1,len(path)):
        if len(path[i])<3:
            canvas.draw_line((path[i][0],path[i][1]),(path[i-1][0],path[i-1][1]),50,"brown")
        else:
            ea=path[i][4]
            aa=path[i][5]
            if path[i][6]:
                ea=path[i][5]
                aa=path[i][4]
            r=math.sqrt((path[i][1]-path[i][3])**2+(path[i][0]-path[i][2])**2)
            canvas.draw_arc((path[i][2],path[i][3]),r,aa,ea,50,"brown")
            canvas.draw_circle((path[i][0],path[i][1]),12.5,25,"brown")
            canvas.draw_circle((path[i][2]+r*math.cos(aa),path[i][3]+r*math.sin(aa)),12.5,25,"brown")
    for i in range(len(towers)):
        sprite(towers[i][0],towers[i][1],towers[i][2],towers[i][3])
    
    if not waveend:
        for i in range(len(enemy)-1,-1,-1):
            if enemy[i][3]<0:
                enemy[i][3]+=1
            elif enemy[i][3]<pathlength:
                if (enemy[i][3]==0):
                    ecount+=1
                c=0
                while pathsegment[c]<enemy[i][3]:
                    c+=1
                p=(enemy[i][3]-pathsegment[c-1])/(pathsegment[c]-pathsegment[c-1])
                if len(path[c])<3:
                    enemy[i][1]=(path[c][0]-path[c-1][0])*p+path[c-1][0]
                    enemy[i][2]=(path[c][1]-path[c-1][1])*p+path[c-1][1]
                else:
                    r=math.sqrt((path[c][1]-path[c][3])**2+(path[c][0]-path[c][2])**2)
                    if path[c][6]:
                        a=path[c][5]
                        if (path[c][4]>path[c][5]):
                            a=2*math.pi+a
                        enemy[i][1]=r*math.cos((a-path[c][4])*p+path[c][4])+path[c][2]
                        enemy[i][2]=r*math.sin((a-path[c][4])*p+path[c][4])+path[c][3]
                    else:
                        a=path[c][4]
                        if (path[c][5]>path[c][4]):
                            a=2*math.pi+a
                        enemy[i][1]=r*math.cos((path[c][5]-a)*p+path[c][4])+path[c][2]
                        enemy[i][2]=r*math.sin((path[c][5]-a)*p+path[c][4])+path[c][3]

                enemy[i][3]+=stats[enemy[i][0]][1]
                sprite(enemy[i][0],enemy[i][1],enemy[i][2],0)
                for t in range(len(towers)):
                    if (towers[t][4]<=0):
                        if (enemy[i][1]-towers[t][1])**2+(enemy[i][2]-towers[t][2])**2<(stats[towers[t][0]][5]+stats[enemy[i][0]][0])**2:
                            if type(towers[t][5])==str or enemy[towers[t][5]][3]<enemy[i][3]:
                                towers[t][5]=i
                                towers[t][3]=math.atan2(enemy[i][2]-towers[t][2],enemy[i][1]-towers[t][1])
            else:
                lives-=enemy[i][0]
                ecount-=1
                enemy.pop(i)
    for t in range(len(towers)):
        if (towers[t][4]<=0 and towers[t][5]!=""):
            towers[t][5]=""
            towers[t][4]=stats[towers[t][0]][2]
            proj.append(["p:"+towers[t][0],towers[t][1],towers[t][2],towers[t][3],stats[towers[t][0]][3],stats[towers[t][0]][4],stats[towers[t][0]][1],(stats[towers[t][0]][5]*1.66)/stats[towers[t][0]][3],hit_value])
            hit_value+=1
        else:
            towers[t][4]-=1
    for i in range(len(proj)-1,-1,-1): #[type,x,y,angle,speed,size,pierce,life,hit value]
        if (proj[i][7]>0 and proj[i][6]>0):
            proj[i][7]-=1
            proj[i][1]+=math.cos(proj[i][3])*proj[i][4]
            proj[i][2]+=math.sin(proj[i][3])*proj[i][4]
            sprite(proj[i][0],proj[i][1],proj[i][2],proj[i][3])
            for o in range(ecount-1,-1,-1):
                if proj[i][6]>0:
                    if not(proj[i][8] in enemy[o][4]):
                        if (proj[i][1]-enemy[o][1])**2+(proj[i][2]-enemy[o][2])**2<(proj[i][5]+stats[enemy[o][0]][0])**2:
                            proj[i][6]-=1
                            for p in range(stats[proj[i][0].lstrip("p:")][0]):
                                if (enemy[o][0]>0):
                                    enemy[o][0]-=1
                                    money+=1
                            if (enemy[o][0]<=0):
                                enemy.pop(o)
                                ecount-=1
                            else:
                                enemy[o][4].append(proj[i][8])
                        #else:
                        #    print ("enemy: "+str(enemy[o]))
                        #    print ("proj: "+str(proj[i]))
                        #    print ("")
        else:
            proj.pop(i)
    if not waveend and len(enemy)==0:
        waveend=True
        money+=99+wave
    if h_a:
        if valid:
            canvas.draw_circle((hold[1],hold[2]),stats[hold[0]][5],1,"black","rgba(100,100,100,0.3)")
        else:
            canvas.draw_circle((hold[1],hold[2]),stats[hold[0]][5],1,"black","rgba(255,0,0,0.3)")
        sprite(hold[0],hold[1],hold[2],0)
    if select>-1:
        canvas.draw_circle((towers[select][1],towers[select][2]),stats[towers[select][0]][5],1,"black","rgba(100,100,100,0.3)")
        sprite(towers[select][0],towers[select][1],towers[select][2],towers[select][3])
    ################################################################################################
    canvas.draw_line((600,0),(600,500),200,"black")
    if select==-1:
        for i in range(9):
            canvas.draw_line((510,48*i+34),(690,48*i+34),48,"rgb("+str(255-i*25)+","+str(i*50-3*i*i*i)+","+str(i*4*i)+")")
        canvas.draw_text("$"+str(stats["arrow"][7])+" Arrow",(515,50),30,"white")
    else:
        canvas.draw_line((600,10),(600,442),180,"rgb(220,150,50)")
    canvas.draw_text(str(lives),(5,50),30,"pink")
    canvas.draw_text("$"+str(money),(5,100),30,"black")
    canvas.draw_line((510,473),(600,473),34,"lime")
    if not waveend:
        canvas.draw_line((540,462),(540,484),15,"white")
        canvas.draw_line((570,462),(570,484),15,"white")
    else:
        canvas.draw_polygon([(540,469),(540,477),(550,473)],15,"white")
    #canvas.draw_arc((250,250),50,0,1.57,10,"green")
    #for i in range(len(enemy)):
    #    print (enemy[i][4])
    #print (hit_value)

    
def click(pos):
    global hold,h_a,valid,path,select
    if (pos[0]>510 and pos[0]<690):
        if (pos[1]>10 and pos[1]<442):
            if (select==-1):
                hold[0]=t_list[int((pos[1]-10)/48)]
                if money>=stats[hold[0]][7]:
                    h_a=True
                    valid=False
                    hold[1]=0
                    hold[2]=0
            #else:
                
        else:
            if (pos[0]<600 and pos[1]>456 and pos[1]<490):
                global wave,waves,waveend,enemy
                if waveend:
                    enemy=[]
                    waveend=False
                    for i in range(len(waves[wave])):    # not enough waves lol
                        for o in range(0,waves[wave][i][1]):
                            enemy.append([waves[wave][i][0],path[0][0],path[0][1],-waves[wave][i][2]*o-waves[wave][i][3],[]])
                    wave+=1
                    for i in range(1,len(enemy)):
                        p=i
                        for j in range(i-1,-1,-1):
                            if enemy[i][3]>enemy[j][3]:
                                p=j
                        enemy.insert(p,enemy.pop(i))
            h_a=False
            select=-1
    elif (pos[0]<500 and h_a):
        hold[1]=pos[0]
        hold[2]=pos[1]
        valid=True
        for i in range(len(towers)):
            if ((hold[1]-towers[i][1])**2+(hold[2]-towers[i][2])**2<(stats[towers[i][0]][6]+stats[hold[0]][6])**2):
                valid=False
        for i in range(1,len(path)):
            if len(path[i])<3:
                if (hold[2]<max(path[i][1],path[i-1][1]) and hold[2]>min(path[i][1],path[i-1][1]) and abs(hold[1]-path[i][0])<25+stats[hold[0]][6]) or (hold[1]<max(path[i][0],path[i-1][0]) and hold[1]>min(path[i][0],path[i-1][0]) and abs(hold[2]-path[i][1])<25+stats[hold[0]][6]):
                    valid=False
            else:
                r=math.sqrt((path[i][1]-path[i][3])**2+(path[i][0]-path[i][2])**2)
                agval=-(math.atan2(path[i][2]-hold[1],path[i][3]-hold[2])-0.5*math.pi)%(2*math.pi)-math.pi#pretty much added stuff to this until it lined up by chance with the angles used to draw the arcs
                if path[i][6]:
                    #if agval>path[i][4] and agval<path[i][5]:
                    if (path[i][4]<path[i][5] and agval>path[i][4] and agval<path[i][5]) or (path[i][4]>path[i][5] and (agval>path[i][4] or agval<path[i][5])):
                        if ((hold[1]-path[i][2])**2+(hold[2]-path[i][3])**2)<(r+25+stats[hold[0]][6])**2 and ((hold[1]-path[i][2])**2+(hold[2]-path[i][3])**2)>(r-25-stats[hold[0]][6])**2:
                            valid=False
                else:
                    #if agval<path[i][4] and agval>path[i][5]:
                    if (path[i][4]>path[i][5] and agval<path[i][4] and agval>path[i][5]) or (path[i][4]<path[i][5] and (agval<path[i][4] or agval>path[i][5])):
                        if ((hold[1]-path[i][2])**2+(hold[2]-path[i][3])**2)<(r+25+stats[hold[0]][6])**2 and ((hold[1]-path[i][2])**2+(hold[2]-path[i][3])**2)>(r-25-stats[hold[0]][6])**2:
                            valid=False
            if (hold[1]-path[i][0])**2+(hold[2]-path[i][1])**2<(25+stats[hold[0]][6])**2:
                valid=False
        val=stats[hold[0]][6]
        if (hold[1]+val>500 or hold[1]-val<0 or hold[2]-val<0 or hold[2]+val>500):
            valid=False
    elif (pos[0]<500):
        select=-1
        for i in range(len(towers)):
            if (pos[0]-towers[i][1])**2+(pos[1]-towers[i][2])**2<(stats[t_list[i]][6])**2:
                select=i
    else:
        h_a=False
        select=-1

def drag(pos):
    global hold,h_a,valid
    if (pos[0]<500 and h_a):
        hold[1]=pos[0]
        hold[2]=pos[1]
        valid=True
        for i in range(len(towers)):
            if ((hold[1]-towers[i][1])**2+(hold[2]-towers[i][2])**2<(stats[towers[i][0]][6]+stats[hold[0]][6])**2):
                valid=False
        for i in range(1,len(path)):
            if len(path[i])<3:
                if (hold[2]<max(path[i][1],path[i-1][1]) and hold[2]>min(path[i][1],path[i-1][1]) and abs(hold[1]-path[i][0])<25+stats[hold[0]][6]) or (hold[1]<max(path[i][0],path[i-1][0]) and hold[1]>min(path[i][0],path[i-1][0]) and abs(hold[2]-path[i][1])<25+stats[hold[0]][6]):
                    valid=False
            else:
                r=math.sqrt((path[i][1]-path[i][3])**2+(path[i][0]-path[i][2])**2)
                agval=-(math.atan2(path[i][2]-hold[1],path[i][3]-hold[2])-0.5*math.pi)%(2*math.pi)-math.pi
                if path[i][6]:
                    if (path[i][4]<path[i][5] and agval>path[i][4] and agval<path[i][5]) or (path[i][4]>path[i][5] and (agval>path[i][4] or agval<path[i][5])):
                        if ((hold[1]-path[i][2])**2+(hold[2]-path[i][3])**2)<(r+25+stats[hold[0]][6])**2 and ((hold[1]-path[i][2])**2+(hold[2]-path[i][3])**2)>(r-25-stats[hold[0]][6])**2:
                            valid=False
                else:
                    if (path[i][4]>path[i][5] and agval<path[i][4] and agval>path[i][5]) or (path[i][4]<path[i][5] and (agval<path[i][4] or agval>path[i][5])):
                        if ((hold[1]-path[i][2])**2+(hold[2]-path[i][3])**2)<(r+25+stats[hold[0]][6])**2 and ((hold[1]-path[i][2])**2+(hold[2]-path[i][3])**2)>(r-25-stats[hold[0]][6])**2:
                            valid=False
            if (hold[1]-path[i][0])**2+(hold[2]-path[i][1])**2<(25+stats[hold[0]][6])**2:
                valid=False
        val=stats[hold[0]][6]
        if (hold[1]+val>500 or hold[1]-val<0 or hold[2]-val<0 or hold[2]+val>500):
            valid=False
def place():
    global hold,h_a,valid,towers,money
    if h_a and valid:
        h_a=False
        towers.append([hold[0],hold[1],hold[2],0,0,""])
        money-=stats[hold[0]][7]
frame = simplegui.create_frame("BBTD (Budget Baloon TD)", 700, 500)
frame.add_button("Place", place)
frame.set_draw_handler(draw)
frame.set_mousedrag_handler(drag)
frame.set_mouseclick_handler(click)
frame.set_canvas_background("white")
frame.start()


