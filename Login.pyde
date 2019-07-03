def setup(): 
   
    size(640,900) 
def login():
    test=loadImage("Logoo.png")
    
    fill(255)
    strokeWeight(1)
    background(100,149,237) 
    image(test,10,20)
    rect(130,400,400,50)
    rect(130,500,400,50)
    fill(255)
    textSize(32)
    text('Username',100,385)
    text('Password',100,485)
    fill(0,255,0)
    
    rect(260,600,130,50)#Log in button
    fill(0)
    textSize(30)
    text('Login',280,635)
    noFill()
    noStroke()
    rect(470,578,100,30)#sign up button
    fill(0)
    stroke(0)
    strokeWeight(3)
    line(480,605,550,605)
    textSize(20)
    text('Signup?',480,600)
def draw():
    login()
