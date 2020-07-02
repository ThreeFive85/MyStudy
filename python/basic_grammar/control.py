# if
# 날씨에 따라 다른 내용을 출력해보자
# if 조건:
#     실행 명령문

# weather = "맑음"
# if weather == "비":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
# else:
#     print("오늘은 준비물이 필요 없습니다.")

# weather = input("오늘 날씨는 어떤가요? ")
# if weather == "비" or weather == "눈":  # 조건 추가
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
# else:
#     print("오늘은 준비물이 필요 없습니다.")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for 문
# for waiting_no in [1, 2, 3, 4]:
#     print("대기번호 : {0}".format(waiting_no))
# for waiting_no in range(1, 6):
#     print("대기번호 : {0}".format(waiting_no))
# starbucks = ["ironman", "thor", "spiderman"]
# for customer in starbucks:
#     print("{0}님, 커피가 준비되었습니다.".format(customer))

# while 문
# customer = "thor"
# index = 5
# while index > 0:
#     print("{0}님, 커피가 준비되었습니다. 호출 {1}번 남았습니다.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("{0}님 커피는 달나라로 갔습니다.".format(customer))

# customer = "thor"
# person = "Unknown"
# while customer != person:
#     print("{0}님, 커피 나왔습니다.".format(customer))
#     person = input("이름이 어떻게 되세요? ")
#     if customer == person:
#         print("맛있게 드세요 {0}님!!".format(customer))
#     else:
#         print("죄송합니다. 이것은 {0}님의 것이 아닙니다.".format(person))

# # continue / break 반복문 내에 사용
# absent = [2, 5]  # 결석
# no_book = [7]  # 책을 깜빡했음
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업은 여기까지. {0}는 교무실로 따라오세요.".format(student))
#         break
#     print("{0}, 책을 읽어봐.".format(student))

# 한 줄 for 문
# 출석번호가 1 2 3 4, 앞에 100을 붙이리고 함 -> 101,102,103,104
# students = [1, 2, 3, 4, 5]
# students = [i+100 for i in students]
# print(students)

# 학생 이름을 길이,대문자로 변환
students = ["IronMan", "Thor", "SpiderMan", "Hulk"]
students_len = [len(i) for i in students]
print(students_len)
students_upper = [i.upper() for i in students]
print(students_upper)
