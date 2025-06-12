#color for 1<=i<=4 "rgb("+str(100*(i)-i**2)+","+str(255*(i-3))+","+str(255-100*(i-1))+")"

import simplegui
import random
p=int(input("# of players (from 2-4)"))
bankrupt1=0
bankrupt2=0
bankrupt3=0
if (p<=3):
    bankrupt1=4
if (p==2):
    bankrupt2=3
p1_money=1500
p2_money=1500
p3_money=1500
p4_money=1500
p1=0
p2=0
p3=0
p4=0
p1_jail=0
p2_jail=0
p3_jail=0
p4_jail=0
p1_mode=0
p2_mode=0
p3_mode=0
p4_mode=0
roll=1
die1=0
die2=0
doubles=0
force_bail=0
flag=0
timer=0
movement=0
done=0
display=0
display2=0
display3=0
display_timer=0
choice=0
buy=0
auction=0
bid=0
bidder=0
top_bid=0
fold=-1
fold2=-1
cursor=1
build=0
trade=0
trade1=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
trade2=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
trader=0
tradee=0
role=0
lastpaid=0
turn=random.randint(0,0)
sort=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
chance_deck=list()
def dlist():
    global alist,elist
    alist=list([list([list(["Advance to GO","",""]),1,"0"]),
                  list([list(["Bank pays you dividend of $50","",""]),2,50]),
                  list([list(["Go back 3 spaces","",""]),3]),
                  list([list(["Advance to nearest Utility","",""]),4]),
                  list([list(["Go to Jail","",""]),5,"10"]),
                  list([list(["Pay poor tax of $15","",""]),6,-15]),
                  list([list(["Advance to St. Charles place","",""]),7,"11"]),
                  list([list(["You have been elected chairman","of the board. Pay each player $50",""]),8]),
                  list([list(["Advance to the nearest railroad","",""]),9]),
                  list([list(["Advance to the nearest railroad","",""]),10]),
                  list([list(["Advance to Reading Railroad","",""]),11,"5"]),
                  list([list(["Advance to Boardwalk","",""]),12,"39"]),
                  list([list(["Your building and loan matures.","Collect $150",""]),13,150]),
                  list([list(["Advance to Illinois avenue","",""]),14,"24"]),
                  list([list(["GET OUT OF JAIL FREE","",""]),15]),
                  list([list(["Make general repairs on all your property.","$25 for each house","$100 for each hotel"]),16]),
                 ])
    elist=list([list([list(["Advance to GO","",""]),1,"0"]),
                  list([list(["Receive $25 for services","",""]),2,25]),
                  list([list(["Pay hospital $100","",""]),3,-100]),
                  list([list(["Doctor's fee. Pay $50","",""]),4,-50]),
                  list([list(["Go to jail","",""]),5,"10"]),
                  list([list(["From sale of stock you get $45","",""]),6,45]),
                  list([list(["You inherit $100","",""]),7,100]),
                  list([list(["Collect $50 from every player","",""]),8]),
                  list([list(["Pay school tax of $150","",""]),9,-150]),
                  list([list(["Life insurance matures.","Collect $100",""]),10,100]),
                  list([list(["You have won second place","in a beauty contest.","Collect $10"]),11,10]),
                  list([list(["Income tax refund.","Collect $25",""]),12,25]),
                  list([list(["Christmas fund matures.","Collect $100",""]),13,100]),
                  list([list(["Bank error in your favor $200","",""]),14,200]),
                  list([list(["GET OUT OF JAIL FREE","",""]),15]),
                  list([list(["You are assessed for street repairs.","$40 per house","$115 per hotel"]),16]),
                 ])
dlist()
for i in range(16):
    vfn=1
    while (vfn==1):
        vfn=0
        s=random.randint(1,16)
        for o in range(16):
            if (s==sort[o]):
                vfn=1
    sort[i]=s
for i in range(16):
    chance_deck.append(alist[sort[i]-1])

sort=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
chest_deck=list()

for i in range(16):
    vfn=1
    while (vfn==1):
        vfn=0
        s=random.randint(1,16)
        for o in range(16):
            if (s==sort[o]):
                vfn=1
    sort[i]=s
for i in range(16):
    chest_deck.append(elist[sort[i]-1])
ownership=list([list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),
                list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),
                list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),
                list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0,0]),list([0,0]),list([0,0])])
gameboard=list([list(["special",0,0,0]),
                 list(["property",60,list([2,10,30,90,160,250])]),
                 list(["chest"]),
                 list(["property",60,list([4,20,60,180,320,450])]),
                 list(["special",-200,0,0]),
                 list(["railroad",200]),
                 list(["property",100,list([6,30,90,270,400,550])]),
                 list(["chance"]),
                 list(["property",100,list([6,30,90,270,400,550])]),
                 list(["property",120,list([8,40,100,300,450,600])]),
                 list(["special",0,0,0]),
                 list(["property",140,list([10,50,150,450,625,750])]),
                 list(["utility",150]),
                 list(["property",140,list([10,50,150,450,625,750])]),
                 list(["property",160,list([12,60,180,500,700,900])]),
                 list(["railroad",200]),
                 list(["property",180,list([14,70,200,550,700,900])]),
                 list(["chest"]),
                 list(["property",180,list([14,70,200,550,700,900])]),
                 list(["property",200,list([16,80,220,600,800,1000])]),
                 list(["special",0,0,0]),
                 list(["property",220,list([18,90,250,700,875,1050])]),
                 list(["chance"]),
                 list(["property",220,list([18,90,250,700,875,1050])]),
                 list(["property",240,list([20,100,300,750,925,1100])]),
                 list(["railroad",200]),
                 list(["property",260,list([22,110,330,800,975,1150])]),
                 list(["property",260,list([22,110,330,800,975,1150])]),
                 list(["utility",150]),
                 list(["property",280,list([24,120,360,850,1025,1200])]),
                 list(["special",0,20,3]),
                 list(["property",300,list([26,130,390,900,1100,1275])]),
                 list(["property",300,list([26,130,390,900,1100,1275])]),
                 list(["chest"]),
                 list(["property",320,list([28,150,450,1000,1200,1400])]),
                 list(["railroad",200]),
                 list(["chance"]),
                 list(["property",350,list([35,175,500,1100,1300,1500])]),
                 list(["special",-75,0,0]),
                 list(["property",400,list([50,200,600,1400,1700,2000])]),
                ])
group=list([list([0,0,0]),list([1,3,3]),list([0,0,0]),list([3,1,1]),list([0,0,0]),list([0,0,0]),list([6,8,9]),list([0,0,0]),list([8,6,9]),list([9,6,8]),list([0,0,0]),list([11,13,14]),
                list([0,0,0]),list([13,11,14]),list([14,11,13]),list([0,0,0]),list([16,18,19]),list([0,0,0]),list([18,16,19]),list([19,16,18]),list([0,0,0]),list([21,23,24]),list([0,0,0]),list([23,21,24]),
                list([24,21,23]),list([0,0,0]),list([26,27,29]),list([27,26,29]),list([0,0,0]),list([29,26,27]),list([0,0,0]),list([31,32,34]),list([32,31,34]),list([0,0,0]),list([34,31,32]),list([0,0,0]),
                list([0,0,0]),list([37,39,39]),list([0,0,0]),list([39,37,37])])
def p(x):
    global p1,p2,p3,p4
    if (x==1):
        return p1%40
    elif (x==2):
        return p2%40
    elif (x==3):
        return p3%40
    else:
        return p4%40
