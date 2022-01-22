#include <stdio.h>

int faster(int* input, int size, int days){
    //getting the amount of fish per state
    long long arr[9] = {0,0,0,0,0,0,0,0,0};
    for( int i = 0; i < size; i++){
        //if( i % 2 == 0 || i == 0)
            switch(input[i]){
                case 0: arr[0]++; printf("0 \n"); break;
                case 1: arr[1]++; printf("1 \n"); break;
                case 2: arr[2]++; printf("2 \n"); break;
                case 3: arr[3]++; printf("3 \n"); break;
                case 4: arr[4]++; printf("4 \n"); break;
                case 5: arr[5]++; printf("5 \n"); break;
                case 6: arr[6]++; printf("6 \n"); break;
                case 7: arr[7]++; printf("7 \n"); break;
                case 8: arr[8]++; printf("8 \n"); break;
            }
        //}
    }
    for( int i = 0; i < days; i++){
        long long tmp = arr[0];
        arr[0] = arr[1];
        arr[1] = arr[2];
        arr[2] = arr[3];
        arr[3] = arr[4];
        arr[4] = arr[5];
        arr[5] = arr[6];
        arr[6] = arr[7] + tmp;
        arr[7] = arr[8];
        arr[8] = tmp;
    }
    long long fish = 0;
    for(int i = 0; i < 9; i++){
        fish += arr[i];
    }
    printf("After %d days, there are %lld fish in the see \n",days,fish);
    return fish;
}
