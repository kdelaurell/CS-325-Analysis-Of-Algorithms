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




int main(int argc, char *argv[]){

  //intializes variables

  FILE* testFile;
  FILE* insertFile;
  int array[1000];
  int arrayCount;


  testFile = fopen("data.txt", "r+");
  insertFile = fopen("insert.out", "w");

  //memset(testBuffer, '\0', sizeof(testBuffer));


  while(fscanf(testFile, "%d", &arrayCount) == 1){
    for(int index = 0; index < arrayCount; index++){
      fscanf(testFile, "%d", &array[index]);
    }
    insertionsort(array, arrayCount);
    for(int index = 0; index < arrayCount; index++){
      fprintf(insertFile,"%d ", array[index]);
    }
    fprintf(insertFile,"\n");
  }
  fclose(testFile);
  fclose(insertFile);
return 0;


}

void insertionsort(int arr[], int n){
  int i;
  int j;
  int k;
  for (i = 0; i < n; i++){
    k = arr[i];
    j = i - 1;
    while(j >= 0 && arr[j] > k){
      arr[j + 1] = arr[j];
      j = j - 1;
    }
    arr[j + 1] = k;
  }
}
