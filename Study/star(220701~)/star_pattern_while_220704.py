# Q3 while 반복문을 활용하여 아래와 같이 출력되는 프로그램을 작성하라

# 0. 층 만들기 및 가로 세로 반복 변수 생성
row = 5
star_col = 1
star_row = 1
repeat = 1

# 1. 총 반복구문 생성
while repeat <= 2:
    # 2. 반복구문이 처음일때 아래 패턴 출력
    if repeat == 1:
        # 3. 세로층 생성
        while star_row <= row:
            # 4. 가로층 생성
            while star_col <= row:
                # 5. 가로층에서 짝수 층일때
                if star_row % 2 == 0:
                    # 6. 원소번호가 홀수일 때만 별 출력, 이외에는 공백 출력
                    if star_col % 2 == 1:
                        print("*", end="")
                    else:
                        print(" ", end="")
                # 7. 가로층에서 홀수 층일때
                else:
                    # 8. 별 출력, 가로층 종료 후 줄바꿈 및 가로층 증가
                    print("*", end="")
                star_col += 1
            print()
            star_col = 1
            # 9. 세로층 증가
            star_row += 1
        # 10. 세로층 가로층 초기화
        star_col = 1
        star_row = 1
        print()
    # 11. 반복구문이 마지막일 때
    else:
        # 12. 세로층 생성
        while star_row <= row:
            # 13. 가로층 생성
            while star_col <= row:
                # 14. 가로층 원소가 세로층 원소의 값과 같을때 공백 출력
                if star_col == star_row:
                    print(" ", end="")
                # 15. 그 외에는 별 출력
                else:
                    print("*", end="")
                # 16. 가로층 증가
                star_col += 1
            # 17. 가로층 종료시 줄바꿈
            print()
            star_col = 1
            star_row += 1
    # 18. 반복값 증가
    repeat += 1
