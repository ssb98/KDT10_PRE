# ## ----------------------------------------------------------------
# ##                        PTYHON EXAM
# ##        제출 : 구글 드라이브에 work_0912_서승빈.py
# ##                한 주 고생 많으셨습니다 ~ ♥♥♥
# ## ----------------------------------------------------------------
# ## ----------------------------------------------------------------
## 1. 점수에 대한 학점을 알려주는 코드를 작성하세요.  
#  [ 예  시 ]
#  [ 입력 ] 당신의 점수 : 81
#  [ 출력 ] 당신의 학점 : B학점

print("[1번 문제]")

jumsu = input("당신의 점수 :")
jumsu = int(jumsu)

if jumsu >= 90:
  grade = 'A'
elif jumsu >= 80:
  grade = 'B'
elif jumsu >= 70:
  grade = 'C'
elif jumsu >= 60:
  grade = 'D'
else:
  grade = 'F'

print(f"당신의 학점 : {grade}학점")

## 2. 입력받은 정수에 대한 약수를 출력하세요.
#      (약수란? 특정한 수를 다른 수로 나누었을 때, 그 나머지가 0이 되는 수)
#  [ 예  시 ]
#  [ 입력 ] 메시지 입력 : Phone 010-2121-9876
#  [ 출력 ] 문자열 내의 숫자  :  0 1 0 2 1 2 1 9 8 7 6
#
#  [ 예  시 ]
#  [ 입력 ] 메시지 입력 : Hello
#  [ 호출 ] 문자열에서 숫자만 출력 함수
#  [ 출력 ] 문자열 내의 숫자  :  없음

print("[2번 문제]")

msg = input("메시지 입력 :")
msg = list(msg)
num = ""

for m in msg:
  if m.isdecimal():
    num += m

if num:
  print(f"문자열 내의 숫자 : {num}")
else:
  print("문자열 내의 숫자  :  없음")

## 3. 입력된 문자열의 코드값을 16진수로 출력하세요.
#  [ 예  시 ]
#  [ 입력 ] 메시지 입력 : Hello
#  [ 출력 ] Hello의 코드값 : 0x480x650x6c0x6c0x6f

print("[3번 문제]")

msg = input("메시지 입력 :")
result = ""

for m in msg:
  msg_ord = ord(m)
  msg_hex = hex(msg_ord)
  result += msg_hex


## 4. 아래 데이터를 적절한 자료형으로 저장해 주세요.
# ----------------------
#  이름    아이디   결과
# ----------------------
# 홍길동   N20123   합격
# 이철수   N20124   합격
# 이나영   N20125   불합격
# 김민우   N20126   대기
# 박보민   N20127   불합격
# 이나영   N20128   합격
# 김지은   N20129   대기
# ----------------------

print("[4번 문제]")

data = [
    {"이름":"홍길동", "아이디":"N20123", "결과":"합격"},
    {"이름":"이철수", "아이디":"N20124", "결과":"합격"},    
    {"이름":"이나영", "아이디":"N20125", "결과":"불합격"},
    {"이름":"김민우", "아이디":"N20126", "결과":"대기"},
    {"이름":"박보민", "아이디":"N20127", "결과":"불합격"},
    {"이름":"이나영", "아이디":"N20128", "결과":"합격"},
    {"이름":"김지은", "아이디":"N20129", "결과":"대기"}    
        ]

## 5. 4번 문제에서 저장된 데이터를 검색어를 입력받아 예시 결과가
##    출력되도록 코드 작성하세요.
#  [ 예  시 ]
#  [ 입력 ] 검색 : 김민우 N20126
#  [ 출력 ] 결과 : 대기

print("[5번 문제]")
search = input("검색 (이름 아이디 입력): ")

for d in data:
    if search == d["이름"] + " " + d["아이디"]:
        print("결과 :", d["결과"])
        break
else:
    print("검색 결과가 없습니다.")

## 6. 4번 문제에서 저장된 데이터를 검색어를 입력받아 예시 결과가
##    출력되도록 코드 작성하세요.
#  [ 예  시 ]
#  [ 입력 ] 검색 : 합격
#  [ 출력 ] 검색 결과 : 홍길동(N20123) 이철수(N20124) 이나영(N20128)
#
#  [ 예  시 ]
#  [ 입력 ] 검색 : 대기
#  [ 출력 ] 검색 결과 : 김민우(N20126) 김지은(대기) 

