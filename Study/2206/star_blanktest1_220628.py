# 220628 수업
# 공백 피라미드를 스스로 만들어봐라

# 0. 층수 설정
row = 10

# 1. 세로줄 제작 / 범위(층수)
for star_row in range(row):
    # 4. 공백 제작 / 범위(층수-1)
    for blank in range(row-star_row-1):  # 5-1. 범위 수정(층수-세로줄(번째))
        print(" ", end="")
    # 2. 가로줄 제작 / 범위(층수)
    for star_col in range(2*star_row+1):  # 5-1. 범위 수정(2*세로줄(번째)+1)
        # 3. 별 만들기 print("*", end="")
        # 6. 반복 중 첫번째 원소 또는 마지막 원소 또는 마지막 줄 일 경우에만 별 출력, 그 이외에는 공백 출력
        # 첫 번쨰 원소는 0, 마지막 원소는 2*star_row, 마지막 줄은 row-1이다
        if star_col == 0 or star_col == 2*star_row or star_row == row-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # 2-1. 가로줄 끝나면 띄워쓰기
