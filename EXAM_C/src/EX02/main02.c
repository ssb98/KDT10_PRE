/*******************************************************
 *                데이터 타입 - 정수형 
 * 메모리 낭비를 막기 위해서 다양한 종류 존재
 * - 2byte(2칸) : short
 * - 4byte(4칸) : int
 * - 4byte(4칸) : long
 * - 8byte(8칸) : long long
 *******************************************************/
 #include <stdio.h>

 // Entry Point Function -------------------------------
 int main(void)
 {
    short sMinNum = -32768;
    short sMaxNum =  32767;

    printf("가장 작은 값 %d, 가장 큰 값 %d \n", sMinNum, sMaxNum);

    short sh = 12;
    int nt = 155;
    long long on = 1666;

    printf("자료형의 크기를 알아보는 코드 \n");
    printf("1. short : %dbyte, %dbyte \n", sizeof(sh), sizeof sh);
    printf("2. int : %dbyte, %dbyte \n", sizeof(nt), sizeof nt);
    printf("3. long long : %dbyte, %dbyte \n", sizeof(on), sizeof on);

    return 0;
 }