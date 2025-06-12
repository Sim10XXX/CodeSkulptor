import simplegui
import math
#level[row][column][layer][0=type,1=face,2=movement flag]
level=[[[["1",1,0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[["21",1,0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[["31",1,0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]],
       [[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]],[[0]]]]
cursorx=0
cursory=0
id=1
compass=-1
ids=[0,1,2,3,4,5,6,"-1","1","2","3","4","5","6","21","31","32","33","34","35","36","37","38","39","40","41","42"]
idsmax=[6,"42",0,"-1"]
facing=1
note=0
def input_handler(code):
    global level,note
    if (len(code)>5):
        level=[]
        r=-1
        c=-1
        l=-1
        s=-1
        for x in range(len(code)):
            if (code[x]=="."):
                s=s+1
                level[r][c][l].append(0)
            elif (code[x]=="'"):
                s=-1
                l=l+1
                level[r][c].append([])
            elif (code[x]==","):
                l=-1
                c=c+1
                level[r].append([])
            elif (code[x]=="|"):
                c=-1
                r=r+1
                level.append([])
            else:
                if (ord(code[x])>=68):
                    level[r][c][l][s]=str(ord(code[x])-69)
                else:
                    level[r][c][l][s]=ord(code[x])-48
        frame = simplegui.create_frame('Game Is You Level Editor', len(level[0])*50+200, len(level)*50)
        frame.set_canvas_background('gray')
        inp = frame.add_input('Level Code (hit enter for code or paste to load)', input_handler,200)
        frame.set_draw_handler(draw_handler)
        frame.set_keydown_handler(key_handler)
        frame.set_mouseclick_handler(mouse_handler)
        button1 = frame.add_button('Add Row', Ar)
        button2 = frame.add_button('Add Column', Ac)
        button3 = frame.add_button('Delete Row', Dr)
        button4 = frame.add_button('Delete Column', Dc)
        frame.start()
        note=200
    else:
        for r in range(len(level)):
            print ("|",end="")
            for c in range(len(level[r])):
                print (",",end="")
                for l in range(len(level[r][c])):
                    print ("'",end="")
                    for s in range(len(level[r][c][l])):
                        print (".",end="")
                        if (type(level[r][c][l][s])==int):
                            print (chr(level[r][c][l][s]+48),end="")
                        else:
                            print (chr(int(level[r][c][l][s])+69),end="")
        print ("")
        print ("")

def draw_handler(canvas):
    global level,cursorx,cursory,id,facing,note,compass
    #print (rules)
    canvas.draw_line([100+len(level[0])*50,0],[100+len(level[0])*50,len(level)*50],200,"orange")
    canvas.draw_text("Preview:",[10+len(level[0])*50,30],30,"black")
    canvas.draw_text("Id: "+str(id),[10+len(level[0])*50,60],25,"black")
    canvas.draw_text("Toggle Text Id:",[10+len(level[0])*50,90],25,"black")
    canvas.draw_line([170+len(level[0])*50,85],[190+len(level[0])*50,85],20,"gray")
    if (type(id)==str):
        canvas.draw_line([174+len(level[0])*50,85],[186+len(level[0])*50,85],12,"lime")
    canvas.draw_line([165+len(level[0])*50,10],[165+len(level[0])*50,60],50,"gray")
    canvas.draw_line([87.5+len(level[0])*50,40],[87.5+len(level[0])*50,60],20,"gray")
    canvas.draw_line([115+len(level[0])*50,40],[115+len(level[0])*50,60],20,"gray")
    canvas.draw_polygon([[91+len(level[0])*50,45],[83.5+len(level[0])*50,50],[91+len(level[0])*50,55]],4,"lime","lime")
    canvas.draw_polygon([[111.5+len(level[0])*50,45],[119+len(level[0])*50,50],[111.5+len(level[0])*50,55]],4,"lime","lime")
    canvas.draw_line([10+len(level[0])*50,115],[90+len(level[0])*50,115],30,"gray")
    canvas.draw_text("place",[20+len(level[0])*50,121],25,"lime")
    canvas.draw_line([110+len(level[0])*50,115],[190+len(level[0])*50,115],30,"gray")
    canvas.draw_text("place on top",[113+len(level[0])*50,120],15,"lime")

    canvas.draw_line([10+len(level[0])*50,150],[90+len(level[0])*50,150],30,"gray")
    canvas.draw_text("delete",[17.5+len(level[0])*50,157.5],25,"lime")
    canvas.draw_line([110+len(level[0])*50,150],[190+len(level[0])*50,150],30,"gray")
    canvas.draw_text("delete top",[120+len(level[0])*50,155],15,"lime")

    canvas.draw_line([10+len(level[0])*50,185],[90+len(level[0])*50,185],30,"gray")
    canvas.draw_text("cycle layer",[11+len(level[0])*50,190],17.5,"lime")
    
    canvas.draw_text("facing:",[110+len(level[0])*50,180],16,"black")
    canvas.draw_line([180+len(level[0])*50,170],[180+len(level[0])*50,190],20,"gray")
    if (facing==1):
        canvas.draw_polygon([[175+len(level[0])*50,184],[180+len(level[0])*50,176.5],[185+len(level[0])*50,184]],4,"lime","lime")
    elif (facing==2):
        canvas.draw_polygon([[176.5+len(level[0])*50,175],[184+len(level[0])*50,180],[176.5+len(level[0])*50,185]],4,"lime","lime")
    elif (facing==3):
        canvas.draw_polygon([[175+len(level[0])*50,176.5],[180+len(level[0])*50,184],[185+len(level[0])*50,176.5]],4,"lime","lime")
    elif (facing==4):
        canvas.draw_polygon([[184+len(level[0])*50,175],[176.5+len(level[0])*50,180],[184+len(level[0])*50,185]],4,"lime","lime")
    canvas.draw_text("# of layers:"+str(len(level[cursory][cursorx])),[97.5+len(level[0])*50,199],14,"black")
    
    if (id!=0):
        if (id==1):
            canvas.draw_circle([25+140+len(level[0])*50,25+10],20,5,"red")
            canvas.draw_line([6+140+len(level[0])*50,10],[6+140+len(level[0])*50,12+10],12,"red")
            canvas.draw_line([6+140+len(level[0])*50,50+10],[6+140+len(level[0])*50,38+10],12,"red")
            canvas.draw_line([44+140+len(level[0])*50,50+10],[44+140+len(level[0])*50,38+10],12,"red")
            canvas.draw_line([44+140+len(level[0])*50,10],[44+140+len(level[0])*50,12+10],12,"red")
        elif (id==2):
            canvas.draw_arc([25+140+len(level[0])*50,10],45,1.05,2.07,10,"green")
            canvas.draw_arc([140+len(level[0])*50,43+10],45,5.25,6.29,10,"green")
            canvas.draw_arc([50+140+len(level[0])*50,43+10],45,3.15,4.2,10,"green")
        elif (id==3):
            canvas.draw_line([10+140+len(level[0])*50,45+10],[16+140+len(level[0])*50,5+10],5,"yellow")
            canvas.draw_circle([10+140+len(level[0])*50,45+10],2,1,"yellow","yellow")
            canvas.draw_circle([16+140+len(level[0])*50,5+10],2,1,"yellow","yellow")
            canvas.draw_line([12+140+len(level[0])*50,14+10],[38.67+140+len(level[0])*50,18+10],15,"yellow")
        elif (id==4):
            canvas.draw_arc([140+len(level[0])*50,10],23,0.1,1.47,10,"blue")
            canvas.draw_arc([50+140+len(level[0])*50,10],23,1.67,3.04,10,"blue")
            canvas.draw_arc([140+len(level[0])*50,50+10],23,4.81,-0.1,10,"blue")
            canvas.draw_arc([50+140+len(level[0])*50,50+10],23,3.24,4.61,10,"blue")
            canvas.draw_circle([25+140+len(level[0])*50,25+10],7,1,"blue","blue")
        elif (id==5):
            canvas.draw_line([25+140+len(level[0])*50,5+10],[25+140+len(level[0])*50,45+10],40,"black")
            canvas.draw_line([25+140+len(level[0])*50,10+10],[25+140+len(level[0])*50,40+10],30,"rgb(50,50,50)")
        elif (id==6):
            canvas.draw_circle([25+140+len(level[0])*50,20+10],15,8,"brown")
            canvas.draw_circle([17.5+140+len(level[0])*50,21+10],7,6,"brown")
            canvas.draw_circle([32.5+140+len(level[0])*50,21+10],7,6,"brown")
            canvas.draw_line([12+140+len(level[0])*50,13+10],[38+140+len(level[0])*50,13+10],14,"brown")
                        
            canvas.draw_line([17.5+140+len(level[0])*50,43+10],[17.5+140+len(level[0])*50,33+10],3,"brown")
            canvas.draw_line([22.5+140+len(level[0])*50,43+10],[22.5+140+len(level[0])*50,13+10],3,"brown")
            canvas.draw_line([27.5+140+len(level[0])*50,43+10],[27.5+140+len(level[0])*50,13+10],3,"brown")
            canvas.draw_line([32.5+140+len(level[0])*50,43+10],[32.5+140+len(level[0])*50,33+10],3,"brown")
        elif (id=="-1"):
            canvas.draw_text("t",[11+140+len(level[0])*50,23+10],30,"white")
            canvas.draw_text("e",[22+140+len(level[0])*50,23+10],30,"white")
            canvas.draw_text("x",[10+140+len(level[0])*50,45+10],30,"white")
            canvas.draw_text("t",[25+140+len(level[0])*50,45+10],30,"white")
        elif (id=="1"):
            canvas.draw_text("red",[5+140+len(level[0])*50,33+10],30,"red")
        elif (id=="2"):
            canvas.draw_text("gre",[5+140+len(level[0])*50,23+10],30,"green")
            canvas.draw_text("en",[10+140+len(level[0])*50,45+10],30,"green")
        elif (id=="3"):
            canvas.draw_text("f",[10+140+len(level[0])*50,23+10],30,"yellow")
            canvas.draw_text("l",[25+140+len(level[0])*50,23+10],30,"yellow")
            canvas.draw_text("ag",[10+140+len(level[0])*50,45+10],30,"yellow")
        elif (id=="4"):
            canvas.draw_text("blue",[0+140+len(level[0])*50,33+10],30,"blue")
        elif (id=="5"):
            canvas.draw_text("bla",[5+140+len(level[0])*50,23+10],30,"black")
            canvas.draw_text("ck",[10+140+len(level[0])*50,45+10],30,"black")
        elif (id=="6"):
            canvas.draw_text("sk",[10+140+len(level[0])*50,23+10],30,"brown")
            canvas.draw_text("ull",[7+140+len(level[0])*50,45+10],30,"brown")
        elif (id=="21"):
            canvas.draw_text("is",[15+140+len(level[0])*50,33+10],30,"white")
        elif (id=="31"):
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"pink")
            canvas.draw_text("you",[2+140+len(level[0])*50,33+10],30,"grey")
        elif (id=="32"):
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"yellow")
            canvas.draw_text("win",[2+140+len(level[0])*50,33+10],30,"grey")
        elif (id=="33"):
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"red")
            canvas.draw_text("s",[10+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("t",[25+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("op",[10+140+len(level[0])*50,45+10],30,"grey")
        elif (id=="34"):
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"rgb(100,75,50)")
            canvas.draw_text("pu",[10+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("sh",[10+140+len(level[0])*50,45+10],30,"grey")
        elif (id=="35"):
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"brown")
            canvas.draw_text("def",[5+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("eat",[5+140+len(level[0])*50,45+10],30,"grey")
        elif (id=="36"): #sink
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"cyan")
            canvas.draw_text("s",[10+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("i",[25+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("nk",[10+140+len(level[0])*50,45+10],30,"grey")
        elif (id=="37"): #hot
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"rgb(255,50,50)")
            canvas.draw_text("hot",[5+140+len(level[0])*50,33+10],30,"grey")
        elif (id=="38"): #melt
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"lightblue")
            canvas.draw_text("m",[8+140+len(level[0])*50,23+10],30,"grey","monospace")
            canvas.draw_text("e",[26+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("l",[10+140+len(level[0])*50,45+10],30,"grey")
            canvas.draw_text("t",[25+140+len(level[0])*50,45+10],30,"grey")
        elif (id=="39"): #open
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"lightyellow")
            canvas.draw_text("op",[10+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("en",[10+140+len(level[0])*50,45+10],30,"grey")
        elif (id=="40"): #shut
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"brown")
            canvas.draw_text("sh",[10+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("ut",[10+140+len(level[0])*50,45+10],30,"grey")
        elif (id=="41"): #float
            canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"rgb(240,240,255)")
            canvas.draw_text("f",[10+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("l",[25+140+len(level[0])*50,23+10],30,"grey")
            canvas.draw_text("oat",[5+140+len(level[0])*50,45+10],30,"grey")
        elif (id=="42"): #move
            canvas.draw_text("missing",[142+len(level[0])*50,40],15,"white")
            #canvas.draw_polygon([[14+140+len(level[0])*50,12.5+10],[36+140+len(level[0])*50,12.5+10],[37.5+140+len(level[0])*50,14+10],[37.5+140+len(level[0])*50,36+10],[36+140+len(level[0])*50,37.5+10],[14+140+len(level[0])*50,37.5+10],[12.5+140+len(level[0])*50,36+10],[12.5+140+len(level[0])*50,14+10]],25,"lightgreen")
            #canvas.draw_text("mo",[5+140+len(level[0])*50,23+10],30,"grey")
            #canvas.draw_text("ve",[10+140+len(level[0])*50,45+10],30,"grey")
        else:
            canvas.draw_text("missing",[142+len(level[0])*50,40],15,"white")
    for r in range(len(level)):
        for c in range(len(level[r])):
            for l in range(len(level[r][c])):
                #print (level[r][c],end="\t")
                if (level[r][c][l][0]!=0):
                    if (level[r][c][l][0]==1):
                        canvas.draw_circle([25+50*c,25+50*r],20,5,"red")
                        canvas.draw_line([6+50*c,50*r],[6+50*c,12+50*r],12,"red")
                        canvas.draw_line([6+50*c,50+50*r],[6+50*c,38+50*r],12,"red")
                        canvas.draw_line([44+50*c,50+50*r],[44+50*c,38+50*r],12,"red")
                        canvas.draw_line([44+50*c,50*r],[44+50*c,12+50*r],12,"red")
                    if (level[r][c][l][0]==2):
                        canvas.draw_arc([25+50*c,50*r],45,1.05,2.07,10,"green")
                        canvas.draw_arc([50*c,43+50*r],45,5.25,6.29,10,"green")
                        canvas.draw_arc([50+50*c,43+50*r],45,3.15,4.2,10,"green")
                    if (level[r][c][l][0]==3):
                        canvas.draw_line([10+50*c,45+50*r],[16+50*c,5+50*r],5,"yellow")
                        canvas.draw_circle([10+50*c,45+50*r],2,1,"yellow","yellow")
                        canvas.draw_circle([16+50*c,5+50*r],2,1,"yellow","yellow")
                        canvas.draw_line([12+50*c,14+50*r],[38.67+50*c,18+50*r],15,"yellow")
                    if (level[r][c][l][0]==4):
                        canvas.draw_arc([50*c,50*r],23,0.1,1.47,10,"blue")
                        canvas.draw_arc([50+50*c,50*r],23,1.67,3.04,10,"blue")
                        canvas.draw_arc([50*c,50+50*r],23,4.81,-0.1,10,"blue")
                        canvas.draw_arc([50+50*c,50+50*r],23,3.24,4.61,10,"blue")
                        canvas.draw_circle([25+50*c,25+50*r],7,1,"blue","blue")
                    if (level[r][c][l][0]==5):
                        canvas.draw_line([25+50*c,5+50*r],[25+50*c,45+50*r],40,"black")
                        canvas.draw_line([25+50*c,10+50*r],[25+50*c,40+50*r],30,"rgb(50,50,50)")
                    if (level[r][c][l][0]==6):
                        canvas.draw_circle([25+50*c,20+50*r],15,8,"brown")
                        canvas.draw_circle([17.5+50*c,21+50*r],7,6,"brown")
                        canvas.draw_circle([32.5+50*c,21+50*r],7,6,"brown")
                        canvas.draw_line([12+50*c,13+50*r],[38+50*c,13+50*r],14,"brown")
                        
                        canvas.draw_line([17.5+50*c,43+50*r],[17.5+50*c,33+50*r],3,"brown")
                        canvas.draw_line([22.5+50*c,43+50*r],[22.5+50*c,13+50*r],3,"brown")
                        canvas.draw_line([27.5+50*c,43+50*r],[27.5+50*c,13+50*r],3,"brown")
                        canvas.draw_line([32.5+50*c,43+50*r],[32.5+50*c,33+50*r],3,"brown")
                    if (level[r][c][l][0]=="-1"):
                        canvas.draw_text("t",[11+50*c,23+50*r],30,"white")
                        canvas.draw_text("e",[22+50*c,23+50*r],30,"white")
                        canvas.draw_text("x",[10+50*c,45+50*r],30,"white")
                        canvas.draw_text("t",[25+50*c,45+50*r],30,"white")
                    if (level[r][c][l][0]=="1"):
                        canvas.draw_text("red",[5+50*c,33+50*r],30,"red")
                    if (level[r][c][l][0]=="2"):
                        canvas.draw_text("gre",[5+50*c,23+50*r],30,"green")
                        canvas.draw_text("en",[10+50*c,45+50*r],30,"green")
                    if (level[r][c][l][0]=="3"):
                        canvas.draw_text("f",[10+50*c,23+50*r],30,"yellow")
                        canvas.draw_text("l",[25+50*c,23+50*r],30,"yellow")
                        canvas.draw_text("ag",[10+50*c,45+50*r],30,"yellow")
                    if (level[r][c][l][0]=="4"):
                        canvas.draw_text("blue",[0+50*c,33+50*r],30,"blue")
                    if (level[r][c][l][0]=="5"):
                        canvas.draw_text("bla",[5+50*c,23+50*r],30,"black")
                        canvas.draw_text("ck",[10+50*c,45+50*r],30,"black")
                    if (level[r][c][l][0]=="6"):
                        canvas.draw_text("sk",[10+50*c,23+50*r],30,"brown")
                        canvas.draw_text("ull",[7+50*c,45+50*r],30,"brown")
                    if (level[r][c][l][0]=="21"):
                        canvas.draw_text("is",[15+50*c,33+50*r],30,"white")
                    if (level[r][c][l][0]=="31"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"pink")
                        canvas.draw_text("you",[2+50*c,33+50*r],30,"grey")
                    if (level[r][c][l][0]=="32"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"yellow")
                        canvas.draw_text("win",[2+50*c,33+50*r],30,"grey")
                    if (level[r][c][l][0]=="33"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"red")
                        canvas.draw_text("s",[10+50*c,23+50*r],30,"grey")
                        canvas.draw_text("t",[25+50*c,23+50*r],30,"grey")
                        canvas.draw_text("op",[10+50*c,45+50*r],30,"grey")
                    if (level[r][c][l][0]=="34"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"rgb(100,75,50)")
                        canvas.draw_text("pu",[10+50*c,23+50*r],30,"grey")
                        canvas.draw_text("sh",[10+50*c,45+50*r],30,"grey")
                    if (level[r][c][l][0]=="35"):
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"brown")
                        canvas.draw_text("def",[5+50*c,23+50*r],30,"grey")
                        canvas.draw_text("eat",[5+50*c,45+50*r],30,"grey")
                    if (level[r][c][l][0]=="36"): #sink
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"cyan")
                        canvas.draw_text("s",[10+50*c,23+50*r],30,"grey")
                        canvas.draw_text("i",[25+50*c,23+50*r],30,"grey")
                        canvas.draw_text("nk",[10+50*c,45+50*r],30,"grey")
                    if (level[r][c][l][0]=="37"): #hot
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"rgb(255,50,50)")
                        canvas.draw_text("hot",[5+50*c,33+50*r],30,"grey")
                    if (level[r][c][l][0]=="38"): #melt
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"lightblue")
                        canvas.draw_text("m",[8+50*c,23+50*r],30,"grey","monospace")
                        canvas.draw_text("e",[26+50*c,23+50*r],30,"grey")
                        canvas.draw_text("l",[10+50*c,45+50*r],30,"grey")
                        canvas.draw_text("t",[25+50*c,45+50*r],30,"grey")
                    if (level[r][c][l][0]=="39"): #open
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"lightyellow")
                        canvas.draw_text("op",[10+50*c,23+50*r],30,"grey")
                        canvas.draw_text("en",[10+50*c,45+50*r],30,"grey")
                    if (level[r][c][l][0]=="40"): #shut
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"brown")
                        canvas.draw_text("sh",[10+50*c,23+50*r],30,"grey")
                        canvas.draw_text("ut",[10+50*c,45+50*r],30,"grey")
                    if (level[r][c][l][0]=="41"): #float
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"rgb(240,240,255)")
                        canvas.draw_text("f",[10+50*c,23+50*r],30,"grey")
                        canvas.draw_text("l",[25+50*c,23+50*r],30,"grey")
                        canvas.draw_text("oat",[5+50*c,45+50*r],30,"grey")
                    if (level[r][c][l][0]=="42"): #move
                        canvas.draw_polygon([[14+50*c,12.5+50*r],[36+50*c,12.5+50*r],[37.5+50*c,14+50*r],[37.5+50*c,36+50*r],[36+50*c,37.5+50*r],[14+50*c,37.5+50*r],[12.5+50*c,36+50*r],[12.5+50*c,14+50*r]],25,"lightgreen")
                        canvas.draw_text("mo",[5+50*c,23+50*r],30,"grey")
                        canvas.draw_text("ve",[10+50*c,45+50*r],30,"grey")
                    if (compass==1):
                        if (level[r][c][l][1]==1):
                            canvas.draw_line([43+50*c,43+50*r],[43+50*c,37+50*r],3,"rgb(25,25,25,0.8)")
                            canvas.draw_line([43+50*c,43+50*r],[43+50*c,37+50*r],2,"yellow")
                        if (level[r][c][l][1]==2):
                            canvas.draw_line([43+50*c,43+50*r],[49+50*c,43+50*r],3,"rgb(25,25,25,0.8)")
                            canvas.draw_line([43+50*c,43+50*r],[49+50*c,43+50*r],2,"yellow")
                        if (level[r][c][l][1]==3):
                            canvas.draw_line([43+50*c,43+50*r],[43+50*c,49+50*r],3,"rgb(25,25,25,0.8)")
                            canvas.draw_line([43+50*c,43+50*r],[43+50*c,49+50*r],2,"yellow")
                        if (level[r][c][l][1]==4):
                            canvas.draw_line([43+50*c,43+50*r],[37+50*c,43+50*r],3,"rgb(25,25,25,0.8)")
                            canvas.draw_line([43+50*c,43+50*r],[37+50*c,43+50*r],2,"yellow")
                        canvas.draw_circle([43+50*c,43+50*r],6,1.5,"rgb(25,25,25)")
    canvas.draw_polygon([[5+50*cursorx,5+50*cursory],[45+50*cursorx,5+50*cursory],[45+50*cursorx,45+50*cursory],[5+50*cursorx,45+50*cursory]],10,"rgb(255,255,0,0.65)")
    if (note>0):
        note=note-1
        canvas.draw_text("close back window^",[-50+len(level[0][0])*50,30],30,"rgb(255,255,255,"+str(note/50)+")")
        canvas.draw_text("to reduce lag",[-50+len(level[0][0])*50,60],30,"rgb(255,255,255,"+str(note/50)+")")
def key_handler(key):
    global level,cursorx,cursory,compass
    #38 = up   |   40 = down   |   39 = right   |   37 = left   |   32 = space   |   82 = r   |   90 = z
    #87 = W   |   65 = A   |   83 = S   |   68 = D
    if ((key==38 or key==87) and cursory>0):
        cursory=cursory-1
    elif ((key==39 or key==68) and cursorx<len(level[0])-1):
        cursorx=cursorx+1
    elif ((key==40 or key==83) and cursory<len(level)-1):
        cursory=cursory+1
    elif ((key==37 or key==65) and cursorx>0):
        cursorx=cursorx-1
    elif (key==67):
        compass=compass*-1

def mouse_handler(pos):
    global level,id,ids,idsmax,facing,cursorx,cursory
    x=pos[0]
    y=pos[1]
    if (y>=75 and y<=95 and x>=170+len(level[0])*50 and x<=190+len(level[0])*50):
        if (type(id)==str):
            id=int(id)
        else:
            id=str(id)
    elif (y>=40 and y<=60 and x>=77.5+len(level[0])*50 and x<=97.5+len(level[0])*50):
        if (type(id)==str):
            id=int(id)
            if (id>int(idsmax[3])):
                id=id-1
                while str(id) not in ids:
                    id=id-1
            else:
                id=idsmax[1]
            id=str(id)
        else:
            if (id>idsmax[2]):
                id=id-1
                while id not in ids:
                    id=id-1
            else:
                id=idsmax[0]
    elif (y>=40 and y<=60 and x>=105+len(level[0])*50 and x<=125+len(level[0])*50):
        if (type(id)==str):
            id=int(id)
            if (id<int(idsmax[1])):
                id=id+1
                while str(id) not in ids:
                    id=id+1
            else:
                id=idsmax[3]
            id=str(id)
        else:
            if (id<idsmax[0]):
                id=id+1
                while id not in ids:
                    id=id+1
            else:
                id=idsmax[2]
    elif (y>=100 and y<=130 and x>=10+len(level[0])*50 and x<=90+len(level[0])*50):
        level[cursory][cursorx]=[[id,facing,1]]
    elif (y>=100 and y<=130 and x>=110+len(level[0])*50 and x<=190+len(level[0])*50):
        level[cursory][cursorx].append([id,facing,1])
    elif (y>=135 and y<=165 and x>=10+len(level[0])*50 and x<=90+len(level[0])*50):
        level[cursory][cursorx]=[[0]]
    elif (y>=135 and y<=165 and x>=110+len(level[0])*50 and x<=190+len(level[0])*50):
        if (len(level[cursory][cursorx])>1):
            level[cursory][cursorx].pop()
        else:
            level[cursory][cursorx]=[[0]]
    elif (y>=170 and y<=200 and x>=10+len(level[0])*50 and x<=90+len(level[0])*50):
        level[cursory][cursorx].append(level[cursory][cursorx].pop(0))
    elif (y>=170 and y<=190 and x>=170+len(level[0])*50 and x<=190+len(level[0])*50):
        facing=facing+1
        if (facing==5):
            facing=1
        
def Ar():
    global level,note
    level.append([])
    for o in range(len(level[len(level)-2])):
        level[len(level)-1].append([[0]])
    frame = simplegui.create_frame('Game Is You Level Editor', len(level[0])*50+200, len(level)*50)
    frame.set_canvas_background('gray')
    inp = frame.add_input('Level Code (hit enter for code or paste to load)', input_handler,200)
    frame.set_draw_handler(draw_handler)
    frame.set_keydown_handler(key_handler)
    frame.set_mouseclick_handler(mouse_handler)
    button1 = frame.add_button('Add Row', Ar)
    button2 = frame.add_button('Add Column', Ac)
    button3 = frame.add_button('Delete Row', Dr)
    button4 = frame.add_button('Delete Column', Dc)
    frame.start()
    note=200
def Ac():
    global level,note
    for o in range(len(level)):
        level[o].append([[0]])
    frame = simplegui.create_frame('Game Is You Level Editor', len(level[0])*50+200, len(level)*50)
    frame.set_canvas_background('gray')
    inp = frame.add_input('Level Code (hit enter for code or paste to load)', input_handler,200)
    frame.set_draw_handler(draw_handler)
    frame.set_keydown_handler(key_handler)
    frame.set_mouseclick_handler(mouse_handler)
    button1 = frame.add_button('Add Row', Ar)
    button2 = frame.add_button('Add Column', Ac)
    button3 = frame.add_button('Delete Row', Dr)
    button4 = frame.add_button('Delete Column', Dc)
    frame.start()
    note=200
def Dr():
    global level,cursorx,cursory,note
    if (len(level)>4):
        cursorx=0
        cursory=0
        level.pop()
        frame = simplegui.create_frame('Game Is You Level Editor', len(level[0])*50+200, len(level)*50)
        frame.set_canvas_background('gray')
        inp = frame.add_input('Level Code (hit enter for save or paste to load)', input_handler,200)
        frame.set_draw_handler(draw_handler)
        frame.set_keydown_handler(key_handler)
        frame.set_mouseclick_handler(mouse_handler)
        button1 = frame.add_button('Add Row', Ar)
        button2 = frame.add_button('Add Column', Ac)
        button3 = frame.add_button('Delete Row', Dr)
        button4 = frame.add_button('Delete Column', Dc)
        frame.start()
        note=200
def Dc():
    global level,cursorx,cursory,note
    if (len(level[0])>4):
        cursorx=0
        cursory=0
        for o in range(len(level)):
            level[o].pop()
        frame = simplegui.create_frame('Game Is You Level Editor', len(level[0])*50+200, len(level)*50)
        frame.set_canvas_background('gray')
        inp = frame.add_input('Level Code (hit enter for code or paste to load)', input_handler,200)
        frame.set_draw_handler(draw_handler)
        frame.set_keydown_handler(key_handler)
        frame.set_mouseclick_handler(mouse_handler)
        button1 = frame.add_button('Add Row', Ar)
        button2 = frame.add_button('Add Column', Ac)
        button3 = frame.add_button('Delete Row', Dr)
        button4 = frame.add_button('Delete Column', Dc)
        frame.start()
        note=200
frame = simplegui.create_frame('Game Is You Level Editor', len(level[0])*50+200, len(level)*50)
frame.set_canvas_background('gray')
inp = frame.add_input('Level Code (hit enter for code or paste to load)', input_handler,200)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler)
frame.set_mouseclick_handler(mouse_handler)
button1 = frame.add_button('Add Row', Ar)
button2 = frame.add_button('Add Column', Ac)
button3 = frame.add_button('Delete Row', Dr)
button4 = frame.add_button('Delete Column', Dc)
frame.start()
