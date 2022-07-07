# Q4 키보드로부터 값을 입력받아 입력받은 값 만큼 층이 나오고 중간값을 기준으로 하행하는 * 패턴을 만들어라

# 0. 층 입력
row = int(input("홀수의 정수를 입력해주세요 : "))

# 1. 세로층 제작
for star_row in range(row):
    # 2. 중간값 판별
    if star_row < row//2+1:
        # 3. 세로층의 중간값에 따른 패턴 1
        for star_col in range(star_row+1):
            print("*",end="")
        print()
    else:
        # 4. 세로층의 중간값에 따른 패턴 2
        for star_col in range(row-star_row):
            print("*",end="")
        print()
        