# 220628 수업
row = 5

for star_row in range(row):  # 세로줄를 row번 실행하는 반복문 <range(5) -> [0, 1, 2, 3, 4]>
    for blank in range((row-1)-star_row):  # 공백을 (row-1)-세로줄의수 번 만큼 출력하는 반복문
        print(" ", end="")  # 해당 반복문이 실행될 때 공백을 출력
    for star_col in range(row):  # 가로줄을 row번 실행하는 반복문 <원소의 개수만큼 반복>
        print("*", end="")  # 해당 반복문이 실행될 때 출력되는 값, end=""로 줄바꿈을 없앤다
    print()  # 가로줄 반복문이 종료되고 나서 줄 바꿈을 실행해준다
