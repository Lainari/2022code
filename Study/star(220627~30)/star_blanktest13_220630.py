# 220629 자습
# 키보드로부터 입력받아 피라미드를 만들어봅시다
# 짝수층은 첫번째 가로원소와 마지막 가로원소와 가운데 가로원소만 출력하고
# 홀수층은 전체 원소를 출력한다
# 마지막층은 전체 원소를 출력한다

# 0. 키보드로 입력받아 층을 얻기

row = int(input("피라미드의 층 수를 입력해주세요 : "))

# 1. 세로줄 제작, 범위는 층수
for star_row in range(row):
    # 5. 세로줄 값에 따라 변하는 공백 반복 출력
    for blank in range(row-star_row-1):
        print(" ", end="")
    # 2. 가로줄 제작, 범위는 층수           # 6. 범위 수정, 2N(N=세로줄+1)-1
    for star_col in range(2*(star_row+1)-1):
        # 3. 별 출력, 줄바꿈X           #
        # 7. 짝수층은 첫원소와 마지막원소, 그리고 가로줄과 세로줄의 값이 같을때 별을 출력, 그 이외에는 공백
        if (star_row+1) % 2 == 0:
            # 9. 만일 여기서 마지막 층이라면 별 전체 출력하고 반복문 탈출
            if star_row == row-1:
                print("*", end="")
                continue
            if star_col == 0 or star_col == star_col == 2*(star_row+1)-2 or star_col == star_row:
                print("*", end="")
            else:
                print(" ", end="")
        # 8. 홀수층은 전체 출력
        else:
            print("*", end="")
    # 4. 가로줄 종료 후 줄바꿈
    print()
