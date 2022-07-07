# 220704 수업
# Q1 반복문을 활용하여 아래와 같이 출력되는 프로그램을 작성하라

# 0. 층 수 입력받기(단, Type이 Str형이므로 Int형으로 Type Casting 할 것)
row = int(input("양의 정수를 입력 하세요 : "))

# 1. 세로줄 출력하기
for star_row in range(row):
    # 2. 세로줄에 따라 늘어나는 가로줄 출력하기, 단 0부터 시작하므로 1를 넣어주도록 하자
    for star_col in range(star_row+1):
        # 3. 숫자 출력, 단 0부터 시작하므로 1를 넣어주도록 하자
        print(star_col+1, end=" ")  # 줄바꿈 X
    # 4. 가로줄 종료 후 줄바꿈 시전
    print()
