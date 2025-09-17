## ---------------------------------------------------------------------
## 내장함수 sorted()
## - 형식 : sorted(iterable, reverse=False, key=None)
## - 기능 : 오름차순 정렬 후 결과를 리스트로 반환
## ---------------------------------------------------------------------
## list 타입의 iterable 데이터 -------------------------------------------
data = [1, 2, 7, 4, 5, 6, 3, 8, 9, 10]

asc  = sorted(data)
desc = sorted(data, reverse=True)
print('asc => ', asc, '\ndesc => ', desc)


## tuple 타입의 iterable 데이터 -------------------------------------------
data = (1, 2, 7, 4, 5, 6, 3, 8, 9, 10)

asc  = sorted(data)
desc = sorted(data, reverse=True)
print('asc => ', asc, '\ndesc => ', desc)


## set 타입의 iterable 데이터 -------------------------------------------
data = {1, 2, 7, 4, 5, 6, 3, 8, 9, 10}

asc  = sorted(data)
desc = sorted(data, reverse=True)
print('asc => ', asc, '\ndesc => ', desc)


## dict 타입의 iterable 데이터 -------------------------------------------
data = {'A':10, 'Z':7, 'D':20, 'B':100}

## => key 위주 : key 정렬
asc  = sorted(data)
desc = sorted(data, reverse=True)
print('asc => ', asc, '\ndesc => ', desc)

## => value 정렬 위해서 정렬 기준을 설정 key매개변수에
## => (k, v) : items()    [0] => k, [1] => value
##                |---------------------(k, v)     v
asc  = sorted(data.items(), key = lambda item : item[1])
desc = sorted(data.items(), key = lambda item : item[1], reverse=True)
print('asc => ', asc, '\ndesc => ', desc)


## => sorted() 내장함수의 정렬 기준 설정 => key 매개변수 --------------------
data = ['Good', 'apple', 'Zoo', 'banana']
asc  = sorted(data)                                 # 코드값 순서대로
desc = sorted(data, reverse=True)
print('asc => ', asc, '\ndesc => ', desc)

##                                'Good' => 'good'
asc  = sorted(data, key = lambda d : d.lower())     # 코드값이 아니라 알파벳 순서대로
desc = sorted(data, key = lambda d : d.lower(), reverse=True)
print('asc => ', asc, '\ndesc => ', desc)