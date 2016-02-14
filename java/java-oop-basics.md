# Basics of OOP in Java

## Key points [(1)][1]

- Object-oriented programming lets you extend a program without having to touch previously-tested, working code.
- All Java code is defined in a **class**.
- A class describes how to make an object of that class type. **A class is like a blueprint**.
- An object can take care of itself; you don’t have to know or care how the object does it.
- An object **knows** things (instance variables) and **does** things (instance methods).
- Things an object knows about itself are called **instance variables**. They represent the state of an object.
- Things an object does are called **methods**. They represent the behavior of an object.
- When you create a class, you may also want to create a separate test class which you’ll use to create objects of your new class type.
- A class can **inherit** instance variables and methods from a more abstract **superclass**.
- At runtime, a Java program is nothing more than objects ‘talking’ to other objects.

## public static void main(String[] args) { }

The two uses of main:

1. to test your real class
2. to launch/start your Java application

## The Heap

Each time an object is created in Java, it goes into an area of memory known as **The Heap**. All objects—no matter when, where, or how they’re created – live on the heap. But it’s not just any old memory heap; the Java heap is actually called the **Garbage-Collectible Heap**.

When the JVM can ‘see’ that an object can never be used again, that object becomes *eligible for garbage collection*. And if you’re running low on memory, the Garbage Collector will run, throw out the unreachable objects, and free up the space, so that the space can be reused

## References
1. [Head First Java, 2nd Edition][1]

[1]: http://shop.oreilly.com/product/9780596009205.do