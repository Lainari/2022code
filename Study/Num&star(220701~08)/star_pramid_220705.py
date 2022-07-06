# 220705 * 피라미드 만들기

# 0. 층 만들기      # 3. 입력값 받기
row = int(input("정수를 입력해주세요 : "))

# 1. 세로층 만들기
for star_row in range(row):
    # 3. 공백 만들기, 위에서부터 4, 3, 2, 1, .. 층-세로층-1 만큼 감소하게 제작
    for blank in range(row-star_row-1):
        print(" ",end="")
    # 2. 가로층 만들기, 위에서부터 1, 3, 5, 7, 9, ... 홀수 값만큼 증가하게 제작
    for star_col in range((2*star_row)+1):
        print("*",end="")
    print()