## ------------------------------------------------------------------------------------------
## break / continue / pass
## ------------------------------------------------------------------------------------------
## [1] "Happy!Good" 데이터에서 원소를 옆으로 출력하세요
##     단 문자가 아니면 중단해 주세요.
# data = "Happy!Good"
# for idx in data:
#     if not idx.isalpha():
#         break
#     print(idx, end = "\t")
# print()

## [2] "Happy!Good" 데이터에서 원소를 옆으로 출력하세요
##     단 문자만 출력하세요.
# for idx in "Happy!Good":
#     if not idx.isalpha():
#         continue
#     print(idx, end = " ")

# for idx in "Happy!Good":
#     if not idx.isalpha():
#         pass
#     print(idx, end = " ")

msg = "Happy!Good"
idx = -1            ## 원소 읽기 위한 인덱스
stop = len(msg)     ## 인덱스 범위 지정위한 변수 : 0 ~ len(msg)-1

# 10
while idx<(stop-1):
    idx += 1        ## -1 => 0, 0 => 1, ..., 9 => 10
    if not msg[idx].isalpha():
        continue
    print(msg[idx], end = " ")