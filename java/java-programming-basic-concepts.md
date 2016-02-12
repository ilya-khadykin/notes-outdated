# Programming in Java: Basic Concepts

## Code structure in Java
![Code Structure](./img/code_structure.jpg)

1. Source code file - **`*.java`** files
2. **Class** definition is put inside a source code file 
3. A Class definition consists of methods and statements

```java
public class Dog {
  void bark() {
    statement1;
    statement2;
  }
}
```
## Anatomy of a class [[1]][1]

Execution of the program in JVM starts from a specially-written method:

```java
  public static void main (String[] args) {
    // your code goes here
  }
```

**Every Java application has to have at least one class, and at least one main method** (not one main per class; just one main per application)

![Class Anatomy](./img/class-anatomy.jpg)

When you run your program, you're really running a class

## Basic Syntax

### Statements
```java
int x = 3;
String name = "Dirk";
x = x * 17;
System.out.print("x is " + x);
double d = Math.random();
// this is a comment
```

### Loops
```java
while (x > 12) {
   x = x - 1;
}
for (int x = 0; x < 10; x = x + 1) {
   System.out.print("x is now " + x);
}
```

### Conditions
```java
if (x == 10) {
   System.out.print("x must be 10");
} else {
   System.out.print("x isn't 10");
}
if ((x < 3) & (name.equals("Dirk"))) {
   System.out.println("Gently");
}
System.out.print("this line runs no matter what");
```


## References
1. [Head First Java, 2nd Edition][1]

[1]: http://shop.oreilly.com/product/9780596009205.do