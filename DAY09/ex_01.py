## ------------------------------------------------------------------------------------------
## List Comprehension
## ------------------------------------------------------------------------------------------
data = ['apple', 'HAPPY', 'Good', 'luck']

## str타입 메서드-----------------------------------------------------------------------------
print(f"{data[2]} isupper()    => 모든 원소가 대문자인지 검사 : {data[2].isupper()}")
print(f"{data[2]} islower()    => 모든 원소가 소문자인지 검사 : {data[2].islower()}")
print(f"{data[2]} upper()      => 모든 원소를 대문자로 : {data[2].upper()}")
print(f"{data[2]} lower()      => 모든 원소를 소문자로 : {data[2].lower()}")
print(f"{data[2]} swapcase()   => 대소문자 토글링      : {data[2].swapcase()}")
print(f"{data[2]} capitalize() => 첫글자만 대문자, 나머지 소문자 : {data[2].capitalize()}")
print(f"{data[3]} capitalize() => 첫글자만 대문자, 나머지 소문자 : {data[3].capitalize()}")
print(f"{data[1]} capitalize() => 첫글자만 대문자, 나머지 소문자 : {data[1].capitalize()}")

## [1] 새로운 리스트에 모든 원소값을 대문자로 저장하기
# data1 = []
# for d in data:
#     data.append(d.upper())

data1 = [d.upper() for d in data]
print(data1)

## [2] 새로운 리스트에 전체 소문자 -> 전체 대문자, 전체 대문자 -> 전체 소문자로 저장하기
# data1 = []
# for d in data:
#     if d.isupper():
#         data1.append(d.lower())
#     else:
#         data1.append(d.upper())
#     data1.append(d.lower() if d.isupper() else d.upper() for d in data)

data2 = [d.lower() if d.isupper() else d.upper() for d in data]
print(data2)

## [3] 새로운 리스트에 int로 저장하기
data = ['3', '-1', '9', '0']
# data1 = []
# for d in data:
#     data.append(ind(d))

data3 = [int(d) for d in data]
print(data3)

## [4] data안에 요소들 중 숫자만 다른 리스트에 저장하기
data = "Good 2025 Happy Day 2026"
# data1 = []
# for d in data:
#     if d.isdecimal():
#         data1.append(d)

data4 = [d for d in data if d.isdecimal()]
print(data4)