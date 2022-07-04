# 220704 자습
# 원을 만들어요

# 0. 층 만들기
row = 5

# 1. 세로줄 만들기
for star_row in range(row):
    # 2. 가로줄 만들기
    for star_col in range(row):
        # 3. 별 출력, 줄바꿈X
        print("*", end="")
    # 4. 가로줄 종료시 줄바꿈
    print()
