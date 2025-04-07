
def setup():
    size(600,400)
    global shar_x,shar_y,shar_dx,shar_dy,ladder_x,score,pause,mode
    shar_x=300
    shar_y=200
    shar_dx=0.5
    shar_dy=0.5
    ladder_x=300
    score=0
    pause=False
    mode="начало"
def keyPressed():
        global pause
        if key == "P" or key == "p" or key == "з" or key == "З":
            if pause == True:
                pause = False
            else:
                pause = True
def mouseClicked():
    global mode,score
    if mode == "начало":
        mode = "игра"
    elif mode == "игра":
        score = 0
        mode = "начало"
        
def draw():
    global shar_x,shar_y,shar_dx,shar_dy,ladder_x,score,pause,mode
    background(150)
    if mode == "начало":
        fill(255)
        rect(225, 150, 150, 100)
        
        fill(0)
        textAlign(CENTER, CENTER)
        textSize(20)
        text(u"Старт", 300, 200)
        
    elif mode == "игра": 
        rect(100, 270, 200, 50)
        fill(0)
        text(u"Перезагрузка", 200,300)
        fill(255)
        if pause == True:
                textAlign(CENTER, CENTER)
                textSize(50)
                text(u"Пауза", 300, 200)
        else:
            
            textSize(20)
            text(u"очки:", 25, 25)
            text(score, 80, 25)
            shar_x = shar_x + shar_dx
            shar_y = shar_y + shar_dy
            if shar_x > 580:
                shar_dx = -shar_dx
            elif shar_x < 20:
                shar_dx = -shar_dx
                
            elif shar_y < 20:
                shar_dy = -shar_dy
                
            ellipse(shar_x,shar_y,20,20)
            rect(ladder_x,380,150,10)
            if shar_y + 10 >= 380 and ladder_x <= shar_x <= ladder_x + 150:
                shar_dy = -random(4,6)        
                shar_dx = random(-5, 5)
                score = score + 1
        
            if shar_y >=380:
                fill(255,0,0)
                textSize(50)
                text(u"ты проиграл",200,200)
                textSize(50)
                text(u"результат:",200,250)
                textSize(50)
                text(score,450,250)
                noLoop()

            if keyPressed and key == CODED:
                    
                if keyCode == LEFT: 
                        ladder_x = ladder_x - 10        
                if keyCode == RIGHT:
                    ladder_x = ladder_x + 10
                    


        


        
    

                
