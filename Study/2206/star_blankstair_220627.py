# 220627수업
row = 5  # 세로줄 확인

for value_row in range(row):  # row번 반복 <- 세로
    for blank_count in range((row-1)-value_row):  # 공백을 출력하는 for문
        print(" ", end="")
    for value_col in range(3+value_row):  # 공백이 끝나고 *를 출력하는 for문
        print("*", end="")
    print()  # 가로줄이 끝나면 세로줄 출력
