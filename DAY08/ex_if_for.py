## ------------------------------------------------------------------------------
##                              if & for
## ------------------------------------------------------------------------------
## [문] 아래 문자열에서 숫자는 숫자끼리, 문자는 문자끼리
##      나누어 주세요.
data = "에어컨 가격은 300만원 24개월 할부"
data1, data2 = "",""

for ch in data:
    if ch.isdecimal():      # 0~9
        data2 += ch
    elif ch.isalpha():      # 언어
        data1 += ch

print(f'data1 = {data1}')
print(f'data2 = {data2}')

# number = ""
# word = ""

# for idx in data:
#     if idx.isalpha():
#         number += idx
#         print(number)
#     else:
#         word += idx
#         print(word)
# print()