# 220701 자습
# 모래시계 모양으로 패턴을 출력합시다

# 0. 층 생성
row = 13

# 1. 세로줄 생성
for star_row in range(row):
    # 2. 가로줄 생성
    for star_col in range(row):
        # 5. 해당 조건식을 만족할 때 별 출력
        # 1) 첫번째, 마지막번째 줄은 무조건 전체 출력
        # 2) 세로줄과 가로줄의 값이 같아질때 출력
        # 3) 가로줄이 층 값 - 세로줄 값 - 1값이 될때 출력
        if star_row == 0 or star_row == row-1 or star_row == star_col or star_col == row-star_row-1:
            # 3. 별 출력, 줄바꿈X
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄 종료 시 줄바꿈
    print()
