def setup():
    background(100,149,237)
    size(640,900)
    donations_screen()

def donations_screen():
    x= loadImage('back.png')
    textSize(50)
    text("STATS", 240, 150)
    rect(30, 320, 250, 500)
    textSize(25)
    text("MY DONATIONS", 60, 300)
    text("TOP DONATIONS", 370, 300)
    rect(350, 320, 250, 500)
    image(x, 10, 10, width/15, height/20)
