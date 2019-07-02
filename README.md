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
def top_supporters():
    background(100, 149, 237)
    x= loadImage('back.png')
    textSize(50)
    text("TOP SUPPORTERS", 110, 120)
    textSize(25)
    text("Top One Time", 45, 250 )
    text ("Top Consistant", 400, 250)
    image(x, 10, 10, width/15, height/20)
    stroke(255)
    line(45, 255, 215, 255)
    line(400, 255, 585, 255)
    
    
    
    
    #dms page
def setup():
    size(640,900)
    background(255,255,255)
    DM_Page()
def DM_Page(): 
    messages="messages..."
    Name="John Doe"
    back_button="back"
    send_button="Send"
    background(255) 
    #profile circle
    stroke(0,0,0)
    ellipse(240,30,40,40)
    noFill()
    rect(0,860,900,40)
    #name of person profile
    fill(0,0,0)
    textSize(26)
    text(Name,280,40)
    textSize(15)
    #messages on the bottom
    textSize(20)
    text(messages,10,890)
    text(send_button,550,890)
    #line accross
    line(5,60,690,60)
    #makingthepictureicon
    noFill()
    rect(470,865,30,30)
    fill(0,0,0)
    ellipse(475,870,5,5)
    ellipse(485,870,5,5)
    ellipse(495,870,5,5)
    line(470,875,500,875)
    textSize(10)
    text("cam",472,885)
    #helpicon
    noFill()
    ellipse(600,30,25,25)
    textSize(25)
    fill(0,0,0)
    text("i",597,40)
    #voiceicon
    noFill()
    ellipse(450,875,10,20)
    line(450,886,450,895)
    line(440,896,457,896)
    line(445,875,455,875)
    line(445,871,455,871)
    line(445,879,455,879)
    line(445,873,455,873)
    line(445,878,455,878)
    #dm messaging
    noFill()
    ellipse(30,190,40,40)
    rect(55,165,465,50)
    textSize(15)
    text("Thank you for the donation for college. I really appreciate it!",60,190)
    ellipse(590,290,40,40)
    rect(100,285,465,50)
    text("Your welcome, good luck in college! Keep me updated!!",130,315)
    
    
    
    
    
    def setup():
    size(640,900)
    settingspage()    
def settingspage(): 
    background(100,149,237) 
    img= loadImage('backblack.png')
    logo=loadImage("Logoo.png")
    image(logo,0,50)
    anonymous="Anonymous"
    Name="Settings"
    Faq="FAQ"
    Change_Account="Change Account"
    About="About Us"
    music="Music"
    yes_button= "Yes"
    no_button= "No"
    privacy= "Privacy"
    notifications="Notifications"
    security="Security"
    log_out="Log Out"
    pay_pal="Pay Pal Settings"
    your_activity="Your Activity"
    Tos="Terms of Service"
    share_app="Share"
    Other=""
    invite_friends=" Invite Friends"
    dm_settings="DM Settings"

    #settings on top
    textSize(26)
    text(Name,280,40)
    textSize(15)
    image(img, 10, 10, width/15, height/20)
    #different setting topics
    textSize(20)
    text(anonymous,50,150)
    text(your_activity,50,200)
    text(invite_friends,50,250)
    text(music,50,300)
    text(security,50,350)
    text(notifications,50,400)
    text(dm_settings,50,450)
    text(Change_Account,50,500)
    text(pay_pal,50,550)
    text(share_app,50,600)
    #text(Other,50,650)
    text(Tos,50,670)
    text(About,50,725)
    text(Faq,50,790)
    text(log_out,50,850)
    #lineacross
    line(0,60,640,60)
    line(0,165,640,165)
    line(0,215,640,215)
    line(0,265,640,265)
    line(0,315,640,315)
    line(0,365,640,365)
    line(0,415,640,415)
    line(0,465,640,465)
    line(0,515,640,515)
    line(0,565,640,565)
    line(0,615,640,615)
    #line(0,665,640,665)
    
