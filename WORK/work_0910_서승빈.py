# ## ----------------------------------------------------------------
# ##                        PTYHON EXAM
# ##        제출 : 구글 드라이브에 work_0910_서승빈.py
# ## ----------------------------------------------------------------
# ## ----------------------------------------------------------------
# 1. words = ["I", "study", "python", "language", "!"] 데이터에 대한 
#    아래 코드 작성하세요.    
#    (1)  words의 모든 요소를 for반복문으로 출력
#    (2)  words에서 홀수번째 요소만 for반복문으로 출력
#    (3)  words에서 길이가 3이상인 요소만 for반복문으로 출력
#    (4)  words를 오름차순 정렬하여 모든 요소 출력
print("[1번 문제]")

words = ["I", "study", "python", "language", "!"]

print("(1)  words의 모든 요소를 for반복문으로 출력")
for idx in words:
  print(idx)

print("(2)  words에서 홀수번째 요소만 for반복문으로 출력")
for idx in range(1,len(words),2):
  print(idx)

print("(3)  words에서 길이가 3이상인 요소만 for반복문으로 출력")
for idx in words:
  if len(idx) >= 3 :
    print(idx)

print("(4)  words를 오름차순 정렬하여 모든 요소 출력")
words.sort()
print(words)

# ## ----------------------------------------------------------------
# 2.  아래 데이터에 대한 구현 코드 작성하세요.
#     files = ['intra.h', 'intra.c', 'define.h', 'run.py', 'ex01.py', 'intro.hwp']
#     (1) 확장자 없이 파일명만 출력
#     (2) 확장자가 ‘h’이거나 ‘c’인 것만 출력
#     (3) 파일명에 ‘e’가 2개 이상 있고 ‘f’가 있는 파일명만 출력
print("[2번 문제]")

files = ['intra.h', 'intra.c', 'define.h', 'run.py', 'ex01.py', 'intro.hwp']

print("(1) 확장자 없이 파일명만 출력")
for file in files:
  dot_index = file.find('.')
  file_name = file[:dot_index]
  print(file_name)

print("(2) 확장자가 ‘h’이거나 ‘c’인 것만 출력")
for file in files:
  dot_index = file.find('.')
  if file[dot_index+1:] in 'hc':
    print(file)

print("(3) 파일명에 ‘e’가 2개 이상 있고 ‘f’가 있는 파일명만 출력")
for file in files:
  if file.count('e') >= 2 and file.count('f') > 0:
    print(file)

# ## ----------------------------------------------------------------
# 3. for 반복문을 사용하여 2단부터 9단까지 모두 출력하세요.
#    단 아래와 같이 출력하세요.

#     3               5     
# 3 * 1 = 03      5 * 1 = 05
# 3 * 2 = 06      5 * 2 = 10
# 3 * 3 = 09      5 * 3 = 15
# 3 * 4 = 12      5 * 4 = 20
# 3 * 5 = 15      5 * 5 = 25
# 3 * 6 = 18      5 * 6 = 30
# 3 * 7 = 21      5 * 7 = 35
# 3 * 8 = 24      5 * 8 = 40
# 3 * 9 = 27      5 * 9 = 45

#     7               9     
# 7 * 1 = 07      9 * 1 = 09
# 7 * 2 = 14      9 * 2 = 18
# 7 * 3 = 21      9 * 3 = 27
# 7 * 4 = 28      9 * 4 = 36
# 7 * 5 = 35      9 * 5 = 45
# 7 * 6 = 42      9 * 6 = 54
# 7 * 7 = 49      9 * 7 = 63
# 7 * 8 = 56      9 * 8 = 72
# 7 * 9 = 63      9 * 9 = 81
print("[3번 문제]")

for dan in range(2, 10):
    print(f"{dan:^10}", end="\t")     # 구구단의 단을 표시하기 위한, 구구단 문자열 10칸의 가운데 정렬
print()

for num in range(1, 10):
    for dan in range(2, 10):
        print(f"{dan} * {num} = {dan * num:02d}", end="\t")
    print()

# ## ----------------------------------------------------------------
# 4. 2개의 정수와 덧셈, 뺄셈, 곱셈, 나눗셈 연산자 1개를 입력 받으세요.
#    연산 결과를 출력합니다. 단, 입력 함수는 1개 사용합니다.
print("[4번 문제]")

