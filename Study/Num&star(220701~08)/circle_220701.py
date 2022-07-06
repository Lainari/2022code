# 220701 수업
# 원을 만들어 봐요..?

# 원을 만들기 위해 윗층이든 아랫층이든 뭔가 패턴을 찾아내자
# 난 지금 반지금이 5칸인 원을 만들고 싶다!


# 0. 층 만들기
row = 8
# 1. 세로줄 만들기
for star_row in range(row):
    # 5. 공백1을 무리함수 형태로 나타낸다
    for blank1 in range(int((row-1)-(((row-1)*(star_row**2))**0.5))):
        print(" ", end="")
    # 6. 공백2를 무리함수 형태로 나타낸다
    for blank2 in range(int(-(row-1)+(((row-1)*(star_row**2))**0.5))):
        print(" ", end="")
    # 2. 가로줄 만들기          # 6. 가로줄을 이차함수 형태의 값으로 출력한다
    for star_col in range(2*row):
        # 3. 별 출력, 줄바꿈X
        print("*", end="")
    # 4. 가로줄 종료 시 줄바꿈
    print()
