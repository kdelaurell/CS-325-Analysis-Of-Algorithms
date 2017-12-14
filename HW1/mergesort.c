/*****************************************
* Author: Kyle De Laurell
* Date: 10/1/2017
* Description: This is the source file for
* that reads a data.txt file of numbers and
* uses merge sort to sort the data
*******************************************/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>




int main(int argc, char *argv[]){

  //intializes variables

  FILE* testFile;
  FILE* mergeFile;
  int array[1000];
  int arrayCount;


  testFile = fopen("data.txt", "r+");
  mergeFile = fopen("merge.out", "w");

  while(fscanf(testFile, "%d", &arrayCount) == 1){
    for(int index = 0; index < arrayCount; index++){
      fscanf(testFile, "%d", &array[index]);
    }
    mergesort(array, 0, arrayCount - 1);
    for(int index = 0; index < arrayCount; index++){
      fprintf(mergeFile,"%d ", array[index]);
    }
    fprintf(mergeFile,"\n");
  }
  fclose(testFile);
  fclose(mergeFile);
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

void merge(int arr[], int l, int r, int m){
  int p = l;
  int q = m+1;
  int k = 0;

  int tempArray[r-l+1];

  for(int i = l ;i <= r ;i++) {
      if(p > m){
         tempArray[k++] = arr[q++];
       } else if (q > r){
         tempArray[k++] = arr[p++];
       } else if( arr[p] < arr[q]){
        tempArray[k++] = arr[p++];
      } else{
        tempArray[k++] = arr[q++];
      }
   }
    for (int p=0 ; p< k ;p ++) {
       arr[l++] = tempArray[p] ;
    }
}

void mergesort(int arr[], int l, int r){
  int m;
  if (r > l){
    m = (l+r-1)/2;
    mergesort(arr, l, m);
    mergesort(arr, m+1, r);
    merge(arr, l, r, m);
  }
}
