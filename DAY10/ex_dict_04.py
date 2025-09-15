## ----------------------------------------------------------------------------
## Dict 자료형 - 전용 메서드(Method)
## ★ 필수 메서드 : keys(), values(), items()
## ----------------------------------------------------------------------------
## [실습] 5과목 점수를 저장합니다.
##       합계, 평균을 출력하기
## ----------------------------------------------------------------------------
## [List]
jumList = [98, 99, 100, 78, 88]
print(f"합계 : {sum(jumList)}, 평균 : {sum(jumList)/len(jumList)}")

## [Dict-1]
jumDict = {'과목1':98, '과목2':99, '과목3':100, '과목4':78, '과목5':88}
values = jumDict.values()
print(f"합계 : {sum(values)}, 평균 : {sum(values)/len(jumDict)}")
print(f"최대 : {max(jumDict)}, 최소 : {min(jumDict)}")  ## 키가 문자열 => 아스키코드로 비교함. sum은 안됨.

## [Dict-2] => 내장함수는 dict의 키만 사용
jumDict = {1:98, 2:99, 3:100, 4:78, 5:88}
print(f"합계 : {sum(jumDict)}, 평균 : {sum(jumDict)/len(jumDict)}")
print(f"최대 : {max(jumDict)}, 최소 : {min(jumDict)}")