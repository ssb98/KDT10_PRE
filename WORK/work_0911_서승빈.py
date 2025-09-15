# ## ----------------------------------------------------------------
# ##                        PTYHON EXAM
# ##        제출 : 구글 드라이브에 work_0911_서승빈.py
# ## ----------------------------------------------------------------
# ## ----------------------------------------------------------------
# 1. 아래 리스트 원소들을 정수형으로 변환 후 저장하세요.
##   List Comprehension 문법으로 작성하세요.
#    data = ['9', '3', '7', '-1']
#
# 출력예시
# [출력] 글자입니다.
print("[1번 문제]")

data = ['9', '3', '7', '-1']
data1 = [int(d) for d in data]
print(f"data1 = {data1}")
print(f"{type(data1)}입니다.")

## ----------------------------------------------------------

# 2. 아래 예시처럼 입력 데이터를 체크해 주세요.
#    5번 반복 질문해 주세요.
# 출력예시 #1
# [입력] 메시지 입력: 하늘 바다
# [출력] 글자입니다.
# 
# 출력예시 #2
# [입력] 메시지 입력:
# [출력] 공백입니다.
# 
# 출력예시 #3
# [입력] 메시지 입력: Good 2025 Happy
# [출력] 글자와 숫자 입니다.
# 
# 출력예시 #4
# [입력] 메시지 입력: GOOD
# [출력] 대문자 입니다.
# 
# 출력예시 #5
# [입력] 메시지 입력: abc good
# [출력] 소문자 입니다.
# 
# 출력예시 #6
# [입력] 메시지 입력: '3²' '½'
# [출력] 숫자 입니다.
print("[2번 문제]")

for m in range(5):
  msg = input("메시지 입력:").replace(' ', '')

  if msg.isalpha():
    if msg.isupper():
      print("대문자 입니다.")
    elif msg.islower():
      print("소문자 입니다.")
    else:
        print("글자입니다.")
  elif msg.isdigit():
    print("숫자입니다.")
  elif msg.isalnum():
    print("글자와 숫자입니다.")
  elif not msg.isspace():
    print("공백입니다.")



## ----------------------------------------------------------

# 3. 알파벳/한글 입력 받은 후 해당 문자의 코드값을 출력하세요.
#    알파벳/한글 외의 문자는 ‘정확한 데이터가 아닙니다’를 출력하세요.
# 
# 출력예시 #1
# [입력] 알파벳/한글 입력: 오늘
# [출력] 50724 45720 
# 
# 출력예시 #2
# [입력] 알파벳/한글 입력: today
# [출력] 116 111 100 97 121 
# 
# 출력예시 #3
# [입력] 알파벳/한글 입력: today12
# [출력] 정확한 데이터가 아닙니다
print("[3번 문제]")

word = input("알파벳/한글 입력:")

if word.isalpha():
  for w in word:
    if w.isalpha():
      print(ord(w), end = ' ')
else:
   print("정확한 데이터가 아닙니다")



## ----------------------------------------------------------

# 4. 1 ~ 100 범위에 숫자를 누적 합계를 계산해 주세요.
##   단, 합계가 33이상이면 계산 중단함.
##  for문 방식
print("[4번 문제]")

total = 0

for num in range(1, 101):
  total += num
  if total >= 33:
    break

print(total)

##  while문 방식
total = 0
num = 1

while not total >= 33:
  total += num
  num += 1

print(total)



## ----------------------------------------------------------

# 5. List Comprehension 문법으로 코드 작성하세요.
#    values=['9', '0', '3', '5', '2']
#
# 출력예시 #1
# [입력] 변환 타입 : 정수형
# [출력] [9, 0, 3, 5, 2]   
#
# 출력예시 #2
# [입력] 변환 타입 : 논리형
# [출력] [True, True, True, True, True]
#
# 출력예시 #3
# [입력] 변환 타입 : 실수형
# [출력] [9.0, 0.0, 3.0, 5.0, 2.0]
print("[5번 문제]")
values=['9', '0', '3', '5', '2']

types = input("변환 타입 :")

if types== '정수형':
   values2 = [int(v) for v in values]
   print(values2)
elif types== '논리형':
   values2 = [bool(v) for v in values]
   print(values2)
elif types== '실수형':
   values2 = [float(v) for v in values]
   print(values2)



## ----------------------------------------------------------

# 6. 1 ~ 100 범위에 숫자를 누적 합계를 계산해 주세요.
##   단, 합계가 33이상이면 계산 중단함.
print("[6번 문제]")

total = 0

for num in range(1,101):
  total += num
  if total >= 33:
    break

print(total)



## ----------------------------------------------------------

# 7. “!@Happy a Good Day~^^” 문자열을 시작과 끝을 검사해 주세요.
#      - 시작 :“!@”         - 끝 : “^^”
print("[7번 문제]")

data = "!@Happy a Good Day~^^"
start = data[0:2]
end = data[data.find('^'):]
print(data)
print(f'- 시작 : "{start}" \t - 끝 : "{end}"')



## ----------------------------------------------------------

