def setup(): 
   
    size(640,900) 
def profile():
    test=loadImage("test1.jpg")
    back=loadImage('back_button.png')
    fill(255)
    background(100,149,237) 
    rect(320,100,300,300)#profile photo
    rect(40,500,550,250)
    textSize(32)
    text('Age/Gender',50,170)
    text('Hometown',50,220)
    text('Bio',50,270)
   
    fill(0)
    text('Resume',230,550)
    
    fill(255)
    textSize(50)
    text('Major/School',130,475)
    textSize(72)
    text("Lil Swahili",150,70)
    fill(0,255,0)
    rect(0,810,200,130,7)
    fill(255,0,0)
    rect(450,810,200,130,7) 
    fill(0)
    textSize(50)
    text('Donate',10,875)
    text('Next',480,875)
    image(test,320,100,width/2,height/3)
    image(back,10,10,width/15,height/20)
def draw():
    profile()
