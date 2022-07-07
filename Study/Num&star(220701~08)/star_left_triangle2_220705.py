# 좌측에서 나오는 삼각형 만들기

# 0. 층 생성
row = 9

# 1. 세로 층 생성
for star_row in range(row):
    # 2. 조건에 따라 달라지는 가로줄 출력
    if star_row < (row // 2 + 1) :
        for star_col in range(star_row+1):
            print("*",end="")
    else:
        for star_col in range(row-star_row):
            print("*",end="")
    print()