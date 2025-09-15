## ------------------------------------------------
## break : for/while 반복을 중단시키는 키워드/명령어
##         - 즉시 반복을 중단함
##         - break 아래의 코드를 절대 실행 안 됨!
##         ★ 중첩 반복문의 경우 break와 가까이 있는
##            반복문만 중단됨!!
## ------------------------------------------------
## [요청] 중첩 반복문과 break문
isstop=False   ## Flag/State체크 변수

for ch in "ABCDEFGHIJKLMN":
    print(ch)
    for num in range(4,20):
        if num == 11:
            isstop=True
            break   ## 즉시 중단. 바깥for문은 중단X
        print(num)

    # 종료 조건: 안쪽 for문 중단되면 함께 중단
    if isstop:
        break