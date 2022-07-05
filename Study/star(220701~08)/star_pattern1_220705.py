# 두 가지의 패턴을 두고 구분지어 출력하라

# 0. 가로, 세로 길이 조절
row = 5
col = 5

# 2. 2번 반복하는 것을 묶어두기
for repeat in range(2):
    # 1. 가로와 세로의 범위만큼 별 출력
    for star_row in range(row):
    # 3. 첫 번째 패턴에서는 아래의 패턴이 출력된다
        if repeat == 0:
            for star_col in range(col):
                # 3-1. 세로줄과 가로줄의 값이 짝수일때만 공백 출력, 그 이외에는 별 출력
                if (star_row+1) % 2 == 0 and (star_col+1) % 2 == 0:
                    print(" ", " ", end="")
                else:
                    print("*", " ", end="")
            print()
    # 4. 마지막 패턴에서는 아래의 패턴이 출력된다
        else:
            for star_col in range(col):
                # 4-1. 가로값과 세로값이 같을때 공백, 그 이외에는 별 출력
                if star_col == star_row:
                    print(" ", " ", end="")
                else:
                    print("*"," ",end="")
            print()
    print()