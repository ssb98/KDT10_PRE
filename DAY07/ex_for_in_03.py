## ---------------------------------------------------------------------------
## for ~ in 반복문 // 이런 종류로 시험 냄. ex) 생년월일 -> 별자리
## ---------------------------------------------------------------------------
## [1] 정수를 10개 입력 받아 최대값, 최소값, 평균 출력하기
## -> input() : str타입의 숫자 => int로 형변환
## -> 10개 정수 입력 및 저장
nums = input("정수 10개 입력: ").split()

## -> str숫자 => int 형변환
for idx in range(len(nums)):
    nums[idx] = int(nums[idx]
                    )
print(f'nums => {nums}')

## -> list 원소 중에서 최대값, 최소값, 평균
print(f'최대값 => {max(nums)} 최소값 => {min(nums)} 평균 => {sum(nums)/len(nums)}')


## [2] Happy 단어의 코드값을 출력하기
##    문자         코드값                 기계어
## 예) AB          6566            0100000101000010
##              ord(문자1개)            bin(10진수)
word = "Happy"
dec_code = ''
bin_code = ''

for w in word:
    ## 문자 1개에 대한 코드값 10진수
    code = ord(w)
    dec_code += str(code)           # A += B : A와 B덧셈 후 결과를 다시 A에 저장 

    ## 코드값을 2진수로 변환
    b_code = bin(code)
    bin_code += b_code[2:]          # A += B : A와 B덧셈 후 결과를 다시 A에 저장

print(f'{word} {dec_code} {bin_code}')