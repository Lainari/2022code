# 220628 수업
# 공백 피라미드를 스스로 만들어봐라
# 이번에는 180도 회전한 형태로 만들어라(위에서 아래로 작아지는...)

# 0. 층수 설정
row = 8

# 1. 세로줄 생성, 범위는 층수
for star_row in range(row):
    # 5. 세로줄에 따른 공백 생성, 범위는 세로층
    for blank in range(star_row):
        print(" ", end="")
    # 2. 가로줄 생성, 범위는 층수
    # 5. 가로줄 범위 수정, 2*(층수-세로줄)부터 1까지, -1씩
    for star_col in range(2*(row-star_row), 1, -1):
        # 3. 별 출력, 줄바꿈 X
        # 6. 가로줄의 원소가 조건에 따라 별을 출력, 그 이외에는 공백
        # 조건 : 맨 꼭대기층(star_row값이 0) 또는 가로줄의 원소가 첫번째 또는 마지막 원소에서 앞에 있는 원소
        # 첫번째 원소는 2*((row-star_row))부터 시작하므로 해당 값이고
        # 마지막 원소는 항상 range(2,1,-1)이 되어 [2,1] 값이 나오므로 star_col == 2가 된다
        if star_row == 0 or star_col == 2*(row-star_row) or star_col == 2:
            print("*", end="")
        else:
            print(" ", end="")
    # 4. 가로줄 종료 시 줄바꿈
    print()
