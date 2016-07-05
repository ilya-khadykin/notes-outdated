# Binary search algorithm

**Binary search** or half-interval search algorithm finds the position of a target value within a sorted array. The binary search algorithm can be classified as a dichotomic divide-and-conquer search algorithm and executes in logarithmic time.

Animation of Binary Search Algorithm:

![binary-and-linear-search-animations.gif](./img/binary-and-linear-search-animations.gif)

The binary search algorithm begins by comparing the target value to the value of the middle element of the sorted array. If the target value is equal to the middle element's value, then the position is returned and the search is finished. If the target value is less than the middle element's value, then the search continues on the lower half of the array; or if the target value is greater than the middle element's value, then the search continues on the upper half of the array. This process continues, eliminating half of the elements, and comparing the target value to the value of the middle element of the remaining elements - until the target value is either found (and its associated element position is returned), or until the entire array has been searched (and "not found" is returned). [(1)][1]

## Performance

Class | Search algorithm
----- | -----
Data structure | Array
Worst case performance | `O(log n)`
Best case performance  | `O(1)`
Average case performance  |  `O(log n)`
Worst case space complexity | `O(1)`

## Pseudocode for the algorithm

```
BinarySearch(A, n, x) {
  start = 0
  end = n-1
  while (start <= end) {
    mid = (start + end)/2
    if (A[mid] == x) {
      return mid
    } else if (x < A[mid]) {
      end = mid - 1
    } else {
      start = mid + 1
    }
  } // while
  return -1 // element is not found
}
```

## Referemces
- [What is binary search](https://www.youtube.com/watch?v=j5uXyPJ0Pew)
- [Binary search algorithm From Wikipedia][1]

[1]: https://en.wikipedia.org/wiki/Binary_search_algorithm