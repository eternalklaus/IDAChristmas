// gcc -m32 -o tree tree.c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
    int *addr;
    int num = addr;

    if (num < 1024){ 
        num += rand();
        num += rand();
        if (num > 512){
            num += rand();
            num += rand();
            if (num > 512 + 256){
                num += rand();
                num += rand();
                if (num > 512 + 256 + 128){
                    num += rand();
                    num += rand();
                }
                else{
                    num -= rand();
                    num -= rand();
                }
            }
            else{
                num -= rand();
                num -= rand();
                if (num > 512 + 128){
                    num += rand();
                    num += rand();
                }
                else{
                    num -= rand();
                    num -= rand();
                }
            }
        }
        else{
            num -= rand();
            num -= rand();
            if (num > 256){
                num += rand();
                num += rand();
                if (num > 256 + 128){
                    num += rand();
                    num += rand();
                }
                else{
                    num -= rand();
                    num -= rand();
                }
            }
            else{
                num -= rand();
                num -= rand();
                if (num > 128){
                    num += rand();
                    num += rand();
                }
                else{
                    num -= rand();
                    num -= rand();
                }
            }
        }
    }
    else{ // more then 1024
        num += rand();
        num += rand();
        if (num > 1024 + 512){
            num += rand();
            num += rand();
            if (num > 1024 + 512 + 256){
                num += rand();
                num += rand();
                if (num > 1024 + 512 + 256 + 128){
                    num += rand();
                    num += rand();
                }
                else{
                    num -= rand();
                    num -= rand();
                }
            }
            else{
                num -= rand();
                num -= rand();
                if (num > 1024 + 512 + 128){
                    num += rand();
                    num += rand();
                }
                else{
                    num -= rand();
                    num -= rand();
                }
            }
        }
        else{
            num -= rand();
            num -= rand();
            if (num > 1024 + 256){
                num += rand();
                num += rand();
                if (num > 1024 + 256 + 128){
                    num += rand();
                    num += rand();
                }
                else{
                    num -= rand();
                    num -= rand();
                }
            }
            else{
                num -= rand();
                num -= rand();
                if (num > 1024 + 128){
                    num += rand();
                    num += rand();
                }
                else{
                    num -= rand();
                    num -= rand();
                }
            }
        }
    }
    printf("Merry Christmas Pow~ Pow~ Pow~\n");
}