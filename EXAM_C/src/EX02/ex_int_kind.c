/*******************************************************
 *                     데이터 타입
 *     정수의 다양한 표현법/진법
 *     2진수  => 0b0101
 *     8진수  => 065
 *     16진수 => 0x23A
 *******************************************************/
#include <stdio.h>

int main(void)
{
    // 숫자의 다양한 진법 표기
    int binValue = 0b1001;      //10진수 - %d
    int otaValue = 067;         // 8진수 - %o
    int hexValue = 0x1F;        //16진수 - %x
    int decValue = 91;          // 2진수 - %d

    // 출력 : %d -- 문자의 코드값, %c -- 문자
    printf("binValue => %d, %o, %x \n", binValue, binValue, binValue);
    printf("otaValue => %o, %d \n", otaValue, otaValue);
    printf("hexValue => %x, %d \n", hexValue, hexValue);
    printf("decValue => %d, %o, %x \n", decValue, decValue, decValue);

    return 0;
}