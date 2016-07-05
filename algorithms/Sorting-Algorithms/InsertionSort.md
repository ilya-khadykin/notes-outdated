# Insertion Sort Algorithm

**Insertion sort** is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, insertion sort provides several advantages [(1)][1]:

- **Simple implementation**: Bentley shows a three-line C version, and a five-line optimized version
- **Efficient for (quite) small data sets**, much like other quadratic sorting algorithms
- **More efficient in practice** than most other simple quadratic (i.e., O(n<sup>2</sup>)) algorithms such as [selection sort][2] or [bubble sort][3]
- **Adaptive**, i.e., efficient for data sets that are already substantially sorted: the time complexity is `O(nk)` when each element in the input is no more than `k` places away from its sorted position
- **Stable**, i.e., does not change the relative order of elements with equal keys
- **In-place**, i.e., only requires a constant amount `O(1)` of additional memory space
- **Online**, i.e., can sort a list as it receives it

When people manually sort cards in a bridge hand, most use a method that is similar to insertion sort

Animation of the insertion sort sorting a 30 element array:

![Insertion_sort.gif](./img/Insertion_sort.gif)

## Performance

Class | Sorting algorithm
----- | -----
Data structure | Array
Worst case performance | О(n<sup>2</sup>) comparisons, swaps
Best case performance | O(n) comparisons, O(1) swaps
Average case performance | О(n<sup>2</sup>) comparisons, swaps
Worst case space complexity | О(n) total, O(1) auxiliary

## Pseudocode for the algorithm

```
InsertionSort(A, n) {
  for i=1 to n-1 {
    value = A[i]
    hole = i
    while (hole > 0 && A[hole-1] > value) {
      A[hole] = A[hole-1]
      hole = hole -1
    }
    A[hole] = value
  }
}
```
Or:
```
 for i = 1 to length(A) - 1
    x = A[i]
    j = i - 1
    while j >= 0 and A[j] > x
        A[j+1] = A[j]
        j = j - 1
    end while
    A[j+1] = x
 end for
```

A graphical example of insertion sort [(1)][1]:

![Insertion-sort-example-300px.gif](./img/Insertion-sort-example-300px.gif)

## References
- [Insertion sort algorithm](https://www.youtube.com/watch?v=i-SKeOcBwko&index=4&list=PL2_aWCzGMAwKedT2KfDMB9YA5DgASZb3U)
- [Insertion sort From Wikipedia][1]

[1]: https://en.wikipedia.org/wiki/Insertion_sort
[2]: SelectionSort.md
[3]: BubbleSort.md