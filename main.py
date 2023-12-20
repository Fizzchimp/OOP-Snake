from window import *
from objects import *
import time

HEIGHT = WIDTH = 800

class Game:

  def __init__(self):

    self.window = Window(WIDTH, HEIGHT)
    self.snake = Snake()
    self.food = Food()
    self.playerScore = 0
    self.highScore = 0

  def keyBoardListener(self):
    self.window.screen.listen()
    self.window.screen.onkey(self.snake.go_up, "Up")
    self.window.screen.onkey(self.snake.go_down, "Down")
    self.window.screen.onkey(self.snake.go_left, "Left")
    self.window.screen.onkey(self.snake.go_right, "Right")
  
  def worldUpdate(self):
    
    if self.snake.bodyColCheck() == True:
      time.sleep(1)
      self.snake.die()
      self.playerScore = 0
      
    if self.snake.snakeHead.distance(self.food.item) < 15:
      self.food.relocate()
      self.snake.grow()
      self.playerScore += 1

      


    
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




runGame(Game())
