# 220704 수업
# Q2 while반복문을활용하여 5 X 5 "*" Matrix 3개를 아래와 같이 출력하는 프로그램을 작성하라

# 0. 층 설정 및 가로, 세로층, 전체 반복에 대한 변수 생성
row = 5
star_row = 1
star_col = 1
repeat = 1

# 7. 3번 반복
while repeat <= 3:
    # 1. 세로층 생성
    while star_row <= row:
        # 2. 가로층 생성
        while star_col <= row:
            # 3. 별 출력, 줄바꿈 X
            print("*", end="")
            # 4. 가로층 원소 범위 증가
            star_col += 1
        # 5. 가로층 종료시 줄바꿈 시전
        print()
        # 6. 세로층 값 증가 및 가로층 값 초기화
        star_row += 1
        star_col = 1
    # 8. repeat 값 증가 및 줄바꿈
    repeat += 1
    print()
    # 9. 가로 세로층 값 초기화
    star_row = 1
    star_col = 1
