cabinet = {3: "renerd", 100: "penny"}
print(cabinet[3])
print(cabinet.get(100))
# cabinet[5]처럼 없는 값을 출력하려고 할 때는 오류를 출력하고 프로그램이 종료되고,
# cabinet.get(5)는 값이 없다라는 None이 출력되고 나머지 프로그램이 동작한다.
# cabinet.get(5, "사용 가능")은 None이 사용 가능으로 바뀌어 출력된다.

# 키 값 확인
print(3 in cabinet)
print(5 in cabinet)

# 키는 정수가 아닌 문자열도 가능하다.
cabinet_str = {"A-3": "renerd", "B-100": "penny"}
print(cabinet_str["A-3"])
print(cabinet_str.get("B-100"))

# 새 손님
cabinet[20] = "shellden"
print(cabinet)

# 간 손님
del cabinet[3]
print(cabinet)

# key 들만 출력
print(cabinet_str.keys())

# value 들만 출력
print(cabinet_str.values())

# key, value 쌍으로 출력
print(cabinet_str.items())

# 비우기
cabinet_str.clear()
print(cabinet_str)
