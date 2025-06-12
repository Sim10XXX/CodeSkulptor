#Click anywhere on the screen to shoot the oncoming enemies
#Every 4-5 rounds you can updrage either reload speed or damage per shot
#Enemies will insta-kill you upon touch
#You can also press "P" to pause
#Enemies increase in numbers and health over time
#Enemies with more health have a color shift to blue
#After round 4 one "buff" enemy spawns each round (marked with lime)
#They have half speed and double health

import simplegui
import random
import math

x=0			#}
y=0			#}Position of where you clicked with (0,0) being centered

x_slope=0	#}Vertical/horizontal movement of the bullet
y_slope=0	#}based on the x and y of the click

typ=0		#The quadrant where you clicked (ie. top-left) used
            #to determine if x_slope and/or y_slope should be negative

d=101		#bullet cooldown

p=0			#}
q=0			#}
p2=0		#}
q2=0		#}Uses x_slope and y_slope to draw the graphic of the bullet

shot1_x=0	#}
shot1_y=0	#}
shot2_x=0	#}
shot2_y=0	#}hitbox of the bullet
shot3_x=0	#}
shot3_y=0	#}

time=0		#Used to calculate the position of enemies
time_max=600# Discarded
min_time=50
game_time=0	#Total time passed
data=0		#Output of the enemy function
level=0		#The current level number
new_level=1	#This is true when all enemies are eliminated
level_count=1#Number of enemies in that round
pause=0		#Determines if the game is paused
lives=3

h=0			#Makes the enemy spawns random but controlled
c=0			#Determines which enemy to refer to (when there are multiple)
dead=list([1])#Stores the health data of each enemy
end=list([0])#list of 0's to determine when the above list is all 0's
f=0			#The value of the list "dead" at position c
hit=0		#hit is -1 when an enemy is shot
buff=-1		#determines which enemy becomes "buff"
health=0.01	#used to make the list "dead"
evasive=-1
equal_1=0
equal_2=0
hit_value=0
hit_value2=0
n_e=0

damage=1	#damage of shot
reload=40	#reload speed modifier (and projectile speed to compensate)
upgrade=0	#pauses the game to let the player choose an upgrade
multishot=0
multishot_first=1
berserk=1.00
color="black"
regen=0
rapidfire=0

help_screen=0
page=0
subpage=0
background="green"
help_val=0
sqrt_val=math.sqrt(300)
swapping=0

fire=0
water=0
ice=0
life=0
fire_v=list([0,0,0,0,0,0,0,0,0,0])
water_v=list([0,0,0,0,0,0,0,0,0,0])
ice_v=list([0,0,0,0,0,0,0,0,0,0])
life_v=list([0,0,0,0,0,0,0,0,0,0])
fire_c=0
water_c=0
ice_c=0
life_c=0
w_pressed=0
a_pressed=0
s_pressed=0
d_pressed=0

explode=0
explode_x=0
explode_y=0
fire2_v=0
burn=0

slow=0
knock=0
drain=0
drain_v=0
#temporary
#if (multishot==1):#
    #shot1_x=list([0,0,0])#
    #shot1_y=list([0,0,0])#
    #shot2_x=list([0,0,0])#
    #shot2_y=list([0,0,0])#
    #hit=list([0,0,0])#