print("[6번 문제]")
search = input("검색 (결과 입력: 합격/불합격/대기): ")

result_list = [f'{d["이름"]}({d["아이디"]})' for d in data if d["결과"] == search]

if result_list:
    print("검색 결과 :", " ".join(result_list))
else:
    print("검색 결과가 없습니다.")

## 7. 입력 문자열을 대문자는 소문자로, 소문자는 대문자로 변환 코드 작성하세요.
##    단! 내장 메서드 사용 불가하며 직접 구현하세요.
#  [ 예  시 ]
#  [ 입력 ] 단어 입력 : Apple
#  [ 출력 ] Apple 변환 결과 : aPPLE

print("[7번 문제]")

word = input("단어 입력 :")
ch_word = word.swapcase()

print(f"{word} 변환 결과 : {ch_word}")

## 8. 10명의 점수를 입력 받습니다. 
##    평균을 계산 후 평균 미만 점수를 출력해 주세요.
#  [ 예  시 ]
#  [ 입력 ]  98, 78, 56, 42, 99, 100, 72, 91, 79, 91
#  [ 출력 ]  평    균 => 80.6
#           평균 미만 => 78, 56, 42, 72, 79

print("[8번 문제]")

jumsu = input("10명의 점수를 입력: ").split(', ')
jumsu = [int(j) for j in jumsu]

avg_jumsu = sum(jumsu)/len(jumsu)

under = []

for i in jumsu:
  if i < avg_jumsu:
    under.append(i)

print(f"평균 => {avg_jumsu}")
print(f"평균 미만 => {under}")

## 9. 사용자로부터 단을 입력 받고 입력 받은 단의 구구단을 출력하세요.
##    단. 리스트컴프리핸션(LC : List Comprehension)으로 구현하세요.

print("[9번 문제]")

dan = input("단을 입력 :")
dan = int(dan)

print([f"{dan} * {n} = {dan * n:>02}" for n in range(1,10)])

## 10. 아래 처럼 출력 되도록 코드 작성하세요.
#        * 
#       *** 
#      *****
#     *******
#    *********
#   ***********
#  *************
# ***************
#       ****
#       ****
#  Merry Christmas
#       2025
	
print("[10번 문제]")

for i in range(1,9):
  star = '*'*(2 * i - 1)
  print(f"{star:^15}")

for i in range(1,3):
  print(f"{'****':^15}")


print(f'{"Merry Christmas":^15}')
print(f'{"2025":^15}')

## 11. 숫자 2개를 입력 받은 후 산술연산 수행 후 출력해 주세요.
##     산술연산 : 덧셈, 뺄셈, 곱셈, 나눗셈
#  [ 예  시 ] 
#  [ 입력 ] 숫자 2개 입력(예: 8 9): 12 5
#  [ 출력 ]   결   과   
#          덧  셈:    17
#          뺄  셈:     7
#          곱  셈:    60
#          나눗셈:  2.40
#  [ 예  시 ] 
#  [ 입력 ] 숫자 2개 입력(예: 8 9): 12 0
#  [ 출력 ]   결   과   
#          덧  셈:    12
#          뺄  셈:    12
#          곱  셈:     0
#          나눗셈:  0으로 나눌 수 없습니다.

print("[11번 문제]")

num1, num2 = input("숫자 2개 입력(예: 8 9): ").split()

num1 = int(num1)
num2 = int(num2)

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "0으로 나눌 수 없습니다."


print("  결 과  ")
print(f"덧  셈: {addition:>}")
print(f"뺄  셈: {subtraction:>}")
print(f"곱  셈: {multiplication:>}")
print(f"나눗셈: {division:>.2f}")

## 12. 아래 조건에 맞도록 코드 구현하세요.
##     데이터 : 1,3,5,7,9,11
##
## (01) 1,3,5,7,9,11,13,15가 되도록 확장해 주세요.
##
## (02) 데이터 5를 꺼내는 코드를 작성하세요.
##
## (03) 내림차순으로 데이터를 정렬해 주세요.
##
## (04) 모든 요소를 삭제하는 코드를 작성해 주세요.
print("[12번 문제]")

data = [1, 3, 5, 7, 9, 11]

data.extend([13, 15])
print("(01)", data)

