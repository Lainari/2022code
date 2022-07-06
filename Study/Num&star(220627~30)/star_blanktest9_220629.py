# 220629 자습
# 공백 피라미드를 스스로 만들어봐라
# 이번에는 좌측에서 우측으로 올라가는 구조다

# 0. 층수 설정
row = 10

# 1. 세로줄 생성, 범위 = 층수
for star_row in range(row):
    # 2. 가로줄 생성, 범위 = 층수       # 5. 범위 수정, 세로줄+1
    for star_col in range(star_row+1):
        # 3. 별을 출력한다, 줄바꿈 X        # 13. 가로줄의 첫 원소 또는 마지막 원소만 별을 출력하고 그 이외에는 공백출력
        if star_col == 0 or star_col == star_row:
            print("*", end="")
        else:
            print(" ", end="")
    # 6. 공백 출력, 범위 = 층수 - 세로줄+1
    for blank in range(row-star_row-1):
        print(" ", end="")
    # 4. 가로줄 이후 줄바꿈
    print()
# 7. star_col 출력 값이 row와 같아졌으므로 역순으로 하행하는 피라미드를 만든다
# 8. 세로줄 생성, 범위 = 층수-1
for star_row in range(row-1):
    # 9. 가로줄 생성, 범위 = 층수-1-세로줄
    for star_col in range(row-star_row-1):
        # 10. 별 출력, 줄바꿈 X         # 13. 가로줄의 첫 원소 또는 마지막 원소만 별을 출력하고 그 이외에는 공백출력
        if star_col == 0 or star_col == row-star_row-2:
            print("*", end="")
        else:
            print(" ", end="")
    # 11. 공백 출력, 범위 = 층수-1
    for blank in range(row-1):
        print(" ", end="")
    # 12. 가로줄 출력 이후 줄바꿈
    print()
