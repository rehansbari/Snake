from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

#setting up the screen of the snake game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Rehan's Snake Game")
screen.tracer(0)

#Creating starting squares
snake = Snake()
food = Food()
score = Scoreboard()
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

    #Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.add_tail()
        score.increase_score()

    #Detecting collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.display_gameover()

    #Detecting collision with the tail, will check every square other than the head
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_is_on = False
            score.display_gameover()


screen.exitonclick()
