# Selection Sort Algorithm

Selection sort is a sorting algorithm, specifically an **in-place comparison sort**. It has O(n<sup>2</sup>) time complexity, making it inefficient on large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity, and it has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited. [(1)][1]

Selection sort animation:

![Selection_sort_animation.gif](./img/Selection_sort_animation.gif)

## Performance

Class |   Sorting algorithm
--- | --- 
Data structure |  Array
Worst case performance | О(n<sup>2</sup>)
Best case performance  | О(n<sup>2</sup>)
Average case performance  |  О(n<sup>2</sup>)
Worst case space complexity | О(n) total, O(1) auxiliary

## Pseudocode for the algorithm

```
SelectionSort(A, n) {
  for i = 0 to n-2 {
    iMin = i
    for j = i+1 to n-1 {
      if(A[j] < A[iMin])
        iMin = j
    }
    temp = A[i]
    A[i] = A[iMin]
    A[iMin] = temp
  }
}
```
Selection sort animation. Red is current min. Yellow is sorted list. Blue is current item: [(1)][1]

![Selection-Sort-Animation-elements.gif](./img/Selection-Sort-Animation-elements.gif)

Implementation in Java:
```java
 private static int[] selectionSort(int[] unsortedArray) {
       int iMin; // index of the minimum element in the array
       for (int i = 0; i < unsortedArray.length - 1; i++) {
          iMin = i; // assuming the first element to be the minimum
          // Scanning elements after i to find the smallest of them 
          for (int j = i+1; j < unsortedArray.length; j++) {
            // if we've found a new minimum
            if (unsortedArray[j] < unsortedArray[iMin]) {
              iMin = j; // updating the index of the minimum
            }
          } // for(j)
          // rearranging the elements and setting a new minimum
          int temp = unsortedArray[i];
          unsortedArray[i] = unsortedArray[iMin];
          unsortedArray[iMin] = temp;
       } // for(i)
       return unsortedArray; // the array is sorted at this point
}
```

## References
- [Selection sort From Wikipedia][1]
- [Selection sort algorithm](https://www.youtube.com/watch?v=GUDLRan2DWM&index=2&list=PL2_aWCzGMAwKedT2KfDMB9YA5DgASZb3U)

[1]: https://en.wikipedia.org/wiki/Selection_sort