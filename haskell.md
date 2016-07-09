# Haskell (Draft)

Haskell platform - haskell.org/platform

Compiler - GHC

Run the interpretor in CLI by typing `GHCi`

## HelloWorld in Haskell

```haskell
main = putStrLn "Hello, world!"
```

Run with `ghci Hello.hs`

## Loading modules

`Prelude> :load Test` and call your function

`:reload` - reloading the module

## Function Declaration

sumSqures x y = x ^ 2 + y ^ 2

In GHCi - let sumSqures x y = x ^ 2 + y ^ 2

## if statement

```haskell
if x > 0 then 1 else (-1)

g x = (if x > 0 then 1 else (-1)) + 3
```

```haskell
max5 x = max 5 x

max5` = max 5
```

```haskell
discount limit proc sum = if sum >= limit then sum * (100 - proc) / 100 else sum
standardDiscount = discount 1000 5
-- standardDiscount 200
```

## Operators

Operators are binary in Haskell (except `-` prefix which gives a negative number)

9 levels of operator's priority (from lowest to highest)

```haskell
:info (+)
```

```haskell
6 `max` 7 -- == max 6 7

(+) 6 7


infixr 8 ^, 'logBase'
infixl 7 *, /, 'div', 'mod'
infix 4 ==, /=, >, >=, <, <= -- no associativity
```

You can define your own operators:
```haskell
{-
! # $ % & * + . / < = ? ? @ \ ^ | - ~
-}

infixl 6 *+* -- 6 is a priority

a *+* b = a ^ 2 + b ^ 2 -- == (*+*) a b = a ^ 2 + b ^ 2
```