from uib_inf100_graphics import *

def app_started(app):

    
   
    app.refresh=True
    app.main_color = "#800d0d" 
    app.loan=False
    app.advice=False
    app.count = 0
    app.egenandel=0
    app.margin=25
    app.page="front"
    app.front_page_buttons = [
        [150,20,180,40,"Lån",loan_calc],
        [230,20,310,40,"Rådgivning", advice_page],
        [340,20,390,40,"om oss", about_us],
        [8,18,90,46,"",front_page],
    ]
    app.buttons = [
        # [x1, y1, x2, y2, "Navn på knapp", funksjon]
        [app.width*0.15, app.height*0.25, app.width*0.25, app.height*0.30, "-", decrease],
        [app.width*0.35,app.height*0.25, app.width*0.45, app.height*0.30, "+", increase],
        
        #[200,20,240,40,"Lån",add_23]
    ]
    # Knapper i top bar
    app.choices= [
        [200,30,220,40,"Lån",loan_calc]]
    

# increases sum of loan
def increase(app):
    app.count += 25_000
# decreases sum of loan
def decrease(app):
    
    app.count -= 25_000
    if app.count<0:
        app.count=0
def loan_calc(app):
    app.page="loan"

    
def advice_page(app):
    app.page="advice"

def about_us(app):
    app.page="about"

def front_page(app):
    app.page="front"
    

def key_pressed(app,event):

    if event.key=="1":
        app.count=1_000_000
    if event.key=="2":
        app.count=2_000_000
    if event.key=="3":
        app.count=3_000_000
    if event.key=="4":
        app.count=4_000_000
    if event.key=="5":
        app.count=5_000_000
    if event.key=="6":
        app.count=6_000_000
    if event.key=="7":
        app.count=7_000_000
    if event.key=="8":
        app.count=8_000_000
    if event.key=="9":
        app.count=9_000_000
    
    
    
    
    
    


def add_23(app):
    app.frontpage=not app.frontpage


def point_in_rectangle(x1, y1, x2, y2, x, y):
    return (min(x1, x2) <= x <= max(x1, x2)
        and min(y1, y2) <= y <= max(y1, y2))

def execute_button_action_if_clicked(app, button, mouse_x, mouse_y):
    x1, y1, x2, y2, label, func = button
    if point_in_rectangle(x1, y1, x2, y2, mouse_x, mouse_y):
        func(app)

def mouse_pressed(app, event):
    for button in app.buttons:
        execute_button_action_if_clicked(app, button, event.x, event.y)
    for button in app.front_page_buttons:
        execute_button_action_if_clicked(app, button, event.x, event.y)

    



def draw_button(canvas, button):
    x1, y1, x2, y2, label, func = button
    color="#e5f2ff"
    if label=="":
        color=""

    
    canvas.create_rectangle(x1, y1, x2, y2, fill=color,outline="black")
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    canvas.create_text(mid_x, mid_y, text=label, fill="black",)


