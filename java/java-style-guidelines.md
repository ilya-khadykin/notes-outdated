# Java Style Guidelines

You can find additional information here:

 - [Java Style Guidelines (Draft)][1]
 - [Java Code Conventions September 12, 1997][2]
 - [Google Java Style][3]


Basic rules:

- Store classes as separate source .java files
- Class name should start from Capital letter: `YetAnotherHelloWorld`
- Variable and method names are lowercase: `longMethodName()`
- For indention use 4 spaces

## Packages

The prefix of a unique package name is always written in all-lowercase and should be one of the top-level domain names.

Subsequent components of the package name vary according to an organization's own internal naming conventions. Such conventions might specify that certain directory name components be division, department, project, machine, or login names.

```java
com.sun.eng

com.apple.quicktime.v2

edu.cmu.cs.bovik.cheese
```

## Classes

Class names should be nouns, in mixed case with the first letter of each internal word capitalized. Try to keep your class names simple and descriptive. Use whole words-avoid acronyms and abbreviations (unless the abbreviation is much more widely used than the long form, such as URL or HTML).

```java
class Raster; 
class ImageSprite;
```

## Interfaces


Interface names should be capitalized like class names.

```java
interface RasterDelegate; 
interface Storing;
```

## Methods


Methods should be verbs, in mixed case with the first letter lowercase, with the first letter of each internal word capitalized.

```java
run(); 
runFast(); 
getBackground();
```

## Variables


Except for variables, all instance, class, and class constants are in mixed case with a lowercase first letter. Internal words start with capital letters. Variable names should not start with underscore _ or dollar sign $ characters, even though both are allowed.

Variable names should be short yet meaningful. The choice of a variable name should be mnemonic- that is, designed to indicate to the casual observer the intent of its use. One-character variable names should be avoided except for temporary "throwaway" variables. Common names for temporary variables are i, j, k, m, and n for integers; c, d, and e for characters.


```java
int             i;
char            c;
float           myWidth;
```

## Constants

The names of variables declared class constants and of ANSI constants should be all uppercase with words separated by underscores ("_"). (ANSI constants should be avoided, for ease of debugging.)

```java
static final int MIN_WIDTH = 4;

static final int MAX_WIDTH = 999;

static final int GET_THE_CPU = 1;
```


## References

 - [Java Style Guidelines (Draft)][1]
 - [Java Code Conventions September 12, 1997][2]
 - [Google Java Style][3]


[1]: http://cr.openjdk.java.net/~alundblad/styleguide/
[2]: http://www.oracle.com/technetwork/java/codeconventions-150003.pdf
[3]: https://google.github.io/styleguide/javaguide.html
