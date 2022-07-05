# 220705 수업
# 지난 시간에 사용한 것을 복습해봅시다

# Q1 키보드로부터 입력받아 숫자를 계단 형식으로 표현하게끔 만들어라
# ex) 입력값 : 3
# 1
# 1 2
# 1 2 3

# 0. 층수와 세로줄, 가로줄의 초기값을 지정해준다
num = 11
num_row = 1
num_col = 1

# 1. 세로줄 반복 시작
while num_row <= num:
    # 2. 가로줄 반복 시작
    while num_col <= num_row:
        print(num_col," ", end="")
        num_col+=1
    print()
    num_col = 1
    num_row +=1