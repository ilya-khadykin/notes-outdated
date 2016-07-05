# Bubble Sort

**Bubble sort**, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted.

Although the algorithm is simple, it is too slow and impractical for most problems even when compared to insertion sort. It can be practical if the input is usually in sort order but may occasionally have some out-of-order elements nearly in position. [(1)][1]

Bubble Sort Animation:

![Bubble_sort_animation.gif](./img/Bubble_sort_animation.gif)

## Performance [(1)][1]

Bubble sort has worst-case and average complexity both О(n<sup>2</sup>), where n is the number of items being sorted. There exist many sorting algorithms with substantially better worst-case or average complexity of O(n log n). Even other О(n<sup>2</sup>) sorting algorithms, such as insertion sort, tend to have better performance than bubble sort. Therefore, bubble sort is not a practical sorting algorithm when n is large.

Bubble sort should be avoided in the case of large collections. It will not be efficient in the case of a reverse-ordered collection.

Class | Sorting algorithm
---- | ----
Data structure | Array
Worst case performance |    O(n<sup>2</sup>)
Best case performance | O(n)
Average case performance |  O(n<sup>2</sup>)
Worst case space complexity | O(1) auxiliary

## Pseudocode for the algorithm

```
// Unoptimized version
UnoptimizedBubbleSort(A, n) {
  for k = 1 to n-1 {
    for i=0 to n-2 { // n-2 ensures we'll stay in range of the array
      if (A[i] > A[i+1]) {
        swap(A[i], A[i+1])
      }
    } // for(i)
  } // for(k)
}
```

```
// Optimized version
OptimizedBubbleSort(A, n) {
  for k = 1 to n-1 {
    flag = 0
    for i=0 to n-k-1 { // n-k-1 We skip already sorted elements
      if (A[i] > A[i+1]) {
        swap(A[i], A[i+1])
        flag = 1
      }
    } // for(i)
    if (flag == 0) { // if the array is already sorted, break from the loop
      break
    }
  } // for(k)
}
```

Animation of Bubble Sort Algorithm. An example of bubble sort. Starting from the beginning of the list, compare every adjacent pair, swap their position if they are not in the right order (the latter one is smaller than the former one). After each iteration, one less element (the last one) is needed to be compared until there are no more elements left to be compared. [(1)][1]

![Bubble-sort-example-300px.gif](./img/Bubble-sort-example-300px.gif)

Implementation in Java:

```java
public static int[] optimizedBubbleSort(int[] unsortedArray) {
      for (int k = 0; k < unsortedArray.length - 1; k++) {
        int flag = 0;
        for (int i = 0; i < unsortedArray.length - k - 1; i++) {
          if (unsortedArray[i] > unsortedArray[i+1]) {
            // swapping the elements
            int temp = unsortedArray[i+1];
            unsortedArray[i+1] = unsortedArray[i];
            unsortedArray[i] = temp;
            flag = 1;
          }
        } // for(i)
        if (flag == 0) {
          break;
        }
      } // for(k)
      return unsortedArray; // the array is sorted at this point
}
```

## References

- [](https://www.youtube.com/watch?v=Jdtq5uKz-w4&list=PL2_aWCzGMAwKedT2KfDMB9YA5DgASZb3U&index=3)
- [Bubble sort From Wikipedia][1]

[1]: https://en.wikipedia.org/wiki/Bubble_sort
