## -------------------------------------------------------------
## 함수 관련
## -------------------------------------------------------------
## [실1] 데이터의 타입에 따른 덧셈 결과를 반환하는 함수
##       함수이름은 back_result
##       매개변수는 3개의 데이터. 타입은 int, float, str 가능
##       단, 타입이 다르면 형변환 후 결과 반환
##       str이면 모두 str로 형변환 후 반환
## -------------------------------------------------------------
## ★정답★
def back_result(d1, d2, d3):
    ## 내장함수 isinstance(data, 타입명) => True/False
    ##         type(data) == 타입명     => True/False
    check = [True if isinstance(d, str) else False for d in [d1, d2, d3]]
    # check = [True if type(d)==str else False for d in [d1, d2, d3]]

    ## 3개 데이터 중 str 타입이 하나라도 있다면 str로 형변환 후 연산 처리
    if sum(check): ## sum : True를 1로, False를 0으로 처리하는 특성 때문에 논리적인 연산
        return str(d1)+str(d2)+str(d3)
    else:
        return d1+d2+d3

## [테스트]
print("1, 3, 4 => ",       back_result(1, 3, 4))
print("1, 3, 0.4987 => ",  back_result(1, 3, 0.4987))
print("'1', 3, 4 => ",     back_result('1', 3, 4))
print("'1', '3', '4' => ", back_result('1', '3', '4'))
print(".1, .3, 4. => ",    back_result(.1, .3, 4.))

## ★내가한거★ - 비교하고 알아가기
# def back_result(data1, data2, data3):
#     back_result = [data1, data2, data3]
#     result = []

#     for data in back_result:
#         result.append(str(data))

#     result = data1 + data2 + data3  

#     return result

# print(back_result(1, 2, 3))


## -------------------------------------------------------------
## [실2] 변환을 원하는 조건에 맞는 결과를 반환하는 함수
##       함수이름은 convert_number
##       매개변수는 정수만 가능
##                 진법(10진수, 8진수, 2진수, 16진수, 그 외 처리)
## -------------------------------------------------------------
## ★정답★
def convert_number(num, kind):
    # if type(num) != int:
    if not str(num).isdecimal():
        return "유요한 데이터 타입이 아닙니다."
    
    if kind not in ['10진수', '8진수', '2진수', '16진수']:
        return "유효한 진법이 아닙니다."
    
    if kind == '16진수':
        return hex(num)
    elif kind =='10진수':
        return num
    elif kind =='8진수':
        return oct(num)
    else:
        return bin(num)

print(convert_number(9.8, '16진수'))
print(convert_number(12 , '10진수'))
print(convert_number(9.8, '8진수'))
print(convert_number(9  , '2진수'))


## ★내가한거★ - 비교하고 알아가기
# def convert_number(num):
#     convert_num = []
#     num = int(num)
#     convert_num.append(bin(num))
#     convert_num.append(oct(num))
#     convert_num.append(hex(num))

#     return convert_num

# print(convert_number(10))

## -------------------------------------------------------------
## [실3] 4칙 연산 결과를 반환하는 함수
##       함수이름은 print_calc
##       매개변수는 list타입의 숫자데이터만 가능
## -------------------------------------------------------------
## ★정답★

    # list안에 원소 검사
def print_calc(dataList):
    ## 4칙 연산 가능한지 검사
    for data in dataList:
        if type(data) not in [int, float]:
            return "유요한 데이터가 아닙니다."
    
    ## 유효한 데이터면 4칙연산 수행
    result = [dataList[0], dataList[0], dataList[0], dataList[0]]
    for data in dataList[1:]:
        result[0] += data
        result[1] -+ data
        result[2] *= data
        result[3] /= data if data != 0 else -1
    return result

print('[1, 2, 3, 4]',   print_calc([1, 2, 3, 4]))
print('[1, 2, "3", 4]', print_calc([1, 2, "3", 4]))
print('[1, 2, 0, 4]',   print_calc([1, 2, 0, 4]))


# is_valid = True
# for data in dataList:
#     if type(data) not in [int, float]:
#         is_valid = False
#         return