# 문제1 Turtle과 반복문을 사용하여 아래 별을 그래픽으로 출력하는 프로그램을 작성하라

import turtle

drone = turtle.Turtle()

for index in range(5):
    drone.right(144)
    drone.forward(100)
    
turtle.done()