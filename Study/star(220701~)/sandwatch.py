# 220701 수업
# 모래시계를 만들어봅시다

# 0. 층 만들기
row = 13

# 1. 세로줄 만들기
for star_row in range(row):
    # 2. 가로줄 만들기
    for star_col in range(row):
        # 5. 세로줄의 첫번째와 마지막은 전체출력하고
        # 6. 세로줄과 가로줄의 값이 같아지거나
        if star_row == 0 or star_row == row-1 or star_col == star_row or row-star_row-1 == star_col:
            # 3. 별 출력, 줄바꿈 X
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄 종료 후 줄바꿈
    print()
