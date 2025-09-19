## ----------------------------------------------------------------
##                        PTYHON EXAM
##        제출 : 구글 드라이브에 work_0918_서승빈.py
##                 이번주도 고생 많으셨습니다~
## ----------------------------------------------------------------
## 1. '1,234,567,890' 문자열에서 숫자들의 합계를 계산 후 반환하는 함수를 
#     작성하세요. ( 숫자들은 1자리 숫자입니다. )
##  [ 예시 ]
##  [ 호출 ]
##  [ 출력 ] '1,234,567,890' 합계 : 45

def add_str(nums):
    nums_list = nums.split(',')
    total = 0
    for num in nums_list:
        for n in num:
            total += int(n)
    return total

nums = '1,234,567,890'
print(f"[Q1] '{nums}' 합계 : {add_str(nums)}")

## ----------------------------------------------------------------
## 2. “가나*마바사*자***파하”에서 요청하는 번째의 * 인덱스를 반환하는
##    함수를 작성하세요.
##  [ 예시 ]
##  [ 입력 ] 몇 번째 * ? 3
##  [ 호출 ]
##  [ 출력 ] 3번째 *의 인덱스는 9

def return_index(s):
    where_star = int(input("몇 번째 * ?"))

    star_count = 0
    star_index = -1

    for i in range(len(s)):
        if s[i] == '*':
            star_count += 1
            if star_count == where_star:
                star_index = i
                break
    print(f"{where_star}번째 *의 인덱스는 {star_index}")

s = "가나*마바사*자***파하"  
return_index(s)

## ----------------------------------------------------------------
## 3. 아래와 같이 구구단을 출력하는 함수를 작성하세요.
##    함수를 작성하세요.
##  [ 예시 ]
##  [ 입력 ] 출력 단 : 3
##  [ 호출 ]
##  [ 출력 ] 3 * 1 =03	 3 * 4 = 12    3 * 7 = 21
##          3 * 2 =06    3 * 5 = 15    3 * 8 = 24
##          3 * 3 =09	 3 * 6 = 18    3 * 9 = 27

def gugudan():
    dan = int(input("출력 단: "))

    for i in range(1, 4):
        for j in range(i, 10, 3):
            print(f"{dan} * {j} = {dan * j:02d}", end = '\t')
        print()

gugudan()

## -----------------------------------------------------------------
## 4. 점수에 대한 학점을 알려주는 함수를 만들어 주세요.
##  [ 예시 ]
##  [ 입력 ] 점수 입력 : 81
##  [ 호출 ]
##  [ 출력 ] 학    점 : B-

def grade():
    jumsu = int(input("점수 입력 : "))

    if jumsu >= 80:
        print("학     점 : B-")

grade()
## -----------------------------------------------------------------
## 5. 구매한 상품명과 가격을 입력 받아 총 구매 금액을 계산하는 함수 만들어 주세요.
##    단) 구매한 상품명과 가격은 없을 수도 있고 여러개 일 수도 있음
##  [ 예시 ]
##  [ 입력 ] 구매상품정보 : 모니터 123000
##  [ 호출 ]
##  [ 출력 ] 총 구매 금액 : 123,000원
##
##  [ 예시 ]
##  [ 입력 ] 구매상품정보 : 
##  [ 호출 ]
##  [ 출력 ] 총 구매 금액 : 구매한 상품 없음

def calc_total_price(*items): ## *items <-- 튜플로 받음

    if not items:
        return print("총 구매 금액 : 구매한 상품 없음")

    total = 0
    
    for item in items:
        total += item[1]

    return total

total1 = calc_total_price(('모니터', 123000), ('키보드', 27000))
total2 = calc_total_price()

print(total1)
print(total2)

## 6. 리스트 [23, 12, 56, 78, 34]가 주어졌을 때, lambda와 max(), min()을 활용하여 
##   최댓값과 최솟값을 반환하는 함수를 작성하세요.
##  [ 예시 ]
##  [ 호출 ]
##  [ 출력 ] 최대값: 78,  최솟값: 12

