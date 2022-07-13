# 유효 주민등록번호 검사 알고리즘

# 체크수는 고정되어있음(상수 : 234567892345), 마지막 자리가 비어있음
checkNum = "234567892345"
# 주민등록 번호 입력 (변수 : 990000-1111111)
userIdList = input("주민번호 13자리를 입력하세요 : ")
# 주민등록번호 값과 체크수 값과 곱하기, 덧셈 계산
count = 0
sum = 0
for value in userIdList: # for문 내 Break 사용? 왜? For 문은 횟수가 정해져 있을 경우 사용...근데......무조건 Break 활용 탈출.
    if value.isdigit():
        sum += (int(value)*int(checkNum[count]))
        count += 1
        if count == 12:
            break
# 체크 계산 => 11 - (덧셈 계산을 11로 나눈 나머지) = 마지막 자리값
check = 11 - (sum % 11)
if check == int(userIdList[-1]) or (check % 10) == int(userIdList[-1]):
    print("유효한 주민번호 입니다.")
else:
    print("유요하지 않은 주민번호입니다.")