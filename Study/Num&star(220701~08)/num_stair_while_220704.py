# 220704 수업
# Q1 while 반복문을 활용하여 아래와 같이 출력되는 프로그램을 작성하라
#
# 1
# 1 2
# 1 2 3

# 세로줄, 가로줄 변수생성
star_row = 1
star_col = 1

# 0. 층 입력받기, 단 입력받을때는 문자열이므로 int형으로 변환해주자
row = int(input("양의 정수를 입력해주세요 : "))

# 1. 세로층 만들기
while star_row <= row:
    # 2. 가로층 만들기
    while star_col <= star_row:
        # 3. 별 출력하기, 줄바꿈X
        print(star_col, end=" ")
        # 4. 가로층 원소 범위 증가
        star_col += 1
    # 5. 가로층 종료시 줄바꿈
    print()
    # 6. 세로층 원소 범위 증가
    star_row += 1
    # 7. 가로층 원소 범위 초기화
    star_col = 1
