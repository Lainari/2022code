# 좌측에서 나오는 삼각형 만들기

# 0. 층 만들기
row = 7

# 1. 세로층 제작
for star_row in range(row):
    # 2. 조건에 따라 변하는 가로줄
    # 조건 : 중간값(row//2+1)을 넘었나 안남었나?
    if star_row < (row//2)+1: # 중간값 이전
        # 3. 가로줄 제작
        for star_col in range(star_row+1): # 1씩 상승구조
            print("*",end="")
        print()
    else: # 중간값 이후
        # 4. 가로줄 제작
        for star_col in range(row-star_row): # 1씩 감소구조(기준 = 중간값)
            print("*",end="")
        print()