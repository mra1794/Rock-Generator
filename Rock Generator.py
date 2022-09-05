Python 3.10.6 (v3.10.6:9c7b4bd164, Aug  1 2022, 17:13:48) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import maya.cmds as cmds
from random import uniform as rand
import time

curF=1

RockCount=cmds.promptDialog(t="Rockgen", m="Enter the number of rocks yo like to generate")
RockNum=int(cmds.promptDialog(q=True,tx=True))
for i in range (1,RockNum+1):
    RanLocX=rand(-50,50)
    RanLocZ=rand(-50,50)
    randRad=rand(0.1,0.5)
    cmds.polySphere(n="Rock",r=randRad, sx=10, sy=10)
    cmds.move(RanLocX,0,RanLocZ)
    cmds.ConvertSelectionToVertices()
    ComponentAll=cmds.ls(sl=True,fl=True) #fl se asegura de que no agrupe todo los elementos

    #With this loop I go through all selection and one by one I move them to the random location
    for i in range(0,len(ComponentAll)):
        cmds.select(ComponentAll[i])
        randomX=rand(0,1.0)
        randomY=rand(0,1.0)
        randomZ=rand(0,1.0)
        cmds.move(randomX,randomY,randomZ,r=True)
    cmds.currentTime(curF)
    curF=curF+1
    time.sleep(.1)