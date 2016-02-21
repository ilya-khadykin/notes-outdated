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


## Compilation to bytecode

You can compile your program using source code compiler for JDK in CLI:

```bash
javac <YourClassName>.java
```

### Classpath

`-classpath` tells to the compiler where to find third-party classes:

```
javac -classpath lib.jar HelloWorld.java
```

And you also should add the classpath while running the program:

```
java -classpath lib.jar:hw.jar HelloWorld
```

You can also read the compiled bytecode using the following tool:

```
javap -v <YourClassName>.class
```
## Running Java program

To run the program use JVM and invoke main class with main() method:
```
java <YourMainClass>
```

Run Java program from jar:

```
java -jar <nameofyourarchave>.jar
java -jar hw.jar

java -classpath <nameofyourarchave>.jar <NameOfMainClass>
java -classpath hw.jar HelloWorld
```

## Java Archive or jar

jar is basically a zip file which contains all classes of the program and one special file - manifest. Manifest (META-INF/MANIFEST.MF) strores meta information about archive, specifically about main class

There is a special tool for working with java archaves - jar.

To create a jar use the following command:

```
jar cfe <nameofyourarchave>.jar <NameOfMainClass> <AllFilesYouWantToAddToArchave>
jar cfe hw.jar HelloWorld HelloWorld.class
```

To see what is inside of jar without unpacking:

```
jar tf <nameofyourarchave>.jar
jar tf hw.jar
```

Unpack the archive:

```
jar xf hw.jar
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
2. [Java Programming Basics by Simon Roberts][2]

[1]: http://shop.oreilly.com/product/9780596009205.do
[2]: https://www.safaribooksonline.com/library/view/java-programming-basics/9780133975154/