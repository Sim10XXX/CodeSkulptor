import simplegui
import math
import time
import random #for graphics
def def_rules(a=0):
    global rules,instance,compression
    rules=[[],[],[],[],[],[],[],[],[],[],[],{}]
    for r in range(len(level[instance])):
        for c in range(len(level[instance][r])):
            i=instance
            while (level[i][r][c]==[[]]):
                i=i-1
            for l in range(len(level[i][r][c])):
                if (len(level[i][r][c][l])>2):
                    level[i][r][c][l][2]=0
                if (level[i][r][c][l][0]=="21"):			#"is"
                    if (r>0 and r<len(level[i])-1):					#vertical rules
                        i1=instance
                        while (level[i1][r-1][c]==[[]]):
                            i1=i1-1
                        for layer in range (len(level[i1][r-1][c])):
                            if (type(level[i1][r-1][c][layer][0])==str):
                                if (int(level[i1][r-1][c][layer][0])<=20):
                                    #value=level[i1][r-1][c][layer]
                                    i2=instance
                                    while (level[i2][r+1][c]==[[]]):
                                        i2=i2-1
                                    for layer2 in range (len(level[i2][r+1][c])):
                                        if (type(level[i2][r+1][c][layer2][0])==str):
                                            if (int(level[i2][r+1][c][layer2][0])>=31):		#normal
                                                rules[int(level[i2][r+1][c][layer2][0])-31].append(int(level[i1][r-1][c][layer][0]))
                                            elif (int(level[i2][r+1][c][layer2][0])<=20):	#conversion
                                                rules[11].setdefault(int(level[i1][r-1][c][layer][0]),[])
                                                rules[11][int(level[i1][r-1][c][layer][0])].append(int(level[i2][r+1][c][layer2][0]))
                                                
                                                
                    if (c>0 and c<len(level[i][r])-1):					#horizontal rules
                        i1=instance
                        while (level[i1][r][c-1]==[[]]):
                            i1=i1-1
                        for layer in range (len(level[i1][r][c-1])):
                            if (type(level[i1][r][c-1][layer][0])==str):
                                if (int(level[i1][r][c-1][layer][0])<=20):
                                    #value=level[i1][r][c-1][layer]
                                    i2=instance
                                    while (level[i2][r][c+1]==[[]]):
                                        i2=i2-1
                                    for layer2 in range (len(level[i2][r][c+1])):
                                        if (type(level[i2][r][c+1][layer2][0])==str):
                                            if (int(level[i2][r][c+1][layer2][0])>=31):		#normal
                                                rules[int(level[i2][r][c+1][layer2][0])-31].append(int(level[i1][r][c-1][layer][0]))
                                            elif (int(level[i2][r][c+1][layer2][0])<=20):	#conversion
                                                rules[11].setdefault(int(level[i1][r][c-1][layer][0]),[])
                                                rules[11][int(level[i1][r][c-1][layer][0])].append(int(level[i2][r][c+1][layer2][0]))
    for o in range(-1,21):
        rules[11].setdefault(o,[o])
    for o in range(len(rules[0])):
        if (rules[0][o] in rules[2]):
            rules[3].append(rules[0][o])
    for o in range(len(rules[3])):
        rules[2].append(rules[3][o])
    if (a==1):
        complist=[]
        compression=[]
        for o in range (-1,21):
            if (o not in rules[0] and o not in rules[1] and o not in rules[4] and o not in rules[5] and o not in rules[6] and o not in rules[7] and o not in rules[8] and o not in rules[9]):
                complist.append(o)
        for r in range(len(level[instance])):
            for c in range(len(level[instance][r])):
                i=instance
                while (level[i][r][c]==[[]]):
                    i=i-1
                compval=0
                for l in range(len(level[i][r][c])):
                    if (level[i][r][c][l][0] not in complist):
                        compval=1
                if (compval==0):
                    compression.append([r,c])
