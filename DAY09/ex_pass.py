## ------------------------------------------------
## pass : 파이썬의 문법 오류 방지 위해서 사용
##        - 아무일도 안 함!
##        - 들여쓰기가 필요한 문법
##        - if, while, for, class, def ...
## ------------------------------------------------
## [반복문과 pass]
for ch in range(50):
    if ch%5==0:
        pass
    print(ch)

## [클래스와 pass]
class MyClass:
    pass

## [함수와 pass]
def myFunc():
    pass