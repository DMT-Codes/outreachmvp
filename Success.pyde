def setup():
    size(640,900) 
def success():
    test=loadImage("Logoo.png")
    font=loadFont('Apple-Chancery-48.vlw')
    orgin=loadFont('AppleSymbols-48.vlw')
    fill(255)
    background(100,149,237) 
    image(test,10,20)
    fill(255)
    textFont(orgin,40)
    text('Back to Login',230,600)
    stroke(255)
    line(225,610,420,610)
    noStroke()
    noFill()
    rect(220,560,210,60)#back to Login 
    fill(0,255,0)
    textFont(font,80)
    text('Sign Up',190,400)
    text('Successful',160,480)
def draw():
    success()