def chance():
    global turn,chance_deck,p1,p2,p3,p4,p1_money,p2_money,p3_money,p4_money,display,display2,display3,display_timer,p1_jail,p2_jail,p3_jail,p4_jail
    if (turn%4==0):
        if (chance_deck[0][1]==2 or chance_deck[0][1]==6 or chance_deck[0][1]==13):
            p1_money=p1_money+chance_deck[0][2]
        elif (chance_deck[0][1]==1 or chance_deck[0][1]==5 or chance_deck[0][1]==7 or chance_deck[0][1]==12 or chance_deck[0][1]==14):
            if (chance_deck[0][1]!=5):
                p1=int(chance_deck[0][2])
            else:
                p1=10
                p1_jail=3
        elif (chance_deck[0][1]==3):
            p1=p1-3
            if (p1%40==4):
                p1_money=p1_money-200
            elif (p1%40==33):
                chest()
        elif (chance_deck[0][1]==4):
            while (p1%40!=12 and p1%40!=28):
                p1=p1+1
                if (p1%40==0):
                    p1_money=p1_money+200
        elif (chance_deck[0][1]==8):
            p1_money=p1_money-150
            p2_money=p2_money+50
            p3_money=p3_money+50
            p4_money=p4_money+50
        elif (chance_deck[0][1]==9 or chance_deck[0][1]==10):
            while (p1%40!=5 and p1%40!=15 and p1%40!=25 and p1%40!=35):
                p1=p1+1
                if (p1%40==0):
                    p1_money=p1_money+200
        #elif (chance_deck[0][1]==16):
            
    elif (turn%4==1):
        if (chance_deck[0][1]==2 or chance_deck[0][1]==6 or chance_deck[0][1]==13):
            p2_money=p2_money+chance_deck[0][2]
        elif (chance_deck[0][1]==1 or chance_deck[0][1]==5 or chance_deck[0][1]==7 or chance_deck[0][1]==12 or chance_deck[0][1]==14):
            if (chance_deck[0][1]!=5):
                p2=int(chance_deck[0][2])
            else:
                p2=10
                p2_jail=3
        elif (chance_deck[0][1]==3):
            p2=p2-3
            if (p2%40==4):
                p2_money=p2_money-200
            elif (p2%40==33):
                chest()
            #elif (p2%40==19):
        elif (chance_deck[0][1]==4):
            while (p2%40!=12 and p2%40!=28):
                p2=p2+1
                if (p2%40==0):
                    p2_money=p2_money+200
        elif (chance_deck[0][1]==8):
            p2_money=p2_money-150
            p1_money=p1_money+50
            p3_money=p3_money+50
            p4_money=p4_money+50
        elif (chance_deck[0][1]==9 or chance_deck[0][1]==10):
            while (p2%40!=5 and p2%40!=15 and p2%40!=25 and p2%40!=35):
                p2=p2+1
                if (p2%40==0):
                    p2_money=p2_money+200
            
        #elif (chance_deck[0][1]==16):
    elif (turn%4==2):
        if (chance_deck[0][1]==2 or chance_deck[0][1]==6 or chance_deck[0][1]==13):
            p3_money=p3_money+chance_deck[0][2]
        elif (chance_deck[0][1]==1 or chance_deck[0][1]==5 or chance_deck[0][1]==7 or chance_deck[0][1]==12 or chance_deck[0][1]==14):
            if (chance_deck[0][1]!=5):
                p3=int(chance_deck[0][2])
            else:
                p3=10
                p3_jail=3
        elif (chance_deck[0][1]==3):
            p3=p3-3
            if (p3%40==4):
                p3_money=p3_money-200
            elif (p3%40==33):
                chest()
            #elif (p3%40==19):
        elif (chance_deck[0][1]==4):
            while (p3%40!=12 and p3%40!=28):
                p3=p3+1
                if (p3%40==0):
                    p3_money=p3_money+200
        elif (chance_deck[0][1]==8):
            p3_money=p3_money-150
            p2_money=p2_money+50
            p1_money=p1_money+50
            p4_money=p4_money+50
        elif (chance_deck[0][1]==9 or chance_deck[0][1]==10):
            while (p3%40!=5 and p3%40!=15 and p3%40!=25 and p3%40!=35):
                p3=p3+1
                if (p3%40==0):
                    p3_money=p3_money+200
            
        #elif (chance_deck[0][1]==16):
    elif (turn%4==3):
        if (chance_deck[0][1]==2 or chance_deck[0][1]==6 or chance_deck[0][1]==13):
            p4_money=p4_money+chance_deck[0][2]
        elif (chance_deck[0][1]==1 or chance_deck[0][1]==5 or chance_deck[0][1]==7 or chance_deck[0][1]==12 or chance_deck[0][1]==14):
            if (chance_deck[0][1]!=5):
                p4=int(chance_deck[0][2])
            else:
                p4=10
                p4_jail=3
        elif (chance_deck[0][1]==3):
            p4=p4-3
            if (p4%40==4):
                p4_money=p4_money-200
            elif (p4%40==33):
                chest()
            #elif (p4%40==19):
        elif (chance_deck[0][1]==4):
            while (p4%40!=12 and p4%40!=28):
                p4=p4+1
                if (p4%40==0):
                    p4_money=p4_money+200
        elif (chance_deck[0][1]==8):
            p4_money=p4_money-150
            p2_money=p2_money+50
            p3_money=p3_money+50
            p1_money=p1_money+50
        elif (chance_deck[0][1]==9 or chance_deck[0][1]==10):
            while (p4%40!=5 and p4%40!=15 and p4%40!=25 and p4%40!=35):
                p4=p4+1
                if (p4%40==0):
                    p4_money=p4_money+200
            
        #elif (chance_deck[0][1]==16):
    display=chance_deck[0][0][0]
    display2=chance_deck[0][0][1]
    display3=chance_deck[0][0][2]
    display_timer=200
    if (chance_deck[0][1]==5):
        doubles=0
        done=1
        roll=0
    if (chance_deck[0][1]==15):
        ownership[40][0]=turn%4+1
        chance_deck.pop(0)
    else:
        chance_deck.append(chance_deck.pop(0))

    
    
    
def chest():
    global turn,chest_deck,p1,p2,p3,p4,p1_money,p2_money,p3_money,p4_money,display,display2,display3,display_timer,p1_jail,p2_jail,p3_jail,p4_jail
    if (turn%4==0):
        if (chest_deck[0][1]==2 or chest_deck[0][1]==3 or chest_deck[0][1]==4 or chest_deck[0][1]==6 or chest_deck[0][1]==7 or (chest_deck[0][1]>=9 and chest_deck[0][1]<=14)):
            p1_money=p1_money+chest_deck[0][2]
        elif (chest_deck[0][1]==1 or chest_deck[0][1]==5):
            p1=int(chest_deck[0][2])
            if (chest_deck[0][1]==5):
                p1_jail=3
            else:
                p1_money=p1_money+200
        elif (chest_deck[0][1]==8):
            p1_money=p1_money+150
            p2_money=p2_money-50
            p3_money=p3_money-50
            p4_money=p4_money-50
            
        #elif (chest_deck[0][1]==16):
        
    elif (turn%4==1):
        if (chest_deck[0][1]==2 or chest_deck[0][1]==3 or chest_deck[0][1]==4 or chest_deck[0][1]==6 or chest_deck[0][1]==7 or (chest_deck[0][1]>=9 and chest_deck[0][1]<=14)):
            p2_money=p2_money+chest_deck[0][2]
        elif (chest_deck[0][1]==1 or chest_deck[0][1]==5):
            p2=int(chest_deck[0][2])
            if (chest_deck[0][1]==5):
                p2_jail=3
            else:
                p2_money=p2_money+200
        elif (chest_deck[0][1]==8):
            p2_money=p2_money+150
            p1_money=p1_money-50
            p3_money=p3_money-50
            p4_money=p4_money-50
            
        #elif (chest_deck[0][1]==16):

    elif (turn%4==2):
        if (chest_deck[0][1]==2 or chest_deck[0][1]==3 or chest_deck[0][1]==4 or chest_deck[0][1]==6 or chest_deck[0][1]==7 or (chest_deck[0][1]>=9 and chest_deck[0][1]<=14)):
            p3_money=p3_money+chest_deck[0][2]
        elif (chest_deck[0][1]==1 or chest_deck[0][1]==5):
            p3=int(chest_deck[0][2])
            if (chest_deck[0][1]==5):
                p3_jail=3
            else:
                p3_money=p3_money+200
        elif (chest_deck[0][1]==8):
            p3_money=p3_money+150
            p2_money=p2_money-50
            p1_money=p1_money-50
            p4_money=p4_money-50
            
        #elif (chest_deck[0][1]==16):
    elif (turn%4==3):
        if (chest_deck[0][1]==2 or chest_deck[0][1]==3 or chest_deck[0][1]==4 or chest_deck[0][1]==6 or chest_deck[0][1]==7 or (chest_deck[0][1]>=9 and chest_deck[0][1]<=14)):
            p4_money=p4_money+chest_deck[0][2]
        elif (chest_deck[0][1]==1 or chest_deck[0][1]==5):
            p4=int(chest_deck[0][2])
            if (chest_deck[0][1]==5):
                p4_jail=3
            else:
                p4_money=p4_money+200
        elif (chest_deck[0][1]==8):
            p4_money=p4_money+150
            p2_money=p2_money-50
            p3_money=p3_money-50
            p1_money=p1_money-50
            
        #elif (chest_deck[0][1]==16):
    display=chest_deck[0][0][0]
    display2=chest_deck[0][0][1]
    display3=chest_deck[0][0][2]
    display_timer=200
    if (chest_deck[0][1]==5):
        doubles=0
        roll=0
        done=1
    if (chest_deck[0][1]==15):
        ownership[41][0]=turn%4+1
        chest_deck.pop(0)
    else:
        chest_deck.append(chest_deck.pop(0))

    
    
