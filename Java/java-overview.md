# Java Overview

**`Java`** is a powerful, general-purpose programming language. It is one of the most widely used programming languages in the world, and has been exceptionnaly successfull in business and enterprise computing. [[1][1]

## History of Java

The Java programming environment has been around since the late 1990s. Java's architecture (separation between the runtime and the language) was novel at the time. That allowed different vendors working on development of Java competing and collaborating with each other which was the main reason of success of Java.

The language has undergone gradual revision (but not complete rewrites) since its inception in 1996.

## The language, the JVM, and the Ecosystem [[1][1]

The Java programming environment comprises the following pieces:
- **the Java language**,
- **the supportive runtime** (known as the Java Virtual Machine **`JVM**)

Java ecosystem is a standardized environment , there are specification for the technologies that comprise the environment.

The current steward of Java is Oracle Corporation (who acquired Sun Microsystems, the originator of Java).

There is also an open source version of Java, called **`OpenJDK`**, which many companies collaborate on.

Java comprises several different, but related environment and specifications:
- **`Java Mobile Edition (Java ME)`**
- **`Java Standard Edition (Java SE)`**
- **`Java Enterprise Edition (Java EE)`**

### the Java Language

the Java language is a human-readable programming language, which is class based and object oriented.

Java 8 has added the most radical changes seen in the language for almost a decade (or since the birth of Java)

The Java language is governed by **`the Java Language Specification (JLS)`**, which defines how a conforming implementation must behave.

### the JVM

The JVM is a program that provides the runtime environment necessary for Java programs to execute.

The JVM has been ported to run on a large number of environments (OS platforms and hardware)

Java programs are typically started by a command line, such as:
```bash
java <arguments> <program name>
```

JVM executes **`Java bytecode`` in a format called class files which must be `compiled` from a source code.

JVM collects runtime information to make better decisions about how to execute code (just-in-time (JIT) compilation, 'hot methods' (the most used methods) compiled into machine code).

The standard that describes how a properly functioning JVM must behave is called **`JVM Specification`**

## References
- [Java in a Nutshell, 6th Edition][1]

[1]: http://shop.oreilly.com/product/0636920030775.do (Java in a Nutshell, 6th Edition)