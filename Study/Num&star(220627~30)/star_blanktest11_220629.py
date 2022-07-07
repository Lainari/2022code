# 220629 자습
# 다이아몬드 만들기

# 0. 층 설정
row = 3

# 1. 세로줄 설정, 범위는 층
for star_row in range(row):
    # 5. 공백을 출력하는 반복문 설정, 범위는 층-세로줄-1
    for blank in range(row-star_row-1):
        print(" ", end="")
    # 2. 가로줄 설정, 범위는 2*층-1     # 6. 범위 수정 : 2*(층수+1)-1
    for star_col in range(2*(star_row+1)-1):
        # 3. 별 출력, 줄바꿈 X          # 13. 첫 원소 또는 마지막 원소만 별 출력, 그 이외에는 공백출력
        if star_col == 0 or star_col == 2*star_row:
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄이 끝나면 줄바꿈
    print()
# 7. 역순으로 느는 층 만들기
# 8. 세로줄 설정, 범위는 층-1
for r_star_row in range(row-1):
    # 12. 공백을 출력하는 반복문 설정, 범위는 세로줄+1
    for r_blank in range(r_star_row+1):
        print(" ", end="")
    # 9. 가로줄 설정, 범위는 층-2*세로줄
    for r_star_col in range((2*row-1)-2*(r_star_row+1)):
        # 10. 별 출력, 줄바꿈X          # 13. 첫 원소 또는 마지막 원소만 별 출력, 그 이외에는 공백출력
        if r_star_col == 0 or r_star_col == (2*row-1)-2*(r_star_row+1)-1:
            print("*", end="")
        else:
            print(" ", end="")
    # 11. 가로줄 완료 시 줄바꿈
    print()
