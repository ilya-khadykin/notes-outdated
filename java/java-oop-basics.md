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

## Encapsulation

It's an idea of restricting direct manipulation of class variables. Every interaction with a class is done using methods.

See the example: [(2)][2]

```java
/*
 *  Date.java
 */
package date1;

public class Date {
  private int day;     // restricting access to an instance variable
  private int month;   // restricting access to an instance 

  ## Inheritance

  variable
  private int year;    // restricting access to an instance variable

  @Override
  public String toString() {
      return this.month + "/" + this.day + "/" + this.year;
  }

  // getters
  public int getDay() {
      return day;
  }

  public int getMonth() {
      return month;
  }

  public int getYear() {
      return year;
  }

  public boolean isLeapYear(int year) {
      return (((year % 4) == 0) && ((year % 100) != 0)) || ((year % 400) == 0);
  }

  public int daysInMonth(int month, int year) {
    int rv;
    switch(month) {
        case 9: // Thirty days hath September
        case 4: // April
        case 6: // June
        case 11: // and November
            rv = 30;
            break;
        case 2:
            if (isLeapYear(year)) {
                rv = 29;
            } else {
                rv = 28;
            }
            break;
        default:
            rv = 31;
            break;
    }
    return rv;
  }

  public void nextDay() {
      int dayCount = daysInMonth(this.month, this.year);
      this.day++;
      if (this.day > dayCount) {
          this.day = 1;
          this.month++;
          if (this.month > 12) {
              this.month = 1;
              this.year++;
          }
      }
  }

  // Constructor
  public Date(int m, ind d, int, y) {
      this.day = d;
      this.month = m;
      this.year = y;
  }
}
```

```java
/*
 *  Date1.java
 */
package date1;

public class Date1 {
  
  public static void main(String[] args) {
      Date meetingDate = new Date(2, 29, 2012);

      System.out.println("Meeting will be on "
                + meetingDate.getMonth() + "/"
                + meetingDate.getDay() + "/"
                + meetingDate.getYear()
      );

      System.out.println("Again meeting will be on"
                + meetingDate.toString()
      );

      System.out.println("Yet again meeting will be on"
                + meetingDate
      );

  }
}
```

## Inheritance

Java supports `single inheritance`: you can extend only one specialized (super) class (but that class can extend something else)

### Method Overriding

Method name, returned type and a sequence of arguments should be identical

```java
  @Override
  public void pet() {
      System.out.println("Super class method was overwritten by its subclass version")
  }
```

### Dynamic invocation or late binding

We can invoke derivative class methods from a superclass, see example below.

```java
/**
 * Zoo.java
 */

package zoo;

import zoo.animals.Lion;
import zoo.animals.Sheep;
import zoo.animals.Zebra;
import zoo.animals.Animal;

public class Zoo {
  
//  private Sheep sheep = new Sheep();
//  private Lion lion = new Lion();
//  private Zebra zebra = new Zebra();

  private Animal [] animals = {
     new Sheep(), new Lion(), new Zebra()
  };

  public void visitAnimal(Animal animal) {
      System.out.println("Try to feed the animal");
      animal.feed();
      System.out.println("Try to pet the animal");
      animal.pet();
  }

  public void visit() {
      System.out.println("You visit the zoo...");
//      System.out.println("You go to see the sheep, you try to feed it");
//      sheep.feed();
//      System.out.println("You try to pet the sheep");
//      sheep.pet();

//      System.out.println("You go to see the lion, you try to feed it");
//      lion.feed();
//      System.out.println("You try to pet the lion");
//      lion.pet();

//      System.out.println("You go to see the zebra, you try to feed it");
//      zebra.feed();
//      System.out.println("You try to pet the zebra");
//      zebra.pet();

      for (int i = 0; i < animals.length; i++) {
          visitAnimal(animals[i]);
      }
  }

  public static void main(String[] args) {
      Zoo z = new Zoo();
      z.visit();
  }
}
```

```java
/**
 * Animal.java
 */
package zoo.animals;

public class Animal {
  public void feed() {
      System.out.println("Animal eats...");
  }

  public void pet() {
      System.out.println("Animal gets petted...");
  }
}

 ```

```java
/**
 * Zebra.java
 */
package zoo.animals;

public class Zebra extends Animal {
  @Override
  public void feed() {
      System.out.println("Zebra eats grass, looking around anxiously...");
  }
  @Override
  public void pet() {
      System.out.println("Zebra looks at you strangely and runs away...");
  }
}
 ```

 ```java
/**
 * Lion.java
 */
package zoo.animals;

public class Lion extends Animal {
  @Override
  public void feed() {
      System.out.println("Lion eats meat and roars to warn you not to try to take its kill");
  }
  @Override
  public void pet() {
      System.out.println("Lion roars as you approach and you decide no to try it...");
  }
}
 ```

  ```java
/**
 * Sheep.java
 */
package zoo.animals;

public class Sheep extends Animal {
  @Override
  public void feed() {
      System.out.println("Sheep eats grass, munching happily...");
  }
  @Override
  public void pet() {
      System.out.println("Sheep pushes against your leg and head-butts "
                 + "your hand for more attention...");
  }
}
 ```

## Abstract class

Abstract is like a concept rather that a physical entity. For that reason there is no point of creating it directly. For example:

```java
  public abstract class Animal {
      public abstract void feed();

      public abstract void pet();
```

Keyword `abstract` protects us of creating an instance of that class. Abstract class can contain any number of real methods or variables, not only abstract ones.

## Interface

Interface is an abstract class which has only abstract methods. You can extend one class to many interfaces.

```java
  public interface Animal {
      public abstract void feed();

      public abstract void pet():
  }

  public class Lion implements Animal {
      @Override
      public void feed() {
        // your code
      }

      @Override
      public void feed() {
        // your code
      }
  }
```



## References
1. [Head First Java, 2nd Edition][1]
2. [Java Programming Basics by Simon Roberts][2]

[1]: http://shop.oreilly.com/product/9780596009205.do
[2]: https://www.safaribooksonline.com/library/view/java-programming-basics/9780133975154/