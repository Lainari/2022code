import turtle # 터틀 모듈 삽입

# 터틀 객체(Object) 생성
# 일단 객체가 캔버스라고 이해하자

page = turtle.Turtle()

for move in range(4):
    # 오른쪽으로 50픽셀 이동
    page.forward(50)
    # 90도로 회전
    page.right(90)

# 터틀 종료 !!!반드시삽입!!!
turtle.done()