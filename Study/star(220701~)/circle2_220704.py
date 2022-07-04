# 220704 자습
# 원의 패턴을 갖고있는 별을 찍어내자

# 0. 반지름 설정
r = 30

# 직각삼각형 공식을 통해 반지름이 일정한구간에 항상 *를 출력할 것

# 1. 세로층 만들기, 초기값은 좌표상에서 봤을 때 음축으로도 뻗쳐나가므로 음수값으로 지정해준다
for star_row in range(-r,r+1):
    # 2. 가로층 만들기
    for star_col in range(-r,r+1):
        # 3. 해당 조건을 만족하는지 검사
        if ((star_row*star_row)+(star_col*star_col))<=r*r:
            # 4. 만족하면 * 출력, 그렇지 않다면 공백 출력
            print("*",end="")
        else:
            print(" ",end="")
    print()