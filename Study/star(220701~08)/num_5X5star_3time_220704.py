# 220704 수업
# Q2 반복문을활용하여 5 X 5 "*" Matrix 3개를 아래와 같이 출력하는 프로그램을 작성하라

# 0. 층 설정
row = 5

# 5. 3번 반복하는 구문 생성
for repeat in range(3):
    # 1. 세로줄 생성
    for star_row in range(row):
        # 2. 가로줄 생성
        for star_col in range(row):
            # 3. 별 출력, 줄바꿈X
            print("*", end="")
        # 4. 가로줄 종료 시 줄바꿈
        print()
    # 6. 해당 구문 종료시 줄바꿈
    print()