value = data.pop(2)
print("(02)", value)

data.sort(reverse=True)
print("(03)", data)

data.clear()
print("(04)", data)

## 13. 아래 조건에 맞도록 코드 구현하세요.
##     데이터 : '가나다', '한글', '가방', '국가', '쏘핫'
## 
## (01) 저장 후 내림차순으로 정렬해 주세요.
##
## (02) 길이가 가장 긴 요소를 출력하세요.
##
## (03) 정수 코드값으로 변환해 새롭게 저장해 주세요.
##
## (04) 최대, 최소 데이터를 출력하세요.
print("[13번 문제]")

data = ['가나다', '한글', '가방', '국가', '쏘핫']

data.sort(reverse=True)
print("(01)", data)

longest = max(data, key=len)
print("(02)", longest)

code_data = [[ord(ch) for ch in word] for word in data]
print("(03)", code_data)

print("(04) max:", max(data), ", min:", min(data))

## 14. 주민등록 번호를 입력 받은 후 아래 조건에 맞도록 구현하세요.
##     입력 형식 : 000000-0000000
## 
## (01) 입력된 주민등록 번호의 길이와 형식이 맞는지 검사해주세요.
##      검사조건 : 길이, 성별식별값 
##      잘못 된 경우 "유효하지 않는 주민번호입니다." 출력
##
## (02) 성별과 내국인/외국인 구별 후 출력하세요.
##
## (03) 생년월일 입력값에서 나이를 계산해 출력하세요. 
##      단, 나이는 년도까지만 입니다. 
##
## (04) 월일과 오늘날짜와 비교해서 생일일 경우 "생일축하합니다" 출력하세요.
##      단, 생일이 지난 경우는 무시합니다. 
print("[14번 문제]")

ssn = input("주민등록번호 입력 (예: 000000-0000000): ")

if len(ssn) != 14 or ssn[6] != '-' or not ssn.replace('-', '').isdigit():
    print("유효하지 않는 주민번호입니다.")
else:
    birth = ssn[:6]
    gender_code = int(ssn[7])

    if gender_code in [1, 2]:
        century = 1900
        nationality = "내국인"
    elif gender_code in [3, 4]:
        century = 2000
        nationality = "내국인"
    elif gender_code in [5, 6]:
        century = 1900
        nationality = "외국인"
    elif gender_code in [7, 8]:
        century = 2000
        nationality = "외국인"
    else:
        print("유효하지 않는 주민번호입니다.")
        exit()

    gender = "남자" if gender_code % 2 == 1 else "여자"
    print("(02)", gender, nationality)

    year = century + int(birth[:2])
    age = 2025 - year
    print("(03) 나이:", age, "세")

    month = int(birth[2:4])
    day = int(birth[4:6])

    if month == 9 and day == 15:
        print("(04) 생일축하합니다")

## 15. 아래 조건에 맞도록 코드 작성 바랍니다.
##     데이터 : ‘Happy Christmas’ 
## 
## (01) 아래와 같이 저장해 주세요.
##      결과 : ['H', 'a', 'p', 'p', 'y', ' ', 'C', 'h', 'r', 'i', 's', 't', 'm', 'a', 's']      
##
##
## (02) 중복을 제거한 데이터로 저장해 주세요.
##      결과 : ['H', 'C', 'm', 'p', 'h', 'a', 'r', 's', 't', 'i', ' ', 'y']
##
##
## (03) 데이터에서 알파벳별로 개수를 저장해 주세요.
##      결과 : {' ': 1, 'C': 1, 'H': 1, 'a': 2, 'h': 1, 'i': 1, 'm': 1, 'p': 2, 'r': 1, 's': 2, 't': 1, 'y': 1}
##

print("[15번 문제]")

data = 'Happy Christmas'

result_01 = list(data)
print(f"결과 (01) : {result_01}")

result_02 = list(set(data))
print(f"결과 (02) : {result_02}")

result_03 = {}
for d in data:
  result_03[d] = result_03.get(d, 0) + 1

print(f"결과 (03) : {result_03}")

## 16. 아래 처럼 결과가 출력되도록 코드 작성하세요.
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
print("[16번 문제]")

for i in range(1, 8, 2):
  star = '*' * i
  print(f"{star:^7}")

for i in range(5, 0, -2):
  star = '*' * i
  print(f"{star:^7}")