def monopoly():
    global ownership,group
    for i in range(40):
        if (group[i][0]!=0):
            if (ownership[i][0]==ownership[group[i][1]][0] and ownership[group[i][1]][0]==ownership[group[i][2]][0]):
                ownership[i][2]=1
                ownership[group[i][1]][2]=1
                ownership[group[i][2]][2]=1
            else:
                ownership[i][2]=0
                ownership[group[i][1]][2]=0
                ownership[group[i][2]][2]=0
                
    if (ownership[5][1]!=-1):
        ownership[5][1]=0
    if (ownership[15][1]!=-1):
        ownership[15][1]=0
    if (ownership[25][1]!=-1):
        ownership[25][1]=0
    if (ownership[35][1]!=-1):
        ownership[35][1]=0
    for i in range(4):
        if (ownership[5+10*i][1]!=-1):
            for o in range(3):
                if (ownership[5+10*i][0]==ownership[(15+10*i+10*o)%40][0]):
                    ownership[5+10*i][1]=ownership[5+10*i][1]+1

    
def draw(canvas):
    global timer,done,display,display_timer,display2,display3,roll,ownership,gameboard,doubles,force_bail,flag,cursor,build,p1,p2,p3,p4,p1_money,p2_money,p3_money,p4_money,p1_jail,p2_jail,p3_jail,p4_jail,movement,buy,choice,auction,bid,bidder,top_bid,fold,fold2,trade,trade1,trade2,trader,tradee,role,die1,bankrupt1,bankrupt2,bankrupt3,lastpaid,die2
    canvas.draw_line((900,0),(900,700),400,"rgb(70,70,250)")
    canvas.draw_line((122.5,112.5),(173,112.5),15,"red")
    canvas.draw_line((223,112.5),(273,112.5),15,"red")
    canvas.draw_line((272.5,112.5),(322,112.5),15,"red")
    canvas.draw_line((373,112.5),(423,112.5),15,"yellow")
    canvas.draw_line((425,112.5),(476,112.5),15,"yellow")
    canvas.draw_line((527,112.5),(578,112.5),15,"yellow")
    canvas.draw_line((112.5,122.5),(112.5,173),15,"orange")
    canvas.draw_line((112.5,175),(112.5,223),15,"orange")
    canvas.draw_line((112.5,272.5),(112.5,322),15,"orange")
    canvas.draw_line((112.5,373),(112.5,423),15,"violet")
    canvas.draw_line((112.5,425),(112.5,476),15,"violet")
    canvas.draw_line((112.5,527),(112.5,578),15,"violet")
    canvas.draw_line((587.5,122.5),(587.5,173),15,"green")
    canvas.draw_line((587.5,175),(587.5,223),15,"green")
    canvas.draw_line((587.5,272.5),(587.5,322),15,"green")
    canvas.draw_line((587.5,425),(587.5,476),15,"blue")
    canvas.draw_line((587.5,527),(587.5,578),15,"blue")
    canvas.draw_line((122.5,587.5),(173,587.5),15,"cyan")
    canvas.draw_line((173,587.5),(223,587.5),15,"cyan")
    canvas.draw_line((272.5,587.5),(322,587.5),15,"cyan")
    canvas.draw_line((425,587.5),(476,587.5),15,"brown")
    canvas.draw_line((527,587.5),(578,587.5),15,"brown")
    canvas.draw_line((5,248),(120,248),50,"lightblue")
    canvas.draw_line((250,580),(250,695),50,"lightgray")
    canvas.draw_line((500,580),(500,695),50,"lightblue")
    canvas.draw_line((200,5),(200,120),50,"lightgray")
    canvas.draw_line((580,248),(695,248),50,"lightblue")
    canvas.draw_line((580,400),(695,400),50,"lightgray")
    canvas.draw_line((80,580),(80,660),80,"rgb(255,70,70)")
    canvas.draw_polygon([(0,0),(0,700),(700,700),(700,0)],10,"black")
    canvas.draw_polygon([(125,125),(125,575),(575,575),(575,125)],10,"black")
    for i in range(4):
        if (i+1!=bankrupt1 and i+1!=bankrupt2 and i+1!=bankrupt3):
            if (p(i+1)%40>=0 and 9>=p(i+1)%40):
                canvas.draw_circle((602.5-50.444*(p(i+1)%40),610+22*i),5,10,"rgb("+str(100*(i+1)-(i+1)**2)+","+str(200*(i-2))+","+str(255-100*(i))+")")
            elif (p(i+1)%40==10):
                if ((p1_jail!=0 and i==0) or (p2_jail!=0 and i==1)):
                    canvas.draw_circle((65,610+22*i),5,10,"rgb("+str(100*(i+1)-(i+1)**2)+","+str(200*(i-2))+","+str(255-100*(i))+")")
                elif ((p3_jail!=0 and i==2) or (p4_jail!=0 and i==3)):
                    canvas.draw_circle((87,610+22*(i-2)),5,10,"rgb("+str(100*(i+1)-(i+1)**2)+","+str(200*(i-2))+","+str(255-100*(i))+")")
                else:
                    canvas.draw_circle((22.5,610+22*i),5,10,"rgb("+str(100*(i+1)-(i+1)**2)+","+str(200*(i-2))+","+str(255-100*(i))+")")
            elif (p(i+1)%40>=11 and 20>=p(i+1)%40):
                canvas.draw_circle((90-22*i,602.5-50.444*((p(i+1)-10)%40)),5,10,"rgb("+str(100*(i+1)-(i+1)**2)+","+str(200*(i-2))+","+str(255-100*(i))+")")
            elif (p(i+1)%40>=21 and 30>=p(i+1)%40):
                canvas.draw_circle((97.5+50.444*((p(i+1)-20)%40),90-22*i),5,10,"rgb("+str(100*(i+1)-(i+1)**2)+","+str(200*(i-2))+","+str(255-100*(i))+")")
            else:
                canvas.draw_circle((610+22*i,97.5+50.444*((p(i+1)-30)%40)),5,10,"rgb("+str(100*(i+1)-(i+1)**2)+","+str(200*(i-2))+","+str(255-100*(i))+")")


        
        
        
    if (1!=bankrupt1 and 1!=bankrupt2 and 1!=bankrupt3):
        canvas.draw_text("$"+str(int(p1_money)),(850,60),50,"black")
        canvas.draw_circle((800,50),15,2,"black","rgb(99,0,255)")
    if (2!=bankrupt1 and 2!=bankrupt2 and 2!=bankrupt3):
        canvas.draw_text("$"+str(int(p2_money)),(850,110),50,"black")
        canvas.draw_circle((800,100),15,2,"black","rgb(196,0,155)")
    if (3!=bankrupt1 and 3!=bankrupt2 and 3!=bankrupt3):
        canvas.draw_text("$"+str(int(p3_money)),(850,160),50,"black")
        canvas.draw_circle((800,150),15,2,"black","rgb(255,0,55)")
    if (4!=bankrupt1 and 4!=bankrupt2 and 4!=bankrupt3):
        canvas.draw_text("$"+str(int(p4_money)),(850,210),50,"black")
        canvas.draw_circle((800,200),15,2,"black","rgb(255,200,0)")
    if (trade==2):
        if (turn%4!=0):
            canvas.draw_line((725,500),(775,500),50,"rgb(99,0,255)")
            canvas.draw_text("p1",(735,515),35,"black")
        if (turn%4!=1):
            canvas.draw_line((800,500),(850,500),50,"rgb(196,0,155)")
            canvas.draw_text("p2",(810,515),35,"black")
        if (turn%4!=2):
            canvas.draw_line((875,500),(925,500),50,"rgb(255,0,55)")
            canvas.draw_text("p3",(885,515),35,"black")
        if (turn%4!=3):
            canvas.draw_line((950,500),(1000,500),50,"rgb(255,200,0)")
            canvas.draw_text("p4",(960,515),35,"black")
    elif (trade==1 and role!=2):
        if (role==0):
            canvas.draw_line((870,300),(970,300),70,"rgb("+str(100*(trader)-(trader)**2)+","+str(200*(trader-3))+","+str(255-100*(trader-1))+")")
        else:
            canvas.draw_line((870,300),(970,300),70,"rgb("+str(100*(tradee)-(tradee)**2)+","+str(200*(tradee-3))+","+str(255-100*(tradee-1))+")")
        canvas.draw_text("Swap",(880,315),45,"black")
        canvas.draw_line((990,300),(1090,300),70,"lime")
        canvas.draw_text("Offer",(1000,315),40,"white")
        display_timer=-1
        display="Red=what you give. Blue=what you get"
        display2="p"+str(trader)+" offers $"+str(trade1[42])
        display3="p"+str(tradee)+" offers $"+str(trade2[42])
    elif (role==2 and trade==1):
        canvas.draw_line((750,300),(850,300),70,"lime")
        canvas.draw_text("Decline",(765,320),35,"white")
        canvas.draw_line((870,300),(970,300),70,"lime")
        canvas.draw_text("Accept",(880,315),35,"white")
        canvas.draw_line((990,300),(1090,300),70,"lime")
        canvas.draw_text("Counter",(1000,315),35,"white")
        display_timer=-1
        display="Red=what you get. Blue=what you give"
        display2="p"+str(trader)+" offers $"+str(trade1[42])
        display3="p"+str(tradee)+" offers $"+str(trade2[42])
    if (build==1 or (trade==1 and role!=2)):
        canvas.draw_line((760,450),(850,450),100,"green")
        canvas.draw_line((950,450),(1040,450),100,"green")
        canvas.draw_polygon([(785,450),(815,480),(815,420)],10,"white")
        canvas.draw_polygon([(985,420),(985,480),(1015,450)],10,"white")
        canvas.draw_line((715,625),(790,625),75,"red")
        canvas.draw_line((740,625),(765,625),10,"white")
        canvas.draw_line((1010,625),(1085,625),75,"lime")
        canvas.draw_line((1035,625),(1060,625),10,"white")
        canvas.draw_line((1047.5,612.5),(1047.5,637.5),10,"white")
        canvas.draw_line((750,300),(850,300),70,"lime")
        canvas.draw_text("End",(765,320),50,"white")
        if (cursor%40>=1 and 9>=cursor%40):
            canvas.draw_line((602.5-50.444*(cursor%40),580),(602.5-50.444*(cursor%40),695),45.5,"rgb(200,200,0,0.5)")
        elif (cursor%40>=11 and 19>=cursor%40):
            canvas.draw_line((5,602.5-50.444*((cursor-10)%40)),(120,602.5-50.444*((cursor-10)%40)),45.5,"rgb(200,200,0,0.5)")
        elif (cursor%40>=21 and 29>=cursor%40):
            canvas.draw_line((97.5+50.444*((cursor-20)%40),5),(97.5+50.444*((cursor-20)%40),120),45.5,"rgb(200,200,0,0.5)")
        else:
            canvas.draw_line((580,97.5+50.444*((cursor-30)%40)),(695,97.5+50.444*((cursor-30)%40)),45.5,"rgb(200,200,0,0.5)")
    if (done==1 and doubles==0 and force_bail==0):
        monopoly()
        canvas.draw_line((750,400),(900,400),70,"lime")
        canvas.draw_text("Build",(755,425),60,"white")
        canvas.draw_line((750,500),(900,500),70,"lime")
        canvas.draw_text("Trade",(755,525),60,"white")
        canvas.draw_line((750,600),(1000,600),70,"red")
        if ((turn%4==0 and p1_money>=0) or (turn%4==1 and p2_money>=0) or (turn%4==2 and p3_money>=0) or (turn%4==3 and p4_money>=0)):
            canvas.draw_text("End Turn",(755,625),60,"white")
        else:
            canvas.draw_text("Bankrupt",(755,625),60,"white")
    elif (done==1 and doubles!=0 and force_bail==0):
        done=0
        roll=1
        doubles=int(doubles)
    elif (done==1 and force_bail==1):
        canvas.draw_line((800,600),(1000,600),100,"lime")
        #if (jailfreecard!=1):
        canvas.draw_text("Pay $50",(815,625),60,"white")
    for i in range(1,40):
        if (i<=10):
            canvas.draw_line((123+50.4444*(i-1),0),(123+50.4444*(i-1),700),5,"black")
            canvas.draw_line((0,123+50.4444*(i-1)),(700,123+50.4444*(i-1)),5,"black")
            if (trade1[i]==1):
                canvas.draw_line((602.5-50.444*(i),580),(602.5-50.444*(i),695),45.5,"rgb(200,0,0,0.5)")
            if (trade2[i]==1):
                canvas.draw_line((602.5-50.444*(i),580),(602.5-50.444*(i),695),45.5,"rgb(0,0,200,0.5)")
            if (ownership[i][0]!=0):
                canvas.draw_line((602.5-50.444*(i)-19.5,695),(602.5-50.444*(i)-19.5,595),7,"rgb("+str(100*(ownership[i][0])-ownership[i][0]**2)+","+str(200*(ownership[i][0]-3))+","+str(255-100*(ownership[i][0]-1))+")")
                canvas.draw_line((602.5-50.444*(i)+19,695),(602.5-50.444*(i)+19,595),7,"rgb("+str(100*(ownership[i][0])-ownership[i][0]**2)+","+str(200*(ownership[i][0]-3))+","+str(255-100*(ownership[i][0]-1))+")")
            if (gameboard[i][0]=="property"):
                if (ownership[i][1]==5):
                    canvas.draw_polygon([(562-50.444*(i-1),592),(542-50.444*(i-1),592),(542-50.444*(i-1),582),(562-50.444*(i-1),582)],1,"black","silver")
                else:
                    for o in range(ownership[i][1]):
                        canvas.draw_polygon([(539-50.444*(i-1)+12*o,592),(529-50.444*(i-1)+12*o,592),(529-50.444*(i-1)+12*o,582),(539-50.444*(i-1)+12*o,582)],1,"black","lime")
        elif (i<=20):
            if (ownership[i][0]!=0):
                canvas.draw_line((5,602.5-50.444*(i-10)-19.5),(105,602.5-50.444*(i-10)-19.5),7,"rgb("+str(100*(ownership[i][0])-ownership[i][0]**2)+","+str(200*(ownership[i][0]-3))+","+str(255-100*(ownership[i][0]-1))+")")
                canvas.draw_line((5,602.5-50.444*(i-10)+19.5),(105,602.5-50.444*(i-10)+19.5),7,"rgb("+str(100*(ownership[i][0])-ownership[i][0]**2)+","+str(200*(ownership[i][0]-3))+","+str(255-100*(ownership[i][0]-1))+")")
            if (trade1[i]==1):
                canvas.draw_line((5,602.5-50.444*(i-10)),(120,602.5-50.444*(i-10)),45.5,"rgb(200,0,0,0.5)")
            if (trade2[i]==1):
                canvas.draw_line((5,602.5-50.444*(i-10)),(120,602.5-50.444*(i-10)),45.5,"rgb(0,0,200,0.5)")
            if (gameboard[i][0]=="property"):
                if (ownership[i][1]==5):
                    canvas.draw_polygon([(108,562-50.444*(i-11)),(108,542-50.444*(i-11)),(118,542-50.444*(i-11)),(118,562-50.444*(i-11))],1,"black","silver")
                else:
                    for o in range(ownership[i][1]):
                        canvas.draw_polygon([(108,539-50.444*(i-11)+12*o),(108,529-50.444*(i-11)+12*o),(118,529-50.444*(i-11)+12*o),(118,539-50.444*(i-11)+12*o)],1,"black","lime")
        elif (i<=30):
            if (ownership[i][0]!=0):
                canvas.draw_line((97.5+50.444*(i-20)-19.5,5),(97.5+50.444*(i-20)-19.5,105),7,"rgb("+str(100*(ownership[i][0])-ownership[i][0]**2)+","+str(200*(ownership[i][0]-3))+","+str(255-100*(ownership[i][0]-1))+")")
                canvas.draw_line((97.5+50.444*(i-20)+19.5,5),(97.5+50.444*(i-20)+19.5,105),7,"rgb("+str(100*(ownership[i][0])-ownership[i][0]**2)+","+str(200*(ownership[i][0]-3))+","+str(255-100*(ownership[i][0]-1))+")")
            if (trade1[i]==1):
                canvas.draw_line((97.5+50.444*(i-20),5),(97.5+50.444*(i-20),120),45.5,"rgb(200,0,0,0.5)")
            if (trade2[i]==1):
                canvas.draw_line((97.5+50.444*(i-20),5),(97.5+50.444*(i-20),120),45.5,"rgb(0,0,200,0.5)")
            if (gameboard[i][0]=="property"):
                if (ownership[i][1]==5):
                    canvas.draw_polygon([(138+50.444*(i-21),108),(158+50.444*(i-21),108),(158+50.444*(i-21),118),(138+50.444*(i-21),118)],1,"black","silver")
                else:
                    for o in range(ownership[i][1]):
                        canvas.draw_polygon([(161+50.444*(i-21)-12*o,108),(171+50.444*(i-21)-12*o,108),(171+50.444*(i-21)-12*o,118),(161+50.444*(i-21)-12*o,118)],1,"black","lime")
        else:
            if (ownership[i][0]!=0):
                canvas.draw_line((695,97.5+50.444*(i-30)-19.5),(595,97.5+50.444*(i-30)-19.5),7,"rgb("+str(100*(ownership[i][0])-ownership[i][0]**2)+","+str(200*(ownership[i][0]-3))+","+str(255-100*(ownership[i][0]-1))+")")
                canvas.draw_line((695,97.5+50.444*(i-30)+19.5),(595,97.5+50.444*(i-30)+19.5),7,"rgb("+str(100*(ownership[i][0])-ownership[i][0]**2)+","+str(200*(ownership[i][0]-3))+","+str(255-100*(ownership[i][0]-1))+")")
            if (trade1[i]==1):
                canvas.draw_line((580,97.5+50.444*(i-30)),(695,97.5+50.444*(i-30)),45.5,"rgb(200,0,0,0.5)")
            if (trade2[i]==1):
                canvas.draw_line((580,97.5+50.444*(i-30)),(695,97.5+50.444*(i-30)),45.5,"rgb(0,0,200,0.5)")
            if (gameboard[i][0]=="property"):
                if (ownership[i][1]==5):
                    canvas.draw_polygon([(592,138+50.444*(i-31)),(592,158+50.444*(i-31)),(582,158+50.444*(i-31)),(582,138+50.444*(i-31))],1,"black","silver")
                else:
                    for o in range(ownership[i][1]):
                        canvas.draw_polygon([(592,161+50.444*(i-31)-12*o),(592,171+50.444*(i-31)-12*o),(582,171+50.444*(i-31)-12*o),(582,161+50.444*(i-31)-12*o)],1,"black","lime")
    canvas.draw_line((350,130),(350,570),440,"white")
    
    if (auction==1 or (trade==1 and role!=2)):
        canvas.draw_line((800,550),(850,550),50,"lime")
        canvas.draw_line((875,550),(925,550),50,"lime")
        canvas.draw_line((950,550),(1000,550),50,"lime")
        canvas.draw_line((800,650),(850,650),50,"red")
        canvas.draw_line((875,650),(925,650),50,"red")
        canvas.draw_line((950,650),(1000,650),50,"red")
        canvas.draw_text("1",(800,610),30,"white")
        canvas.draw_text("10",(875,610),30,"white")
        canvas.draw_text("100",(950,610),30,"white")
        if (auction==1):
            canvas.draw_line((800,450),(900,450),100,"lime")
            canvas.draw_line((950,450),(1050,450),100,"lime")
            canvas.draw_text("Bid",(810,462.5),50,"white")
            canvas.draw_text("Fold",(957.5,462.5),50,"white")
            display_timer=-1
            display="$"+str(top_bid)
            display2="Player "+str(bidder%4+1)+"'s bid:"
            display3="$"+str(bid)
    if (display_timer!=0):
        display_timer=display_timer-1
        canvas.draw_text(display,(175,250),24,"black")
        if (display2!=0):
            canvas.draw_text(display2,(175,300),24,"black")
        if (display3!=0):
            canvas.draw_text(display3,(175,350),24,"black")
    canvas.draw_line((725,50+50*(turn%4)),(765,50+50*(turn%4)),10,"white")
    canvas.draw_line((750,37.5+50*(turn%4)),(765,52.5+50*(turn%4)),10,"white")
    canvas.draw_line((750,62.5+50*(turn%4)),(765,47.5+50*(turn%4)),10,"white")
    
    #
    if (roll==1):
        canvas.draw_line((800,600),(1000,600),100,"lime")
        canvas.draw_text("Roll", (815,625),90,"white")
        if (turn%4==0 and p1_jail!=0):
            canvas.draw_line((800,450),(1000,450),100,"lime")
            #if (jailfree card!=1)
            canvas.draw_text("Pay $50",(815,455),40,"white")
            canvas.draw_text("and roll",(815,485),40,"white")
        elif (turn%4==1 and p2_jail!=0):
            canvas.draw_line((800,450),(1000,450),100,"lime")
            #if (jailfree card!=1)
            canvas.draw_text("Pay $50",(815,455),40,"white")
            canvas.draw_text("and roll",(815,485),40,"white")
        elif (turn%4==2 and p3_jail!=0):
            canvas.draw_line((800,450),(1000,450),100,"lime")
            #if (jailfree card!=1)
            canvas.draw_text("Pay $50",(815,455),40,"white")
            canvas.draw_text("and roll",(815,485),40,"white")
        elif (turn%4==3 and p4_jail!=0):
            canvas.draw_line((800,450),(1000,450),100,"lime")
            #if (jailfree card!=1)
            canvas.draw_text("Pay $50",(815,455),40,"white")
            canvas.draw_text("and roll",(815,485),40,"white")
            
    elif (roll==2):
        timer=timer+1
        die1=random.randint(1,6)
        die2=random.randint(1,6)
        if (timer==20):
            roll=0
            timer=0
            movement=die1+die2
    canvas.draw_line((300,400),(300,475),75,"red")
    canvas.draw_line((400,400),(400,475),75,"red")
        
    if (die1!=1):
        canvas.draw_circle((275,460),2.5,5,"white")
    if (die1>=4):
        canvas.draw_circle((325,460),2.5,5,"white")
    if (die1!=1):
        canvas.draw_circle((325,415),2.5,5,"white")
    if (die1>=4):
        canvas.draw_circle((275,415),2.5,5,"white")
    if (die1%2==1):
        canvas.draw_circle((300,437.5),2.5,5,"white")
    if (die1==6):
        canvas.draw_circle((325,437.5),2.5,5,"white")
        canvas.draw_circle((275,437.5),2.5,5,"white")

    if (die2!=1):
        canvas.draw_circle((375,460),2.5,5,"white")
    if (die2>=4):
        canvas.draw_circle((425,460),2.5,5,"white")
    if (die2!=1):
        canvas.draw_circle((425,415),2.5,5,"white")
    if (die2>=4):
        canvas.draw_circle((375,415),2.5,5,"white")
    if (die2%2==1):
        canvas.draw_circle((400,437.5),2.5,5,"white")
    if (die2==6):
        canvas.draw_circle((425,437.5),2.5,5,"white")
        canvas.draw_circle((375,437.5),2.5,5,"white")
    if (die1==die2 and int(doubles)==doubles and roll==0):
        doubles=doubles+1.1
    elif (die1!=die2 and roll==0):
        doubles=0
    if (flag==0 and roll==0 and doubles!=0 and ((p1_jail!=0 and turn%4==0) or (p2_jail!=0 and turn%4==1) or (p3_jail!=0 and turn%4==2) or (p4_jail!=0 and turn%4==3))):
        doubles=0
        flag=1
        if (turn%4==0):
            p1_jail=0
        elif (turn%4==1):
            p2_jail=0
        elif (turn%4==2):
            p3_jail=0
        elif (turn%4==3):
            p4_jail=0
    elif (flag==0 and roll==0 and ((p1_jail!=0 and turn%4==0) or (p2_jail!=0 and turn%4==1) or (p3_jail!=0 and turn%4==2) or (p4_jail!=0 and turn%4==3))):
        movement=0
        flag=1
        done=1
        if (turn%4==0):
            p1_jail=p1_jail-1
            if (p1_jail==0):
                force_bail=1
        elif (turn%4==1):
            p2_jail=p2_jail-1
            if (p2_jail==0):
                force_bail=1
        elif (turn%4==2):
            p3_jail=p3_jail-1
            if (p3_jail==0):
                force_bail=1
        elif (turn%4==3):
            p4_jail=p4_jail-1
            if (p4_jail==0):
                force_bail=1
    if (roll==0 and int(doubles)==3):
        movement=0
        doubles=0
        done=1
        if (turn%4==0):
            p1=10
            p1_jail=3
        elif (turn%4==1):
            p2=10
            p2_jail=3
        elif (turn%4==2):
            p3=10
            p3_jail=3
        elif (turn%4==3):
            p4=10
            p4_jail=3
    if (roll==0 and movement!=0):
        if (turn%4==0):
            p1=p1+1
            if (p1%40==0):
                p1_money=p1_money+200
        elif (turn%4==1):
            p2=p2+1
            if (p2%40==0):
                p2_money=p2_money+200
        elif (turn%4==2):
            p3=p3+1
            if (p3%40==0):
                p3_money=p3_money+200
        elif (turn%4==3):
            p4=p4+1
            if (p4%40==0):
                p4_money=p4_money+200
        movement=movement-1
    elif (movement==0 and done==0 and roll==0 and build==0 and trade==0):
        if (ownership[p(turn%4+1)%40][0]==0 and gameboard[p(turn%4+1)%40][0]!="special" and gameboard[p(turn%4+1)%40][0]!="chance" and gameboard[p(turn%4+1)%40][0]!="chest"):
            if (gameboard[p(turn%4+1)%40][0]=="property" and display_timer<=0):
                display="COST: $"+str(gameboard[p(turn%4+1)%40][1])+"   rent: $"+str(gameboard[p(turn%4+1)%40][2][0])+" 1 house: $"+str(gameboard[p(turn%4+1)%40][2][1])
                display2="2 houses: $"+str(gameboard[p(turn%4+1)%40][2][2])+" 3 houses: $"+str(gameboard[p(turn%4+1)%40][2][3])
                display3="4 houses: $"+str(gameboard[p(turn%4+1)%40][2][4])+" Hotel: $"+str(gameboard[p(turn%4+1)%40][2][5])
                display_timer=-1
            elif (gameboard[p(turn%4+1)%40][0]!="utility" and display_timer<=0):
                display="COST: $200   rent: $25"
                display2="2 railroads: $50, 3 railroads: $100"
                display3="4 railroads: $200"
                display_timer=-1
            elif (display_timer<=0):
                display="COST: $150"
                display2="1 utility: $4 x dice roll"
                display3="2 utilities: $10 x dice roll"
                display_timer=-1
            choice=1
            if (auction!=1):
                canvas.draw_line((800,500),(900,500),50,"lime")
                canvas.draw_text("Buy",(800,520),50,"white")
                canvas.draw_line((800,600),(1000,600),50,"lime")
                canvas.draw_text("Auction",(800,620),50,"white")
            if (buy==1):
                choice=0
                done=1
                display2=0
                display3=0
                display_timer=0
        if (ownership[p(turn%4+1)%40][1]==0 and ownership[p(turn%4+1)%40][2]==1):
            r=2
        else:
            r=1
        if (ownership[p(turn%4+1)%40][1]==0 and gameboard[p(turn%4+1)%40][0]=="utility"):
            r=4
        elif (gameboard[p(turn%4+1)%40][0]=="utility"):
            r=10
        if (gameboard[p(turn%4+1)][0]=="property"):
            if (ownership[p(turn%4+1)%40][0]==1 and turn%4!=0):
                p1_money=p1_money+gameboard[p(turn%4+1)%40][2][ownership[p(turn%4+1)%40][1]]*r
            elif (ownership[p(turn%4+1)%40][0]==2 and turn%4!=1):
                p2_money=p2_money+gameboard[p(turn%4+1)%40][2][ownership[p(turn%4+1)%40][1]]*r
            elif (ownership[p(turn%4+1)%40][0]==3 and turn%4!=2):
                p3_money=p3_money+gameboard[p(turn%4+1)%40][2][ownership[p(turn%4+1)%40][1]]*r
            elif (ownership[p(turn%4+1)%40][0]==4 and turn%4!=3):
                p4_money=p4_money+gameboard[p(turn%4+1)%40][2][ownership[p(turn%4+1)%40][1]]*r
        elif (gameboard[p(turn%4+1)][0]=="railroad"):
            if (ownership[p(turn%4+1)%40][0]==1 and turn%4!=0):
                p1_money=p1_money+25*2**ownership[p(turn%4+1)%40][1]
            elif (ownership[p(turn%4+1)%40][0]==2 and turn%4!=1):
                p2_money=p2_money+25*2**ownership[p(turn%4+1)%40][1]
            elif (ownership[p(turn%4+1)%40][0]==3 and turn%4!=2):
                p3_money=p3_money+25*2**ownership[p(turn%4+1)%40][1]
            elif (ownership[p(turn%4+1)%40][0]==4 and turn%4!=3):
                p4_money=p4_money+25*2**ownership[p(turn%4+1)%40][1]
        elif (gameboard[p(turn%4+1)][0]=="utility"):
            if (ownership[p(turn%4+1)%40][0]==1 and turn%4!=0):
                p1_money=p1_money+r*(die1+die2)
            elif (ownership[p(turn%4+1)%40][0]==2 and turn%4!=1):
                p2_money=p2_money+r*(die1+die2)
            elif (ownership[p(turn%4+1)%40][0]==3 and turn%4!=2):
                p3_money=p3_money+r*(die1+die2)
            elif (ownership[p(turn%4+1)%40][0]==4 and turn%4!=3):
                p4_money=p4_money+r*(die1+die2)
        if (turn%4==0):
            if (gameboard[p1%40][0]=="special"):
                p1_money=p1_money+gameboard[p1%40][1]
                done=1
                p1_jail=p1_jail+gameboard[p1%40][3]
                p1=p1+gameboard[p1%40][2]
                choice=0
            elif (gameboard[p1%40][0]=="chance"):
                value=p1%40
                chance()
                if (value!=p1%40):
                    done=1
                    choice=0
            elif (gameboard[p1%40][0]=="chest"):
                chest()
                done=1
            else:
                if (ownership[p1%40][0]==0):
                    if (buy==1):
                        p1_money=p1_money-gameboard[p1%40][1]
                        ownership[p1%40][0]=1
                        buy=0
                else:
                    vfn=ownership[p1%40][0]
                    if (ownership[p1%40][1]!=-1 and vfn!=1 and gameboard[p1%40][0]=="property"):
                        p1_money=p1_money-gameboard[p1%40][2][ownership[p1%40][1]]*r
                    elif (ownership[p1%40][2]==0 and vfn!=1 and gameboard[p1%40][0]!="utility"):
                        p1_money=p1_money-25*2**ownership[p1%40][1]
                    elif (ownership[p1%40][2]==0 and vfn!=1):
                        p1_money=p1_money-r*(die1+die2)
                        
                    done=1
        elif (turn%4==1):
            if (gameboard[p2%40][0]=="special"):
                p2_money=p2_money+gameboard[p2%40][1]
                done=1
                p2_jail=p2_jail+gameboard[p2%40][3]
                p2=p2+gameboard[p2%40][2]
                choice=0
            elif (gameboard[p2%40][0]=="chance"):
                value=p2%40
                chance()
                if (value!=p2%40):
                    done=1
                    choice=0
            elif (gameboard[p2%40][0]=="chest"):
                chest()
                done=1
            else:
                if (ownership[p2%40][0]==0):
                    if (buy==1):
                        p2_money=p2_money-gameboard[p2%40][1]
                        ownership[p2%40][0]=2
                        buy=0
                else:
                    vfn=ownership[p2%40][0]
                    if (ownership[p2%40][1]!=-1 and vfn!=2 and gameboard[p2%40][0]=="property"):
                        p2_money=p2_money-gameboard[p2%40][2][ownership[p2%40][1]]*r
                    elif (ownership[p2%40][2]==0 and vfn!=2 and gameboard[p2%40][0]!="utility"):
                        p2_money=p2_money-25*2**ownership[p2%40][1]
                    elif (ownership[p2%40][2]==0 and vfn!=2):
                        p2_money=p2_money-r*(die1+die2)
                        
                    done=1
        elif (turn%4==2):
            if (gameboard[p3%40][0]=="special"):
                p3_money=p3_money+gameboard[p3%40][1]
                done=1
                p3_jail=p3_jail+gameboard[p3%40][3]
                p3=p3+gameboard[p3%40][2]
                choice=0
            elif (gameboard[p3%40][0]=="chance"):
                value=p3%40
                chance()
                if (value!=p3%40):
                    done=1
                    choice=0
            elif (gameboard[p3%40][0]=="chest"):
                chest()
                done=1
            else:
                if (ownership[p3%40][0]==0):
                    if (buy==1):
                        p3_money=p3_money-gameboard[p3%40][1]
                        ownership[p3%40][0]=3
                        buy=0
                else:
                    vfn=ownership[p3%40][0]
                    if (ownership[p3%40][1]!=-1 and vfn!=3 and gameboard[p3%40][0]=="property"):
                        p3_money=p3_money-gameboard[p3%40][2][ownership[p3%40][1]]*r
                    elif (ownership[p3%40][2]==0 and vfn!=3 and gameboard[p3%40][0]=="railroad"):
                        p3_money=p3_money-25*2**ownership[p3%40][1]
                    elif (ownership[p3%40][2]==0 and vfn!=3):
                        p3_money=p3_money-r*(die1+die2)
                    done=1
        else: #(turn%4==3):
            if (gameboard[p4%40][0]=="special"):
                p4_money=p4_money+gameboard[p4%40][1]
                done=1
                p4_jail=p4_jail+gameboard[p4%40][3]
                p4=p4+gameboard[p4%40][2]
                choice=0
            elif (gameboard[p4%40][0]=="chance"):
                value=p4%40
                chance()
                if (value!=p4%40):
                    done=1
                    choice=0
            elif (gameboard[p4%40][0]=="chest"):
                chest()
                done=1
            else:
                if (ownership[p4%40][0]==0):
                    if (buy==1):
                        p4_money=p4_money-gameboard[p4%40][1]
                        ownership[p4%40][0]=4
                        buy=0
                else:
                    vfn=ownership[p4%40][0]
                    if (ownership[p4%40][1]!=-1 and vfn!=4 and gameboard[p4%40][0]=="property"):
                        p4_money=p4_money-gameboard[p4%40][2][ownership[p4%40][1]]*r
                    elif (ownership[p4%40][2]==0 and vfn!=4 and gameboard[p4%40][0]=="railroad"):
                        p4_money=p4_money-25*2**ownership[p4%40][1]
                    elif (ownership[p4%40][2]==0 and vfn!=4):
                        p4_money=p4_money-r*(die1+die2)
                    done=1
        if ((turn%4==0 and p1_money<=0) or (turn%4==1 and p2_money<=0) or (turn%4==2 and p3_money<=0) or (turn%4==3 and p4_money<=0)):
            lastpaid=ownership[p(turn%4+1)][0]
            doubles=0
            done=1
