# 220629 자습
# 공백 피라미드를 스스로 만들어봐라
# 이번에는 우측에서 좌측으로 올라가는 구조다

# 0. 층수 설정
row = 10

# 1. 세로줄 생성, 범위 = 층수
for star_row in range(row):
    # 5. 세로줄 값에 따라 변화는 공백 출력 반복문, 범위 = 층수 - 세로줄 - 1
    for blank in range(row-star_row-1):
        print(" ", end="")
    # 2. 가로줄 생성, 범위 = 층수       # 6. 범위 변경, 세로줄+1
    for star_col in range(star_row+1):
        # 3. 별 출력, 줄바꿈 X          # 13. 가로줄의 첫 원소 또는 마지막 원소만 별 출력, 그 이외에는 공백출력
        if star_col == 0 or star_col == star_row:
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄 완료이후 줄바꿈
    print()
# 7. 마지막 줄에 다다랐으니 역순으로 피라미드를 만들어준다
# 8. 세로줄 생성, 범위 = 층수-1
for r_star_row in range(row-1):
    # 12. 세로줄 값에 따라 변화는 공백 출력 반복문, 범위 = 세로줄 + 1
    for r_blank in range(r_star_row+1):
        print(" ", end="")
    # 9. 가로줄 생성, 범위 = 층수 - 세로줄 - 1
    for r_star_col in range(row-r_star_row-1):
        # 10. 별 생성, 줄바꿈 X          # 13. 가로줄의 첫 원소 또는 마지막 원소만 별 출력, 그 이외에는 공백출력
        if r_star_col == 0 or r_star_col == row-r_star_row-2:
            print("*", end="")
        else:
            print(" ", end="")
    # 11. 가로줄 종료 후 줄바꿈
    print()
