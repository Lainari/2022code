# Q3 반복문을 활용하여 아래와 같이 출력되는 프로그램을 작성하라
# 합쳐보자요~

# 0. 층만들기
row = 5

# 6. 새로운패턴을 위해 한번 더 반복
for repeat in range(2):
    # 7. 만약 첫번째 반복에서라면 아래의 패턴을 출력하고
    if repeat == 0:
        # 1. 세로줄 제작
        for star_row in range(row):
            # 2. 가로줄 제작
            for star_col in range(row):
                # 5. 해당 조건에 맞으면 별, 아니면 공백 출력
                if (star_row+1) % 2 == 0:
                    if (star_col+1) % 2 == 1:
                        print("*", end="")
                    else:
                        print(" ", end="")
                else:
                    # 3. 별 출력, 줄바꿈X
                    print("*", end="")
            # 4. 가로줄 종료 후 줄바꿈
            print()
        print()
    # 8. 그것이 아니라면 아래의 패턴을 출력해라
    else:
        # 9. 가로줄 생성
        for star_row in range(row):
            # 10. 세로줄 생성
            for star_col in range(row):
                # 13. 해당 조건식을 충족할 때는 공백을, 이외에는 별을 출력하라
                if star_col == star_row:
                    print(" ", end="")
                else:
                    # 11. 별 출력, 줄바꿈 X
                    print("*", end="")
            # 12. 가로줄 종료시 줄바꿈
            print()
