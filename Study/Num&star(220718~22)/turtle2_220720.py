# 문제 2 • Turtle과 반복문을 사용하여 아래 Hexagon을 그래픽으로 출력하는 프로그램을 작성하라

import turtle

drone = turtle.Turtle()

for index in range(6):
    drone.right(60)
    drone.forward(100)
turtle.done()