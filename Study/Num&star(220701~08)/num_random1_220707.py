# 랜덤 함수
# -> 난수 발생기

# import random

# # 0이상 1미만의 실수를 반환
# # 0.0 ~ 0.9999999999......
# for value in range(10):
#     print(int(random.random()* 3)+1)


# List : 자료 구조(Data Structure)
# Composite Data Type : -> Array 와 Linked List
# Abstract Data Type : -> List
# 학생 100 명의 성적을 입력 받아 평균을 계산하시오.



# CRUD
#  - Create
#  - Read
#  - Update
#  - Delete


# Create : 값을 생성
# 초기값
# myList = [3, 4, 5, 2.0, True, "Test"]

# # 매소드 append 이용 : 제일 마지막 원소 뒤에 추가
# myList.append(20)

# # insert : 지정된 위치에 추가
# myList.insert(1, 80)

# Read
myList = [3, 4, 5, 2.0, True, "Test"]

# 변수의 동작 모드는 두 가지
# GET, SET
# test = 2
# print(test) <- Get Mode
# test = 3 <- Set Mode

# [ ] 연산자를 이용합니다.
print(myList[1])

myList[1] = 1000
