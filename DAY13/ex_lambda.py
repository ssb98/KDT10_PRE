## ---------------------------------------------------------------------
## 다양한 lambda 사용법
## ---------------------------------------------------------------------
## 변수 2개 사용하는 lambda 표현식/함수
print((lambda x, y : x + y)(5, 4))

result = (lambda x, y : x + y)(5, 4)
three  = (lambda x, y, z : x + y + z)(4,5,6)


## lambda 표현식/함수 코드 전에 선언된 변수 사용
y = 100
print((lambda x : x + y)(5))

## 매개변수 없는 lambda 표현식/함수 ----------------------------------------
print((lambda : 100)())

print("A")
print("B")
print("C")

## 세미콜론(;)의 의미: 종료 즉, 마침표(.)
print("A"); print("B"); print("C")

## map() + lambda + 조건부표현식 ------------------------------------------
## 3의 배수는 str타입으로 변환하고 나머지 숫자는 float으로 변환해서 저장
a = range(15)

print(list(map(lambda x : float(x) if x%3 else str(x), a)))
