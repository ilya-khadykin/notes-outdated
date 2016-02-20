This page was created in order to further investigate some of java code snippets I've come across, analyze them and fill gaps in my knowledge of java syntax.

## Declarations

```java
int[] a = {1,2,3,4,5};
int[] b = new int[5];
int c [] = {4,3,7};
int [] myScores [];
ClassName myClasses [];
boolean results[] = new boolean [] {true, false, true};

char c1 = 064770;
char c3 = 0xbeef;
char c6 = '\uface';

boolean b4 = new Boolean("false");

String s1 = null;

for(;;) {}
```
## Passing the arguments

```java
public class CommandArgs {
  public static void main(String[] args) {
    String s1 = args[1];
    String s2 = args[2];
    String s3 = args[3];
    String s4 = args[4];
    System.out.print(" args[2] = " + s2);
  }
}

// from CLI
// java CommandArgs 1 2 3 4 5
```

```java
public class Test {
  static int s;
  public static void main(String[] args) {
    int I = 1;
    do while (I < 1)  // why this is valid?
    System.out.print("I is " + I);
    while (I > 1); // why this is valid?
  }
}
```