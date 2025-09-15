## [1] 문자열을 입력 받은 후 문자열 구성요소 검사 결과를 출력하세요.
##     예) 문자만 있는지, 숫자만 있는지

data = input()
print(f"문자만 있는지 : {data.isalpha()}")
print(f"숫자만 있는지 : {data.isdigit()}")

## [2] 'Merry Christmas'에 대해서 아래 조건에 맞는 코드 작성하세요.
##      - 대문자는 소문자로 소문자는 대문자로 변환 저장 및 추력
##      - 모두 대문자로 변환 후 저장 및 출력
##      - 모두 소문자로 변환 후 저장 및 출력

data = 'Merry Christmas'

swapcase_data = data.swapcase()
print("대문자는 소문자로 소문자는 대문자로 변환 : ",swapcase_data)

upper_data = data.upper()
print("모두 대문자로 변환 : ", upper_data)

lower_data = data.lower()
print("모두 소문자로 변환 : ", lower_data)

## [3] [2]의 문자열을 구성하는 문자의 갯수와 인덱스 범위를 출력하세요
## - 예: Merry Christmas  문  자 개수 : OO개 
##       Merry Christmas  인덱스 범위 : O ~ O

data = 'Merry Christmas'

print(f"{data}  문자   개수 : {len(data)}개")
print(f"{data}  인덱스 범위 : 0 ~ {len(data) -1}개")

## [4] 문자열에서 조건에 맞는 문자열 출력
## - HappyAppleanimal : a의 인덱스 모두 출력
data = "HappyAppleanimal"
print(f"a의 인덱스 : {data.find('a', 1, len(data))}")
print(f"a의 인덱스 : {data.find('a', 10, len(data))}")
print(f"a의 인덱스 : {data.find('a', 14, len(data))}")

## [5] 사용자로부터 아래 정보를 1개 input()함수로 입력 받은 후
##     분리해서 출력 바랍니다.
##     - [예시] 이름, 고향, 나이, 성별 입력 : 
##     - [입력] "홍길동, 대구, 29, 남"
##     - [출력] ['홍길동', '대구', '29', '남']

data = input("이름, 고향, 나이, 성별 입력 : ")
print(data.split(", "))

## [6] 알고 싶은 구구단을 입력 받은 후 구구단을 출력하세요.
##     문자열 포맷과 이스케이프문자를 사용해서 출력하세요.
##     - [입력] 구구단 : 5
##     - [출력] 5 * 1 = 05    5 * 2 = 10       5 * 3 = 15   
##             5 * 4 = 20   5 * 5 = 25     5 * 6 = 20
##             5 * 7 = 35   5 * 8 = 40     5 * 9 = 45   

data = input("구구단 : ")
data = int(data)
print(f"{data} * {1} = {data * 1}\t{data} * {2} = {data * 2}\t{data} * {3} = {data * 3}\n{data} * {4} = {data * 4}\t{data} * {5} = {data * 5}\t{data} * {6} = {data * 6}\n{data} * {7} = {data * 7}\t{data} * {8} = {data * 8}\t{data} * {9} = {data * 9}")

## [7] 아래 조건을 만족하는 코드를 작성하세요.
##     7-1. 주민등록번호 881120-1068234
##          연월일(YYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력하세요.

data = "881120-1068234"
print("연월일(YYMMDD) : ", data[:6])
print("그 뒤의 숫자 부분 : ", data[7:])

##     7-2. 문자열 a:b:c:d
##          해당 문자열에서 a, b, c, d 만 출력해 주세요.

data = "a:b:c:d"
print(f'해당 문자열에서 a, b, c, d 만 출력 : {data.split(":")}')

##     7-3. “에이컨 월 48,584원에 무이자 36개월의 조건으로 판매" 
##          에서 총 금액을 출력해 주세요.
##          [출력] 에어컨 금액 : OOOOOOO원  

월금액 = 48584
개월수 = 36
print(f"에어컨 금액 : {월금액 * 개월수}원")

##     7-4. “가로 10cm, 세로 11cm인 직사각형 넓이 계산” 
##          넓이 계산 후 출력하세요.
##          [출력] 직사각형 넓이 : 가로 10 x  세로 11 = 110

가로 = 10
세로 = 11
print(f'직사각형 넓이 : 가로 {가로} x 세로 {세로} = {가로 * 세로}')

## [8] 아래 조건을 만족하는 코드를 작성해 주세요.
##     8-1. 아래 데이터를 jumsu라는 변수명으로 저장해 주세요.  
##          점수 98 71 90  82  88

jumsu = ["점수", 98, 71, 90, 82, 88]
print(jumsu)

##     8-2. 정수 1개를 입력받은 후 그 숫자만큼 리스트 원소를 출력해 주세요.
##          - data = [10, 8, 3, "A"]
##          - [입력] 정수 입력: 2
##          - [출력] [10, 8, 3, "A", 10, 8, 3, "A"]

data = [10, 8, 3, "A"]
정수 = int(input("정수 입력: "))
print(data * 정수)

##     8-3. [1,3,5,7,9,11]를 [1,15]가 되도록 코드를 구현해 주세요.
##          단, 2가지 방법으로 구현해주세요.

data = [1,3,5,7,9,11]
data[1]=15
del data[2:]
print(data)

data[1:]=[15]
print(data)

##     8-4. [11, 22, ['Good', 'Luck'], 33, 44, 55] 데이터를 저장하세요.
##          'Luck' 데이터를 출력하세요.
##          'Luck' 데이터를 'lUCK'로 출력해주세요.

data = [11, 22, ['Good', 'Luck'], 33, 44, 55]
print(data[2][1])
print(data[2][1].swapcase())