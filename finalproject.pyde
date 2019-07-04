global searchindex
searchindex=0


import webbrowser

FACEBOOK_APP_ID=str('<1088529684669523>')
FACEBOOK_APP_MONEY   = str('your app money')

def setup():
    size(640,900)
    login()
    frameRate(10)

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
    fill(255)
    fill(0)
    stroke(0)
    strokeWeight(3)
    line(480,605,550,605)
    textSize(20)
    text('Signup?',480,600)
    fill(255)
    
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
    text('Sign Up',280,755)
    back=loadImage('back_button.png')
    image(back, 10, 10, width/15, height/20)
    fill(255)
    
    
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
    p=loadImage("ProfilePagenew.png")
    image(p, 0, 0, width, height)
    textSize(60)
    text("Kobe Petrus",30,150)
    textSize(26)
    text("Recent Donation: $1",30,200)
    text("$100",230,520)
    textSize(30)
    fill(0,0,0)
    text("86",110,325)
    textSize(25)
    text("Ohio,United States",375, 325)
    textSize(30)
    text("Software Engineer who gives back.",110,380)
    text("CEO and founder of Micropplesoft Inc.", 22, 380+50)
    text("Looking to help underprivileged students", 22, 380+100)
    text("interested in tech oriented degrees fund", 22, 380+150)
    text("their education. I want to give back to", 22, 380+200)
    text("my community. We need more people", 22, 380+250)
    text("like me involved in the advancemnent of", 22, 380+300)
    text("technology.", 22, 380+350)
    text1=loadImage("kobe.png")
    image(text1,397,15,228,244)
def search():
    test=loadImage("baby.jpg")
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
    rect(0,810,200,130)
    fill(255,0,0)
    rect(450,810,200,130) 
    fill(0)
    textSize(30)
    text('Resume',230,550)
    textSize(50)
    text('Donate',10,875)
    text('Next',480,875)
    fill(255)
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
    

     
def top_supporters():
    background(100, 149, 237)
    x= loadImage('back.png')
    textSize(50)
    text("TOP SUPPORTERS", 110, 120)
    textSize(25)
    text("Top One Time Donations", 45, 250 )
    text ("Top Donations", 400, 250)
    image(x, 10, 10, width/15, height/20)
    stroke(255)
    line(45, 255, 215, 255)
    line(400, 255, 585, 255)
    
    
def DmPageFirst(): 
    background(255,255,255) 
    img= loadImage('backblack.png')
    logo=loadImage("Logoo.png")
    name1="Peter Parker"
    Name="DM Page"
    name2="Clark Kent"
    name3="Barry Allen"
    name4="John Stewart"
    name5="John Jons"
    name6= "Bruce Wayne"
    name7="John Doe"
    name8="Tony Stark"
    fill(0,0,0)
    #settings on top
    textSize(26)
    text(Name,280,40)
    textSize(15)
    image(img, 10, 10, width/15, height/20)
    #different setting topics
    textSize(20)
    text(name1,50,150)
    text(name2,50,250)
    text(name3,50,350)
    text(name4,50,450)
    text(name5,50,550)
    text(name6,50,650)
    text(name7,50,750)
    text(name8,50,850)
    #text under the names
    textSize(15)
    text("Thanks for the donation!",50,180)
    text("I would like to earn some tuition money!",50,280)
    text("How much would you like to donate?",50,380)
    text("I'm looking for at least $10,000",50,480)
    text("I can give you as much you need!",50,580)
    text("What college are you going to?",50,680)
    text("I need money for college, can you help?",50,780)
    text("Hi,how are you?",50,880)
    #lineacross
    line(0,60,640,60)
    line(0,185,640,185)
    line(0,285,640,285)
    line(0,385,640,385)
    line(0,485,640,485)
    line(0,585,640,585)
    line(0,685,640,685)
    line(0,785,640,785)
    line(0,885,640,885)
    #circles around the names
    noFill()
    ellipse(20,150,30,30)
    ellipse(20,250,30,30)
    ellipse(20,350,30,30)
    ellipse(20,450,30,30)
    ellipse(20,550,30,30)
    ellipse(20,650,30,30)
    ellipse(20,750,30,30)
    ellipse(20,850,30,30)
    
    
   
   
    #line(0,665,640,665)
    
    #dms page
def DM_Page(): 
    messages="messages..."
    Name="Peter Parker"
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
    text("messages",10,890)
    text("send",550,890)
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
    ellipse(590,310,40,40)
    rect(100,285,465,50)
    text("Your welcome, good luck in college! Keep me updated!!",130,315)
    x= loadImage('backblack.png')
    image(x, 10, 10, width/15, height/20)
    
#settingspage    
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
    Other="OTHER"
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
    text(Other,50,650)
    text(Tos,50,700)
    text(About,50,750)
    text(Faq,50,800)
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
    line(0,665,130,665)
    #arrows


