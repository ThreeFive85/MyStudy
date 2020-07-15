import sys
print("python", "java")
print("python" + "java")
# sep 값을 지정해주므로써 다양한 출력 형태를 나타낸다.
print("python", "java", sep=",")
print("python", "java", "javascript", sep=" vs ")

# end= 의 사용으로 2개의 print문장이 한 줄에 표시 된다.
print("python", "java", sep=",", end="? ")
print("무엇이 더 재밌을까요?")

print("python", "java", file=sys.stdout)  # 표준 출력으로 표시
print("python", "java", file=sys.stderr)  # 표준 에러로 표시(필요시 따로 에러 처리를 할 때 사용)

# 시험 성적
scores = {"Math": 0, "English": 50, "coding": 100}
for subject, score in scores.items():  # subject = keys, score = values
    #print(subject, score)
    # ljust(8)은 8칸을 확보한 뒤 왼쪽 정렬, rjust는 4칸을 확보한 뒤 왼쪽 정렬
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 11):
    # zfill(3)은 3자리의 숫자로 채우되 빈 공간은 0으로 채운다.
    print("대기번호 : " + str(num).zfill(3))

# 표준 입력 input
# 사용자 입력을 통해서 받은 값은 항상 문자열로 저장이 된다.
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다")
