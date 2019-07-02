def setup():
    size(640,900)

def search():

    background(255)
    search= loadImage('Search.png')
    rect(100,130,400,30,10)
    rect(0,0,640,100)
    fill(0)
    textSize(50)
    text('Search',200,85)
    image(search,365,40,width/20,height/19)
    text('...',110,150)
    fill(100)
    textSize(20)
    text('Top Searches',10,220)
    y=225
    noFill()
    while y< 900:
        rect(-1,y,650,60)
        y+=60
    textSize(30)
    text('Computer Science',50,270)
    text('Enviromental Science',50,330)
    text('Visual/Performing Arts',50,390)
    text('Architecture',50,450)
def draw():
    search()
