# 오른쪽에서 솟아난 삼각형을 만들어봅시다

# 0. 층 만들기          # 5. 층 입력받기로 수정
row = int(input("홀수의 정수값을 입력해주세요 : "))

# 1. 세로 만들기
for star_row in range(row):
    # 2. 조건에 따른 가로 출력문 조절
    # 조건 : 중간값(row//2+1)보다 작은가?
    if star_row < (row//2) +1:
        # 3. 작다면 공백이 줄어든 다음 별을 출력하는 구조
        for blank in range(row-star_row-1):
            print(" ",end="")
        for star_col in range(star_row+1):
            print("*",end="")
    else:
        # 4. 크다면 공백이 커진 다음 별을 출력하는 구조
        for blank in range(star_row):
            print(" ",end="")
        for star_col in range(row-star_row):
            print("*",end="")
    print()