def top_supporters():
    background(100, 149, 237)
    x= loadImage('back_button.png')
    textSize(50)
    text("TOP SUPPORTERS", 130, 120)
    textSize(25)
    image(x, 10, 10, width/15, height/20)
    line(130, 130, 550, 130)
    rect(170,300,350,200)
    fill(0,0,0)
    text("Kobe Petrus - $1,000,000", 185, 350)
    text("Ellen Winfrey- $100,000", 185, 400)
    text("God - $12,000", 185, 450)
    fill(255,255,255)
    rect(170,620,350,200)
    fill(0,0,0)
    text("Deantay - $2,000,000", 185, 660)
    text("Kobe Petrus - $1,000,001", 185, 710)
    text("Kav - $13,000", 185, 760)  
    x1=loadImage('topdonations.png')
    image(x1,200,510,300,100)
    x2=loadImage("onetime.png")
    image(x2,200,190,300,100)

def search1():
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
    img= loadImage('backblack.png')
    image(img, 10, 10, width/15, height/20)
    
def donationbutton():
    donate_now=loadImage("DONATE NOW.png")
    fill(255,255,255)
    rect(10,450,600,300)
    textSize(30)
    fill(0,0,0)
    text("Thank you for helping!",150,480)
    text("Donate",240,520)
    textSize(15)
    text("Select an Amount",230,540)
    line(10,545,610,545)
    fill(90,149,237)
    rect(30,550,70,40)
    rect(240,550,70,40)
    rect(140,550,70,40)
    rect(350,550,70,40)
    rect(450,550,100,40)
    fill(255,255,255)
    textSize(20)
    text("$5",55,580)
    text("$50",245,580)
    text("$10",145,580)
    rect(465,580,40,10)
    text("$100",355,580)
    fill(255,255,255)
    textSize(20)
    text(".00",520,585)
    image(donate_now,150,630,300,100)
    rect(465,580,40,10)
    fill(255,255,255)
    rect(450,550,70,40)

     
def draw():
    global searchindex
    
    if searchindex==0 and mouseX>260 and mouseX<390 and mouseY>600 and mouseY<650 and mousePressed:
        homescreen()
        searchindex=1
        print (searchindex)
    
    elif searchindex== 0 and mouseX>470 and mouseX<570 and mouseY>578 and mouseY<608 and mousePressed: #searchbar
        signup()
        searchindex=0
        print (searchindex)
        
    elif searchindex== 1 and mouseX>0 and mouseX<400 and mouseY>100 and mouseY<200 and mousePressed: #searchbar
        search1()
        searchindex=2
        print (searchindex)
    elif searchindex== 2 and mouseX>0 and mouseX<650 and mouseY>300 and mouseY<350 and mousePressed:#searchbar1
        search()
        searchindex=3
        print (searchindex)
    elif searchindex== 3 and mouseX>0 and mouseX<200 and mouseY>810 and mouseY<940 and mousePressed:#donayte button
        donationbutton()
        searchindex=10
        print (searchindex)
    elif searchindex== 1 and mouseX>0 and mouseX<400 and mouseY>300 and mouseY<400 and mousePressed :
        profilepage()
        searchindex= 4
        print (searchindex)
    elif searchindex== 1 and mouseX>0 and mouseX<400 and mouseY>500 and mouseY<600 and mousePressed :
        mydonations()
        searchindex= 5
        print (searchindex)
    elif searchindex== 1 and mouseX>540 and mouseX<640 and mouseY>150 and mouseY<250 and mousePressed :
        top_supporters()
        searchindex= 6
        print (searchindex)
    elif searchindex== 1 and mouseX>540 and mouseX<640 and mouseY>350 and mouseY<450 and mousePressed :
        DmPageFirst()
        searchindex= 7
        print (searchindex)
    elif searchindex== 7 and mouseX>0 and mouseX<640 and mouseY>150 and mouseY<200 and mousePressed :
        DM_Page()
        searchindex= 8
        print (searchindex)
    elif searchindex== 1 and mouseX>540 and mouseX<640 and mouseY>550 and mouseY<650 and mousePressed :
        settingspage()
        searchindex= 9
        print (searchindex)
        #BACKJ BUTTONS
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==2: #homescreen
        homescreen()
        searchindex=1
        print (searchindex)
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==3: #homescreen
        search1()
        searchindex=2
        print (searchindex)
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==4: #homescreen
        homescreen()
        searchindex=1
        print (searchindex)
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==5: #homescreen
        homescreen()
        searchindex=1
        print (searchindex)
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==6: #homescreen
        homescreen()
        searchindex=1
        print (searchindex)
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==7: #homescreen
        homescreen()
        searchindex=1
        print (searchindex)
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==8: #homescreen
        DmPageFirst()
        searchindex=7
    
        print (searchindex)
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==9: #homescreen
        homescreen()
        searchindex=1
        print (searchindex)
    
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==0: #signupback button
        login()
        searchindex=0
        print (searchindex)
    
    elif mouseX>0 and mouseX<50 and mouseY>0 and mouseY<50 and mousePressed and searchindex==10: #signupback button
        search()
        searchindex=3
        print (searchindex)
        
    #paypal link
    elif mouseX>150 and mouseX<550 and mouseY>630 and mouseY<850 and mousePressed and searchindex==10: #signupback button
        search()
        searchindex=3
        print (searchindex)
        webbrowser.open('https://www.paypal.me/outreachcssi')
        
            
