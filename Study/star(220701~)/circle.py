# 220701 수업
# 원을 만들어 봐요..?

# 0. 층을 설정

row = 6

# 1. 세로줄 만들기
for star_row in range(row):
    # 2. 가로줄 만들기
    for star_col in range(row):
        # 3. 별 출력 후 줄바꿈X
        print("*", end="")
    # 4. 가로줄 종료 후 줄바꿈
    print()
