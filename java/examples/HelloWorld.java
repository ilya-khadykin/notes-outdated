/*
 *   Every Java program should have at least one class
 *   It's a good practice to store classes as separate source .java files
 */

// 'public' access modifier makes class accessible from anywhere
public class HelloWorld {  // in that case the name of the class should match to a source file HelloWorld.java in this example

  // this method is an entry point to the program and if you change access modifier or returning value the program can be compiled but won't run
  // 'static' means that you can use this method without creating an instance of the class
  // 'void' means that the method doesn't return anything
  public static void main(String[] args) {  // 'args' contains arguments from CLI passed to the program: String s0 = args[0];
    System.out.println("Hello, World!");  // printing String using special function
    System.exit(-1); // terminating the program and sending none zero exit code to Operating System
  }

  class Foo {} // It's possible but not recommended
}

class Bar {} // It's possible but not recommended