def max_min(list_data):
    max_value = max(list_data, key = lambda x: x)
    min_value = min(list_data, key = lambda x :x)
    return max_value, min_value

Q6_list = [23, 12, 56, 78, 34]
max_val, min_val = max_min(Q6_list)
print(f"최댓값 = {max_val}, 최솟값 = {min_val}")

## 7. 생년월일을 입력받아서 나이를 계산해주는 함수 작성하세요.
##  [ 예시 ]
##  [ 입력 ] 생년월일 : 2010년 9월 16일
##  [ 호출 ]
##  [ 출력 ] 나    이 : 15세

def calc_age():
    birth = input("생년월일 : ").split(' ')
    year = birth[0].replace('년', '')
    age = 2025 - int(year)
    return age

print(f"나    이 : {calc_age()}세")

## 8. 주어진 데이터에서 평균, 중앙값, 표준편차 반환하는 함수 작성하세요.
##  [ 예시 ]
##  [ 입력 ] 데이터 : 1,2,3,4,5,6,7,8,9,10
##  [ 호출 ]
##  [ 출력 ] 평균 : 5.5, 중앙값 : 5.5, 표준편차 : 2.87

def trans_data(data):
    
    mean = sum(data)/len(data)

    std = ((sum((x - mean) ** 2 for x in data))/len(data))**0.5

    return mean, std

mean_result, std_result = trans_data([1,2,3,4,5,6,7,8,9,10])
print(f"평균 :{mean_result} 표준편차 : {std_result:.2f}")


## 9. 내정 문자 'A'를 선정하고 사용자가 입력한 문자가 내정 문자와 동일할때까지
##    반복합니다. 단, x/X 입력 시 내정 문자를 맞추지 못해도 종료합니다.
##
##  [ 예시 ] 내정된 문자 A
##  [ 입력 ] 문자를 입력하세요 (종료: x/X): a
##  [ 출력 ] 다릅니다.
##  [ 입력 ] 문자를 입력하세요 (종료: x/X): b
##  [ 출력 ] 다릅니다.
##  [ 입력 ] 문자를 입력하세요 (종료: x/X): X
##  [ 출력 ] 프로그램을 종료합니다.

##  [ 예시 ] 내정된 문자 A
##  [ 입력 ] 문자를 입력하세요 (종료: x/X): a
##  [ 출력 ] 다릅니다.
##  [ 입력 ] 문자를 입력하세요 (종료: x/X): A
##  [ 출력 ] 정답입니다!
##          프로그램을 종료합니다.

secret_char = 'A'

while True:
    user_input = input("문자를 입력하세요 (종료: x/X): ")

    if user_input.upper() == 'X' or user_input.upper() == 'x':
        print("프로그램을 종료합니다.")
        break
    elif user_input == secret_char:
        print("정답입니다!")
        print("프로그램을 종료합니다.")
        break
    else:
        print("다릅니다.")

## 10. 학생들의 시험 점수를 저장했습니다.
##     각 행은 한 학생의 점수를 나타내며, [국어, 영어, 수학] 순서로 저장되었습니다.
scores = [
     [90, 85, 70],   # 1번 학생
     [88, 79, 92],   # 2번 학생
     [100, 100, 90], # 3번 학생
     [55, 60, 65]    # 4번 학생
 ]
## 10-1. 각 학생의 총점과 평균을 계산하여 출력하세요.
## [출력]
## 1번 학생 → 총점: 245, 평균: 81.67
## 2번 학생 → 총점: 259, 평균: 86.33
## 3번 학생 → 총점: 290, 평균: 96.67
## 4번 학생 → 총점: 180, 평균: 60.00

for i in range(len(scores)):
    student_scores = scores[i]
    total_score = sum(student_scores)
    average_score = total_score / len(student_scores)
    
    # 소수점 둘째 자리까지 출력합니다.
    print(f"{i + 1}번 학생 → 총점: {total_score}, 평균: {average_score:.2f}")

## 10-2. 과목별(국어, 영어, 수학) 평균 점수를 계산하여 출력하세요.
## [출력]
## 과목별 평균
## 국어: 83.25, 영어: 81.00, 수학: 79.25