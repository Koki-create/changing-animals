def setup():
    size(1500,700)

def face(x,y):
    fill(0)#色を黒に
    ellipse(x-70,y-50,50,70)#右目
    ellipse(x+70,y-50,50,70)#左目
    ellipse(x,y,50,30)#鼻
    stroke(0)#枠を黒に
    strokeWeight(10)#枠を太く
    noFill()#図は塗りつぶさない
    arc(x-50,y,100,100,0,HALF_PI)#1/4の円を書く（左口）
    arc(x+50,y,100,100,HALF_PI,PI)#1/4の円を書く（右口）

def dog(xd, yd):
    noStroke()#枠をなしに
    fill(115,78,48)#茶色に
    rect(xd-150,yd-230, 300,300, 50)#顔
    fill(84,52,39)#濃い茶色に
    rect(xd-200,yd-240,100,200,50)#右耳
    rect(xd+100,yd-240,100,200,50)#左耳

def ber(xb, yb):
    noStroke()#枠をなし
    fill(142,62,31)#茶色に
    ellipse(xb, yb-50, 350, 350)#顔
    ellipse(xb-120,yb-190,100,100)#右耳
    ellipse(xb+120,yb-190,100,100)#左耳
    fill(255)#白色に
    ellipse(xb,yb+20,150,150)#口回り

def cat(xc,yc):
    noStroke()#枠なし
    fill(100)#灰色に
    ellipse(xc, yc-80, 350, 300)#顔
    triangle(xc-180,yc-270,xc-60,yc-210,xc-170,yc-120)#左耳
    triangle(xc+60,yc-220,xc+180,yc-270,xc+170,yc-120)#右耳

def draw():
    background(255)
    
    if mouseX <= 500:
        dog(mouseX, mouseY)
        
    elif mouseX <= 1000:
        cat(mouseX, mouseY)
        
    else:
        ber(mouseX, mouseY)
            
    face(mouseX, mouseY)