data = input("2개의 정수와 덧셈, 뺄셈, 곱셈, 나눗셈 연산자 1개를 입력: ").split()

nums = []
oper = ""

for idx in data:
  if idx.isdigit():
    nums.append(int(idx))
  else:
    oper = idx

if len(nums) != 2 or oper not in ['+', '-', '*', '/']:
    print("입력 형식이 잘못되었습니다.")
else:
    a = nums[0]
    b = nums[1]  
    
if oper == '+':
        result = a + b
elif oper == '-':
        result = a - b
elif oper == '*':
        result = a * b
elif oper == '/':
        result = a / b if b != 0 else "0으로 나눌 수 없습니다."

print(f"{a} {oper} {b} = {result}")

# ## ----------------------------------------------------------------
# 5. “가나*마바사*자***파하”에서 첫 번째 *의 인덱스를 출력하세요.
#    세 번째 ‘*’의 인덱스를 출력하세요.
print("[5번 문제]")

msg = "가나*마바사*자***파하"
idx_1 = msg.find('*')
print(f"첫 번째 *의 인덱스를 출력: {idx_1}")
idx_2 = msg.find('*',idx_1+1)
idx_3 = msg.find('*',idx_2+1)
print(f"세 번째 *의 인덱스를 출력: {idx_3}")

# ## ----------------------------------------------------------------
# 6. 좋아하는 단어를 입력 받은 후 대문자로 변환하여 출력하세요.
#    그리고 각 알파벳이 단어안에 몇개 있는지 출력하세요.
#    [예시] Hello
#          H - 1개     e - 1개      l - 2개        o - 1개
print("[6번 문제]")

word = input("좋아하는 단어를 입력:").strip()
Word = word.upper()
print(f'대문자로 변환: {Word}')

word_idx = []

for idx in word:
    if idx not in word_idx:
        word_idx.append(idx)

for idx in word_idx:
    print(f"{idx} - {word.count(idx)}개", end="\t")
print()

# ## ----------------------------------------------------------------
# 7. “1,234,567,890” 문자열에서 숫자들의 합계를 계산 후 출력하세요.
#    숫자들은 1자리 숫자입니다.
print("[7번 문제]")

nums = "1,234,567,890"
nums = nums.replace(",", "")

total = 0

for num in nums:
  num = int(num)
  total += num

print(f"문자열에서 숫자들의 합계: {total}")


# ## ----------------------------------------------------------------
# 8. “산토끼 토끼야 어디를 가느냐 폴짝 폴짝 뛰면서 어디를 가느냐” 문장을 
#     아래와 같이 출력하세요.
#     [출력] 끼토산 야끼토 를디어 냐느가 짝폴 짝폴 서면뛰 를디어 냐느가
print("[8번 문제]")

sentence = "산토끼 토끼야 어디를 가느냐 폴짝 폴짝 뛰면서 어디를 가느냐"
words = sentence.split(" ")
reverse_sentence = ""

for word in words:
  reverse_sentence = "".join(reversed(word))
  print(reverse_sentence, end = ' ')
print()

# ## ----------------------------------------------------------------
# 9. [9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7] 에서 중복된 데이터 제외한 
#     데이터들 평균 출력하세요.
print("[9번 문제]")

data = [9, 3, 1, 8, 7, 2, 1, 4, 2, 3, 5, 7]
data_list = []

for num in data:
  if num not in data_list:
    data_list.append(num)

print(f"중복된 데이터 제외한 데이터들 평균 출력: {sum(data_list)/len(data_list)}")

# ## ----------------------------------------------------------------
# 10. [1,1,5,2,6,9,2]와 [5,9,1,3,4,2,8,7,1,2,5] 데이터 중복된 값을 제거한
#     하나의 리스트를 생성해 주세요.
print("[10번 문제]")

data1 = [1,1,5,2,6,9,2]
data2 = [5,9,1,3,4,2,8,7,1,2,5]

list = []

for num in data1:
  if num not in list:
    list.append(num)

for num in data2:
  if num not in list:
    list.append(num)

print(f"데이터 중복된 값을 제거한 하나의 리스트: {list}")

# ## ----------------------------------------------------------------