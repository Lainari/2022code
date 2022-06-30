# 220629 자습
# 키보드로부터 입력받아 상하좌우를 나오게끔 하는 프로그램을 만들어봅시다

# 몇층 피라미드를 만들것인지 따로 함수로 받읍시다
def pramid_row():
    value = int(input("몇 층짜리 피라미드를 만들까요? : "))
    return value


# 0. while 문을 통해 상,하,좌,우 그리고 프로그램 종료까지 만들어봅시다
play = True
while play:
    # 키보드로부터 값을 입력받아 상,하,좌,우,종료를 실행하자
    print("1. 일반적인 피라미드")
    print("2. 떨어지는 피라미드")
    print("3. 왼쪽에서 솓아난 피라미드")
    print("4. 오른쪽에서 솓아난 피라미드")
    print("0. 프로그래밍 종료")
    play_number = int(input("어떤 피라미드를 만들어볼까요? : "))

    # 프로그래밍 종료 부분
    if play_number == 0:
        play = False

    # 일반적인 피라미드 부분
    elif play_number == 1:
        row = pramid_row()
        print()
        # 1. 층을 구했으니 세로줄을 만든다. 범위는 층
        for star_row in range(row):
            # 5. 공백 출력 반복문, 범위는 층-세로줄-1
            for blank in range(row-star_row-1):
                print(" ", end="")
            # 2. 가로줄, 범위 층        # 6. 범위 수정, 2*(세로줄+1)-1
            for star_col in range(2*(star_row+1)-1):
                # 3. 별 출력, 줄바꿈 X
                print("*", end="")
            # 4. 가로줄 종료 시 줄바꿈
            print()
        print()

    # 떨어지는 피라미드 부분
    elif play_number == 2:
        row = pramid_row()
        print()
        # 1. 층을 구했으니 세로줄을 만든다. 범위는 층
        for star_row in range(row):
            # 5. 공백 출력 반복문, 범위는 세로줄
            for blank in range(star_row):
                print(" ", end="")
            # 2. 가로줄, 범위 층        # 6. 범위 변경, 2*층-2*세로줄-1
            for star_col in range(2*row-2*star_row-1):
                # 3. 별 출력, 줄바꿈X
                print("*", end="")
            # 4. 가로줄 종료 시 줄바꿈
            print()
        print()

    # 왼쪽에서 솓아난 피라미드 부분
    elif play_number == 3:
        row = pramid_row()
        print()
        # 1. 층을 구했으니 상단 부분을 제작한다, 세로줄, 범위 층
        for star_row in range(row):
            # 2. 가로줄, 범위 층
            for star_col in range(star_row+1):         # 6. 범위 수정, 세로줄+1
                # 3. 별 출력, 줄바꿈 X
                print("*", end="")
            # 5. 공백 생성 반복문, 범위 층-세로줄-1
            for blank in range(row-star_row-1):
                print(" ", end="")
            # 4. 가로줄 이후 줄바꿈
            print()
        # 7. 하단 부분 제작, 세로줄, 범위 층-1
        for r_star_row in range(row-1):
            # 8. 하단 가로줄, 범위 층-세로줄-1
            for r_star_col in range(row-r_star_row-1):
                # 9. 별 제작, 줄바꿈 X
                print("*", end="")
            # 10. 가로줄 완료 후 줄바꿈
            print()
        print()
    # 오른쪽에서 솓아난 피라미드 부분
    elif play_number == 4:
        row = pramid_row()
        print()
        # 1. 층을 구했으니 상단 부분을 제작한다, 세로줄 범위 = 층
        for star_row in range(row):
            # 5. 공백 출력 반복문, 범위 = 층-세로줄-1
            for blank in range(row-star_row-1):
                print(" ", end="")
            # 2. 가로줄 범위 = 층               # 6. 범위 수정 = 세로줄 + 1
            for star_col in range(star_row+1):
                # 3. 별 출력, 줄바꿈X
                print("*", end="")
            # 4. 가로줄 종료 후 줄바꿈
            print()
        # 7. 하단 부분 제작, 세로줄 범위 = 층-1
        for r_star_row in range(row-1):
            # 11. 공백 생성 반복문, 범위 = 세로줄+1
            for r_blank in range(r_star_row+1):
                print(" ", end="")
            # 8. 가로줄 범위 = 층-세로줄-1
            for r_star_col in range(row-r_star_row-1):
                # 9. 별 생성, 줄바꿈X
                print("*", end="")
            # 10. 가로줄 종료 후 줄바꿈
            print()
        print()

    else:
        print()
        print("잘못된 값입니다!!!")
        print()
