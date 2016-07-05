## Overview

In Computer Science a `queue` is an abstract `Data Structure` where items are kept in order. New items can be added at the back of the `queue` and old items are taken off from the front of the `queue`.


## JavaScript
```js
/*
    Queue implementation in JavaScript
*/
function queue(arr, item) {
  arr.push(item); // adding a new item to the end of the array

  return arr.splice(0,1)[0];  // removing the first element from the array and returning it
}
```

## References
- [Chapter 2 Stacks and Queues](http://www.cmpe.boun.edu.tr/~akin/cmpe223/chap2.htm)