# 220628 수업
# 공백 피라미드를 스스로 만들어봐라

# 0. 층수 설정
row = 5

# 1. 세로줄 제작 : 반복범위(층수)
for star_row in range(row):
    # 5. 세로줄 값에 따라 변하는 공백 출력 : 반복범위(층수-세로줄-1)
    for blank in range(row-star_row-1):
        print(" ", end="")
    # 2. 가로줄 제작 : 반복범위(층수)
    # 6. 공백 설정 이후 가로줄 별 출력 범위 조절, 반복범위(2*세로줄+1)
    for star_col in range(2*star_row+1):
        # 7. 첫 원소 또는 마지막 원소일 경우 또는 마지막 줄 인경우에만 별을 출력하고 그 이외에는 공백 출력
        # star_col == 0 or star_col == 2*star_row or star_row = row-1 인 경우다
        if star_col == 0 or star_col == 2*star_row or star_row == row-1:
            # 3. 별 출력, 줄바꿈 X
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄 출력 완료 후 줄바꿈 시전
    print()
