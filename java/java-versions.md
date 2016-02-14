
## Java Versions [(1)][1] | [(3)][3]

| Date |       Version         |         JDK        | New Language Features   | Number of Classes |
|:----:|:---------------------:|:------------------:|:-----------------------:|:-----------------:|
| 1996 |        Java 1.0       |  Java JDK 1.0      | The language itself     |      211          |
| 1997 |        Java 1.1       |  Java JDK 1.1      |     Inner classes       |      477          |
| 1998 |        Java 2 (1.2)   |  J2SE v1.2         | The `strictfp` modifier |     1 524         |
| 2000 |        Java 2 (1.3)   |  J2SE v1.3         |           None          |     1 840         |
| 2002 |        Java 2 (1.4)   |  J2SE v1.4         |       Assertions        |     2 723         |
| 2004 | Java 2 Platform 5.0   |  J2SE 5            | Generic classes, `for each` loop, varargs, autoboxing, metadata, enumerations, static import |       3 279          |
| 2006 |        Java 6         |  Java SE 6 (u1-45) |           None          |     3 793         |
| 2011 |        Java 7         |  Java SE 7 (u1-51) | Switch with strings, diamond operator, binary literals, exception handling enchantments |      4 024         |
| 2014 |        Java 8         |  Java SE 8         | Lambda expressions, interfaces with default  methods, stream and date/time libraries |      4 240         |


From Java 6 instead of bumping the versions updates were shipped

## A Brief History of Java and the JVM [(2)][2]

### Java 1.0 (1996)
This was the first public version of Java. It contained just 212 classes organized in eight packages. The Java platform has always had an emphasis on backward compatibility,  and code written with Java 1.0 will still run today on Java 8 without modification or recompilation.

### Java 1.1 (1997)
This release of Java more than doubled the size of the Java platform. This release introduced “inner classes” and the first version of the Reflection API.

### Java 1.2 (1998)
This was a very significant release of Java; it tripled the size of the Java platform. This release marked the first appearance of the Java Collections API (with sets, maps, and lists). The many new features in the 1.2 release led Sun to rebrand the platform as “the Java 2 Platform.” The term “Java 2” was simply a trademark, however, and not an actual version number for the release.

### Java 1.3 (2000)
This was primarily a maintenance release, focused on bug fixes, stability, and performance improvements. This release also brought in the HotSpot Java Virtual Machine, which is still in use today (although heavily modified and improved since then).

### Java 1.4 (2002)
This was another fairly big release, adding important new functionality such as a higher-performance, low-level I/O API; regular expressions for text handling; XML and XSLT libraries; SSL support; a logging API; and cryptography support.

### Java 5 (2004)
This large release of Java introduced a number of changes to the core language itself including generic types, enumerated types (enums), annotations, varargs methods, autoboxing, and a new for loop. These changes were considered significant enough to change the major version number, and to start numbering as major releases. This release included 3,562 classes and interfaces in 166 packages. Notable additions included utilities for concurrent programming, a remote management framework, and classes for the remote management and instrumentation of the Java VM itself.

### Java 6 (2006)
This release was also largely a maintenance and performance release. It introduced the Compiler API, expanded the usage and scope of annotations, and provided bindings to allow scripting languages to interoperate with Java. There were also a large number of internal bugfixes and improvements to the JVM and the Swing GUI technology.

### Java 7 (2011)
The first release of Java under Oracle’s stewardship included a number of major upgrades to the language and platform. The introduction of try-with-resources and the NIO.2 API enabled developers to write much safer and less error-prone code for handling resources and I/O. The Method Handles API provided a simpler and safer alternative to reflection—and opened the door for invokedynamic (the first new bytecode since version 1.0 of Java).

### Java 8 (2014)
This latest release of Java introduces potentially the most significant changes to the language since Java 5 (or possibly ever). The introduction of lambda expressions promises the ability to significantly enhance the productivity of developers; the Collections have been updated to make use of lambdas, and the machinery required to achieve this provides a fundamental change in Java’s approach to object orientation. Other major updates include an implementation of JavaScript that runs on the JVM (Nashorn), new date and time support, and Java profiles (which provide for different versions of Java that are especially suitable for headless or server deployments).

## References

- [Learning Java 8 by Infinite Skills, 2014][1]
- [Java in a Nutshell, 6th Edition][2]
- [Core Java® Volume I—Fundamentals, Tenth Edition][3]

[1]: http://www.infiniteskills.com/training/learning-java-8.html
[2]: http://shop.oreilly.com/product/0636920030775.do (Java in a Nutshell, 6th Edition)
[3]: http://www.amazon.com/Core-Volume-I-Fundamentals-Edition-Series/dp/0134177304