## 8. 알고 싶은 구구단을 입력 받은 후 구구단을 출력하세요.
## -  문자열 포맷과 이스케이프문자를 사용해서 출력하세요.
## - [입력] 구구단 : 5
## - [출력] 5 * 1 = 05    5 * 2 = 10       5 * 3 = 15   
##         5 * 4 = 20   5 * 5 = 25     5 * 6 = 20
##         5 * 7 = 35   5 * 8 = 40     5 * 9 = 45   
print("[8번 문제]")

dan = int(input("구구단 :"))

print(f"""{dan} * 1 = {dan * 1:02d}\t{dan} * 2 = {dan * 2:02d}\t{dan} * 3 = {dan * 3:02d}
{dan} * 4 = {dan * 4:02d}\t{dan} * 5 = {dan * 5:02d}\t{dan} * 6 = {dan * 6:02d}
{dan} * 7 = {dan * 7:02d}\t{dan} * 8 = {dan * 8:02d}\t{dan} * 9 = {dan * 9:02d}""")

## ----------------------------------------------------------

# 9. 계절명을 입력받고 해당하는 달을 출력해주세요.
## - [입력] 좋아하는 계절 : 여름
## - [출력] 여름은 6월~8월 입니다.
print("[9번 문제]")

season = input("좋아하는 계절 :")

if season == "봄":
  print(f"{season}은 3월~5월 입니다.")
elif season == "여름":
  print(f"{season}은 6월~8월 입니다.")
elif season == "가을":
  print(f"{season}은 9월~11월 입니다.")
elif season == "겨울":
  print(f"{season}은 12월~2월 입니다.")

  

## ----------------------------------------------------------

## 10. 5과목 점수를 입력 받아서 저장해 주세요.
## - 아래 조건에 맞도록 메시지 출력하세요.
## - 입력 데이터 여부 체크           => 입력된 데이터가 없습니다. 
## - 입력 데이터가 숫자가 맞는지 체크  => 정확한 데이터가 아닙니다. 
## - 5과목 점수에서 최고 점수, 최저 점수, 총합, 평균 출력
print("[10번 문제]")

jumsu_input = input("5과목 점수를 입력(예: 10 20 30 40 50):")

if jumsu_input.isspace():
  print("입력된 데이터가 없습니다.")

jumsu_list = jumsu_input.split()

jumsu = []

for j in jumsu_list:
  if not j.isdecimal():
    print("정확한 데이터가 아닙니다.")
  jumsu.append(int(j))

total_j = sum(jumsu)
avg_j = total_j/len(jumsu)
max_j = max(jumsu)
min_j = min(jumsu)

print(f"최고 점수 : {max_j}점")
print(f"최저 점수 : {min_j}점")
print(f"총합 점수 : {total_j}점")
print(f"평균 점수 : {avg_j}점")



## ----------------------------------------------------------

# 11. 월을 숫자로 입력 받고 영어로 월을 출력해 주세요.
## - [입력] 좋아하는 월 : 3
## - [출력] 3월은 March
print("[11번 문제]")

mon = input("좋아하는 월 :")

if mon == "1":
  print(f"{mon}은 January")
elif mon == "2":
  print(f"{mon}은 February")
elif mon == "3":
  print(f"{mon}은 March")
elif mon == "4":
  print(f"{mon}은 April")
elif mon == "5":
  print(f"{mon}은 May")
elif mon == "6":
  print(f"{mon}은 June")
elif mon == "7":
  print(f"{mon}은 July")
elif mon == "8":
  print(f"{mon}은 August")
elif mon == "9":
  print(f"{mon}은 September")
elif mon == "10":
  print(f"{mon}은 October")
elif mon == "11":
  print(f"{mon}은 November")
elif mon == "12":
  print(f"{mon}은 December")



## ----------------------------------------------------------

# 12. 로그인 기능을 구현합니다. 
#     아이디(10자리 숫자, 영어, 기호)와 패스워드(8자리 숫자, 영어) 입력 받습니다.
#     [예] 임의의 아이디 : kkk12!,  비밀번호: 123aa
#     미리 지정한 아이디와 비밀번호가 맞다면 "kkk12!님! 반갑습니다."
#                                틀리면 "아이디 또는 비밀번호 확인하세요."
print("[12번 문제]")

valid_id = "kkk12!"
valid_pw = "123aa"

user_id = input("아이디를 입력하세요(예: 10자리 숫자, 영어, 기호)): ")
user_pw = input("비밀번호를 입력하세요(예:8자리 숫자, 영어)): ")

if user_id == valid_id and user_pw == valid_pw:
    print(f"{user_id}님! 반갑습니다.")
else:
    print("아이디 또는 비밀번호를 확인하세요.")


## ----------------------------------------------------------

# 13. 조건에 맞게 구현하세요.
# [13-1] 아래와 같은 크기로 출력
#       *
#       ***
#       *****
#       ***
#       *
print("[13-1번 문제]")

for i in range(1, 6, 2):
    stars = "*" * i
    print(stars)

for i in range(3, 0, -2):
    stars = "*" * i
    print(stars)

# [13-2] 입력 받은 크기로 출력
#        크기 입력: 3
#        *
#        ***
#        *
print("[13-2번 문제]")

size = int(input("크기 입력: "))

for i in range(1, size +1, 2):
    stars = "*" * i
    print(stars)

for i in range(size - 2, 0, -2):
    stars = "*" * i
    print(stars)

## ----------------------------------------------------------