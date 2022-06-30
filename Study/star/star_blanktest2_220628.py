# 220628 수업
# 공백 피라미드를 스스로 만들어봐라

# 0. 층수 설정
row = 5

# 1. 세로줄 만들기(범위 : 층수)
for star_row in range(row):
    # 5. 공백 만들기(범위 : 층수 - 세로줄 - 1)
    # -> [4 3 2 1 0(공백 X)], 즉 층수 - 세로줄의 번째 - 1(세로줄의 번째가 0부터 시작)
    for blank in range(row-star_row-1):
        print(" ", end="")
    # 2. 가로줄 만들기(범위 : 층수)
    for star_col in range(2*star_row+1):  # 6. 범위 수정(범위 : 2*세로줄+1)
        # 3. 별 만들기, 줄바꿈 X
        # 7. 조건식에 따라 *를 출력하게끔 한다. 조건은 star_col의 첫번째 값 또는 마지막 값 또는 마지막 줄일 경우고 그 이외는 공백출력
        # 즉 star_col == 0 or star_col == 2*star_row or star_row == row-1
        if star_col == 0 or star_col == 2*star_row or star_row == row-1:
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄이 끝나면 줄바꿈 O
    print()
