global value
value=1

def setup():
    size(640,900)
    SearchStatus=True
    ProfileStatus=True
    My_Donations= True
    homescreen()

    
def homescreen():
    background(100,149,237)
    logo=loadImage("Logoo.png")
    image(logo,0,800)
    fill(0,201,87)
    rect(0,100,400,100) #1 st rectangle
    fill(0,201,87)
    rect(0,300,400,100) #2nd rectangle
    fill(0,201,87)
    rect(0,500,400,100) #3rd rectangle 
    #fill(0,201,87)
    #rect(0,700,400,HR) #4th rectangle
    fill(0,201,87)
    rect(540,150,100,100) # 1st square
    rect(540,350,100,100) #2nd square
    rect(540,550,100,100) #3rd square
    fill(255)
    textSize(32)
    text("Search",50,150)
    text("Profile",50,350)
    text("My Donations",50,550)
    textSize(20)
    text("Top",543,180)
    text("Supporter",543,210)
    text("Messages",543,385)
    text("Settings",543,585)

def profilepage():
    background(100,149,237)
    textSize(60)
    text("Kobe Petrus",190,70)
    rect(340,130,300,300)
    textSize(26)
    text("Age:",10,150)
    text("Location:",10,210)
    text("Bio:",10,270)
    text("Recent Donation:",10,520)
    text("$100",230,520)
    textSize(19)
    text("37",10,175)
    text("Ohio,United States",10,230)
    text("Software Engineer who gives back.",10,290)
    text1=loadImage("kobe.png")
    image(text1,341,131,299,299)
    x= loadImage('back_button.png')
    image(x, 10, 10, width/15, height/20)
def search():
    test=loadImage("test1.jpg")
    back=loadImage('back_button.png')
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
    textSize(20)
    text('I like my books like',50,315)
    text('i like my meat. JUICY!!',50,340)
    

    text('Major/School',50,430)
    textSize(30)
    text('Enviromental Science,Harvard University',50,475)
    textSize(72)
    text("Lil Swahili",150,70)
    fill(0,255,0)
    rect(0,810,200,130,7)
    fill(255,0,0)
    rect(450,810,200,130,7) 
    fill(0)
    textSize(30)
    text('Resume',230,550)
    textSize(50)
    text('Donate',10,875)
    text('Next',480,875)
    image(test,320,100,width/2,height/3)
    image(back,10,10,width/15,height/20)
    
def mydonations():
    background(100,149,237) 
    x= loadImage('back_button.png')
    textSize(50)
    text("STATS", 240, 150)
    rect(30, 320, 250, 500)
    textSize(25)
    text("MY DONATIONS", 60, 300)
    text("TOP DONATIONS", 370, 300)
    rect(350, 320, 250, 500)
    image(x, 10, 10, width/15, height/20)
    
def DMS():
    background(255) 
    profile_pic=loadImage('back_button.png')
    #profile circle
    stroke(0,0,0)
    ellipse(240,30,40,40)
    noFill()
    rect(0,860,900,40)
    #name of person profile
    fill(0,0,0)
    textSize(26)
    text("Lil Swahili",280,40)
    textSize(15)
    image(profile_pic, 10, 10, width/15, height/20)
    #messages on the bottom
    textSize(20)
    text("messages",10,890)
    #line accross
    line(5,60,690,60)
    #makingthepictureicon
    noFill()
    rect(470,865,30,30)
    fill(0,0,0)
    ellipse(475,870,5,5)
    line(470,875,500,875)
    

     
def draw():
    global value
    if mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed:
        homescreen()
        value=1
        print (value)
    if value == 1 and mouseX>0 and mouseX<400 and mouseY>100 and mouseY<200 and mousePressed:
        search()
        value=2
        print (value)
    if value == 1 and mouseX>0 and mouseX<400 and mouseY>300 and mouseY<400 and mousePressed :
        profilepage()
        value = 3
        print (value)
    if value == 1 and mouseX>0 and mouseX<400 and mouseY>500 and mouseY<600 and mousePressed :
        mydonations()
        value = 4
        print (value)
    #if value == 1 and mouseX>540 and mouseX<640 and mouseY>350 and mouseY<450 and mousePressed :
      #  DMS()
       # value = 5
        #print (value)
    if value == 1 and mouseX>540 and mouseX<640 and mouseY>350 and mouseY<450 and mousePressed :
        DMS()
        value = 5
        print (value)