def click_handler(n):
    global roll,p1,p2,p3,p4,p1_money,p2_money,p3_money,p4_money,p1_jail,p2_jail,p3_jail,p4_jail
    global done,buy,auction,bid,bidder,top_bid,fold,fold2,build
    global turn,display,display2,display_timer,display3,group,trade,trade1,trade2,trader,tradee,role
    global choice,movement,die1,die2,force_bail,flag,cursor,bankrupt1,bankrupt2,bankrupt3,lastpaid
    x=n[0]
    y=n[1]
    if (roll==1 and x>=800 and x<=1000 and y>=550 and y<=650):
        roll=2
    if (roll==1 and ((p1_jail!=0 and turn%4==0) or (p2_jail!=0 and turn%4==1) or (p3_jail!=0 and turn%4==2) or (p4_jail!=0 and turn%4==3))):
        if (x>=800 and y>=400 and x<=1000 and y<=500):
            if (turn%4==0):
                p1_money=p1_money-50
                p1_jail=0
            elif (turn%4==1):
                p2_money=p2_money-50
                p2_jail=0
            elif (turn%4==2):
                p3_money=p3_money-50
                p3_jail=0
            elif (turn%4==3):
                p4_money=p4_money-50
                p4_jail=0
            roll=2
    if (auction==1):
        if (x>=800 and x<=850 and y<=575 and y>= 525):
            bid=bid+1
        elif (x>=875 and x<=925 and y<=575 and y>= 525):
            bid=bid+10
        elif (x>=950 and x<=1000 and y<=575 and y>= 525):
            bid=bid+100
        elif (x>=800 and x<=850 and y<=675 and y>= 625):
            bid=bid-1
        elif (x>=875 and x<=925 and y<=675 and y>= 625):
            bid=bid-10
        elif (x>=950 and x<=1000 and y<=675 and y>= 625):
            bid=bid-100
        if (bid<=top_bid):
            bid=top_bid+1
        
        if (x>=950 and x<=1050 and y>=400 and y<= 500):
            if (fold==0):
                fold=bidder%4
            elif (fold2==0):
                fold2=bidder%4
            else:
                bidder=bidder+1
                while (fold==bidder%4 or fold2==bidder%4):
                    bidder=bidder+1
                choice=0
                auction=0
                display_timer=0
                display2=0
                display3=0
                done=1
                if (bidder%4==0):
                    p1_money=p1_money-top_bid
                    ownership[p(turn%4+1)][0]=1
                elif (bidder%4==1):
                    p2_money=p2_money-top_bid
                    ownership[p(turn%4+1)][0]=2
                elif (bidder%4==2):
                    p3_money=p3_money-top_bid
                    ownership[p(turn%4+1)][0]=3
                elif (bidder%4==3):
                    p4_money=p4_money-top_bid
                    ownership[p(turn%4+1)][0]=4
                    
            bidder=bidder+1
            bid=top_bid+1
        elif (x>=800 and x<=900 and y>=400 and y<= 500):
            top_bid=bid
            bid=top_bid+1
            bidder=bidder+1
            while (fold==bidder%4 or fold2==bidder%4):
                bidder=bidder+1
    if (choice==1 and auction!=1):
        if (x>=800 and x<=900 and y>=475 and y<= 525):
            buy=1
        elif (x>=800 and x<=1000 and y>=575 and y<=625):
            auction=1
            bidder=turn
            bid=1
            top_bid=0
            fold=bankrupt1
            fold2=bankrupt2
    if (build==1):
        if (x>=760 and x<=850 and y<=500 and y>=400):
            cursor=cursor-1
        elif (x>=950 and x<=1040 and y<=500 and y>=400):
            cursor=cursor+1
        elif (x>=750 and y>=265 and x<=850 and y<=335):
            build=0
            done=1
        if (ownership[cursor%40][0]==turn%4+1):
            if (x>=715 and x<=790 and y<=662.5 and y>=587.5):
                if (ownership[cursor%40][1]>=ownership[group[cursor%40][1]][1] and ownership[cursor%40][1]>=ownership[group[cursor%40][2]][1] and ownership[cursor%40][1]!=-1):
                    ownership[cursor%40][1]=ownership[cursor%40][1]-1
                    if (ownership[cursor%40][1]==-1):
                        r=1
                    else:
                        r=0
                    if (turn%4==0):
                        p1_money=p1_money+(int((cursor%40)/10)+1)*25*(1-r)+(gameboard[cursor%40][1]/2)*r
                    elif (turn%4==1):
                        p2_money=p2_money+(int((cursor%40)/10)+1)*25*(1-r)+(gameboard[cursor%40][1]/2)*r
                    elif (turn%4==2):
                        p3_money=p3_money+(int((cursor%40)/10)+1)*25*(1-r)+(gameboard[cursor%40][1]/2)*r
                    elif (turn%4==3):
                        p4_money=p4_money+(int((cursor%40)/10)+1)*25*(1-r)+(gameboard[cursor%40][1]/2)*r
            elif (x>=1010 and x<=1085 and y<=662.5 and y>=587.5):
                if ((ownership[cursor%40][2]==1 or ownership[cursor%40][1]==-1) and ownership[cursor%40][1]!=5 and (gameboard[cursor%40][0]=="property" or ownership[cursor%40][1]==-1) and ownership[cursor%40][1]<=ownership[group[cursor%40][1]][1] and ownership[cursor%40][1]<=ownership[group[cursor%40][2]][1]):
                    if (ownership[cursor%40][1]==-1):
                        r=1
                    else:
                        r=0
                    if (turn%4==0):
                        p1_money=p1_money-(int((cursor%40)/10)+1)*50*(1-r)-(gameboard[cursor%40][1]/2+round(gameboard[cursor%40][1]/10))*r
                    elif (turn%4==1):
                        p2_money=p2_money-(int((cursor%40)/10)+1)*50*(1-r)-(gameboard[cursor%40][1]/2+round(gameboard[cursor%40][1]/10))*r
                    elif (turn%4==2):
                        p3_money=p3_money-(int((cursor%40)/10)+1)*50*(1-r)-(gameboard[cursor%40][1]/2+round(gameboard[cursor%40][1]/10))*r
                    elif (turn%4==3):
                        p4_money=p4_money-(int((cursor%40)/10)+1)*50*(1-r)-(gameboard[cursor%40][1]/2+round(gameboard[cursor%40][1]/10))*r
                    ownership[cursor%40][1]=ownership[cursor%40][1]+1
    if (trade==1 and role!=2):
        if (x>=760 and x<=850 and y<=500 and y>=400):
            cursor=cursor-1
        elif (x>=950 and x<=1040 and y<=500 and y>=400):
            cursor=cursor+1
        elif (x>=750 and y>=265 and x<=850 and y<=335):
            trade=0
            done=1
            trader=0
            tradee=0
            trade1=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            trade2=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            display2=0
            display3=0
            display_timer=0
        r=0
        if (x>=800 and x<=850 and y<=575 and y>= 525):
            r=1
        elif (x>=875 and x<=925 and y<=575 and y>= 525):
            r=10
        elif (x>=950 and x<=1000 and y<=575 and y>= 525):
            r=100
        elif (x>=800 and x<=850 and y<=675 and y>= 625):
            r=-1
        elif (x>=875 and x<=925 and y<=675 and y>= 625):
            r=-10
        elif (x>=950 and x<=1000 and y<=675 and y>= 625):
            r=-100
        if (role==0):
            trade1[42]=trade1[42]+r
        else:
            trade2[42]=trade2[42]+r
        if (trade1[42]<0):
            trade1[42]=0
        if (trade2[42]<0):
            trade2[42]=0
        if (x>=870 and y<=335 and x<=970 and y>=265):
            role=(-2*(role-0.5)+1)/2
        elif (x>=990 and y<=335 and x<=1090 and y>=265):
            role=2
        if (x>=715 and x<=790 and y<=662.5 and y>=587.5):
            if (role==0):
                trade1[cursor%40]=0
            else:
                trade2[cursor%40]=0
        elif (x>=1010 and x<=1085 and y<=662.5 and y>=587.5 and ownership[cursor%40][1]+ownership[group[cursor%40][1]][1]+ownership[group[cursor%40][2]][1]<=0):
            if (role==0 and ownership[cursor%40][0]==trader):
                trade1[cursor%40]=1
            elif (role==1 and ownership[cursor%40][0]==tradee):
                trade2[cursor%40]=1
    elif (role==2 and trade==1):
        if (x>=750 and y>=265 and x<=850 and y<=335):
            trade=0
            done=1
            trader=0
            tradee=0
            trade1=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            trade2=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            display2=0
            display3=0
            display_timer=0
        elif (x>=870 and y<=335 and x<=970 and y>=265):
            for i in range(42):
                if (trade1[i]==1):
                    ownership[i][0]=tradee
                if (trade2[i]==1):
                    ownership[i][0]=trader
            if (trader==1):
                p1_money=p1_money+trade2[42]-trade1[42]
            elif (trader==2):
                p2_money=p2_money+trade2[42]-trade1[42]
            elif (trader==3):
                p3_money=p3_money+trade2[42]-trade1[42]
            else:
                p4_money=p4_money+trade2[42]-trade1[42]
            if (tradee==1):
                p1_money=p1_money-trade2[42]+trade1[42]
            elif (tradee==2):
                p2_money=p2_money-trade2[42]+trade1[42]
            elif (tradee==3):
                p3_money=p3_money-trade2[42]+trade1[42]
            else:
                p4_money=p4_money-trade2[42]+trade1[42]
            trade=0
            done=1
            trader=0
            tradee=0
            trade1=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            trade2=list([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
            display2=0
            display3=0
            display_timer=0
        elif (x>=990 and y<=335 and x<=1090 and y>=265):
            vfn=trade1
            trade1=trade2
            trade2=vfn
            vfn=trader
            trader=tradee
            tradee=vfn
            role=0
    elif (trade==2 and y>=475 and y<=525):
        if (x>=725 and x<=775 and trader!=1):
            tradee=1
            trade=1
        elif (x>=800 and x<=850 and trader!=2):
            tradee=2
            trade=1
        elif (x>=875 and x<=925 and trader!=3):
            tradee=3
            trade=1
        elif (x>=950 and x<=1000 and trader!=4):
            tradee=4
            trade=1
                
    if (done==1 and force_bail==0 and x>=750):
        if (x<=1000 and y<=635 and y>=565):
            done=0
            flag=0
            roll=1
            if ((turn%4==0 and p1_money<0) or (turn%4==1 and p2_money<0) or (turn%4==2 and p3_money<0) or (turn%4==3 and p4_money<0)):
                if (bankrupt1==0):
                    bankrupt1=turn%4+1
                elif (bankrupt2==0):
                    bankrupt2=turn%4+1
                else:
                    bankrupt3=turn%4+1
                for i in range(42):
                    if (ownership[i][0]==turn%4+1):
                        ownership[i][0]=lastpaid
            turn=turn+1
            while (bankrupt3==turn%4+1 or bankrupt2==turn%4+1 or bankrupt1==turn%4+1):
                turn=turn+1
        elif (y>=365 and x<=900 and y<=435):
            done=0
            build=1
        elif (y<=535 and x<=900 and y>=465):
            done=0
            role=0
            trade=2
            trader=turn%4+1
    elif (done==1 and force_bail==1):
        if (x>=800 and y<=650 and x<=1000 and y>=550):
            if (turn%4==0):
                p1_money=p1_money-50
            elif (turn%4==1):
                p2_money=p2_money-50
            elif (turn%4==2):
                p3_money=p3_money-50
            elif (turn%4==3):
                p4_money=p4_money-50
            done=0
            force_bail=0
            movement=die1+die2
def save():
    global p1,p2,p3,p4,p1_money,p2_money,p3_money,p4_money,p1_jail,p2_jail,p3_jail,p4_jail,roll,ownership,turn,choice,doubles,chance_deck,chest_deck,bid,top_bid,auction,bidder,done,display,display2,display3,display_timer,fold,fold2,trade,trader,tradee,trade1,trade2,role,bankrupt1,bankrupt2,bankrupt3
    r1=str(int(p1_money))
    r2=str(int(p2_money))
    r3=str(int(p3_money))
    r4=str(int(p4_money))
    for i in range(4-len(r1)):
        r1="0"+r1
    for i in range(4-len(r2)):
        r2="0"+r2
    for i in range(4-len(r3)):
        r3="0"+r3
    for i in range(4-len(r4)):
        r4="0"+r4
    print ("")
    print (chr(p1%40+200)+chr(p2%40+200)+chr(p3%40+200)+chr(p4%40+200)+chr(int(r1[0]+r1[1])+100)+chr(p1_jail+250)+chr(int(r2[0]+r2[1])+100)+chr(p2_jail+250),end="")
    print (chr(int(r3[0]+r3[1])+100)+chr(p3_jail+250)+chr(int(r4[0]+r4[1])+100)+chr(p4_jail+250),end="")
    print (chr(int(r1[2]+r1[3])+100)+chr(int(r2[2]+r2[3])+100)+chr(int(r3[2]+r3[3])+100)+chr(int(r4[2]+r4[3])+100),end="")
    print (chr(roll+50)+chr(turn%4+50)+chr(auction+100)+chr(bidder%4+100)+chr(done+100)+chr(choice+150)+chr((doubles+10)*10)+chr(fold+125)+chr(fold2+125),end="")
    print (random.randint(10000,99999),end="")
    for i in range(40):
        for o in range(3):
            print (chr(ownership[i][o]+i*o+70),end="")
    for i in range(16):
        print (chr(chance_deck[i][1]+130),end="")
        print (chr(chest_deck[i][1]+130),end="")
    print (chr(trade+122)+chr(bankrupt1+75)+chr(bankrupt2+75)+chr(bankrupt3+75),end="")
    if (auction==1):
        print (chr(int(bid/111+100))+chr(bid%111+100)+chr(int(top_bid/111+100))+chr(top_bid%111+100),end="")
    if (trade!=0):
        print (chr(trader+122)+chr(role+122)+chr(tradee+122),end="")
        for i in range(42):
            print (chr(trade1[i]+i+150),end="")
            print (chr(trade2[i]+i+100),end="")
        r1=str(trade1[42])
        r2=str(trade2[42])
        for i in range(4-len(r1)):
            r1="0"+r1
        for i in range(4-len(r2)):
            r2="0"+r2
        print (chr(int(r1[0]+r1[1])+100)+chr(int(r2[0]+r2[1])+100)+chr(int(r1[2]+r1[3])+100)+chr(int(r2[2]+r2[3])+100),end="")

def Load(load):
    global p1,p2,p3,p4,p1_money,p2_money,p3_money,p4_money,p1_jail,p2_jail,p3_jail,p4_jail,roll,ownership,turn,choice,doubles,chance_deck,chest_deck,bid,top_bid,auction,bidder,done,display,display2,display3,display_timer,fold,fold2,trade,trader,tradee,trade1,trade2,role,bankrupt1,bankrupt2,bankrupt3,alist,elist
    p1=ord(load[0])-200
    p2=ord(load[1])-200
    p3=ord(load[2])-200
    p4=ord(load[3])-200
    p1_money=(ord(load[4])-100)*100+ord(load[12])-100
    p2_money=(ord(load[6])-100)*100+ord(load[13])-100
    p3_money=(ord(load[8])-100)*100+ord(load[14])-100
    p4_money=(ord(load[10])-100)*100+ord(load[15])-100
    p1_jail=ord(load[5])-250
    p2_jail=ord(load[7])-250
    p3_jail=ord(load[9])-250
    p4_jail=ord(load[11])-250
    roll=ord(load[16])-50
    turn=ord(load[17])-50
    auction=ord(load[18])-100
    bidder=ord(load[19])-100
    done=ord(load[20])-100
    choice=ord(load[21])-150
    doubles=(ord(load[22])/10)-10
    fold=ord(load[23])-125
    fold2=ord(load[24])-125
    random.seed(int(load[25]+load[26]+load[27]+load[28]+load[29]))
    for i in range(40):
        for o in range(3):
            ownership[i][o]=ord(load[i*3+o+30])-(i*o+70)
    for i in range(16):
        chance_deck[i][1]=ord(load[150+i*2])-130
        chest_deck[i][1]=ord(load[151+i*2])-130
    dlist()
    trade=ord(load[182])-122
    bankrupt1=ord(load[183])-75
    bankrupt2=ord(load[184])-75
    bankrupt3=ord(load[185])-75
    if (auction==1):
        bid=(ord(load[186])-100)*111+ord(load[187])-100
        top_bid=(ord(load[188])-100)*111+ord(load[189])-100
    elif (trade!=0):
        trader=ord(load[186])-122
        role=ord(load[187])-122
        tradee=ord(load[188])-122
        for i in range(42):
            trade1[i]=ord(load[189+2*i])-i-150
            trade2[i]=ord(load[190+2*i])-i-100
        trade1[42]=(ord(load[272])-100)*100+ord(load[274])-100
        trade2[42]=(ord(load[273])-100)*100+ord(load[275])-100
    for i in range (16):
        e=0
        while (alist[e][1]!=chance_deck[i][1]):
            e=random.randint(0,15)
        chance_deck[i]=alist[e]
        while (elist[e][1]!=chest_deck[i][1]):
            e=random.randint(0,15)
        chest_deck[i]=elist[e]
        
frame = simplegui.create_frame("Monopulley", 1100, 700)
button1 = frame.add_button('Save', save, 200)
load = frame.add_input('Load', Load,200)
frame.set_mouseclick_handler(click_handler)
frame.set_canvas_background('White')
frame.set_draw_handler(draw)

frame.start()
