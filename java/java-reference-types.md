# Reference types in Java

## Wrapper classes

Primitive | Class
 -------- | -------- 
boolean   | Boolean
byte      | Byte
short     | Short
int       | Integer !
long      | Long
char      | Character !
float     | Float
double    | Double

```java
int primitive = 0;

Integer reference = Integer.valueOf(primitive);
int backToPrimitive = reference.intValue();
```

### boxing

```java
Integer reference = Integer.valueOf(primitive);
```

### unboxing

```java
int backToPrimitive = reference.intValue();
```

### Implicit conversion
```java
Integer a = 1;
int b = a;

Integer c = 10;
Integer d = 10;
Integer e = c + d; // much slower than primitives due to overhead of boxing/unboxing
```

### Conversion to/from String

```java
long fromString = Long.parseLong("12345"); // static method

String fromLong = Long.toString(12345); // static method

String concatenation = "area" + 51; // automatic conversion
```

### Useful methods

```java
short maxShortValue = Short.MAX_VALUE;

int bitCount = Integer.bitCount(123);

boolean isLetter = Character.isLetter('a');

float floatInfinity = Float.POSITIVE_INFINITY;

double doubleNaN = Double.NaN;

boolean isNaN = Double.isNaN(doubleNaN);
```