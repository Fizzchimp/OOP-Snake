import turtle, random
import time
width = height = 720

class Snake:

  def __init__(self):
    self.snakeHead = turtle.Turtle()
    self.InitialiseSnake()
    self.snakeBody = []

  def InitialiseSnake(self):
    self.snakeHead.speed(0)
    self.snakeHead.shape("square")
    self.snakeHead.color("black")
    self.snakeHead.penup()
    self.snakeHead.goto(0, 100)
    self.snakeHead.direction = "stop"

  def go_up(self):
    if self.snakeHead.direction != "down":
      self.snakeHead.direction = "up"

  def go_down(self):
    if self.snakeHead.direction != "up":
      self.snakeHead.direction = "down"

  def go_right(self):
    if self.snakeHead.direction != "left":
      self.snakeHead.direction = "right"

  def go_left(self):
    if self.snakeHead.direction != "right":
      self.snakeHead.direction = "left"

  def move(self):
    for i in range(len(self.snakeBody) - 1, 0, -1):
      x = self.snakeBody[i - 1].xcor()
      y = self.snakeBody[i - 1].ycor()
      self.snakeBody[i].goto(x, y)

    if self.snakeBody != []:
      self.snakeBody[0].goto(self.snakeHead.xcor(), self.snakeHead.ycor())

    if self.snakeHead.direction == "up":
      self.snakeHead.sety(self.snakeHead.ycor() + 20)

    if self.snakeHead.direction == "down":
      self.snakeHead.sety(self.snakeHead.ycor() - 20)

    if self.snakeHead.direction == "right":
      self.snakeHead.setx(self.snakeHead.xcor() + 20)

    if self.snakeHead.direction == "left":
      self.snakeHead.setx(self.snakeHead.xcor() - 20)

  def grow(self):
    part = turtle.Turtle()
    part.speed(0)
    part.shape("square")
    part.color("light sea green")
    part.penup()
    part.goto(self.snakeHead.xcor(), self.snakeHead.ycor())
    self.snakeBody.append(part)

  def update(self):
    self.move()
    self.sideSwap()

  def bodyColCheck(self):
    for part in self.snakeBody:
      if part.distance(self.snakeHead) < 15:
        return True

  def die(self):
    self.snakeHead.goto(0, 100)
    self.snakeHead.direction = "stop"
    for part in self.snakeBody:
      part.hideturtle()
    self.snakeBody = []

  def sideSwap(self):
    if self.snakeHead.xcor() > width / 2:
      self.snakeHead.goto(-width / 2, self.snakeHead.ycor())
      self.snakeHead.direction = "right"

    elif self.snakeHead.xcor() < -width / 2:
      self.snakeHead.goto(width / 2, self.snakeHead.ycor())
      self.snakeHead.direction = "left"

    if self.snakeHead.ycor() > height / 2:
      self.snakeHead.goto(self.snakeHead.xcor(), -height / 2)
      self.snakeHead.direction = "up"

    elif self.snakeHead.ycor() < -height / 2:
      self.snakeHead.goto(self.snakeHead.xcor(), height / 2)
      self.snakeHead.direction = "down"


class Food:

  def __init__(self):
    self.item = turtle.Turtle()
    self.item.speed(0)
    self.item.shape("circle")
    self.item.color("crimson")
    self.item.penup()
    self.item.shapesize(0.5, 0.5)
    self.item.goto(0, 0)
    self.move = False

  def setMove(self, decision):
    self.move = decision

  def relocate(self):
    x = random.randint((-width // 40) + 1, (width // 40 - 1))
    y = random.randint((-height // 40 + 1), (height // 40 - 1))
    self.item.goto(20 * x, 20 * y)


class Wall:
  def __init__(self):
    self.item = turtle.Turtle()
    self.item.speed(0)
    self.item.shape("square")
    self.item.color("slate gray")
    self.item.penup()
    x = random.randint((-width // 40) + 1, (width // 40 - 1))
    y = random.randint((-height // 40 + 1), (height // 40 - 1))
    self.item.goto(20 * x, 20 * y)
  
  def destroy(self):
    self.item.goto(1000, 1000)
    del self.item