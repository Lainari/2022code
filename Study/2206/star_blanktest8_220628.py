# 220628 수업
# 공백 피라미드를 스스로 만들어봐라
# 이번에는 좌측에서 우측으로 올라가는 구조다

# 0. 층수 생성

row = 5

# 1. 세로줄 생성, 범위=층수
for star_row in range(row):
    # 2. 가로줄 생성, 범위=층수
    for star_col in range(star_row+1):
        # 3. 별 생성, 줄바꿈 X
        print("*", end="")
    # 5. 각 층마다 별표는 세로줄+1 개만큼, 공백은 층수-세로줄+1 만큼 생성한다
    for blank in range(row-star_row+1):
        print(" ", end="")
    # 4. 가로줄 종료 후 줄바꿈
    print()
