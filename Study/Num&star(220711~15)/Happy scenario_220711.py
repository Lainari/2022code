# 연산자 활용 프로그램
inputValue = 0
count = 1
while inputValue != 20000:
    # 키보드로부터 정수 값 입력
    inputValue = int(input("값을 입력해주세요 : "))
    # 1이상의 값만 입력하고 해당 입력값을 카운트 및 홀수 짝수 판별, 거기다 3의배수 7의 배수면 해당 배수임을 표출할 것
    if inputValue > 0 and inputValue != 20000:
        print(count,"번째 값은 = ",inputValue)
        if inputValue % 2 == 1:
            print("\t홀수 입니다.")
        else:
            print("\t짝수 입니다.")
        if inputValue % 3 == 0:
            print("\t3의 배수입니다.")
        if inputValue % 7 == 0:
            print("\t7의 배수입니다.")
        count +=1
    # 20000 값을 입력 받으면 이용해주셔서 감사합니다 출력 후 종료
    if inputValue == 20000:
        print("이용해주셔서 감사합니다.")
        break
    # 0 이하의 값 입력시 1 이상의 양수를 입력해주세요 문구 출력, 카운트 X
    elif inputValue <= 0:
        print("1 이상의 양수를 입력해주세요")