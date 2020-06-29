# 리스트 [] : 순서를 가지는 객체의 집합

subway = ["renerd", "shellden", "penny"]
print(subway)

# shellden은 몇 번째 칸에 타고 있는가?
print(subway.index('shellden'))

# ammy가 다음 정류장에서 다음 칸에 탐
subway.append("ammy")
print(subway)

# haword를 renerd / shellden 사이에 태워봄
subway.insert(1, "haword")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("renerd")
print(subway)
print(subway.count("renerd"))

# 정렬도 가능
num_list = [5, 1, 3, 2, 4]
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
mix_list = ["renerd", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)
