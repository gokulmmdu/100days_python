from snake import Snake
from food import Food
from score import Score
from turtle import Screen
import time


my_screen = Screen()

my_screen.title('snake game')

my_screen.setup(600,600)

my_screen.bgcolor('black')


my_screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

my_screen.listen()
my_screen.onkey(snake.Up,'Up')
my_screen.onkey(snake.Down,'Down')
my_screen.onkey(snake.Right,'Right')
my_screen.onkey(snake.Left,'Left')



game_on = True    

while game_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collied with food

    if snake.head.distance(food)  < 15:
        food.refresh()
        snake.extend()
        score.increse_score()
 


    if snake.head.xcor() > 290  or  snake.head.xcor() < -290 or snake.head.ycor() > 290 or  snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    for segment in snake.all_segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()


my_screen.exitonclick()

#time.sleep(3)    