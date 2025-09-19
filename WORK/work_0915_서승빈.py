# ## ----------------------------------------------------------------
# ##                        PTYHON EXAM
# ##                   제출 : work_0915_이름.py
# ## ----------------------------------------------------------------

# ## ----------------------------------------------------------------
# 1. 제곱 사전 만들기 문제 입니다. 
#    정수 리스트 [1, 2, 3, 4, 5]가 주어졌을 때,
#    key는 원래 숫자, value는 제곱 값으로 하는 딕셔너리를 
#    dict comprehension으로 작성하세요.

print("[1번 문제]")

dict_com = {n: n**2 for n in [1,2,3,4,5]}

print(f"{{원래숫자:제곱값}} => {dict_com}")

 
# ## ----------------------------------------------------------------
# 2. 홀수만 추출한 집합 만들기
#    정수 리스트 [1, 2, 3, 4, 5, 6, 7]에서 홀수만 모은 set을 
#    set comprehension으로 작성하세요.

print("[2번 문제]")

set_com = {n for n in [1, 2, 3, 4, 5, 6, 7] if n%2}

print(f"홀수만 모은 set => {set_com}")


# ## ----------------------------------------------------------------
# 3. 문자열 길이 매핑 
#    문자열 리스트 ["apple", "banana", "cherry"]가 있을 때,
#    key는 문자열, value는 문자열의 길이가 되도록 딕셔너리를 
#    dict comprehension으로 작성하세요.

print("[3번 문제]")

dict_com = {n:len(n) for n in ["apple", "banana", "cherry"]}

print(f"{{문자열:문자열길이}} => {dict_com}")


# ## ----------------------------------------------------------------
# 4. 구구단 dict
#    2단(2×1 ~ 2×9)의 결과를 딕셔너리로 만들되,
#    key는 곱하는 수(1~9), value는 곱셈 결과가 되도록 
#    dict comprehension으로 작성하세요.

print("[4번 문제]")

dict_com = {num:2*num for num in range(1,10)}

print(f"{{곱하는수:곱셈결과}} => {dict_com}")


# ## ----------------------------------------------------------------
# 5. 중복 없는 알파벳 집합 
#    문자열 "hello world"에서 공백을 제외한 알파벳 집합을 
#    set comprehension으로 작성하세요.

print("[5번 문제]")

msg = "hello world"
msg_set = {m for m in msg if m != ' '}

print(msg_set)

# ## ----------------------------------------------------------------
# 6. 조건부 딕셔너리
#    정수 리스트 range(1, 11)이 있을 때,
#    짝수만 key로 사용하고, value는 제곱 값을 가지는 딕셔너리를 
#    dict comprehension으로 작성하세요.

print("[6번 문제]")

dict_com = {n:n**2 for n in range(1,11) if not n%2}
print(f"{{짝수:제곱값}} => {dict_com}")


# ## ----------------------------------------------------------------
# 7. 정수 리스트를 입력받아 최댓값을 반환하는 함수 find_max(nums)를 작성하세요.
#    (내장 함수 max()는 사용하지 말 것)

print("[7번 문제]") ## ★★

## 함수기능 : 정수 리스트를 입력받아 최댓값을 반환
## 함수이름 : find_max
## 매개변수 : nums
## 반환결과 : 최댓값

def find_max(nums):
  max_num = nums[0]
  for num in nums:
    if num > max_num:
      max_num = num
  return max_num

nums_str = input("정수 입력(예: 1 2 3 4): ").split()
print(nums_str)
nums = [int(n) for n in nums_str]

print(f"find_max(nums) => {find_max(nums)}")

# ## ----------------------------------------------------------------
# 8. 정수 n을 입력받아 n! (팩토리얼)을 반환하는 함수 factorial(n)을 작성하세요.
#    (반복문 사용 가능)

print("[8번 문제]")

## 함수기능 : 정수 n을 입력받아 n! (팩토리얼)을 반환
## 함수이름 : factorial
## 매개변수 : n
## 반환결과 : 팩토리얼

def factorial(n):
  fact = 1
  for i in range(1, n+1):
    fact = fact * i
  return fact

