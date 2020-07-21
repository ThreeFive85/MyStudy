# pickle : 프로그램상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장을 해주는 것
'''
프로그램을 작성하다 AttributeError: module 'pickle' has no attribute 'dump'와 같은 에러가 났다.
그래서 찾아보니 파일명을 pickle.py로 만들었는데 파일이름과 import한 pickle이 동일한 이름이라 에러가 난것이였다.
그래서 파일명을 usePickle.py로 수정하고 나니 해결되었다.
'''
import pickle
# 파일 쓰기
# profile_file = open("profile.pickle", "wb")
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file에 저장
# profile_file.close()

# 파일 읽기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()
