# 파일 입출력
# 컴퓨터의 파일들을 불러와 사용

# 파일을 하나 열어서 어떤 점수 정보를 쓰는 예제
# score_file = open("score.txt", "w", encoding="utf8") # w는 덮어쓰기
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close()  # 파일을 열었으면 항상 닫아주어야 한다.

# score_file = open("score.txt", "a", encoding="utf8")  # a는 이어쓰기(append)
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")  # .write는 줄바꿈이 따로 없어서 명시적으로 표시해하함
# score_file.close()  # 파일을 열었으면 항상 닫아주어야 한다.

# 파일 읽기
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())  # 파일의 모든 내용을 읽음
# # print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로
# score_file.close()

# 파일이 몇 줄인지 모를 때에는 반복문을 사용
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line) # 줄바꿈이 필요없을 때에는 end="" 사용
# score_file.close()

# 파일 라인을 리스트 형태로 사용
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
