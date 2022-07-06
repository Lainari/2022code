# Q4 반복문을 활용하여 아래와 같이 출력되는 프로그램을 작성하라
# 라인 넘버를 입력하세요 : 5
# *
# **
# ***
# **
# *

# 0. 층 값 설정 # 6. 라인 넘버 입력문 수정
row = int(input("라인 넘버를 입력하세요(짝수 입력 시 한 줄이 더 추가 됩니다) : "))
if row % 2 == 0:
    row +=1

# 1. 세로줄 제작
for star_row in range(row):
    # 2. 가로줄 제작
    for star_col in range(star_row+1):
    # 3. 만일, 세로줄의 값이 정수형(층값 /2) + 1 보다 크거나 같을 경우에는
        if star_row >= row // 2 +1:
            # 4. 가로 출력 값의 범위를 층 - 세로층으로 잡아둔다
            for star_col in range(row-star_row):
                print("*",end="")
            break # 5. 해당 반복문을 탈출하여 중복 출력이 안되게끔 만들어준다
        # 3. 조건식에 해당이 되지 않은 세로줄의 범위에서는 별을 출력
        print("*",end="")
    # 4. 줄 바꿈
    print()