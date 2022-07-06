# 220706 수업
# 지난 수업 시간때 배운 내용 복습

count = 1
while True:
    # 키보드로 입력
    inputNumber = int(input("정수 값을 입력하세요 : "))
    # 입력 값 예외처리
    if inputNumber <= 0:
        print("양의 정수를 입력하세요")
        continue

    # 20000이면 프로그램 종료
    elif inputNumber == 20000:
        break
    # 입력 횟수와 입력 값 출력
    else:
        print(count,"번째 입력 값 = ",inputNumber)
        count += 1

    # 짝수 또는 홀수 판별 후 출력
    if inputNumber % 2 == 0:
        print("\t짝수 입니다.")
    else:
        print("\t홀수 입니다.")
    # 3의 배수 판별 후 출력
    if inputNumber % 3 == 0:
        print("\t3의 배수 입니다.")
    # 7의 배수 판별 후 출력
    if inputNumber % 7 == 0:
        print("\t7의 배수 입니다.")
print("이용해주셔서 감사합니다.")