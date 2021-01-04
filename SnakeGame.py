import turtle
import time
import random

delay = 0
scor = 0

# set up game screen
root = turtle.Screen()
root.title("snake game by ishan")
root.setup(width = 600 , height = 600)
root.bgcolor("black")
#root.tracer(0)

# snake hade
head = turtle.Turtle()
head.speed(1)
head.color("green")
head.shape("circle")
head.penup()
head.goto(0,0)
head.direction = "up"

#food
food = turtle.Turtle()
food.speed(0)
food.color("red")
food.shape("circle")
food.penup()
food.goto(0,100)



#function
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"     

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)

    elif head.direction == "down":
        y = head.ycor()
        head.sety(y-20)

    elif head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

    elif head.direction == "left":
        x = head.xcor()
        head.setx(x-20)

body = []  


#input from keybord
root.listen()
root.onkeypress(go_up,"w")
root.onkeypress(go_down,"s")
root.onkeypress(go_right,"d")
root.onkeypress(go_left,"a")


while True:

    if head.xcor() < -290 or head.xcor() > 290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)

        for i in body:
            i.goto(1000,1000)
        
        print("your scor is = " + str(scor))
        body.clear()
        break

    for i in body:
        if i.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)

            for i in body:
                i.goto(1000,1000)

            print("your scor is = " + str(scor))
            body.clear()
            break



    if head.distance(food) < 20:
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(x,y)

        #add body 
        new_body = turtle.Turtle()
        new_body.speed(0)
        new_body.shape("circle")
        new_body.color("green")
        new_body.penup()
        body.append(new_body)

        scor = scor + 1

    for i in range(len(body)-1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)

    if len(body) > 0:
        x = head.xcor()
        y = head.ycor()
        body[0].goto(x,y)

    move()
    
    #time.sleep(delay)

root.mainloop()