n = int(input("팩토리얼로 반환할 정수를 입력: "))
print(f"factorial({n}) => {factorial(n)}")

# ## ----------------------------------------------------------------
# 9.  문자열을 입력받아 거꾸로 뒤집은 문자열을 반환하는 함수 reverse_string(s)를 
#     작성하세요.
print("[9번 문제]")

## 함수기능 : 문자열을 입력받아 거꾸로 뒤집은 문자열을 반환
## 함수이름 : reverse_string
## 매개변수 : s
## 반환결과 : 뒤집힌 문자열

def reverse_string(s):
  return s[::-1]

print(reverse_string("Happy 2025"))

# ## ----------------------------------------------------------------
# 10. 정수 n을 입력받아 n단을 문자열 리스트 형태로 반환하는 함수 
#     multiplication_table(n)을 작성하세요.
#     예시 (n=3)
#     ["3 x 1 = 3", "3 x 2 = 6", ..., "3 x 9 = 27"]
print("[10번 문제]")

## 함수기능 : 정수 n을 입력받아 n단을 문자열 리스트 형태로 반환
## 함수이름 : multiplication_table
## 매개변수 : n
## 반환결과 : 문자열 리스트

def multiplication_table(n):
    return [f"{n} x {i} = {n*i}" for i in range(1, 10)]

print(multiplication_table(3))

# ## ----------------------------------------------------------------
# 11. 문자열이 회문(palindrome: 앞뒤가 같은 문자열)인지 판별하는 함수 
#     is_palindrome(s)를 작성하세요.
print("[11번 문제]")

## 함수기능 : 문자열이 회문(palindrome: 앞뒤가 같은 문자열)인지 판별
## 함수이름 : is_palindrome
## 매개변수 : s
## 반환결과 : Bool

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"))
print(is_palindrome("hello"))

# ## ----------------------------------------------------------------
# 12. 문자열 문장을 입력받아 단어별 등장 횟수를 딕셔너리로 반환하는 함수 
#     word_count(sentence)를 작성하세요.
#     예시 : "apple banana apple"  → {"apple": 2, "banana": 1}
print("[12번 문제]")

## 함수기능 : 문자열 문장을 입력받아 단어별 등장 횟수를 딕셔너리로 반환
## 함수이름 : word_count
## 매개변수 : sentence
## 반환결과 : 단어별 등장 횟수를 딕셔너리

def word_count(sentence):
  words = sentence.split()
  
  counts = {}

  for word in words:
    counts[word] = counts.get(word, 0) + 1
      
  return counts

sentence1 = "apple banana apple"
print(f"'{sentence1}'의 단어별 등장 횟수: {word_count(sentence1)}")

# ## ----------------------------------------------------------------
# 13. 정수 n을 입력받아, n번째 항까지의 피보나치 수열을 리스트로 반환하는 함수 
#     fibonacci(n)을 작성하세요.
# 예시 : fibonacci(5) → [0, 1, 1, 2, 3]
print("[13번 문제]")

## 함수기능 : 정수 n을 입력받아, n번째 항까지의 피보나치 수열을 리스트로 반환
## 함수이름 : fibonacci
## 매개변수 : n
## 반환결과 : 피보나치 수열을 리스트

def fibonacci(n):
    seq = []
    a, b = 0, 1
    for i in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

print(fibonacci(5))


# ## ----------------------------------------------------------------
# 14. 정수 리스트를 입력받아 평균과 표준편차를 튜플 (mean, std)로 반환하는 함수 
#     stats(nums)를 작성하세요.
#     ( 공식을 직접 구현하세요)
print("[14번 문제]")

## 함수기능 : 정수 리스트를 입력받아 평균과 표준편차를 튜플 (mean, std)로 반환
## 함수이름 : stats
## 매개변수 : nums
## 반환결과 : 평균과 표준편차를 튜플

def stats(nums):
    n = len(nums)
    mean = sum(nums) / n  # 평균
    variance = sum((x - mean) ** 2 for x in nums) / n  # 분산
    std = variance ** 0.5  # 표준편차
    return (mean, std)

print(stats([1, 2, 3, 4, 5]))