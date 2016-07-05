# Linear Search

In computer science, **linear search** or **sequential search** is a method for finding a particular value in a list that checks each element in sequence until the desired element is found or the list is exhausted. [(1)][1]

There is no need for an array to be sorted before using this algorithm.

Linear search is the simplest search algorithm; it is a special case of **brute-force search**.

Pseudocode for the algorithm:
```
 For each item in the list:
     if that item has the desired value,
         stop the search and return the item's location.
 Return Λ.
```
Or:
```
LinearSearch(A, size, target)
  for i = 0 to size - 1
    if (A[i] == target)
      return i
  return -1
```

## Performance

### The best case

We'll do only one comparison (the target is at the first index in the array)

### The worst case

We'll do n comparisons where n is the length of the array (the target is at the last index in the array or isn't present in the array at all)

### Average

On average there is an equally likely chance of target be in any index of the array, the average performance is equal to **`(n+1)/2`** comparisons

## References
- [Linear search From Wikipedia][1]
- [Algorithms Lesson 5: Linear and Binary Searching](https://www.youtube.com/watch?v=wNVCJj642n4)

[1]: https://en.wikipedia.org/wiki/Linear_search