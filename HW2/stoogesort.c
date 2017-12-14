/*****************************************
* Author: Kyle De Laurell
* Date: 10/1/2017
* Description: This is the source file for
* that reads a data.txt file of numbers and
* uses insertion sort to sort the data
*******************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>




int main(int argc, char *argv[]){

  //intializes variables

  FILE* testFile;
  FILE* insertFile;
  int array[1000];
  int arrayCount;


  testFile = fopen("data.txt", "r+");
  insertFile = fopen("stooge.out", "w");

  //memset(testBuffer, '\0', sizeof(testBuffer));


  while(fscanf(testFile, "%d", &arrayCount) == 1){
    for(int index = 0; index < arrayCount; index++){
      fscanf(testFile, "%d", &array[index]);
    }
    stoogesort(array, 0, arrayCount - 1);
    for(int index = 0; index < arrayCount; index++){
      fprintf(insertFile,"%d ", array[index]);
    }
    fprintf(insertFile,"\n");
  }
  fclose(testFile);
  fclose(insertFile);
return 0;


}

void stoogesort(int arr[], int s, int e){
  //printf("BEGIN SORT: s = %d, e = %d\n",s, e);
  int n = e - s + 1;
    //printf("n = %d\n", n);
  if (arr[s] > arr[e]){
    //printf("MADE IT!!!\n");
    int temp = arr[e];
    arr[e] = arr[s];
    arr[s] = temp;
  }
  if (n > 2){
    int m = ceil(2 * (float) e / 3);
    //printf("%d\n", m);
    printf("STOOGE1: START: %d, END: %d\n", s, m);

    stoogesort(arr, s, m - 1);
    printf("STOOGE2: START: %d - %d, END: %d\n", e, m, e);

    stoogesort(arr, (e - m), e - 1);
    printf("STOOGE1: START: %d, END: %d\n", s, m);

    stoogesort(arr, s, m - 1);
  }
}
