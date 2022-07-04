# 220704 자습
# 원을 만들어요

# 0. 층 만들기
row = 10

# 1. 세로줄 만들기
for star_row in range(int(row/2)+1):
    # 5. 공백 생성 반복문
    for blank in range(int(row/2)-star_row):
        print(" ",end="")
    # 2. 가로줄 만들기
    for star_col in range(row+(star_row*2)):
        # 3. 별 출력, 줄바꿈X
        print("*", end="")
    # 4. 가로줄 종료시 줄바꿈
    print()
if row % 2 == 0:
    for star_row in range(int(row/2)):
        # 5. 공백 생성 반복문
        for blank in range(star_row+1):
            print(" ",end="")
        for star_col in range((2*row)-((star_row+1)*2)):
            print("*",end="")
        print()
else:
    for star_row in range(int(row/2)):
        # 5. 공백 생성 반복문
        for blank in range(star_row+1):
            print(" ",end="")
        for star_col in range((2*row)-((star_row+1)*2)-1):
            print("*",end="")
        print()