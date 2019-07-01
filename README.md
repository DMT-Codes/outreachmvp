def setup():
    def homescreen(HR,WR,HS,WS):
        background(100,149,237)
        size(640,900)
        fill(0,201,87)
        rect(0,100,400,100) #1 st rectangle
        fill(0,201,87)
        rect(0,300,400,100) #2nd rectangle
        fill(0,201,87)
        rect(0,500,400,100) #3rd rectangle 
        #fill(0,201,87)
        #rect(0,700,400,100) #4th rectangle
        fill(0,201,87)
        rect(540,150,500,100) # 1st square
        rect(540,350,500,100) #2nd square
        rect(540,550,500,100) #3rd square
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
        
        
        
        #dms page
def setup():
    size(640,900)
    background(255,255,255)
    DM_Page()
def DM_Page(): 
    messages="messages..."
    Name="name of person"
    back_button="back"
    #profile circle
    stroke(0,0,0)
    ellipse(240,30,40,40)
    rect(400,869,30,30)
    fill(0,0,0)
    ellipse(410,875,5,5)
    #name of person profile
    fill(0,0,0)
    textSize(26)
    text(Name,280,40)
    textSize(15)
    text(back_button,10,40)
    #messages on the bottom
    textSize(20)
    text(messages,280,890)
    #line accross
    line(5,60,690,60)
    line(440,880,470,880)
    

        
        
        

        
        
        

    
   
    
        
