# Q3 반복문을 활용하여 아래와 같이 출력되는 프로그램을 작성하라

# 0. 층 만들기
row = 11

# 1. 세로줄 만들기
for star_row in range(row):
    # 5. 짝수 층 일때 별은 홀수 번째만 출력할 것
    if (star_row + 1) % 2 == 0:
        for star_col in range(row):
            if (star_col+1) % 2 == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    # 2. 가로줄 만들기
    else:
        for star_col in range(row):
            # 3. 별 출력, 줄바꿈X
            print("*", end="")
    # 4. 가로줄 종료 시 줄바꿈
        print()
print()

# 다음 패턴은 공백이 첫번쨰부터 마지막까지 늘어나면서 그 이외에는 별을 출력하게 한다
# 6. 세로줄 재 생성
for star_row_2 in range(row):
    # 7. 가로줄 재 생성
    for star_col_2 in range(row):
        # 8. 해당 조건 만족하는지 검사, 맞으면 공백 아니면 별 출력
        if star_row_2 == star_col_2:
            print(" ", end="")
        else:
            print("*", end="")
    # 9. 가로줄 종료 후 줄바꿈
    print()
