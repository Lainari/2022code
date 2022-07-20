import turtle

myturtle = turtle.Turtle()

myturtle.forward(300) # 현 방향으로 앞쪽으로 300 픽셀
myturtle.setposition(0,0) # 0,0 좌표로 이동
myturtle.color("RED") # 펜 색을 빨강으로 변경
myturtle.backward(300) # 현 방향으로 뒤쪽으로 300 픽셀
myturtle.setposition(0,0) # 0,0 좌표로 이동
myturtle.color("BLUE") # 펜 색을 파랑으로 변경
myturtle.left(90) # 현 방향으로 왼쪽으로 300 픽셀
myturtle.forward(300) # 현 방향으로 앞쪽으로 300 픽셀
myturtle.setposition(0,0) # 0,0 좌표로 이동
myturtle.color("YELLOW") # 펜 색을 노랑으로 변경
myturtle.left(180) # 현 방향으로 오른쪽으로 300 픽셀
myturtle.forward(300) # 현 방향으로 앞쪽으로 300 픽셀
turtle.done()