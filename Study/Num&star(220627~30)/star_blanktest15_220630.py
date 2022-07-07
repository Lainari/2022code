# 220630 자습
# 키보드로부터 입력받아 N단짜리 햄버거를 만들어봅시다

# 0. 층만들기
row = int(input("몇단 햄버거인가요? : "))

# 1. 세로줄 만들기, 범위 = 2*층
for star_row in range(2*row):
    # 2. 가로줄 만들기, 범위 = 2*층-1
    for star_col in range(2*row-1):
        if star_row % 2 == 0:
            # 3. 별 출력하기, 줄바꿈X
            print("*", end="")
        else:
            # 5. 짝수 층일때 공백을 한칸 두면서 별을 출력하게끔 한다
            if star_col % 2 == 1 and star_col >= 1:
                print("*", end="")
            else:
                print(" ", end="")
    # 4. 가로줄 종료 시 줄바꿈
    print()
# 6. 버거 하단 부분 만들기
for star_col in range(2*row-1):
    print("*", end="")
print()
print("맛있게 드세용~^^")