#level[instance][row][column][layer][0=type,1=face (unused),2=movement flag]
level=[[[[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[["4",1,0]],[["21",1,0]],[["33",1,0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[4,1,0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[1,2,0]],[[0]],[[0]],[[4,1,0]],[[0]],[[0]],[[0]],[[3,1,0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[4,1,0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[["1",1,0]],[["21",1,0]],[["31",1,0]],[[0]],[[0]],[["3",1,0]],[["21",1,0]],[["32",1,0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]]]]
instance=0
win=0
time1=-210
value=-1
part=1
h=random.randint(0,200000)
time2=150
part2=1
h2=random.randint(0,200000)
time3=-30
part3=1
h3=random.randint(0,200000)
note=0
particle=7
hp=random.randint(0,200000)
tick=0
ppos=[]
hw=[]
for i in range(10):
    hw.append(random.randint(0,200000))
#rules[0]="you"    rules[1]="win"    rules[2]="stop"    rules[3]="push"    rules[4]="defeat"    rules[5]="sink"
#rules[6]="hot"   rules[7]="melt"    rules[8]="open"        rules[9]="shut"        rules[10]="float"         rules[11]=conversion
def_rules()

def input_handler(code):
    global level,instance,note
    if (len(code)>5):
        level=[[]]
        instance=0
        win=0
        r=-1
        c=-1
        l=-1
        s=-1
        for x in range(len(code)):
            if (code[x]=="."):
                s=s+1
                level[instance][r][c][l].append(0)
            elif (code[x]=="'"):
                s=-1
                l=l+1
                level[instance][r][c].append([])
            elif (code[x]==","):
                l=-1
                c=c+1
                level[instance][r].append([])
            elif (code[x]=="|"):
                c=-1
                r=r+1
                level[instance].append([])
            else:
                if (ord(code[x])>=68):
                    level[instance][r][c][l][s]=str(ord(code[x])-69)
                else:
                    level[instance][r][c][l][s]=ord(code[x])-48
        frame = simplegui.create_frame('Game Is You', len(level[0][0])*50, len(level[0])*50)
        frame.set_canvas_background('gray')
        inp = frame.add_input('Level Code (hit enter for code or paste to load)', input_handler,200)
        frame.set_draw_handler(draw_handler)
        frame.set_keydown_handler(key_handler)
        frame.start()
        note=150
    else:
        for r in range(len(level[instance])):
            print ("|",end="")
            for c in range(len(level[instance][r])):
                print (",",end="")
                i=instance
                while (level[i][r][c]==[[]]):
                    i=i-1
                for l in range(len(level[i][r][c])):
                    print ("'",end="")
                    for s in range(len(level[i][r][c][l])):
                        print (".",end="")
                        if (type(level[i][r][c][l][s])==int):
                            print (chr(level[i][r][c][l][s]+48),end="")
                        else:
                            print (chr(int(level[i][r][c][l][s])+69),end="")
        print ("")
        print ("")
    def_rules()


def draw_handler(canvas):
    global level,instance,rules,note
    global time1,h,part,x,y,time2,h2,part2,x2,y2,time3,h3,part3,x3,y3 #for fireworks
    global flo,f,particle,tick,ppos,hp,hw
    #print (rules)
    tick=tick+1
    flo=(math.sin(tick/15)+0.7)*8
    if (particle<7):
        particle=particle+1
    else:
        ppos=[]
    for r in range(len(level[instance])):
        for c in range(len(level[instance][r])):
            i=instance
            while (level[i][r][c]==[[]]):
                i=i-1
            fval=-1
            fchk=0
            for l in range(len(level[i][r][c])):
                #print (level[i][r][c],end="\t")
                if (level[i][r][c][l][0]!=0):
                    if (level[i][r][c][l][0] in rules[10] or (type(level[i][r][c][l][0])==str and -1 in rules[10])):
                        f=flo
                        if (fval==-1):
                            fval=l
                    else:
                        f=0
                        if (fval!=-1):
                            fchk=1
                    if (level[i][r][c][l][0]==1):
                        canvas.draw_circle([25+50*c,25+50*r-f],20,5,"red")
                        canvas.draw_line([6+50*c,50*r-f],[6+50*c,12+50*r-f],12,"red")
                        canvas.draw_line([6+50*c,50+50*r-f],[6+50*c,38+50*r-f],12,"red")
                        canvas.draw_line([44+50*c,50+50*r-f],[44+50*c,38+50*r-f],12,"red")
                        canvas.draw_line([44+50*c,50*r-f],[44+50*c,12+50*r-f],12,"red")
                    if (level[i][r][c][l][0]==2):
                        canvas.draw_arc([25+50*c,50*r-f],45,1.05,2.07,10,"green")
                        canvas.draw_arc([50*c,43+50*r-f],45,5.25,6.29,10,"green")
                        canvas.draw_arc([50+50*c,43+50*r-f],45,3.15,4.2,10,"green")
                    if (level[i][r][c][l][0]==3):
                        canvas.draw_line([10+50*c,45+50*r-f],[16+50*c,5+50*r-f],5,"yellow")
                        canvas.draw_circle([10+50*c,45+50*r-f],2,1,"yellow","yellow")
                        canvas.draw_circle([16+50*c,5+50*r-f],2,1,"yellow","yellow")
                        canvas.draw_line([12+50*c,14+50*r-f],[38.67+50*c,18+50*r-f],15,"yellow")
                    if (level[i][r][c][l][0]==4):
                        canvas.draw_arc([50*c,50*r-f],23,0.1,1.47,10,"blue")
                        canvas.draw_arc([50+50*c,50*r-f],23,1.67,3.04,10,"blue")
                        canvas.draw_arc([50*c,50+50*r-f],23,4.81,-0.1,10,"blue")
                        canvas.draw_arc([50+50*c,50+50*r-f],23,3.24,4.61,10,"blue")
                        canvas.draw_circle([25+50*c,25+50*r-f],7,1,"blue","blue")
                    if (level[i][r][c][l][0]==5):
                        canvas.draw_line([25+50*c,5+50*r-f],[25+50*c,45+50*r-f],40,"black")
                        canvas.draw_line([25+50*c,10+50*r-f],[25+50*c,40+50*r-f],30,"rgb(50,50,50)")
                    if (level[i][r][c][l][0]==6):
                        canvas.draw_circle([25+50*c,20+50*r-f],15,8,"brown")
                        canvas.draw_circle([17.5+50*c,21+50*r-f],7,6,"brown")
                        canvas.draw_circle([32.5+50*c,21+50*r-f],7,6,"brown")
                        canvas.draw_line([12+50*c,13+50*r-f],[38+50*c,13+50*r-f],14,"brown")
                        
                        canvas.draw_line([17.5+50*c,43+50*r-f],[17.5+50*c,33+50*r-f],3,"brown")
                        canvas.draw_line([22.5+50*c,43+50*r-f],[22.5+50*c,13+50*r-f],3,"brown")
                        canvas.draw_line([27.5+50*c,43+50*r-f],[27.5+50*c,13+50*r-f],3,"brown")
                        canvas.draw_line([32.5+50*c,43+50*r-f],[32.5+50*c,33+50*r-f],3,"brown")
                    if (level[i][r][c][l][0]=="-1"):
                        canvas.draw_text("t",[11+50*c,23+50*r-f],30,"white")
                        canvas.draw_text("e",[22+50*c,23+50*r-f],30,"white")
                        canvas.draw_text("x",[10+50*c,45+50*r-f],30,"white")
                        canvas.draw_text("t",[25+50*c,45+50*r-f],30,"white")
                    if (level[i][r][c][l][0]=="1"):
                        canvas.draw_text("red",[5+50*c,33+50*r-f],30,"red")
                    if (level[i][r][c][l][0]=="2"):
                        canvas.draw_text("gre",[5+50*c,23+50*r-f],30,"green")
                        canvas.draw_text("en",[10+50*c,45+50*r-f],30,"green")
                    if (level[i][r][c][l][0]=="3"):
                        canvas.draw_text("f",[10+50*c,23+50*r-f],30,"yellow")
                        canvas.draw_text("l",[25+50*c,23+50*r-f],30,"yellow")
                        canvas.draw_text("ag",[10+50*c,45+50*r-f],30,"yellow")
                    if (level[i][r][c][l][0]=="4"):
                        canvas.draw_text("blue",[0+50*c,33+50*r-f],30,"blue")
                    if (level[i][r][c][l][0]=="5"):
                        canvas.draw_text("bla",[5+50*c,23+50*r-f],30,"black")
                        canvas.draw_text("ck",[10+50*c,45+50*r-f],30,"black")
                    if (level[i][r][c][l][0]=="6"):
                        canvas.draw_text("sk",[10+50*c,23+50*r-f],30,"brown")
                        canvas.draw_text("ull",[7+50*c,45+50*r-f],30,"brown")
                    if (level[i][r][c][l][0]=="21"):
                        canvas.draw_text("is",[15+50*c,33+50*r-f],30,"white")
                    if (level[i][r][c][l][0]=="31"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"pink")
                        canvas.draw_text("you",[2+50*c,33+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="32"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"yellow")
                        canvas.draw_text("win",[2+50*c,33+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="33"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"red")
                        canvas.draw_text("s",[10+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("t",[25+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("op",[10+50*c,45+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="34"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"rgb(100,75,50)")
                        canvas.draw_text("pu",[10+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("sh",[10+50*c,45+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="35"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"rgb(100,0,0)")
                        canvas.draw_text("def",[5+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("eat",[5+50*c,45+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="36"): #sink
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"cyan")
                        canvas.draw_text("s",[10+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("i",[25+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("nk",[10+50*c,45+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="37"): #hot
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"rgb(255,50,50)")
                        canvas.draw_text("hot",[5+50*c,33+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="38"): #melt
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"lightblue")
                        canvas.draw_text("m",[8+50*c,23+50*r-f],30,"grey","monospace")
                        canvas.draw_text("e",[26+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("l",[10+50*c,45+50*r-f],30,"grey")
                        canvas.draw_text("t",[25+50*c,45+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="39"): #open
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"lightyellow")
                        canvas.draw_text("op",[10+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("en",[10+50*c,45+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="40"): #shut
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"brown")
                        canvas.draw_text("sh",[10+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("ut",[10+50*c,45+50*r-f],30,"grey")
                    if (level[i][r][c][l][0]=="41"): #float
                        canvas.draw_polygon([[14+50*c,12.5+50*r-f],[36+50*c,12.5+50*r-f],[37.5+50*c,14+50*r-f],[37.5+50*c,36+50*r-f],[36+50*c,37.5+50*r-f],[14+50*c,37.5+50*r-f],[12.5+50*c,36+50*r-f],[12.5+50*c,14+50*r-f]],25,"rgb(240,240,255)")
                        canvas.draw_text("f",[10+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("l",[25+50*c,23+50*r-f],30,"grey")
                        canvas.draw_text("oat",[5+50*c,45+50*r-f],30,"grey")
                if (level[i][r][c][l][0] in rules[1] or (-1 in rules[1] and type(level[i][r][c][l][0])==str)):
                    #random.seed(hw)
                    #hw2=random.randint(0,200000)
                    for par in range(10):
                        if ((tick+par)%10==0):
                            hw[par]=random.randint(0,200000)
                        random.seed(hw[par])
                        o=random.uniform(1.5,10)
                        o=o*random.randrange(-1,2,2)
                        k=random.uniform(1.5,10)
                        k=k*random.randrange(-1,2,2)
                        s=random.uniform(6,7)
                        if ((tick+par)%10!=0):
                            canvas.draw_line([25+50*c+o*math.sqrt((tick+par)%10),25+50*r+k*math.sqrt((tick+par)%10)+s*0.5],[25+50*c+o*math.sqrt((tick+par)%10),25+50*r+k*math.sqrt((tick+par)%10)+-s*0.5],s,"rgb(255,255,0,"+str(1-((tick+par)%10/7))+")")

            if (fchk==1):
                level[i][r][c].append(level[i][r][c].pop(fval))
            if ([r,c] in ppos):
                random.seed(hp)
                for par in range(random.randint(10,15)):
                    o=random.uniform(1.5,10)
                    o=o*random.randrange(-1,2,2)
                    k=random.uniform(1.5,10)
                    k=k*random.randrange(-1,2,2)
                    s=random.uniform(6,7)
                    canvas.draw_line([25+50*c+o*math.sqrt(particle),25+50*r+k*math.sqrt(particle)+s*0.5],[25+50*c+o*math.sqrt(particle),25+50*r+k*math.sqrt(particle)+-s*0.5],s,"rgb(0,0,0,"+str(1-(particle/7))+")")
    if (win==1):
        time1=time1+5
        random.seed(h)
        canvas.draw_text("WIN",[(len(level[0][0])*50)/2-(frame.get_canvas_textwidth("WIN",200,"sans-serif"))/2,(len(level[0])*50)/2+75],200,"rgb(235,235,235,0.8)","sans-serif")
        if (part==1):
            a=random.uniform(-0.16,0.16)
            x=random.randint(30,len(level[0][0])*50-30)
            canvas.draw_line([x-3*a+time1*a,len(level[0])*50+3*(1-a)-time1*(1-a)],[x+time1*a,len(level[0])*50-time1*(1-a)],1,"orange")
            canvas.draw_line([x+time1*a,len(level[0])*50-time1*(1-a)],[x+10*a+time1*a,len(level[0])*50-10*(1-a)-time1*(1-a)],3,"black")
            canvas.draw_circle([x+10*a+time1*a,len(level[0])*50-10*(1-a)-time1*(1-a)],1.5,0.1,"black","black")
            if (time1>random.randint(len(level[0])*30,len(level[0])*45)):
                part=2
                x=x+10*a+time1*a
                y=len(level[0])*50-10*(1-a)-time1*(1-a)
                time1=0
        if (part==2):
            canvas.draw_circle([x-time1*0.3,y+0.3*time1**1.2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time1/250)+")")
            canvas.draw_circle([x+time1*0.3,y+0.3*time1**1.2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time1/250)+")")

            canvas.draw_circle([x-time1*0.5,y+0.3*time1**1.15-0.3*time1],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time1/250)+")")
            canvas.draw_circle([x+time1*0.5,y+0.3*time1**1.15-0.3*time1],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time1/250)+")")

            canvas.draw_circle([x-time1*0.3,y+0.3*time1**1.2-time1],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time1/250)+")")
            canvas.draw_circle([x+time1*0.3,y+0.3*time1**1.2-time1],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time1/250)+")")

            if (time1>250):
                part=1
                time1=0
                h=random.randint(0,200000)
        time2=time2+5
        random.seed(h2)
        if (part2==1):
            a2=random.uniform(-0.16,0.16)
            x2=random.randint(30,len(level[0][0])*50-30)
            canvas.draw_line([x2-3*a2+time2*a2,len(level[0])*50+3*(1-a2)-time2*(1-a2)],[x2+time2*a2,len(level[0])*50-time2*(1-a2)],1,"orange")
            canvas.draw_line([x2+time2*a2,len(level[0])*50-time2*(1-a2)],[x2+10*a2+time2*a2,len(level[0])*50-10*(1-a2)-time2*(1-a2)],3,"black")
            canvas.draw_circle([x2+10*a2+time2*a2,len(level[0])*50-10*(1-a2)-time2*(1-a2)],1.5,0.1,"black","black")
            if (time2>random.randint(len(level[0])*30,len(level[0])*45)):
                part2=2
                x2=x2+10*a2+time2*a2
                y2=len(level[0])*50-10*(1-a2)-time2*(1-a2)
                time2=0
        if (part2==2):
            canvas.draw_circle([x2-time2*0.3,y2+0.3*time2**1.2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time2/250)+")")
            canvas.draw_circle([x2+time2*0.3,y2+0.3*time2**1.2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time2/250)+")")

            canvas.draw_circle([x2-time2*0.5,y2+0.3*time2**1.15-0.3*time2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time2/250)+")")
            canvas.draw_circle([x2+time2*0.5,y2+0.3*time2**1.15-0.3*time2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time2/250)+")")

            canvas.draw_circle([x2-time2*0.3,y2+0.3*time2**1.2-time2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time2/250)+")")
            canvas.draw_circle([x2+time2*0.3,y2+0.3*time2**1.2-time2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time2/250)+")")


            if (time2>250):
                part2=1
                time2=0
                h2=random.randint(0,200000)
                
        time3=time3+5
        random.seed(h3)
        if (part3==1):
            a3=random.uniform(-0.16,0.16)
            x3=random.randint(30,len(level[0][0])*50-30)
            canvas.draw_line([x3-3*a3+time3*a3,len(level[0])*50+3*(1-a3)-time3*(1-a3)],[x3+time3*a3,len(level[0])*50-time3*(1-a3)],1,"orange")
            canvas.draw_line([x3+time3*a3,len(level[0])*50-time3*(1-a3)],[x3+10*a3+time3*a3,len(level[0])*50-10*(1-a3)-time3*(1-a3)],3,"black")
            canvas.draw_circle([x3+10*a3+time3*a3,len(level[0])*50-10*(1-a3)-time3*(1-a3)],1.5,0.1,"black","black")
            if (time3>random.randint(len(level[0])*30,len(level[0])*45)):
                part3=2
                x3=x3+10*a3+time3*a3
                y3=len(level[0])*50-10*(1-a3)-time3*(1-a3)
                time3=0
        if (part3==2):
            canvas.draw_circle([x3-time3*0.3,y3+0.3*time3**1.2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time3/250)+")")
            canvas.draw_circle([x3+time3*0.3,y3+0.3*time3**1.2],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time3/250)+")")

            canvas.draw_circle([x3-time3*0.5,y3+0.3*time3**1.15-0.3*time3],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time3/250)+")")
            canvas.draw_circle([x3+time3*0.5,y3+0.3*time3**1.15-0.3*time3],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time3/250)+")")

            canvas.draw_circle([x3-time3*0.3,y3+0.3*time3**1.2-time3],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time3/250)+")")
            canvas.draw_circle([x3+time3*0.3,y3+0.3*time3**1.2-time3],5,0.1,"rgb(0,0,0,0)","rgb("+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(random.randint(100,255))+","+str(1-time3/250)+")")


            if (time3>250):
                part3=1
                time3=0
                h3=random.randint(0,200000)
    if (note>0):
        note=note-1
        canvas.draw_text("close back window^",[-250+len(level[0][0])*50,30],30,"rgb(255,255,255,"+str(note/50)+")")
        canvas.draw_text("to reduce lag",[-250+len(level[0][0])*50,60],30,"rgb(255,255,255,"+str(note/50)+")")
def push(i,r,c,l,p,q):
    global level,value,rules,instance
    level[i][r+p][c+q][l][2]=3			#change when adding move rule
    if (p>0):
        p2=1
    elif (p==0):
        p2=0
    elif (p<0):
        p2=-1
    if (q>0):
        q2=1
    elif (q==0):
        q2=0
    elif (q<0):
        q2=-1
    if ((p==-1 and q==0 and r+p>0) or (p==0 and q==1 and c+q<len(level[i][r+p])-1) or (p==1 and q==0 and r+p<len(level[i])-1) or (p==0 and q==-1 and c+q>0)):
        i2=instance
        while (level[i2][r+p+p2][c+q+q2]==[[]]):
            i2=i2-1
        value=0
        pushval=[]
        for layer in range(len(level[i2][r+p+p2][c+q+q2])):
            if (len(level[i2][r+p+p2][c+q+q2][layer])>2):
                if ((p==-1 and q==0 and r+p>0) or (p==0 and q==1 and c+q<len(level[i][r+p])-1) or (p==1 and q==0 and r+p<len(level[i])-1) or (p==0 and q==-1 and c+q>0)):
                    if ((level[i2][r+p+p2][c+q+q2][layer][0] in rules[2]) and ((level[i2][r+p+p2][c+q+q2][layer][0] not in rules[3]) and (type(level[i2][r+p+p2][c+q+q2][layer][0])!=str)) and not((level[i2][r+p+p2][c+q+q2][layer][0] in rules[8] and level[i][r+p][c+q][layer][0] in rules[9]) or (level[i2][r+p+p2][c+q+q2][layer][0] in rules[9] and level[i][r+p][c+q][layer][0] in rules[8]))):
                        value=3
                    elif ((level[i2][r+p+p2][c+q+q2][layer][0] in rules[3]) or (type(level[i2][r+p+p2][c+q+q2][layer][0])==str) and value==0):
                        value=0
                        pushval.append([i2,r+p,c+q,layer,p2,q2])
                else:
                    value=3
        if (value==0):
            for n in range(len(pushval)):
                push(pushval[n][0],pushval[n][1],pushval[n][2],pushval[n][3],pushval[n][4],pushval[n][5])
    else:
        value=3
    if (value==3):
        level[i][r+p][c+q][l][2]=0
def key_handler(key):
    global level,instance,rules,win,value,particle,ppos,hp,compression
    #38 = up   |   40 = down   |   39 = right   |   37 = left   |   32 = space   |   82 = r   |   90 = z   |   67 = c
    #87 = W   |   65 = A   |   83 = S   |   68 = D
    move=-1
    if ((key==38 or key==87) and win==0):
        move=1
        v1=-1
        v2=0
    elif ((key==39 or key==68) and win==0):
        move=2
        v1=0
        v2=1
    elif ((key==40 or key==83) and win==0):
        move=3
        v1=1
        v2=0
    elif ((key==37 or key==65) and win==0):
        move=4
        v1=0
        v2=-1
    elif (key==90 and instance!=0):
        print (level.pop())
        instance=instance-1
        win=0
        def_rules()
    elif (key==82 and instance!=0):
        temp=level[0]
        level=[]
        level.append(temp)
        instance=0
        win=0
        def_rules()
    elif (key==32 and win==0):
        move=0
    if (move!=-1):
        def_rules(a=1)
        move_rule=0
        if (rules[11]!=[]):
            move_rule=1
        level.append([])
        for o in range(len(level[instance])):
            level[instance+1].append([])
            for p in range(len(level[instance][0])):
                level[instance+1][o].append([[]])
        for r in range(len(level[instance])):
            for c in range(len(level[instance][r])):
                i=instance
                while (level[i][r][c]==[[]]):
                    i=i-1
                value=-1
                stop=0
                for l in range(len(level[i][r][c])):
                    if (level[i][r][c][l][0] in rules[0] or (-1 in rules[0] and type(level[i][r][c][l][0])==str)):			#you_rule
                        if ((move==1 and r>0) or (move==2 and c<len(level[i][r])-1) or (move==3 and r<len(level[i])-1) or (move==4 and c>0)):					#movement check
                            value=0
                            i2=instance
                            while (level[i2][r+v1][c+v2]==[[]]):
                                i2=i2-1
                            for layer in range (len(level[i2][r+v1][c+v2])):
                                if (((level[i2][r+v1][c+v2][layer][0] in rules[2]) or (type(level[i2][r+v1][c+v2][layer][0])==str)) and not((level[i2][r+v1][c+v2][layer][0] in rules[8] and level[i][r][c][l][0] in rules[9]) or (level[i2][r+v1][c+v2][layer][0] in rules[9] and level[i][r][c][l][0] in rules[8]))):
                                    value=2 							#stop_rule
                                    if ((level[i2][r+v1][c+v2][layer][0] not in rules[3]) and (type(level[i2][r+v1][c+v2][layer][0])!=str)):
                                        stop=1
                            for layer in range (len(level[i2][r+v1][c+v2])):
                                if (((level[i2][r+v1][c+v2][layer][0] in rules[3]) or (type(level[i2][r+v1][c+v2][layer][0])==str)) and stop==0):    #push_rule
                                    push(i2,r,c,layer,v1,v2)                            
                if (value==0 and stop==0):                               #movement flag set
                    for layer in range(len(level[i][r][c])):
                        if (len(level[i][r][c][layer])>2):
                            if (level[i][r][c][layer][2]!=3):
                                if (level[i][r][c][layer][0] in rules[0] or (-1 in rules[0] and type(level[i][r][c][l][0])==str)):
                                    level[i][r][c][layer][2]=1
                                else:
                                    level[i][r][c][layer][2]=0
                else:
                    for layer in range(len(level[i][r][c])):
                        if (len(level[i][r][c][layer])>2):
                            if (level[i][r][c][layer][2]!=3):
                                level[i][r][c][layer][2]=0
        for r in range(len(level[instance])):
            for c in range(len(level[instance][r])):
                i=instance
                while (level[i][r][c]==[[]]):
                    i=i-1
                value=-1
                stop=0
                for l in range(len(level[i][r][c])):
                    if (len(level[i][r][c][l])>2):
                        if ((level[i][r][c][l][0] in rules[0] or (-1 in rules[0] and type(level[i][r][c][l][0])==str)) or level[i][r][c][l][2]==3):			#you_rule
                            if ((move==1 and r>0) or (move==2 and c<len(level[i][r])-1) or (move==3 and r<len(level[i])-1) or (move==4 and c>0)):					#movement check
                                value=0
                                i2=instance
                                while (level[i2][r+v1][c+v2]==[[]]):
                                    i2=i2-1
                                for layer in range (len(level[i2][r+v1][c+v2])):
                                    if (((level[i2][r+v1][c+v2][layer][0] in rules[2]) or (type(level[i2][r+v1][c+v2][layer][0])==str)) and not((level[i2][r+v1][c+v2][layer][0] in rules[8] and level[i][r][c][l][0] in rules[9]) or (level[i2][r+v1][c+v2][layer][0] in rules[9] and level[i][r][c][l][0] in rules[8]))):    #stop_rule
                                        if (level[i2][r+v1][c+v2][layer][2]!=3 and level[i2][r+v1][c+v2][layer][2]!=1):
                                            value=2
                                            stop=1
                                        if ((level[i2][r+v1][c+v2][layer][0] not in rules[3]) and (type(level[i2][r+v1][c+v2][layer][0])!=str)):
                                            stop=1
                            else:
                                stop=1
                if (stop==1 and move!=0):
                    level[instance+1][r][c].append([level[i][r][c][layer][0],move,level[i][r][c][layer][2]])
                if (value==0 and stop==0):                               #movement
                    i3=instance
                    while (level[i3][r+v1][c+v2]==[[]]):
                        i3=i3-1
                    for layer in range(len(level[i3][r+v1][c+v2])):
                        if (len(level[i3][r+v1][c+v2][layer])>2):
                            if (level[i3][r+v1][c+v2][layer][2]==0):      #movement flag check
                                level[instance+1][r+v1][c+v2].append(level[i3][r+v1][c+v2][layer])
                                level[i3][r+v1][c+v2][layer][2]=2
                        else:
                            level[instance+1][r+v1][c+v2].append(level[i3][r+v1][c+v2][layer])
                    for layer in range(len(level[i][r][c])):
                        if ((level[i][r][c][layer][0] in rules[0] or (-1 in rules[0] and type(level[i][r][c][layer][0])==str)) or level[i][r][c][layer][2]==3):
                            level[instance+1][r+v1][c+v2].append([level[i][r][c][layer][0],move,level[i][r][c][layer][2]])
                            if (level[instance+1][r][c]==[[]]):
                                level[instance+1][r][c]=[[0]]
                        else:
                            if (len(level[i][r][c][layer])>2):
                                if (level[i][r][c][layer][2]!=2):
                                    level[instance+1][r][c].append(level[i][r][c][layer])
                                    level[i][r][c][layer][2]=2
                elif (instance%10==9):
                    for layer in range(len(level[i][r][c])):
                        if (len(level[i][r][c][layer])>2):
                            if (level[i][r][c][layer][2]!=2):
                                level[instance+1][r][c].append(level[i][r][c][layer])
                                level[i][r][c][layer][2]=2
                        elif (len(level[i][r][c])==1):
                            level[instance+1][r][c].append([0])
                            level[instance+1][r][c].remove([])
        instance=instance+1
        execute_rules()
    print ("instance "+str(instance))
    def_rules()
def layer_cleanup():
    global level,instance
    for r in range(len(level[instance])):
        for c in range(len(level[instance][r])):
            val=-1
            if (len(level[instance][r][c])>1):
                while (len(level[instance][r][c])>1 and val!=0):
                    val=0
                    for l in range(len(level[instance][r][c])):
                        if (level[instance][r][c][l]==[]):
                            val=1
                        elif (level[instance][r][c][l]==[0]):
                            val=2
                    if (val==1):
                        level[instance][r][c].remove([])
                    elif (val==2):
                        level[instance][r][c].remove([0])
def execute_rules():
    global level,instance,rules,win,value,particle,ppos,hp,compression
    layer_cleanup()
    def_rules()
    for o in range (-1,21):							#conversion
        if o not in rules[11][o]:
            for r in range(len(level[instance])):
                for c in range(len(level[instance][r])):
                    i=instance
                    while (level[i][r][c]==[[]]):
                        i=i-1
                    temp=level[i][r][c]
                    for l in range(len(temp)):
                        if (i!=instance):
                            if (level[i][r][c][l][0]==o or (o==-1 and type(temp[l][0])==str)):
                                if (rules[11][o][0]==-1):
                                    level[instance][r][c].append([str(level[i][r][c][l][0]),level[i][r][c][l][1],level[i][r][c][l][2]])
                                else:
                                    level[instance][r][c].append([rules[11][o][0],level[i][r][c][l][1],level[i][r][c][l][2]])
                                if (len(rules[11][o])>1):
                                    for m in range (1,len(rules[11][o])):
                                        if (rules[11][o][m]==-1):
                                            level[instance][r][c].append([str(temp[l][0]),1,0])
                                        else:
                                            level[instance][r][c].append([rules[11][o][m],1,0])
                            else:
                                level[instance][r][c].append(level[i][r][c][l]) 
                        else:
                            if (temp[l][0]==o or (o==-1 and type(temp[l][0])==str)):
                                if (rules[11][o][0]==-1):
                                    level[instance][r][c].append([str(temp[l][0]),1,0])
                                else:
                                    level[instance][r][c].append([rules[11][o][0],1,0])
                                level[instance][r][c].remove(temp[l])
                                if (len(rules[11][o])>1):
                                    for m in range (1,len(rules[11][o])):
                                        if (rules[11][o][m]==-1):
                                            level[instance][r][c].append([str(temp[l][0]),1,0])
                                        else:
                                            level[instance][r][c].append([rules[11][o][m],1,0])
            layer_cleanup()
    def_rules(a=1)
    ppos=[]
    for r in range(len(level[instance])):			#rule application
        for c in range(len(level[instance][r])):
            if ([r,c] not in compression):
                i=instance
                while (level[i][r][c]==[[]]):
                    i=i-1
                value=[]
                if (len(level[i][r][c])>1): #lag reduction
                    for l in range(len(level[i][r][c])):
                        value.append([])
                        if (level[i][r][c][l][0] in rules[10] or (type(level[i][r][c][l][0])==str and -1 in rules[10])): #float
                            value[l].append(10)
                        if (level[i][r][c][l][0] in rules[0] or (type(level[i][r][c][l][0])==str and -1 in rules[0])):	#you
                            value[l].append(0)
                        if (level[i][r][c][l][0] in rules[1] or (type(level[i][r][c][l][0])==str and -1 in rules[1])):	#win
                            value[l].append(1)
                        if (level[i][r][c][l][0] in rules[4] or (type(level[i][r][c][l][0])==str and -1 in rules[4])):	#defeat
                            value[l].append(4)
                        if (level[i][r][c][l][0] in rules[5] or (type(level[i][r][c][l][0])==str and -1 in rules[5])):	#sink
                            value[l].append(5)
                        if (level[i][r][c][l][0] in rules[6] or (type(level[i][r][c][l][0])==str and -1 in rules[6])):	#hot
                            value[l].append(6)
                        if (level[i][r][c][l][0] in rules[7] or (type(level[i][r][c][l][0])==str and -1 in rules[7])):	#melt
                            value[l].append(7)
                        if (level[i][r][c][l][0] in rules[8] or (type(level[i][r][c][l][0])==str and -1 in rules[8])):	#open
                            value[l].append(8)
                        if (level[i][r][c][l][0] in rules[9] or (type(level[i][r][c][l][0])==str and -1 in rules[9])):	#shut
                            value[l].append(9)
                    for o in range(len(value)):
                        for k in range(len(value)):
                            if ((10 in value[o] and 10 in value[k]) or (10 not in value[o] and 10 not in value[k])):
                                if (5 in value[o] and -1 not in value[o] and -1 not in value[k] and k!=o): #sink
                                    value[o].append(-1)
                                    value[k].append(-1)
                                if (8 in value[o] and 9 in value[k] and -1 not in value[o] and -1 not in value[k]): #open/shut
                                    value[o].append(-1)
                                    value[k].append(-1)
                                if (0 in value[o] and 4 in value[k] and -1 not in value[o] and -1 not in value[k]): #you/defeat
                                    value[o].append(-1)
                                if (7 in value[o] and 6 in value[k] and -1 not in value[o] and -1 not in value[k]): #melt/hot
                                    value[o].append(-1)
                    for o in range(len(value)-1,-1,-1):
                        if (i==instance):
                            if (-1 in value[o]):
                                level[i][r][c].pop(o)
                                value.pop(o)
                                ppos.append([r,c])
                                particle=0
                                hp=random.randint(0,200000)
                                if (len(level[i][r][c])<1):
                                    level[i][r][c].append([0])
                        else:
                            if (-1 in value[o]):
                                value.pop(o)
                                ppos.append([r,c])
                                particle=0
                                hp=random.randint(0,200000)
                                level[instance][r][c].append([0])
                            else:
                                level[instance][r][c].append(level[i][r][c][o])
                    if (i!=instance and len(level[instance][r][c])>1):
                        level[instance][r][c].reverse()
                    for o in range(len(value)):
                        for k in range(len(value)):
                            if ((10 in value[o] and 10 in value[k]) or (10 not in value[o] and 10 not in value[k])):
                                if (0 in value[o] and 1 in value[k]): #you/win
                                    win=1
                    layer_cleanup()
                elif (level[i][r][c][0][0]!=0):
                    if (level[i][r][c][0][0] in rules[0]):
                        for o in range(len(rules[0])):
                            if (rules[0][o] in rules[4]): #you/defeat
                                level[i][r][c].pop()
                                level[i][r][c].append([0])
                    if (level[i][r][c][0][0] in rules[7]):
                        for o in range(len(rules[7])):
                            if (rules[7][o] in rules[6]): #melt/hot
                                level[i][r][c].pop()
                                level[i][r][c].append([0])
                    if (level[i][r][c][0][0] in rules[8]):
                        for o in range(len(rules[8])):
                            if (rules[8][o] in rules[9]): #open/shut
                                level[i][r][c].pop()
                                level[i][r][c].append([0])
                    if (level[i][r][c][0][0] in rules[1]):
                        for o in range(len(rules[1])):
                            if (rules[1][o] in rules[0]): #you/win
                                win=1
frame = simplegui.create_frame('Game Is You', len(level[0][0])*50, len(level[0])*50)
frame.set_canvas_background('gray')
inp = frame.add_input('Level Code (hit enter for code or paste to load)', input_handler,200)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler)
frame.start()
