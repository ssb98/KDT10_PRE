## -------------------------------------------------------------
## 순서 있는(Sequence) 자료형 - tuple
## - 변경/삭제 위한 list 형변환 진행 ==> tuple 다시 변환
## -------------------------------------------------------------
## phone => 010, 016, 017, 018, 019
phone=('010','016','017','018','019')
print(f'phone : {type(phone)}, {len(phone)}개, {phone}')

## 전부다 010 변경 => list로 형변환
phone = list(phone)
phone[:]=['010']
print(f'phone : {type(phone)}, {len(phone)}개, {phone}')

## 다시 => tuple로 형변환
phone = tuple(phone)
print(f'phone : {type(phone)}, {len(phone)}개, {phone}')


## 총정리

## 순서있는 자료형 => 인덱스
## 종류 : str, list, tuple, range

## str   => '  ',"  ",'''  ''',"""  """
## list  => [1, 2], ["A", 100]
## tuple => (11, 22), ('A',)
## range => range(시작, 끝+1, 간격)

## -> 인덱싱, 슬라이싱
## -> 덧셈연산, 곱셈연산 가능 => range 제외