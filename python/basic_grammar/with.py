# with를 사용함으로 파일의 열고 닫음을 좀 더 편하게 쓸 수 있다.

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# profile.pickle 파일을 열어서 내용을 profile_file이란 변수에 넣는다.
# 따로 close()를 쓰지 않아도 된다.

# pickle을 사용하지 않고 일반 파일을 사용할 때
# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
