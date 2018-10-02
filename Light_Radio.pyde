def setup():
    global loading_time,loading_movement,loading_screen,click_start,NiceforWhatmusic_page, description_movement, reverse_description
    loading_movement = 0
    loading_time = 0
    loading_screen = True
    click_start = False
    NiceforWhatmusic_page = False
    description = False
    description_movement = 600
    reverse_description = 450
    size(1000,600)
    background(0)
def draw():
    global loading_time, loading_movement,loading_screen,click_start,NiceforWhatmusic_page, description, description_movement, reverse_description
    if loading_screen:
        textSize(32)
        text("Loading",430,270)
        noFill()
        stroke(255)
        rect(370,289,250,22)
        fill(255)
        rect(370,290,loading_movement,20)
        if loading_time >= 10 and loading_movement <= 250:
            loading_movement = loading_movement + 2
        if loading_movement > 250:
            loading_screen = False
            click_start = True
            background(0)
    loading_time = loading_time + 1
    if click_start:
        fill(255)
        textSize(48)
        text("Light Radio", 360,270)
        noFill()
        stroke(255)
        rect(440,380,100,50)
        textSize(30)
        text("START",444,413)
        if mouseX>=440 and mouseY >380 and mouseX <=540 and mouseY<=430:
            fill(30,255,50)
            rect(440,380,100,50)
            if mousePressed:
                background(0)
                click_start = False
                NiceforWhatmusic_page = True
    if NiceforWhatmusic_page:
        img = loadImage("Scorpion.jpg")
        image(img,370,200)
        descriptionF()
        if mouseY >=450:
            fill(255)
            textSize(48)
            text("Nice For What", 30, 500)
        
def descriptionF():
    global loading_time, loading_movement,loading_screen,click_start,music_page, description, description_movement, reverse_description
    description = True      
    if description:
        if mouseY >= 450 and description_movement >= 450:
            noStroke()
            fill(100)
            rect(0,450,1000,1000)
                #description_movement = description_movement - 1
        if mouseY <=450 and description_movement >= 449:
            noStroke()
            fill(0)
            rect(0,450,1000,reverse_description)
            reverse_description = description_movement + 1

        
            

                

            
    print description_movement

    
    
