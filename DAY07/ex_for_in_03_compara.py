## ---------------------------------------------------------------------------
## for ~ in 반복문
## ---------------------------------------------------------------------------
## [1] 정수를 10개 입력 받아 최대값, 최소값, 평균 출력하기
## -> input() : str타입의 숫자 => int로 형변환
## -> 10개 정수 입력 및 저장
nums = input("정수 10개 입력: ").split()

## -> str숫자 => int 형변환


for data in nums:
    nums[data] = int[data]
    max(data), min(data)
    nums[data] = str[data]
    print(f'최대값 : {max(data)}, 최소값 : {min(data)}')


## [2] Happy 단어의 코드값을 출력하기
##    문자 코드값    기계어
## 예) AB 6566 0100000101000010
msg = "Happy"
for idx in range(len(msg)):
    print(ord(idx))