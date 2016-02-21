# Primitive data types

Primitive type is basically a cell in computer memory which holds particular value

Primitive types are passed by value, not by reference, so that their value is copied.

 - boolean
 - char
 - byte, short, int, long
 - float, double

## `boolean`

boolean can have only `true` or `false` as values. It's impossible to convert other primitive types to boolean like this `boolean b = 10;`

boolean is returned when comparison operator is used: `< <= > >= == !=`

It supports the following logic operators: `! && || ^ | &` or `&= |= ^=`

```java
public boolean booleanExpression(boolean a, boolean b, boolean c) {
  return (c & secretFunction()) || (a ^ b);  // & is used instead of && because secretFunction() should always be called
}
```

## byte, short, int, long

Type  | Size (bit) | Range
----- | ----- | -----
byte  |   8   | -128 ... +127
short |  16   | -2<sup>15</sup> ... +2<sup>15</sup>-1
int   |  32   | -2<sup>31</sup> ... +2<sup>31</sup>-1
long  |  64   | -2<sup>63</sup> ... +2<sup>63</sup>-1

```java
int decimal = 99;

int octal = 0755;

int hex = 0xFF;

int binary = 0b101;

int tenMillion = 10_000_000;

long tenBillion = 10_000_000_000L;  // long
```

Overflow isn't consider as an error:
```java
byte b = 127; // 01111111
b++; // 10000000 == -128
```

```java
int neg = ^a;

int and = a & b;

int or = a | b;

int xor = a ^ b;

int arithmeticShiftRight = a >> b;  // % 32

int logicalShiftRight = a >>> b;

int shiftLeft = a << b;
```

## char

16 bit, unsigned; 0 .. 2<sup>16</sup>-1

Returns Unicode code UTF-16

## float, double


Type | Size (bit) | Sign | Stagnat | Exponent 
----- | ----- | ----- | ----- | -----
float | 32 | 1 | 23 | 8
double | 64 | 1 | 52 | 11

+-m2<sup>e</sup> IEEE 754

```java
double simple = -1.234;

double exponential = -123.4e-2; // -123.4 * 10^2

double hex = 0x1.Fp10; // 1.F * 2^10

float floatWithSuffix = 36.6f;

double doubleWithSuffix = 4d;
```

```java
double positiveInfinity = 1.0 / 0.0; // Infinity, not an error

double negativeInfinity = -1.0 / 0.0; // Infinity, not an error
// 1/Infinity == 0

double nan = 0.0 / 0.0;

boolean notEqualIsItself = nan != nan;
```

### comparison of float, double

|a-b| <= epsilon where epsilon is measure of inaccuracy

## Reference types

All none primitive types. This type holds a reference to a cell in computer memory where the actual data is stored

`null (String u = null;)` shows that the variable doesn't have any reference and is empty.

 - Strings;
 - all classes.