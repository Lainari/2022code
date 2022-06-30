# 220628 수업
# 공백 피라미드를 스스로 만들어봐라

# 0. 층수 만들기
row = 5

# 1. 세로줄 만들기 범위(층수)
for star_row in range(row):
    # 5. 세로줄 값에 따라 바뀌는 공백 반복 범위(층수-세로줄-1)
    for blank in range(row-star_row-1):
        print(" ", end="")
    # 2. 가로줄 만들기 범위(층수) # 6. 가로줄 범위 수정(2*세로줄+1)
    for star_col in range(2*star_row+1):
        # 3. 별 출력, 줄바꿈 X # 7. 조건에 따른 별 출력, 그 이외에는 공백 출력
        # 조건식 : 가로줄의 첫번째 원소 또는 마지막 원소 또는 마지막 줄인 경우에만 별 출력
        if star_col == 0 or star_col == 2*star_row or star_row == row-1:
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄 완료시 줄바꿈
    print()
