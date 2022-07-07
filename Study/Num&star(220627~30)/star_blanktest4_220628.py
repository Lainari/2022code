# 220628 수업
# 공백 피라미드를 스스로 만들어봐라

# 0. 층수 설정
row = 10

# 1. 세로줄 설정, 범위는 층수
for star_row in range(row):
    # 5. 세로줄 값에 따라 변하는 공백 출력 반복문, 범위는 층수 - 세로줄 -1
    for blank in range(row-star_row-1):
        print(" ", end="")
    # 2. 가로줄 설정, 범위는 층수
    # 6. 가로줄 범위 수정, 2*세로줄 + 1
    for star_col in range(2*star_row+1):
        # 3. 별 출력, 줄바꿈 X
        # 7. 해당 조건에 따라 출력하는 선택문, 조건 이외에는 공백 출력
        # 조건 : star_col의 첫 원소 또는 마지막 원소 또는 마지막 줄(row-1)
        if star_col == 0 or star_col == 2*star_row or star_row == row-1:
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄 출력 다 끝나고 줄바꿈
    print()
