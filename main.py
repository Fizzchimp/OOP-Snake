from window import *
from objects import *
import time

HEIGHT = WIDTH = 720

class Game:

  def __init__(self, highScore):

    self.window = Window(WIDTH, HEIGHT)
    self.wall = []
    self.snake = Snake()
    self.food = Food()
    self.playerScore = 0
    self.highScore = highScore

  def keyBoardListener(self):
    self.window.screen.listen()
    self.window.screen.onkey(self.snake.go_up, "Up")
    self.window.screen.onkey(self.snake.go_down, "Down")
    self.window.screen.onkey(self.snake.go_left, "Left")
    self.window.screen.onkey(self.snake.go_right, "Right")

  def die(self):
    time.sleep(1)
    self.snake.die()
    self.playerScore = 0
    while self.wall != []:
      self.wall[0].destroy()
      self.wall.pop(0)
    self.wall = []
    self.food.item.goto(0, 0)
  



  def worldUpdate(self):
    
    if self.snake.bodyColCheck() == True:
      self.die()
      
    if self.snake.snakeHead.distance(self.food.item) < 15:
      self.wall.append(Wall())
      self.food.relocate()
      self.snake.grow()
      self.playerScore += 1
    
    for wall in self.wall:
        if self.snake.snakeHead.distance(wall.item) < 15:
            self.die()
      


    
    if self.highScore < self.playerScore:
      self.highScore = self.playerScore



def runGame(self):
  while True:
    self.window.screen.update()
    self.keyBoardListener()

    self.snake.update()
    self.worldUpdate()
    
    
    self.window.drawHud(self.playerScore, self.highScore)
    time.sleep(0.1)


def writeScore()


dict= {}
with open("scores.txt", "r") as file:
    for x in file.readlines():
        x = x.split(":")
        dict[x[0]] = x[1]


userName = input("Enter username here\n: ").strip(" ")

if userName == "":
    highScore = 0

#runGame(Game(highScore))
