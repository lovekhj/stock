import json

# zip()함수는 iterable 객체를 인자로 받아서 사용합니다. 여러 개의 iterable객체를 받은 후 자료형 들을 묶어서 튜플 형태로 출력해줍니다.
# # zip(*iterable) : 동일한 개수로 이루어진 자료형을 묶어 줌
# a = ['one', 'two', 'three']
# b = ['a', 'b', 'c']
# list(zip(a, b))
# >>> [('one', 'a'), ('two', 'b'), ('three', 'c')]
# # 두 리스트의 요소 끄집어내기
# # zip 함수 사용한 방법
# for val1, val2 in zip(a, b):
#     print(val1, val2)
#
# >>>
# one a
# two b
# three c

# dictionary 만들기
# A = ['name', 'age', 'phone', 'gender']
# B = ['CHAN', 28, '010-XXXX-YYYY', 'male']
# d = dict(zip(A, B))
# d
# >>>
# {'name': 'CHAN', 'age': 28, 'phone': '010-XXXX-YYYY', 'gender': 'male'}

# 참고 : https://www.daleseo.com/python-json/
# loads() 함수: JSON 문자열을 Python 객체로 변환
# dumps() 함수: Python 객체를 JSON 문자열로 변환
#

# # ******************************************************************
# # 파일읽기
# # ******************************************************************
#
# file_name = 'log_test_01.log'
# file = open(file_name, 'r')
# data = []
# order = ['date', 'url', 'type', 'message']
#
# for line in file.readlines():
#     details = line.split('|')
#     # for 문으로 데이터 만들기
#     details = [x.strip() for x in details]
#     # map함수로 structure만들기
#     structure = {key: value for key, value in zip(order, details)}
#     data.append(structure)
#     # print(structure)
#
# print(data)
# # for entry in data:
# #     print(json.dumps(entry, indent='4'))


# # ******************************************************************
# # 파일읽기
# # ******************************************************************
# import os
# file_nm = r'C\mintit~~~~ '
# with open(file_nm, 'r', endcoding='UTF-8') as f:
#     lines = f.readlines()
#     for line lines:
#         print(line)


