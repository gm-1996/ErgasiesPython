
from PIL import Image, ImageDraw
import random
import math

im = Image.new("RGB", (1024, 1024), "white")
crds = []

for i in range(20):
    
    r = random.randint(50,100)
    x = random.randint(0,1024)
    while(x-r<0 or x+r>1024):
       x = random.randint(0,1024)
    y = random.randint(0,1024)
    while(y-r<0 or y+r>1024):
        y = random.randint(0,1024)   
    crds.append([x,y,r])   
    draw = ImageDraw.Draw(im)
    draw.ellipse((x-r, y-r, x+r, y+r), fill=(255,255,0), outline ='red')

tk=0
inTheLst = []
for i in range(20): 
    iii=True        
    for j in range(i+1,20):
        add = 2 
        #vres to mikos tis ipotinousas
        x = crds[i][0]-crds[j][0]
        y = crds[i][1]-crds[j][1]
        distance = (math.sqrt(x**2 + y**2))
        if(distance < crds[i][2]+crds[j][2]): 
            for x in range(len(inTheLst)):
                if(inTheLst[x]==i):
                    add-=1
                    iii = False
                if(inTheLst[x]==j):
                    add-=1                
            if(add==2):
                inTheLst.append(i);inTheLst.append(j)
            elif(add==1):
                 if(iii):
                     inTheLst.append(i)
                 else:
                     inTheLst.append(j) 
            #print add                 
            tk+=add
           
          

print tk
im.save("circles.bmp")