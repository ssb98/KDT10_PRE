## ------------------------------------------------------------
## for ~ in 반복문 : 원소 읽기용
## ------------------------------------------------------------
## [1] List와 tuple 
persons = [('홍길동', '대구',), ('마징가', '부산'), 'Good', range(5)]
#              원소0번              원소1번        원소2번  원소3번

for p in persons:
    print(p, type(p))

## [2] List와 언패킹(Unpacking)
persons = [('홍길동', '대구',)]

for name, loc in persons:
    print(name, loc, type(name), type(loc))         ## 따로따로 들어가서 str 타입


## ------------------------------------------------------------
## for ~ in range() 반복문 : 카운팅/인덱싱용
## ------------------------------------------------------------
datas = ['1', '5', '0']

## str숫자 ==> int숫자로 타입변경
datas[0] = int(datas[0])
datas[1] = int(datas[1])
datas[2] = int(datas[2])

print(datas)

## int 숫자 ==> str 숫자 변환
for idx in range(len(datas)):
    datas[idx] = str(datas[idx])

print(datas)