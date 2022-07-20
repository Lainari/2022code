# 문제 3  Turtle을 이용하여 본인이 작성하고 싶은 자유양식 도형 스케치. 목요일 수업 시간 중 발표 예정

import turtle

drone = turtle.Turtle()

count = 1

drone.speed(0)
drone.setposition(0,-300)
drone.screen.bgcolor("Black") # 배경색 변경(검정)
drone.color("WHITE") # 펜 색상 화이트
drone.width(3) # 펜 굵기 3
drone.circle(300) # 현 위치 기준 반지름 50픽셀 원 출력
drone.color("")
drone.setposition(0,0)

drone.width(1) # 펜 굵기 1
while count <= 450:
    if count % 5 == 0:
        drone.color("RED")
        drone.forward(100)
    else:
        drone.forward(50)
        drone.color("BLUE")
        drone.right(1)
    drone.setposition(0,0)
    count += 1
turtle.done()