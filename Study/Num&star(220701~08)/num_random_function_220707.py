# 1. 1 ~ 20 사이 양의 정수 중 난수 값 20개 생성 후 List에 저장
import random
randList=[]
for rand_count in range(20):
    randList.append(int((random.random()*20))+1)

# 2. List 내 원소와 원소 값에 대한 합계, 평균, 최대값, 최소값 출력
# 원소 출력
print("랜덤 값 : ")
for show in range(20):
    print(" ",randList[show]," ",end="")
print()
list_avg = 0
list_sum = 0
list_max = 0
list_min = 0
# 최대 최소값 판별
list_max = randList[0]
for max_search_1 in range(20):
    for max_search_2 in range(20):
        if randList[max_search_1] == randList[max_search_2]:
            continue
        elif randList[max_search_1] > randList[max_search_2]:
            if randList[max_search_1] > list_max:
                list_max = randList[max_search_1]
        elif randList[max_search_2] < randList[max_search_2]:
            if randList[max_search_2] > list_max:
                list_max = randList[max_search_2]
print("최대 값 : ",list_max)
list_min = randList[0]
for min_search_1 in range(20):
    for min_search_2 in range(20):
        if randList[min_search_1] == randList[min_search_2]:
            continue
        elif randList[min_search_1] < randList[min_search_2]:
            if randList[min_search_1] < list_min:
                list_min = randList[min_search_1]
        elif randList[min_search_2] < randList[min_search_2]:
            if randList[min_search_2] < list_min:
                list_min = randList[min_search_2]
print("최소 값 : ",list_min)
# 합계 평균 구하고 출력
for num in range(20):
    list_sum = randList[num]+list_sum
list_avg = list_sum / 20
print("합계 : ",list_sum)
print("평균 : ",list_avg)
# 3. List 내 중복 값과 중복 횟수 정보 출력[중복 값 중복 횟수]
count = 1
overlap = 0
    
# 4. 구간 별 히스토그램 정보 출력[1~5 : *개, 6~10 : *개 ...]