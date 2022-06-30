# 220628 수업
# 공백 피라미드를 스스로 만들어봐라
# 이번에는 좌측에서 우측으로 올라가는 구조다

# 0. 층수 생성

row = 5

# 1. 세로줄 생성, 범위=층수
for star_row in range(row):
    # 2. 가로줄 생성, 범위=층수
    for star_col in range(star_row+1):
        # 3. 별 생성, 줄바꿈 X     # 12. 가로줄의 첫 원소 또는 마지막 원소만 출력하게한다. 그외엔 공백 출력
        if star_col == 0 or star_col == star_row:
            print("*", end="")
        else:
            print(" ", end="")
        # 5. 각 층마다 별표는 세로줄+1 개만큼, 공백은 층수-세로줄+1 만큼 생성한다
    for blank in range(row-star_row+1):
        print(" ", end="")
        # 4. 가로줄 종료 후 줄바꿈
    print()
# 6. star_col 값이 row와 같아졌으므로 이제 역순으로 내려가는 피라미드를 만들어본다
# 7. 세로줄 생성, 범위=층수-1(하행 시작 부분이므로)
for star_row in range(row-1):
    # 8. 가로줄 생성, 범위 = 층수-세로줄-1
    for star_col in range(row-star_row-1):
        # 9. 별 생성, 줄바꿈 X     # 12. 가로줄의 첫 원소 또는 마지막 원소만 출력하게한다. 그외엔 공백 출력
        if star_col == 0 or star_col == row-star_row-2:
            print("*", end="")
        else:
            print(" ", end="")
    # 10. 공백 생성, 범위 = 층수-세로줄+1
    for blank in range(row-star_row+1):
        print(" ", end="")
    # 11. 가로줄 종료 후 줄바꿈
    print()
