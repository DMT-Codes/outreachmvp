def setup():
    size(640,900) 
    
def signup():
    test=loadImage("Logoo.png")
    fill(255)
    background(100,149,237) 
    image(test,10,20)
    y=220
    while y<700:
        rect(130,y,400,40)
        y+=80
    textSize(30)
    text('Full Name:',100,200)
    text('Create Username:',100,290)
    text('Create Password:',100,372)
    text('Verify Password:',100,452)
    text('Email:',100,530)
    text('Verify Email:',100,610)
    fill(0,255,0)
    rect(260,720,130,50)
    fill(0)
    text('Sign In',280,755)
def draw():
    signup()
    #rect1= 130,220,400,40
    #rect2= ,300,,
    #rect3= ,380
    #rect4= ,460,,
    #rect5= ,540,,
    #rect6= ,620,,
