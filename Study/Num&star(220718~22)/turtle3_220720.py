# 문제 3  Turtle을 이용하여 본인이 작성하고 싶은 자유양식 도형 스케치. 목요일 수업 시간 중 발표 예정

from re import A
import turtle

drone = turtle.Turtle()

count = 1
drone.speed(0)
drone.screen.bgcolor("oldlace") # 배경색 변경(검정)

drone.width(1) # 펜 굵기 1

drone.setposition(0,0)
drone.color("BLUE")
for index in range(60):
    for value in range(12):
        drone.forward(80)
        drone.right(30)
    drone.right(6)

drone.setposition(0,0)
drone.color("SKYBLUE")
for index in range(60):
    for value in range(8):
        drone.forward(120)
        drone.right(45)
    drone.right(6)


drone.setposition(0,0)
drone.color("AQUA")
for index in range(60):
    for value in range(4):
        drone.forward(200)
        drone.right(90)
    drone.right(6)


while count <= 360:
    if count % 3 == 0:
        drone.color("OLIVE")
        drone.forward(200)
        drone.right(1)
    else:
        drone.forward(195)
        drone.color("KHAKI")
        drone.right(1)
    drone.setposition(0,0)
    count += 1
drone.setposition(0,0)
drone.color("WHITE")
for index in range(60):
    for value in range(5):
        drone.forward(300)
        drone.right(144)
    drone.right(6)

drone.setposition(0,0)
drone.color("GOLD")
for index in range(60):
    for value in range(100):
        drone.forward(10)
        drone.right(3.6)
    drone.right(6)


turtle.done()