p=list([0,0,0,0,0,0,0,0,0,0])
q=list([0,0,0,0,0,0,0,0,0,0])
p2=list([0,0,0,0,0,0,0,0,0,0])
q2=list([0,0,0,0,0,0,0,0,0,0])
x_slope=list([0,0,0,0,0,0,0,0,0,0])
y_slope=list([0,0,0,0,0,0,0,0,0,0])
shot1_x=list([0,0,0,0,0,0,0,0,0,0])
shot1_y=list([0,0,0,0,0,0,0,0,0,0])
shot2_x=list([0,0,0,0,0,0,0,0,0,0])
shot2_y=list([0,0,0,0,0,0,0,0,0,0])
hit=list([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
bersk=list([1,1,1,1,1,1,1,1,1,1])

if (multishot==1):
    vfn=0
    while (vfn<=4):
        p[vfn]=list([-100,-100,-100])
        q[vfn]=list([-100,-100,-100])
        p2[vfn]=list([-100,-100,-100])
        q2[vfn]=list([-100,-100,-100])
        shot1_x[vfn]=list([-100,-100,-100])
        shot1_y[vfn]=list([-100,-100,-100])
        shot2_x[vfn]=list([-100,-100,-100])
        shot2_y[vfn]=list([-100,-100,-100])
        hit[vfn]=list([0,0,0])
        vfn=vfn+1
def enemy(n):
    global f
    global c
    global buff
    global evasive
    global e_seed
    if (n==1 or 3):
        u=random.randint(0,700)
    elif (n==2 or 4):
        u=random.randint(0,1100)      
    if (c!=evasive):
        if (c==buff):
            speed=random.randint(1400*0.72,1600*0.72)
        else:
            speed=random.randint(750*0.72,850*0.72)
    else:
        speed=800*0.9
    if (f>0):
        global d
        global p
        global q
        global p2
        global q2
        global shot1_x
        global shot1_y
        global shot2_x
        global shot2_y
        global time
        global time_max
        global hit
        global hit_value
        global hit_value2
        global lives
        global multishot
        global multishot_first
        global n_e
        global explode_x
        global explode_y
        global fire_v
        global fire2_v
        global burn
        global ice_v
        global slow
        global water_v
        global knock
        global life_v
        global drain
        
#must travel 521 X-pixels to touch player or 321 Y-pixels
        burn=0
        if (n==1):
            x=(521/speed)*(time[c]-c*(100-level))-5
            y=u-(((u-350)/speed)*(time[c]-c*(100-level)))-5
            x2=x+10
            y2=y+10
        elif (n==2):
            x=u-(((u-550)/speed)*(time[c]-c*(100-level)))-5
            y=(321/speed)*(time[c]-c*(100-level))-5
            x2=x+10
            y2=y+10
        elif (n==3):
            x=(-521/speed)*(time[c]-c*(100-level))-5+1100
            y=u-(((u-350)/speed)*(time[c]-c*(100-level)))-5
            x2=x+10
            y2=y+10
        elif (n==4):
            x=u-(((u-550)/speed)*(time[c]-c*(100-level)))-5
            y=(-321/speed)*(time[c]-c*(100-level))-5+700
            x2=x+10
            y2=y+10
        if ((x2+10-explode_x)**2+(y2+10-explode_y)**2<=fire2_v**2):
            burn=1
        elif ((x-10-explode_x)**2+(y2+10-explode_y)**2<=fire2_v**2):
            burn=1
        elif ((x2+10-explode_x)**2+(y-10-explode_y)**2<=fire2_v**2):
            burn=1
        elif ((x-10-explode_x)**2+(y-10-explode_y)**2<=fire2_v**2):
            burn=1
        vfn=0
        while (vfn<=9):
            if (multishot==0 or multishot == -1):
                hitv=hit[vfn]
                fire_v_v=fire_v[vfn]
                ice_v_v=ice_v[vfn]
                water_v_v=water_v[vfn]
                life_v_v=life_v[vfn]
                if (hitv==0):
                    v1x=shot1_x[vfn]
                    v2x=shot2_x[vfn]
                    v1y=shot1_y[vfn]
                    v2y=shot2_y[vfn]
                    if (v1y > y-10 and v1y < y2+10 and v1x > x-10 and v1x < x2+10):
                        if (fire_v_v>=1):
                            explode_x=v1x
                            explode_y=v1y
                        if (ice_v_v>=1):
                            slow[c]=slow[c]+ice_v_v
                        if (water_v_v>=1):
                            knock[c]=water_v_v
                        if (life_v_v>=1):
                            drain[c]=life_v_v
                        shot1_x[vfn]=550
                        shot1_y[vfn]=350
                        shot2_x[vfn]=550
                        shot2_y[vfn]=350
                        if (c==evasive):
                            e_seed=random.randint(1,100000)
                            n_e=n
                        hit_value=vfn
                        print ("hit")
                        return "hit"
                    elif (v2y > y-10 and v2y < y2+10 and v2x > x-10 and v2x < x2+10):
                        if (fire_v_v>=1):
                            explode_x=v2x
                            explode_y=v2y
                        if (ice_v_v>=1):
                            slow[c]=slow[c]+ice_v_v
                        if (water_v_v>=1):
                            knock[c]=water_v_v
                        if (life_v_v>=1):
                            drain[c]=life_v_v
                        shot1_x[vfn]=550
                        shot1_y[vfn]=350
                        shot2_x[vfn]=550
                        shot2_y[vfn]=350
                        if (c==evasive):
                            e_seed=random.randint(1,100000)
                            n_e=n
                        hit_value=vfn
                        print ("hit")
                        return "hit"
            elif (multishot==1):
                val=0
                while (val<3):
                    hitv=hit[vfn][val]
                    if (hitv==0):
                        a1=shot1_x[vfn][val]
                        a2=shot2_x[vfn][val]
                        b1=shot1_y[vfn][val]
                        b2=shot2_y[vfn][val]
                        if (b1 > y-10 and b1 < y2+10 and a1 > x-10 and a1 < x2+10):
                            shot1_x[vfn][val]=550
                            shot1_y[vfn][val]=350
                            shot2_x[vfn][val]=550
                            shot2_y[vfn][val]=350
                            hit_value=vfn
                            hit_value2=val
                            if (c==evasive):
                                e_seed=random.randint(1,100000)
                                n_e=n
                            return "hit"
                        elif (b2 > y-10 and b2 < y2+10 and a2 > x-10 and a2 < x2+10):
                            shot1_x[vfn][val]=550
                            shot1_y[vfn][val]=350
                            shot2_x[vfn][val]=550
                            shot2_y[vfn][val]=350
                            hit_value=vfn
                            hit_value2=val
                            if (c==evasive):
                                e_seed=random.randint(1,100000)
                                n_e=n
                            return "hit"
                    val=val+1
            vfn=vfn+1
        if (time[c]-c*(100-level) >= speed):
            if (lives>0):
                lives=lives-1
                dead[c]=0
            else:
                print (0/0)
        return([[x,y],[x,y2],[x2,y2],[x2,y]],20,"rgb("+str(255-(dead[c]*16))+",0,"+str(dead[c]*16)+")")
    
def draw_handler(canvas):
    
    global x_slope
    global y_slope
    global typ
    global d
    global p
    global q
    global p2
    global q2
    global shot1_x
    global shot1_y
    global shot2_x
    global shot2_y
    global game_time
    global lives
    global time
    global time_max
    global min_time
    global data
    global level
    global new_level
    global h
    global c
    global dead
    global end
    global f
    global hit
    global hit_value
    global hit_value2
    global n_e
    global buff
    global evasive
    global health
    global level_count
    global damage
    global reload
    global upgrade
    global equal_1
    global equal_2
    global pause
    global multishot
    global berserk
    global bersk
    global color
    global e_seed
    global help_screen
    global page
    global subpage
    global background
    global help_val
    global sqrt_val
    global swapping
    global fire
    global water
    global ice
    global life
    global fire_v
    global water_v
    global ice_v
    global life_v
    global fire_c
    global water_c
    global ice_c
    global life_c
    global explode
    global explode_x
    global explode_y
    global fire2_v
    global burn
    global slow
    global knock
    global drain
    global drain_v
    if (help_screen==1 and background=="white"):
        canvas.draw_line([0,350],[1100,350],999,"white")
    if (upgrade==0 and pause==0):
        #Enemies:
    
        if (game_time>=min_time and game_time<min_time+time_max):
            if (new_level==1):
                n_e=0
                level=level+1
                a=random.randint(-1-equal_2,2+equal_1)
                if (level > 1):
                    if (a<=0):
                        if (level>5):
                            level_count=level_count+random.uniform(1,1/level+0.35)
                        else:
                            level_count=level_count+1
                        equal_1=equal_1+1
                        equal_2=0
                    else:
                        if (level>50):
                            health=health+random.uniform(0.5,0.3)
                            if (level_count>5):
                                level_count=level_count-1
                                health=health+1
                        elif (level>5):
                            health=health+random.uniform(0.5,0.5/level+0.125)
                        else:
                            health=health+0.5
                        equal_2=equal_2+1
                        equal_1=0
                print ("Health: "+str(health))
                print ("Count: "+str(level_count))
                print ("")
                if (level > 4):
                    buff=random.randint(0,int(level_count-1))
                if (level > 12):
                    evasive=random.randint(0,int(level_count-1))
                    while (buff==evasive):
                        buff=random.randint(0,int(level_count-1))
                time_max=4000+100*level
                new_level=0
                #if (berserk>=2):
                    #berserk=1+berserk/100
                if (level%5==0):
                    upgrade=1
                    if (level%2==0):
                        upgrade=3
                        if (level%20==10):###########################################################################
                            upgrade=2
                #if (multishot==1):
                    #shot1_x=list([0,0,0])
                    #shot1_y=list([0,0,0])
                    #shot2_x=list([0,0,0])
                    #shot2_y=list([0,0,0])
                    #hit=list([0,0,0])
                dead=list()
                end=list()
                time=list()
                slow=list()
                knock=list()
                drain=list()
                ct=0
                while (ct<int(level_count)):
                    if (buff==ct):
                        dead.append(2+(health-0.01)*2.2*(random.randint(8,12)/10))
                    else:
                        dead.append(1+(health-0.01)*(random.randint(8,12)/10))
                    time.append(0)
                    slow.append(0)
                    knock.append(0)
                    drain.append(0)
                    end.append(0)
                    ct=ct+1
                e_seed=random.randint(1,100000)
                h=random.randint(1,20000)
            random.seed(h)
            e2_seed=random.randint(0,100000)
            c=0
            while (c < int(level_count)):
                slow_v=slow[c]
                if (slow_v==0):
                    time[c]=time[c]+1
                else:
                    time[c]=time[c]+1/(slow_v+1)
                knock_v=knock[c]
                if (knock_v>0):
                    time[c]=time[c]-10*knock[c]
                    knock[c]=knock[c]-0.01
                    time__v=time[c]
                    if (time__v<0):
                        knock[c]=knock[c]-0.01*knock[c]
                        time[c]=time[c]-0.01*time[c]
                        if (time__v<-1000):
                            time__v=-1000
                f=dead[c]
                if (c==evasive):
                    random.seed(e_seed)
                elif (c==evasive+1):
                    random.seed(e2_seed)
                enemy_v=random.randint(1,4)
                while (c==evasive and n_e==enemy_v):
                    enemy_v=random.randint(1,4)
                data=enemy(enemy_v)
                if (f>0):
                    if (burn==1):
                        dead[c]=dead[c]-0.1
                    if (life!=0):
                        drain_v=drain[c]
                        if (drain_v>0):
                            drain1_v=dead[c]
                            dead[c]=dead[c]-drain[c]/35
                            f=dead[c]
                            if (f<0):
                                dead[c]=0
                            drain2_v=dead[c]
                            lives=lives+(drain1_v-drain2_v)/4.455
                            drain[c]=drain[c]-(0.00333+drain[c]/200)
                    if (data=="hit"):
                        bv=bersk[hit_value]
                        if (bv<2 or multishot==1):
                            if (multishot!=1):
                                dead[c]=dead[c]-damage                         #<---- damage dealt here
                            else:
                                dead[c]=dead[c]-damage*0.80
                        else:
                            dead[c]=dead[c]-damage*bersk[hit_value]
                        #print (bersk)
                        #print (berserk)
                            if (berserk>=2):
                                berserk=1+berserk/100
                        if (multishot==0 or multishot == -1):
                            hit[hit_value]=-1
                            fire_v[hit_value]=0
                            if (explode_x!=0 and explode_y!=0):
                                explode=1
                            water_v[hit_value]=0
                            ice_v[hit_value]=0
                            life_v[hit_value]=0
                        else:
                            hit[hit_value][hit_value2]=-1
                    
                    else:
                        canvas.draw_polygon(data[0], data[1], data[2])
                        if (c==buff):
                            canvas.draw_polygon(data[0],5, "lime")
                        elif (c==evasive):
                            canvas.draw_polygon(data[0],5, "yellow")
                        if (slow_v!=0):
                            canvas.draw_polygon([[data[0][1][0]-7,data[0][1][1]+7],[data[0][1][0]-11,data[0][1][1]+7],[data[0][1][0]-11,data[0][1][1]+11],[data[0][1][0]-7,data[0][1][1]+11]],5, "cyan")
                        if (drain_v!=0):
                            canvas.draw_circle([data[0][1][0]+5,data[0][1][1]-5],45,5,"rgb(50,255,50,"+str(drain[c]/abs(life))+")")
                    f=dead[c]
                    if (f<0):
                        dead[c]=0
                        if (1<berserk<2 and multishot != 1):
                            berserk=(berserk-1)*100
                c=c+1
            ct=0
            if (dead==end):
                game_time=min_time+time_max
        elif (game_time >=min_time+time_max):
            min_time=min_time+time_max+100
            new_level=1
        game_time=game_time+1


    
        #Graphics:
        canvas.draw_line([32,693],[32,546+reload],50,"black")
        canvas.draw_line([32,690],[32,549+reload],44,"red")
        canvas.draw_line([32,690],[32,690-int(d)],44,"lime")
        #if (int(d)==0):
            #if (multishot==0):
            #    p=list([-100,-100,-100,-100,-100])
            #    q=list([-100,-100,-100,-100,-100])
            #    p2=list([-100,-100,-100,-100,-100])
            #    q2=list([-100,-100,-100,-100,-100])
            #    hit=list([-100,-100,-100,-100,-100])
            #elif (multishot==1):
            #    p=list([0,0,0])
            #    q=list([0,0,0])
            #    p2=list([0,0,0])
            #   q2=list([0,0,0])
            #    shot1_x=list([0,0,0])
            #    shot1_y=list([0,0,0])
            #    shot2_x=list([0,0,0])
            #    shot2_y=list([0,0,0])
            #    hit=list([0,0,0])
            #data=0
        if (int(d)<=140-reload):
            d=d+1.4
        else:
            d=141-reload
        val=0
        val2=0
        while (val2<=9):
            if (multishot==0 or multishot == -1):
                hitv=hit[val2]
                bv=bersk[val2]
                if (bv>=2):
                    color="red"
                else:
                    color="black"
                if (hitv!=-1):
                    #if (data != "hit"):
                    if(1==1):
                        pv=p[val2]
                        qv=q[val2]
                        if (pv>-600 and pv<600 and qv>-400 and qv<400):
                            p[val2]=p[val2]+x_slope[val2]
                            q[val2]=q[val2]+y_slope[val2]
                            shot1_x[val2]=550+p[val2]
                            shot1_y[val2]=350+q[val2]
                            shot2_x[val2]=550+p2[val2]
                            shot2_y[val2]=350+q2[val2]
                            canvas.draw_line([shot1_x[val2],shot1_y[val2]],[shot2_x[val2],shot2_y[val2]],2,color)
                            p2[val2]=p[val2]
                            q2[val2]=q[val2]
                        else:
                            hit[val2]=-1
                            fire_v[val2]=0
                            water_v[val2]=0
                            ice_v[val2]=0
                            life_v[val2]=0
                    else:
                        hit[val2]=-1
                        fire_v[val2]=0
                        water_v[val2]=0
                        ice_v[val2]=0
                        life_v[val2]=0
                else:
                    shot1_x[val2]=0
                    shot1_y[val2]=0
                    shot2_x[val2]=0
                    shot2_y[val2]=0
                    p[val2]=0
                    q[val2]=0
                    p2[val2]=0
                    q2[val2]=0
            elif (multishot==1):
                hit0=hit[val2][0]
                hit1=hit[val2][1]
                hit2=hit[val2][2]
                while (val<3):
                    hit3=hit[val2][val]
                    if (hit3==0):
                        pv=p[val2][val]
                        qv=q[val2][val]
                        if (pv>-600 and pv<600 and qv>-400 and qv<400):
                            p[val2][val]=p[val2][val]+x_slope[val2][val]
                            q[val2][val]=q[val2][val]+y_slope[val2][val]
                            shot1_x[val2][val]=550+p[val2][val]
                            shot1_y[val2][val]=350+q[val2][val]
                            shot2_x[val2][val]=550+p2[val2][val]
                            shot2_y[val2][val]=350+q2[val2][val]
                            p2[val2][val]=p[val2][val]
                            q2[val2][val]=q[val2][val]
                        else:
                            hit[val2][val]=-1
                    val=val+1
                val=0
                if (hit0==0):
                    canvas.draw_line([shot1_x[val2][0],shot1_y[val2][0]],[shot2_x[val2][0],shot2_y[val2][0]],1,color)
                else:
                    shot1_x[val2][0]=0
                    shot1_y[val2][0]=0
                    shot2_x[val2][0]=0
                    shot2_y[val2][0]=0
                    p[val2][0]=0
                    q[val2][0]=0
                    p2[val2][0]=0
                    q2[val2][0]=0
                if (hit1==0):
                    canvas.draw_line([shot1_x[val2][1],shot1_y[val2][1]],[shot2_x[val2][1],shot2_y[val2][1]],1,color)
                else:
                    shot1_x[val2][1]=0
                    shot1_y[val2][1]=0
                    shot2_x[val2][1]=0
                    shot2_y[val2][1]=0
                    p[val2][1]=0
                    q[val2][1]=0
                    p2[val2][1]=0
                    q2[val2][1]=0
                if (hit2==0):
                    canvas.draw_line([shot1_x[val2][2],shot1_y[val2][2]],[shot2_x[val2][2],shot2_y[val2][2]],1,color)
                else:
                    shot1_x[val2][2]=0
                    shot1_y[val2][2]=0
                    shot2_x[val2][2]=0
                    shot2_y[val2][2]=0
                    p[val2][2]=0
                    q[val2][2]=0
                    p2[val2][2]=0
                    q2[val2][2]=0
            val2=val2+1
        canvas.draw_circle([550,350],7,14,"black")
        if (multishot==-1):
            canvas.draw_line([100,675],[100,655],6,"black")
            canvas.draw_line([145,675],[135,675-sqrt_val],3,"rgba(100,100,100,0.8)")
            canvas.draw_line([150,675],[150,655],3,"rgba(100,100,100,0.8)")
            canvas.draw_line([155,675],[165,675-sqrt_val],3,"rgba(100,100,100,0.8)")
        if (multishot==1):
            canvas.draw_line([145,675],[135,675-sqrt_val],3,"black")
            canvas.draw_line([150,675],[150,655],3,"black")
            canvas.draw_line([155,675],[165,675-sqrt_val],3,"black")
            canvas.draw_line([100,675],[100,655],6,"rgba(100,100,100,0.8)")
        if (swapping!=0):
            canvas.draw_text("swapping...",[200,665],30,"black")
        if (berserk>=2):
            canvas.draw_circle([543,343],2,4,"red")
        if (explode>0):
            fire2=abs(fire)
            fire2_v=(-0.16*explode)*(explode-40-10*fire2)
            canvas.draw_circle([explode_x,explode_y],0.5*fire2_v,fire2_v,"orange")
            explode=explode+1
            if (explode>=40+10*fire2):
                explode=0
                explode_x=0
                explode_y=0
        if (lives>0):
            canvas.draw_line([1058,675],[1032,650],24,"pink")
            canvas.draw_line([1040,675],[1066,650],24,"pink")
            if (lives>1):
                canvas.draw_line([998,675],[972,650],24,"pink")
                canvas.draw_line([980,675],[1006,650],24,"pink")
                if (lives>2):
                    canvas.draw_line([938,675],[912,650],24,"pink")
                    canvas.draw_line([920,675],[946,650],24,"pink")
                    if (lives>3):
                        canvas.draw_line([878,675],[852,650],24,"pink")
                        canvas.draw_line([860,675],[886,650],24,"pink")
                        if (lives>4):
                            canvas.draw_line([818,675],[792,650],24,"pink")
                            canvas.draw_line([800,675],[826,650],24,"pink")
                            if (lives>5):
                                canvas.draw_line([745,662],[715,662],10,"white")
                                canvas.draw_line([730,677],[730,647],10,"white")
                                canvas.draw_text(str(int(lives-5)),[685,670],25,"white")
        if (lives<=5):
            canvas.draw_line([780,662],[780+(5-lives)*60,662],100,"green")            
        if (fire>=1):
            canvas.draw_circle([550,340],2,4,"orange")
            if (w_pressed==1):
                canvas.draw_circle([550,340],1,2,"black")
        elif (fire<=-1):
            fire_c=fire_c+1
            if (fire_c>=1000):
                fire_c=0
                fire=abs(fire)
        if (water>=1):
            canvas.draw_circle([550,360],2,4,"blue")
            if (s_pressed==1):
                canvas.draw_circle([550,360],1,2,"black")
        elif (water<=-1):
            water_c=water_c+1
            if (water_c>=1000):
                water_c=0
                water=abs(water)
        if (ice>=1):
            canvas.draw_circle([560,350],2,4,"cyan")
            if (d_pressed==1):
                canvas.draw_circle([560,350],1,2,"black")
        elif (ice<=-1):
            ice_c=ice_c+1
            if (ice_c>=1000):
                ice_c=0
                ice=abs(ice)
        if (life>=1):
            canvas.draw_circle([540,350],2,4,"lime")
            if (a_pressed==1):
                canvas.draw_circle([540,350],1,2,"black")
        elif (life<=-1):
            life_c=life_c+1
            if (life_c>=1000):
                life_c=0
                life=abs(life)
    else:
        if (upgrade==1 and pause==0): 
            canvas.draw_text("Press 'd' to upgrade damage",[30,250],40,"red")
            canvas.draw_text("Damage: "+str(round(damage+0.0,2))+" -> "+str(round(damage+0.1*damage+0.5,2)),[30,300],40,"black")
            canvas.draw_text("Damage per hectotick: "+str(round((damage*100)/((140-reload)/1.4),3))+" dpht -> "+str(round(((damage+0.1*damage+0.5)*100)/((140-reload)/1.4),3))+" dpht",[30,350],40,"cyan")
            if (reload<135):
                canvas.draw_text("Press 'r' to upgrade reload",[30,450],40,"red")
                canvas.draw_text("Reload Time: "+str(round(round(140-reload,2),2))+" -> "+str(round(140-(reload+((140-reload)*0.3)),2)),[30,500],40,"black")
                canvas.draw_text("Damage per hectotick: "+str(round((damage*100)/((140-reload)/1.4),3))+" dpht -> "+str(round((damage*100)/((140-(reload+((140-reload)*0.3)))/1.4),3))+" dpht",[30,550],40,"cyan")
        elif (upgrade==2 and pause==0):
            if (multishot==0):
                canvas.draw_text("'m' to enable multishot",[30,50],40,"red")
            if (berserk==1.00):
                canvas.draw_text("'b' to enable berserk (double damage after kill)",[30,100-(50*multishot)],40,"red")
            else:
                if (berserk<2):
                    canvas.draw_text("'b' to upgrade berserk ("+str((berserk-1+0.01)*100)+" times damage after kill)",[3,100-(50*multishot)],40,"red")
                else:
                    canvas.draw_text("'b' to upgrade berserk ("+str(int(berserk+1))+" times damage after kill)",[3,100-(50*multishot)],40,"red")
        elif (upgrade==3 and pause==0):
            if (fire==0 and water==0 and ice==0 and life==0):
                canvas.draw_text("F- unlock fire bullets: area damage",[30,200],40,"red")
                canvas.draw_text("W- unlock water bullets: knockback",[30,250],40,"red")
                canvas.draw_text("I- unlock ice bullets: slowness",[30,300],40,"red")
                canvas.draw_text("L- unlock life bullets: health regen",[30,350],40,"red")
            else:
                canvas.draw_text("_- unlock burst",[30,250],40,"red")
                canvas.draw_text("_- unlock forcefield",[30,300],40,"red")
                canvas.draw_text("_- unlock _ ",[30,350],40,"red")
                canvas.draw_text("_- unlock _ ",[30,400],40,"red")
                if (fire!=0):
                    canvas.draw_text("F- upgrade fire bullets",[30,200],40,"red")
                if (water!=0):
                    canvas.draw_text("W- upgrade water bullets",[30,200],40,"red")
                if (ice!=0):
                    canvas.draw_text("I- upgrade ice bullets",[30,200],40,"red")
                if (life!=0):
                    canvas.draw_text("L- upgrade life bullets",[30,200],40,"red")
                    
        elif (pause==1):
            if (help_screen==0):
                canvas.draw_text("Paused",[450,350],40,"red")
                canvas.draw_text("Press 'h' for help",[375,400],40,"red")
            else:
                canvas.draw_text("1) Enemies",[10,50],40,"red")
                canvas.draw_text("2) Weapons",[10,100],40,"red")
                canvas.draw_text("3) Swapping",[10,150],40,"red")
                canvas.draw_text("4) Elemental:",[10,200],40,"red")
                canvas.draw_text("a) Fire",[50,225],20,"red")
                canvas.draw_text("b) Water",[50,250],20,"red")
                canvas.draw_text("c) Ice",[50,275],20,"red")
                canvas.draw_text("d) Life",[50,300],20,"red")
                if (page==0):
                    canvas.draw_text("Click the number keys to switch",[350,100],40,"black")
                    canvas.draw_text("between the different pages",[350,150],40,"black")
                elif (page==1):
                    help_val=help_val+1
                    canvas.draw_polygon([[300,95],[310,95],[310,85],[300,85]],20,"rgb("+str(255-help_val%256)+",0,"+str(help_val%256)+")")
                    canvas.draw_text("-Normal enemy,the health of all enemies",[350,100],40,"black")
                    canvas.draw_text("is based on how blue they are",[350,150],40,"black")
                    canvas.draw_text("Fun Fact: every enemy moves at slightly",[350,200],40,"black")
                    canvas.draw_text("different speeds",[350,250],40,"black")
                    canvas.draw_polygon([[300,345],[310,345],[310,335],[300,335]],20,"rgb("+str(255-(help_val*2)%256)+",0,"+str((help_val*2)%256)+")")
                    canvas.draw_polygon([[300,345],[310,345],[310,335],[300,335]],5, "lime")
                    canvas.draw_text("-Buff enemy, moves at half speed but",[350,350],40,"black")
                    canvas.draw_text("has double health",[350,400],40,"black")
                    canvas.draw_polygon([[300,495],[310,495],[310,485],[300,485]],20,"rgb("+str(255-help_val%256)+",0,"+str(help_val%256)+")")
                    canvas.draw_polygon([[300,495],[310,495],[310,485],[300,485]],5, "yellow")
                    canvas.draw_text("-Evasive enemy, teleports when shot;",[350,500],40,"black")
                    canvas.draw_text("multishot is ineffective against them",[350,550],40,"black")
                elif (page==2):
                    canvas.draw_text("-Multishot: shoots one bullet where you click",[250,100],40,"black")
                    canvas.draw_text("and two more beside it. Your damage is split so",[250,150],40,"black")
                    canvas.draw_text("that each bullet only deals 80% of the total damage",[250,200],40,"black")
                    canvas.draw_text("-Berserk: upgrades your single-shot weapon to deal",[250,300],40,"black")
                    canvas.draw_text("double damage on the next shot after a kill",[250,350],40,"black")
                elif (page==3):
                    canvas.draw_text("Swapping weapons: When you press space, your",[250,100],40,"black")
                    canvas.draw_text("weapon will be swapped to the other weapon type",[250,150],40,"black")
                    canvas.draw_text("after you finish reloading (if your reload is",[250,200],40,"black")
                    canvas.draw_text("quick, the last bullet shot will disappear)",[250,250],40,"black")
                    canvas.draw_text("Why do this? Multishot deals less damage per bullet",[250,350],40,"black")
                    canvas.draw_text("than single-shot and berserk only applies to the",[250,400],40,"black")
                    canvas.draw_text("single shot bullets",[250,450],40,"black")
                elif (page==4):
                    if (subpage==0):
                        canvas.draw_text("Elemental bullets, once unlocked, will show",[250,100],40,"black")
                        canvas.draw_text("up as a dot on your character when ready",[250,150],40,"black")
                        canvas.draw_text("to use. They can be selected by pressing",[250,200],40,"black")
                        canvas.draw_text("W,A,S, or D, whether the marker is on the",[250,250],40,"black")
                        canvas.draw_text("top, left, bottom, or right of you,",[250,300],40,"black")
                        canvas.draw_text("respectively. Only affects single shots.",[250,350],40,"black")
                    elif (subpage==1):
                        canvas.draw_text("Fire: Orange marker on top, press W to",[250,100],40,"black")
                        canvas.draw_text("activate. When it hits an enemy, it",[250,150],40,"black")
                        canvas.draw_text("explodes in a fiery aura that burns all",[250,200],40,"black")
                        canvas.draw_text("near enemies for 0.1 damage per tick",[250,250],40,"black")
                        canvas.draw_text("(10 dpht)",[250,300],40,"black")
                    elif (subpage==2):
                        canvas.draw_text("Water: When an enemy is hit, they are knocked",[250,100],40,"black")
                        canvas.draw_text("back by an amount determined by the upgrade",[250,150],40,"black")
                        canvas.draw_text("level of water. Knockback amount is the same",[250,200],40,"black")
                        canvas.draw_text("for all enemies regardless of their speed",[250,250],40,"black")
                    elif (subpage==3):
                        canvas.draw_text("Ice: Slows down an enemy to half speed.",[250,100],40,"black")
                        canvas.draw_text("If upgraded this becomes a third speed",[250,150],40,"black")
                        canvas.draw_text("and then quarter speed and so on. Ice",[250,200],40,"black")
                        canvas.draw_text("effect is stackable on the same enemy",[250,250],40,"black")

                    elif (subpage==4):
                        canvas.draw_text("Life: Drains an enemy's health, both",[250,100],40,"black")
                        canvas.draw_text("damaging it and healing you. The first",[250,150],40,"black")
                        canvas.draw_text("unlock of this attack drains roughly a max",[250,200],40,"black")
                        canvas.draw_text("of 3 health into 0.5 lives from the affected",[250,250],40,"black")
                        canvas.draw_text("enemy",[250,300],40,"black")
    if (level <= 1 and pause==0):
        canvas.draw_text("Press 'p' to pause and see the help screen",[10,30],40,"black")
    if (swapping != 0):
        if (d>=140-reload):
            if (swapping==-1):
                p=list([0,0,0,0,0,0,0,0,0,0])
                q=list([0,0,0,0,0,0,0,0,0,0])
                p2=list([0,0,0,0,0,0,0,0,0,0])
                q2=list([0,0,0,0,0,0,0,0,0,0])
                x_slope=list([0,0,0,0,0,0,0,0,0,0])
                y_slope=list([0,0,0,0,0,0,0,0,0,0])
                shot1_x=list([0,0,0,0,0,0,0,0,0,0])
                shot1_y=list([0,0,0,0,0,0,0,0,0,0])
                shot2_x=list([0,0,0,0,0,0,0,0,0,0])
                shot2_y=list([0,0,0,0,0,0,0,0,0,0])
                hit=list([-1,-1,-1,-1,-1,-1,-1,-1,-1,-1])
                multishot=-1
                swapping=0
            if (swapping==1):
                vfn=0
                while (vfn<=9):
                    p[vfn]=list([0,0,0])
                    q[vfn]=list([0,0,0])
                    p2[vfn]=list([0,0,0])
                    q2[vfn]=list([0,0,0])
                    shot1_x[vfn]=list([0,0,0])
                    shot1_y[vfn]=list([0,0,0])
                    shot2_x[vfn]=list([0,0,0])
                    shot2_y[vfn]=list([0,0,0])
                    hit[vfn]=list([-1,-1,-1])
                    x_slope[vfn]=list([0,0,0])
                    y_slope[vfn]=list([0,0,0])
                    vfn=vfn+1
                multishot=1
                swapping=0

def click(pos):
    global x
    global y
    global typ
    global y_slope
    global x_slope
    global p
    global q
    global p2
    global q2
    global shot1_x
    global shot1_y
    global shot2_x
    global shot2_y
    global hit
    global d
    global berserk
    global bersk
    global reload
    global upgrade
    global pause
    global multishot
    global w_pressed
    global a_pressed
    global s_pressed
    global d_pressed
    global fire
    global water
    global ice
    global life
    global fire_v
    global water_v
    global ice_v
    global life_v
    if (upgrade==0 and pause==0 and swapping==0):
        if (int(d)>140-reload):
            x=pos[0]-550
            y=pos[1]-350
            typ=0
                    #typ=0 -> +x  +y
                    #typ=1 -> +x  -y
                    #typ=2 -> -x  +y
                    #typ=3 -> -x  -y
            vfn=-1
            vfn2=0
            while (vfn2==0):
                if (multishot==0 or multishot == -1):
                    vfn=vfn+1
                    if (hit[vfn]!=0):
                        vfn2=1
                    elif (vfn==9):
                        hit[0]=-1
                        vfn=-1
                        vfn2=0
                else:
                    vfn=vfn+1
                    if (hit[vfn]==list([-1,-1,-1])):
                        vfn2=1
                    elif (vfn==9):
                        hit[0]=list([-1,-1,-1])
                        vfn=-1
                        vfn2=0
            if (multishot==0 or multishot==-1):
                shot1_x[vfn]=0
                shot1_y[vfn]=0
                shot2_x[vfn]=0
                shot2_y[vfn]=0
                p[vfn]=0
                q[vfn]=0
                p2[vfn]=0
                q2[vfn]=0
            elif (multishot==1):
                shot1_x[vfn]=list([0,0,0])
                shot1_y[vfn]=list([0,0,0])
                shot2_x[vfn]=list([0,0,0])
                shot2_y[vfn]=list([0,0,0])
                p[vfn]=list([0,0,0])
                q[vfn]=list([0,0,0])
                p2[vfn]=list([0,0,0])
                q2[vfn]=list([0,0,0])
            #print ("typ= "+str(typ))
            #print (str(x)+", "+str(y))
            if (x!=0):
                deg=math.atan(y/x)
            else:
                deg=math.atan(y/(x+0.00001))
            #print (deg)
            bersk[vfn]=berserk
            if (berserk>=2 and multishot != 1):
                berserk=1+berserk/100
            if (multishot==0 or multishot -1):
                if (fire>=1 and w_pressed==1):
                    fire_v[vfn]=fire
                    fire=-1*fire
                    w_pressed=0
                if (water>=1 and s_pressed==1):
                    water_v[vfn]=water
                    water=-1*water
                    s_pressed=0
                if (ice>=1 and d_pressed==1):
                    ice_v[vfn]=ice
                    ice=-1*ice
                    d_pressed=0
                if (life>=1 and a_pressed==1):
                    life_v[vfn]=life
                    life=-1*life
                    a_pressed=0
                #print (x_slope)
                x_slope[vfn]=(math.cos(deg))*10
                y_slope[vfn]=(math.sin(deg))*10
            elif (multishot==1):
                x_slope[vfn]=list([(math.cos(deg-0.09))*10])
                x_slope[vfn].append((math.cos(deg))*10)
                x_slope[vfn].append((math.cos(deg+0.09))*10)
                y_slope[vfn]=list([(math.sin(deg-0.09))*10])
                y_slope[vfn].append((math.sin(deg))*10)
                y_slope[vfn].append((math.sin(deg+0.09))*10)

            #print(x_slope[vfn])
            #print(y_slope[vfn])
            #print("")
            if (x<0):
                typ=typ+2
            if (y<0):
                typ=typ+1
            val=0
            if (multishot==0 or multishot ==-1):
                hit[vfn]=0
            else:
                hit[vfn]=list([0,0,0])
            #if (typ==0):
            #    x_slope=math.fabs(x_slope)
            #    y_slope=math.fabs(y_slope)
            #if (typ==1):
            #    x_slope=math.fabs(x_slope)
            #    y_slope=-1*math.fabs(y_slope)
            if (multishot==0 or multishot == -1):
                if (typ==2):
                    x_slope[vfn]=-1*math.fabs(x_slope[vfn])
                    y_slope[vfn]=math.fabs(y_slope[vfn])
                if (typ==3):
                    x_slope[vfn]=-1*math.fabs(x_slope[vfn])
                    y_slope[vfn]=-1*math.fabs(y_slope[vfn])
            elif (multishot==1):
                a0=x_slope[vfn][0]
                a1=x_slope[vfn][1]
                a2=x_slope[vfn][2]
                b0=y_slope[vfn][0]
                b1=y_slope[vfn][1]
                b2=y_slope[vfn][2]
                while (val<3):
                    if (typ==2):
                        x_slope[vfn][val]=-1*math.fabs(x_slope[vfn][val])
                        y_slope[vfn][val]=math.fabs(y_slope[vfn][val])
                    if (typ==3):
                        x_slope[vfn][val]=-1*math.fabs(x_slope[vfn][val])
                        y_slope[vfn][val]=-1*math.fabs(y_slope[vfn][val])
                    val=val+1
                if (x<0):
                    if ((a0>=0 and a1>=0 and a2<0)or(a0<0 and a1<0 and a2>=0)):
                        x_slope[vfn][2]=-1*x_slope[vfn][2]
                    elif ((a0>=0 and a1<0 and a2<0)or(a0<0 and a1>=0 and a2>=0)):
                        x_slope[vfn][0]=-1*x_slope[vfn][0]
                    if ((b0>=0 and b1>=0 and b2<0)or(b0<0 and b1<0 and b2>=0)):
                        y_slope[vfn][2]=-1*y_slope[vfn][2]
                    elif ((b0>=0 and b1<0 and b2<0)or(b0<0 and b1>=0 and b2>=0)):
                        y_slope[vfn][0]=-1*y_slope[vfn][0]
            d=0
            
    
def key_handler(key):
    
    global upgrade
    global damage
    global reload
    global d
    global pause
    global p
    global q
    global p2
    global q2
    global shot1_x
    global shot1_y
    global shot2_x
    global shot2_y
    global hit
    global x_slope
    global y_slope
    global multishot
    global berserk
    global help_screen
    global page
    global subpage
    global background
    global swapping
    global fire
    global water
    global ice
    global life
    global w_pressed
    global a_pressed
    global s_pressed
    global d_pressed
    if (upgrade==0 and pause==0):
        if (fire>=1 and key==87):
            if (w_pressed==1):
                w_pressed=0
            else:
                w_pressed=1
        if (water>=1 and key==83):
            if (s_pressed==1):
                s_pressed=0
            else:
                s_pressed=1
        if (ice>=1 and key==68):
            if (d_pressed==1):
                d_pressed=0
            else:
                d_pressed=1
        if (life>=1 and key==65):
            if (a_pressed==1):
                a_pressed=0
            else:
                a_pressed=1
    elif (upgrade==1 and pause==0):
        if (key==68):
            damage=damage+0.1*damage+0.5
            upgrade=0
        elif (key==82):
            if (reload<125):
                reload=reload+((140-reload)*0.3)
                d=140-reload
                upgrade=0
    elif (upgrade==2 and pause==0):
        if (key==77):
            if (multishot==0):
                vfn=0
                while (vfn<=9):
                    p[vfn]=list([0,0,0])
                    q[vfn]=list([0,0,0])
                    p2[vfn]=list([0,0,0])
                    q2[vfn]=list([0,0,0])
                    shot1_x[vfn]=list([0,0,0])
                    shot1_y[vfn]=list([0,0,0])
                    shot2_x[vfn]=list([0,0,0])
                    shot2_y[vfn]=list([0,0,0])
                    hit[vfn]=list([-1,-1,-1])
                    x_slope[vfn]=list([0,0,0])
                    y_slope[vfn]=list([0,0,0])
                    vfn=vfn+1
                multishot=1
                upgrade=0
        elif (key==66):
            if (berserk==1.00):
                berserk=1.02
                upgrade=0
            else:
                if (berserk<2):
                    berserk=berserk+0.01
                else:
                    berserk=berserk+1
                upgrade=0
    elif (upgrade==3 and pause==0):
        if (fire==0 and water==0 and ice==0 and life==0):
            if (key==70):
                fire=1
                upgrade=0
            elif (key==87):
                water=1
                upgrade=0
            elif (key==73):
                ice=1
                upgrade=0
            elif (key==76):
                life=1
                upgrade=0
        elif (fire!=0):
            if (key==70):
                fire=fire+1
                upgrade=0
        elif (water!=0):
            if (key==87):
                water=water+1
                upgrade=0
        elif (ice!=0):
            if (key==73):
                ice=ice+1
                upgrade=0
        elif (life!=0):
            if (key==76):
                life=life+1
                upgrade=0
    
    if (key==80):
        if (pause==0):
            pause=1
            help_screen=0
            background="green"
        elif (pause==1):
            pause=0
            help_screen=0
            background="green"
    if (pause==1 and key==72):
        if (help_screen==1):
            help_screen=0
            page=0
            subpage=0
            background="green"
        elif (help_screen==0):
            help_screen=1
            page=0
            subpage=0
            background="white"
    if (help_screen==1):
        if (key==49):
            page=1
            subpage=0
        if (key==50):
            page=2
            subpage=0
        if (key==51):
            page=3
            subpage=0
        if (key==52):
            page=4
            subpage=0
        if (key==65):
            subpage=1
        if (key==66):
            subpage=2
        if (key==67):
            subpage=3
        if (key==68):
            subpage=4
    if (key==32):
        if (multishot==1):
            swapping=-1
        elif (multishot==-1):
            swapping=1
            
def input_handler(inp): #<---- For mobile compatability
    
    global upgrade
    global damage
    global reload
    global d
    global pause
    global p
    global q
    global p2
    global q2
    global shot1_x
    global shot1_y
    global shot2_x
    global shot2_y
    global hit
    global x_slope
    global y_slope
    global multishot
    global berserk
    global help_screen
    global page
    global subpage
    global background
    global swapping
    global fire
    global water
    global ice
    global life
    global w_pressed
    global a_pressed
    global s_pressed
    global d_pressed
    if (upgrade==1 and pause==0):
        if (inp=="d" or inp=="D"):
            damage=damage+0.1*damage+0.5
            upgrade=0
        elif (inp=="r" or inp=="R"):
            if (reload<125):
                reload=reload+((140-reload)*0.3)
                d=140-reload
                upgrade=0
    elif (upgrade==2 and pause==0):
        if (inp=="m" or inp=="M"):
            if (multishot==0):
                vfn=0
                while (vfn<=9):
                    p[vfn]=list([0,0,0])
                    q[vfn]=list([0,0,0])
                    p2[vfn]=list([0,0,0])
                    q2[vfn]=list([0,0,0])
                    shot1_x[vfn]=list([0,0,0])
                    shot1_y[vfn]=list([0,0,0])
                    shot2_x[vfn]=list([0,0,0])
                    shot2_y[vfn]=list([0,0,0])
                    hit[vfn]=list([-1,-1,-1])
                    x_slope[vfn]=list([0,0,0])
                    y_slope[vfn]=list([0,0,0])
                    vfn=vfn+1
                multishot=1
                upgrade=0
        elif (inp=="b" or inp=="B"):
            if (berserk==1.00):
                berserk=1.02
                upgrade=0
            else:
                if (berserk<2):
                    berserk=berserk+0.01
                else:
                    berserk=berserk+1
                upgrade=0
    elif (upgrade==3 and pause==0):
        if (fire==0 and water==0 and ice==0 and life==0):
            if (inp=="f" or inp=="F"):
                fire=1
                upgrade=0
            elif (inp=="w" or inp=="W"):
                water=1
                upgrade=0
            elif (inp=="i" or inp=="I"):
                ice=1
                upgrade=0
            elif (inp=="l" or inp=="L"):
                life=1
                upgrade=0
        elif (fire!=0):
            if (inp=="f" or inp=="F"):
                fire=fire+1
                upgrade=0
        elif (water!=0):
            if (inp=="w" or inp=="W"):
                water=water+1
                upgrade=0
        elif (ice!=0):
            if (inp=="i" or inp=="I"):
                ice=ice+1
                upgrade=0
        elif (life!=0):
            if (inp=="l" or inp=="L"):
                life=life+1
                upgrade=0
    

    if (pause==1 and (inp=="h" or inp=="H")):
        if (help_screen==1):
            help_screen=0
            page=0
            background="green"
        elif (help_screen==0):
            help_screen=1
            page=0
            background="white"
    if (help_screen==1):
        if (inp=="1"):
            page=1
        if (inp=="2"):
            page=2
        if (inp=="3"):
            page=3
        if (inp=="4"):
            page=4
        if (inp=="a" or inp=="A"):
            subpage=1
        if (inp=="b" or inp=="B"):
            subpage=2
        if (inp=="c" or inp=="C"):
            subpage=3
        if (inp=="d" or inp=="D"):
            subpage=4
    
def pse():
    global page
    global pause
    global help_screen
    global background
    if (pause==0):
        pause=1
        help_screen=0
        background="green"
    elif (pause==1):
        pause=0
        help_screen=0
        background="green"
def space():
    global multishot
    global swapping
    if (multishot==1):
        swapping=-1
    elif (multishot==-1):
        swapping=1
def fire_b():
    global fire
    global w_pressed
    if (fire>=1):
        w_pressed=1
def water_b():
    global water
    global s_pressed
    if (water>=1):
        s_pressed=1
def ice_b():
    global ice
    global d_pressed
    if (ice>=1):
        d_pressed=1
def life_b():
    global life
    global a_pressed
    if (life>=1):
        a_pressed=1

frame = simplegui.create_frame('Testing', 1100, 700)
inp = frame.add_input('Mobile Keyboard Input', input_handler,50)
button1 = frame.add_button('Pause', pse, 200)
button2 = frame.add_button('Swap Weapon', space, 200)
button3 = frame.add_button('Fire', fire_b, 200)
button4 = frame.add_button('Water', water_b, 200)
button5 = frame.add_button('Ice', ice_b, 200)
button6 = frame.add_button('Life', life_b, 200)
frame.set_canvas_background(background)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw_handler)
frame.set_keydown_handler(key_handler)
frame.start()
