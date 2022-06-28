# 별 피라미드를 만드는데
# 꼭대기 층은 하나만, 마지막 층은 전체별 출력, 나머지 층은 해당 패턴에서 첫번째와 끝 별만 출력한다

row = int(input("공백 피라미드의 층 수를 입력해주세요 : "))

# 1. row층짜리 피라미드를 만들어준다
for star_row in range(row):
    # 2. row층짜리 피라미드중에서 몇 층인지 판별한다
    if star_row == 0:  # 꼭대기 층 일경우
        for star_col in range(2*row-1):
            if star_col == row-1:  # 정 중앙이라면 별을 출력하고
                print("*", end="")
            else:  # 나머지는 공백을 출력하라
                print(" ", end="")
        print("")  # 줄바꿈
    elif star_row == row-1:  # 마지막 층 일경우
        for star_col in range(2*row-1):
            print("*", end="")
    else:  # 나머지 층 일 경우, 아래의 조건식에 따라 별과 공백을 출력한다
        for star_blank in range(row-star_row-1):
            print(" ", end="")
        print("*", end="")
        for star_blank in range(2*star_row-1):
            print(" ", end="")
        print("*", end="")
        for star_blank in range(2*row-1, row+star_row):
            print(" ", end="")
        print("")
