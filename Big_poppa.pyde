def setup():
    size(640,900)
    test=loadImage("baby.jpg")
    back=loadImage('back_button.png')
    resume=loadImage('resume.jpeg')
    fill(255)
    background(100,149,237) 
    rect(320,100,300,300)#profile photo
    rect(40,500,550,250)
    textSize(32)
    text('Age/Gender',50,130)
    text('Hometown',50,200)
    text('Bio',50,280)
    textSize(25)
    text('19',50,165)
    text('Toronto',50,235)
    textSize(22)
    text('I am one to strive for ',50,315)
    text('success for myself and',50,340)
    text('others.',50,365)
    image(resume,40,500,width/1.1,height/3)

    text('Major/School',50,430)
    textSize(30)
    text('Enviromental Science,Harvard University',50,475)
    textSize(72)
    text("Big Poppa",150,70)
    fill(0,255,0)
    rect(0,810,200,130)
    fill(255,0,0)
    rect(450,810,200,130) 
    fill(0)
    textSize(50)
    text('Donate',10,875)
    text('Next',480,875)
    fill(255)
    image(test,325,100,width/2.2,height/3)
    image(back,10,10,width/15,height/20)
    
