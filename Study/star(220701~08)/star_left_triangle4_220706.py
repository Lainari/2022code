# 220706 수업
# 지난 시간 배운 것 복습

# num 5
# *
# **
# ***   
# **
# *

num = int(input("홀수의 양의 정수를 입력해주세요 : "))
median = num // 2 + 1

# [0, 1, 2, 3, 4]
for star_row in range(num):
    # * 증가 반복문 : star_row < median
    if star_row < median:
        for star_col in range(star_row+1):
            print("*"," ",end="")
    # * 감소 반복문
    else:
        for star_col in range(num-star_row):
            print("*"," ",end="")
    print()