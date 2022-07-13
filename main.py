from turtle import Screen, Turtle
from snake import Snake
import time

#setting up the screen of the snake game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Rehan's Snake Game")
screen.tracer(0)

squares = []
starting_positions = [(0,0), (-20,0), (-40,0)]

#Creating starting squares
snake = Snake()
screen.listen()

#Setting up the movement of the snake
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

#Starting the snake game
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()





screen.exitonclick()