def redraw_all(app, canvas):
    
    if app.page=="front":
        canvas.create_rectangle(0,0,app.width,app.height,fill="#e5f2ff")
        canvas.create_text(app.width/2, app.height*0.3, text="Velkommen",
                                                    font="Sans 26",fill="#644e85")
        canvas.create_text(app.width/2, app.height*0.4, text=f"Vi er banken som er her for deg når du trenger det",
                                                    font="Sans 20",fill="#644e85")  
        canvas.create_text(app.width/2, app.height*0.5, text=f"Bruk knappene øverst for å navigere på siden\nTrykk på logoen for å returnere til forsiden",
                                                                                                               
                                                    font="Sans 12",fill="#644e85")                                            
        for button in app.front_page_buttons:
            draw_button(canvas, button)
        #Top bar                                             
        canvas.create_rectangle(0,2,app.width,60,fill="#644e85")      
        #Brand name                                      
        canvas.create_text(50,30, text=f"BigBank",
                                                    font="Sans 20")  
        for button in app.front_page_buttons:
            draw_button(canvas, button)                                         
    
    if app.page=="advice":
         #Top bar                                             
        canvas.create_rectangle(0,2,app.width,60,fill=app.main_color)      
        #Brand name                                      
        canvas.create_text(50,30, text=f"BigBank",
                                                    font="Sans 20")  
         #Grå bakgrunn
        canvas.create_rectangle(0,0,app.width,app.height,fill="#e6e4e3")
        #Hvit boks med innhold
        canvas.create_rectangle(40,40,app.width-40,app.height-40,fill="#ffffff")
         #Top bar                                             
        canvas.create_rectangle(0,2,app.width,60,fill="#644e85")      
        #Brand name                                      
        canvas.create_text(50,30, text=f"BigBank",
                                                    font="Sans 20") 
        for button in app.front_page_buttons:
            draw_button(canvas, button)  
        canvas.create_text(app.width/2, app.height*0.18, text=f"Her har du en oversikt over våre rådgivere:",
                                                        font="Arial 24",fill="black")
        canvas.create_text(app.width/3, app.height*0.3, text=f"Randi Jensen : rj@BigBank.no\nTlf : 95278141",
                                                        font="Arial 20",fill="black")
        canvas.create_text(app.width/3, app.height*0.4, text=f"Fredrik Foo : FF@BigBank.no\nTlf : 67542901",
                                                        font="Arial 20",fill="black")
        canvas.create_text(app.width/3, app.height*0.5, text=f"Faizar Tjekile : ft@BigBank.no\nTlf : 79876578",
                                                        font="Arial 20",fill="black")

    if app.page=="about":
         #Top bar                                             
        canvas.create_rectangle(0,2,app.width,60,fill=app.main_color)      
        #Brand name                                      
        canvas.create_text(50,30, text=f"BigBank",
                                                    font="Sans 20")  
         #Grå bakgrunn
        canvas.create_rectangle(0,0,app.width,app.height,fill="#e6e4e3")
        #Hvit boks med innhold
        canvas.create_rectangle(40,40,app.width-40,app.height-40,fill="#ffffff")
         #Top bar                                             
        canvas.create_rectangle(0,2,app.width,60,fill="#644e85")      
        #Brand name                                      
        canvas.create_text(50,30, text=f"BigBank",
                                                    font="Sans 20") 
        for button in app.front_page_buttons:
            draw_button(canvas, button)  
        canvas.create_text(app.width/2, app.height*0.18, text=f"Fersk bank Fersk utvikler\n",
                                                        font="Arial 24",fill="black")

        """"  canvas.create_text(app.width/3, app.height*0.3, text=f"Randi Jensen : rj@BigBank.no\nTlf : 95278141",
                                                     font="Arial 20",fill="black")
        canvas.create_text(app.width/3, app.height*0.4, text=f"Fredrik Foo : FF@BigBank.no\nTlf : 67542901",
                                                        font="Arial 20",fill="black")
        canvas.create_text(app.width/3, app.height*0.5, text=f"Faizar Tjekile : ft@BigBank.no\nTlf : 79876578",
                                                        font="Arial 20",fill="black")
    """

    if app.page=="loan":
        #Grå bakgrunn
        canvas.create_rectangle(0,0,app.width,app.height,fill="#e6e4e3")
        #Hvit boks med innhold
        canvas.create_rectangle(40,40,app.width-40,app.height-40,fill="#ffffff")
        # tegn knappene
        for button in app.buttons:
            draw_button(canvas, button)
        
        # tegn telleren
        canvas.create_rectangle(0,2,app.width,60,fill="#644e85")      
        #Brand name                                      
        canvas.create_text(50,30, text=f"BigBank",
                                                    font="Sans 20")  
        for button in app.front_page_buttons:
            draw_button(canvas, button)                            
        canvas.create_text(app.width/4, app.height*0.13, text=f"Lånekalkulator",
                                                        font="Arial 20",fill="black")
        canvas.create_text(app.width/2.6, app.height*0.20, text=f"Bruk nummertastene for å angi anntall millioner\nog finjuster med pluss og minus",
                                                        font="Arial 13 ",fill="black")                                                
        canvas.create_text(app.width/4, app.height*0.4, text=f"Kjøpesum: \n {app.count}",
                                                        font="Arial 20",fill="black")
        canvas.create_text(app.width/4, app.height*0.5, text=f"Egenandel:\n {app.count*0.15}",
                                                        font="Arial 20",fill="black")
        canvas.create_text(app.width/3, app.height*0.6, text=f"Måndelig beløp (3.8%):\n {round((((app.count - (app.count*0.15))*0.038/12)+4240),1)}",
                                                        font="Arial 20",fill="black")
        canvas.create_text(app.width/3, app.height*0.8, text=f"For beløp over 9 millioner:\nkontakt rådgiver for egen veiledning",
                                                        font="Arial 13",fill="black")
run_app(width=600, height=600)