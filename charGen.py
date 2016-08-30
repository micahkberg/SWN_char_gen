"""
generates random characters for the purposes of my superhero based RPG I'm running
with friends based on the world of "Worm" by Wildbow.

To use, make sure that distable and advtable point to the corret locations of 
disadvantage and advantage tables.

Also create a local file with a list of civilian names that this program will
match a bunch of stats and randomly generated atributes for.

Possible ideas for how to improve this generator:
1. Maybe add power levels to the power class generator
2. More complicated personality generator (tastes, interests, hometown, etc.)
3. Better stat distributions for ability scores
4. something along the lines of a program that can randomly generate powers?
5. randomly generated Cape ID's?
"""
import numpy as np
names=np.genfromtxt("C:/Users/iceberg/Desktop/DUNGEONS_AND_DRAGONS/WORM/charnames.txt",dtype="str",delimiter=",")
distable=np.genfromtxt("C:/Users/iceberg/Desktop/DUNGEONS_AND_DRAGONS/WORM/distable.txt",dtype="str",delimiter=' "," ')
advtable=np.genfromtxt("C:/Users/iceberg/Desktop/DUNGEONS_AND_DRAGONS/WORM/advtable.txt",dtype="str",delimiter=' "," ')
traits=np.genfromtxt("C:/Users/iceberg/Desktop/DUNGEONS_AND_DRAGONS/WORM/character_traits.txt",dtype="str",delimiter=' "," ')
haircolors=("brown","brown","brown","dark brown","light brown","black",
"black","red","blonde","blonde","blonde","dirty blonde","dyed","bald")
eyecolors=("brown","blue","green")
charhair=[]
chareyes=[]
charage=[]
dis=[]
adv=[]
charisma=[]
strength=[]
dexterity=[]
brains=[]
hp=[]
chartrait=[]
mutantstatus=[]
classes=("mover","shaker","brute","blaster","breaker","master","tinker","stiker","stranger") 
powertype=[]
for i in np.arange(0,len(names)):
    c53=np.random.randint(1,20)
    if c53==13:
        mutantstatus.append("case 53")
    else: 
        mutantstatus.append("")
    charhair.append(haircolors[np.random.randint(0,13)]+" hair")
    luck=(np.random.randint(1,6)+np.random.randint(1,6))
    chareyes.append(eyecolors[np.random.randint(0,3)]+ " eyes")
    charage.append(str(np.random.randint(16,40)) +" years")
    chartrait1=np.random.randint(0,len(traits))
    chartrait2=np.random.randint(0,len(traits))
    while chartrait2==chartrait1:
        chartrait2=np.random.randint(0,len(traits))
    chartrait.append(traits[chartrait1]+" and " + traits[chartrait2])
    if luck<3:
        disnum=2
        advnum=0
    else:
        if luck<7:
            disnum=1
            advnum=0
        else:
            if luck<11:
                disnum=1
                advnum=1
            else:
                if luck<12:
                    disnum=0
                    advnum=1
                else:
                    disnum=0
                    advnum=2
    if disnum==0:
        dis.append("no disadvantages")
    else:
        if disnum==1:
            dis.append(distable[np.random.randint(0,len(distable))])
        if disnum==2:
            dis1=np.random.randint(0,len(distable))
            dis2=np.random.randint(0,len(distable))
            if dis2==dis1:
                dis2=np.random.randint(0,len(distable))
            dis.append(distable[dis1]+"             "+distable[dis2])
            
    if advnum==0:
        adv.append("no advantages")
    else:
        if advnum==1:
            adv.append(advtable[np.random.randint(0,len(advtable))])
        if advnum==2:
            adv1=np.random.randint(0,len(advtable))
            adv2=np.random.randint(0,len(advtable))
            if adv2==adv1:
                adv2=np.random.randint(0,len(advtable))
            adv.append(advtable[adv1]+"             "+advtable[adv2])
    charisma.append("char:"+str(int(np.ceil(float(np.random.randint(1,5)+np.random.randint(1,5))/2))))
    strength.append("str:"+str(int(np.ceil(float(np.random.randint(1,5)+np.random.randint(1,5))/2))))
    dexterity.append("dex:"+str(int(np.ceil(float(np.random.randint(1,5)+np.random.randint(1,5)+1)/2))))
    brains.append("brains:"+str(int(np.ceil(float(np.random.randint(1,5)+np.random.randint(1,5))/2))))
    hp.append("HP:"+str(int(strength[i].strip("str:"))+int(dexterity[i].strip("dex:"))+int(brains[i].strip("brains:"))+np.random.randint(1,6)))
    powernum=(np.random.randint(1,4)+np.random.randint(1,4)+np.random.randint(1,4))
    if powernum<7:
        tempower=np.random.randint(0,len(classes))
        if classes[tempower]=="master" or classes[tempower]=="stranger":
            tempower=np.random.randint(0,len(classes))
        powertype.append(classes[tempower])
    else:
        if powernum<9:
            tempower1=np.random.randint(0,len(classes))
            if classes[tempower1]=="master" or classes[tempower1]=="stranger":
                tempower1=np.random.randint(0,len(classes))
            tempower2=np.random.randint(0,len(classes))
            if classes[tempower2]=="master" or classes[tempower2]=="stranger":
                tempower2=np.random.randint(0,len(classes))
            while tempower2==tempower1:
                tempower2=np.random.randint(0,len(classes))
            powertype.append(classes[tempower1]+" and "+classes[tempower2])
        else:
            tempower1=np.random.randint(0,len(classes))
            if classes[tempower1]=="master" or classes[tempower1]=="stranger":
                tempower1=np.random.randint(0,len(classes))
            tempower2=np.random.randint(0,len(classes))
            if classes[tempower2]=="master" or classes[tempower2]=="stranger":
                tempower2=np.random.randint(0,len(classes))
            while tempower2==tempower1:
                tempower2=np.random.randint(0,len(classes))
            tempower3=np.random.randint(0,len(classes))
            if classes[tempower3]=="master" or classes[tempower3]=="stranger":
                tempower3=np.random.randint(0,len(classes))
            while tempower3==tempower2 or tempower3==tempower1:
                tempower3=np.random.randint(0,len(classes))
            powertype.append(classes[tempower1]+", "+classes[tempower2]+", and "+classes[tempower3])
    
    #powertype.append()
fulldata=np.column_stack((names,charhair,chareyes,charage,mutantstatus,chartrait,dis,adv,charisma,strength,dexterity,brains,hp,powertype))        
fdata=np.asarray(fulldata)
np.savetxt("chars.txt",fulldata, fmt="%s", delimiter="          ",newline="\n \n \n")
