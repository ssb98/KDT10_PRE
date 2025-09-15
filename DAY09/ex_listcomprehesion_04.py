## ---------------------------------------------------------------
## List Comperhension : [] + for~in + if~else
## ---------------------------------------------------------------
## [실습] 아래 데이터를 ListComprehension의 3가지 방식으로
##       코드 작성하세요.
## ---------------------------------------------------------------
data1 = [20, 9, 32, 100, 0, -7]

## [요청1] 원소값을 논리타입으로 변환해서 새로운 리스트에 저장하기
data2 = [bool(d) for d in data1]

print(f'data1 : {data1} ==> data2 : {data2}')


## [요청2] 원소값이 30이상인 원소만 새로운 리스트에 저장하기
data2 = [d for d in data1 if d>=30]

print(f'data1 : {data1} ==> data2 : {data2}')


## [요청3] 원소값이 2의 배수면 2진수로 아니면 16진수로 새로운 리스트에 저장하기
# data2 = [bin(d) if d%2==0 else hex(d) for d in data1]
data2 = [hex(d) if d%2 else bin(d) for d in data1]

print(f'data1 : {data1} ==> data2 : {data2}')