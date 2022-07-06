# 220630 자습
# 키보드로부터 입력받아 피라미드를 만들어봅시다

# 층을 입력받고, 그 층 값의 2배 -1 인 가로길이를 갖는 직사각형에다가
# 공백으로 역삼각형 형태의 피라미드로 채워진 도형을 만들어봅시다

# 0. 키보드로부터 층을 입력받아 저장하자
row = int(input("층을 입력해주세요 : "))

# 1. 세로줄 만들기, 범위 = 층
for star_row in range(row):
    # 2. 가로줄 만들기, 범위 = 2*층-1
    for star_col in range(2*row-1):
        # 7. 마지막 줄인지 판별하여, 마지막 줄은 가운데 원소를 제외한 전부 출력한다
        if star_row == row-1:
            if star_col == row-1:
                print(" ", end="")
                continue
            print("*", end="")
            continue
        # 5. 공백을 출력하는 반복문, 해당 조건을 만족해야한다
        if star_col >= star_row and star_col <= 2*row-star_row-2:
            print(" ", end="")
        # 6. 그 이외라면 별을 출력한다
        else:
            # 3. 별 출력하기, 줄바꿈 X
            print("*", end="")
    # 4. 가로줄 종료 후 줄바꿈
    print()
