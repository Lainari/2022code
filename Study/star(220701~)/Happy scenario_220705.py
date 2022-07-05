# 연산자 활용 프로그램
# 키보드로부터 정수 값 입력
# 1이상의 값만 입력하고 해당 입력값을 카운트 및 홀수 짝수 판별, 거기다 3의배수 7의 배수면 해당 배수임을 표출할 것
# 0 이하의 값 입력시 1 이상의 양수를 입력해주세요 문구 출력, 카운트 X
# 20000 값을 입력 받으면 이용해주셔서 감사합니다 출력 후 종료

# 0. 정수값 입력 받을 공간과 카운트 공간을 할당
num_value = 0
count = 1

# 1. while 문을 통해 프로그램이 계속 지속될 것, 20000인 경우에는 종료
while num_value != 20000:
    num_value = int(input())
    if num_value == 20000:
        break
    if num_value <= 0:
        print("1 이상의 양수를 입력해주세요")
        continue
    else:
        print(count,"번째 입력값은 = ",num_value)
        if num_value % 2 == 0:
            print("짝수 입니다.")
        else:
            print("홀수 입니다.")
        if num_value % 3 == 0:
            print("3의 배수입니다.")
        elif num_value % 7 == 0:
            print("7의 배수입니다.")
        count+=1
print("이용해주셔서 감사합니다.")