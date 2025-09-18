/*******************************************************
 *                     데이터 타입
 *     타입별 저장이 가능한 범위가 정해져 있음
 *     해당 범위를 넘을 경우 => overflow/underflow
 *******************************************************/
 #include <stdio.h>

 // Entry Point Function -------------------------------
 int main(void)
 {
   // short 범위 : -32768 ~ 32767
    short sMinNum = -32768;
    short sMaxNum =  32767;
    float fNum = 1.8f;

    printf("sMinNum : %d ,sMaxNum : %d, fNum : %f \n", sMinNum, sMaxNum, fNum);

    return 0;
 }