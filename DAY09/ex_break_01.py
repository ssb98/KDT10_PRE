## ------------------------------------------------
## break : for/while 반복을 중단시키는 키워드/명령어
##         - 즉시 반복을 중단함
##         - break 아래의 코드를 절대 실행 안 됨!
## ------------------------------------------------
## [요청] data 리스트의 원소가 7의 배수면 반복을 중단
data = [1, 3, 5, 7, 9, 11, 13]

for num in data:
    if not num%7:
        break  ## 즉시 중단!! 아래 코드 실행 X
    print(num)

idx = 0             ## 원소 읽기 위한 인덱스
size = len(data)    ## 원소 범위 지정위한 변수

while idx < size:
    if not data[idx]%7:
        break
    print(data[idx])
    idx += 1
