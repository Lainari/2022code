# 5X5 형식인 * 들을 3번 출력하라

# 0. 가로, 세로 길이 조절
row = 5
col = 5

# 2. 3번 반복하는 것을 묶어두기
for repeat in range(3):
    # 1. 가로와 세로의 범위만큼 별 출력
    for star_row in range(row):
        for star_col in range(col):
            print("*", " ", end="")
        print()
    print()