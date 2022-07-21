# 리스트의 모든 값이 고유한 값이라면 T, 아니면 F 를 반환하는 함수
def all_unique(lst):
    return len(lst) == len(set(lst))
# Set 함수는 중복값을 허용하지 않음

x = [1,2,3,4,5,6]       # True
y = [1,2,2,3,4,5]     # False
print(all_unique(x))
print(all_unique(y))
