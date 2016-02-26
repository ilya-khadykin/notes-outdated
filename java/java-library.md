# Java library (the API)

## ArrayList

Package - java.util

```java
import java.util.ArrayList;
```

ArrayLists are parameterized - `ArrayList<String>`, type parameter is declared in `< >`

Methods:

- `add(Object elem)`
- `remove(int Index)`
- `remove(Object elem)`
- `contains(Object elem)`
- `isEmpty()`
- `indexOf(Object elem)`
- `size()`
- `get(int index)`

```java
ArrayList<Egg> myList = new ArrayList<Egg>(); // Egg - name of the object

Egg s = new Egg();
myList.add(s);
```


## References

1. [Head First Java, 2nd Edition][1]

[1]: http://shop.oreilly.com/product/9780596009205.do