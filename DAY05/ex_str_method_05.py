## -------------------------------------------------------------------
## str 전용 메서드 : 문자열 검사해주는 메서드 => True/False
##                  메서드명 특징 : is____()
## -------------------------------------------------------------------
## 대소문자 검사해주는 메서드 : isupper(), islower(), isspace()
## -------------------------------------------------------------------

print(f'GOOD.isupper(): {"GOOD".isupper()}')
print(f'GOOD.islower(): {"GOOD".islower()}')
print(f'GOOD.isspace(): {"GOOD".isspace()}')

## -------------------------------------------------------------------
## 문자 구성요소 종류 검사해주는 메서드 : isalpha(), isdigit()
## -------------------------------------------------------------------
print(f'GOOD.isalpha() : {"GOOD".isalpha()}')           ## 알파벳
print(f'GOOD7.isalpha(): {"GOOD7".isalpha()}')
print(f'123.8.isdigit(): {"123.8".isdigit()}')          ## '.'은 숫자가 아니라 False
print(f'오늘.isalpha() : {"오늘".isalpha()}')
print(f'今日.isalpha() : {"今日".isalpha()}')

## 숫자문자 검사 메서드 3개 범위 : isdecimal() < isdigit() < isnumeric()
## -, + 기호, 실수는 X
## 'VI', '½', '3²'
print(f'123.isdigit()  : {"123".isdigit()}')            ## 숫자만
print(f'123.isdecimal(): {"123".isdecimal()}')          ## 10진수
print(f'123.isnumeric(): {"123".isnumeric()}')          

print(f'-123.isdigit()  : {"-123".isdigit()}')          ## 숫자만
print(f'-123.isdecimal(): {"-123".isdecimal()}')        ## 10진수
print(f'-123.isnumeric(): {"-123".isnumeric()}')       

print(f'123.5.isdigit()  : {"123.5".isdigit()}')        ## 숫자만, 제곱근 가능
print(f'123.5.isdecimal(): {"123.5".isdecimal()}')      ## 10진수(0~9)
print(f'123.5.isnumeric(): {"123.5".isnumeric()}')      ## 로마자(I, VI), 분수(½), 제곱근(3²)