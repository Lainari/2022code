# 220628 수업
# 공백 피라미드를 스스로 만들어봐라
# 이번에는 180도 회전한 형태로 만들어라(위에서 아래로 작아지는...)

# 0. 층수 선택
row = 9

# 1. 세로줄 생성, 범위=층수
for star_row in range(row):
    # 5. 세로줄에 따라 변화는 공백의 수, 범위=세로줄
    for blank in range(star_row):
        print(" ", end="")
    # 2. 가로줄 생성, 범위=층수
    # 6. 가로줄 범위 수정, 2*(층수-세로줄)-1
    for star_col in range(2*(row-star_row)-1):
        # 3. 별 생성, 줄바꿈 X
        # 7. 조건에 따라 별을 출력하고, 그 이외에는 공백을 출력하라
        # 조건 : 첫번째 줄 또는 각 가로줄의 첫번째 원소 또는 마지막 원소
        if star_row == 0 or star_col == 0 or star_col == 2*(row-star_row)-2:
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄 종료 시 줄바꿈
    print()
