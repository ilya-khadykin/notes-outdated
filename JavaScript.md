Different notes about `JavaScript`, its syntax and related concepts

- [JavaScript Best Practices](javaScript-best-practices.md)

> The secret to writing large apps in JavaScript is not to write large apps. Write many small apps that can talk to each other.

## JavaScript vs ECMAScript

ECMAScript is the official name for JavaScript. This is due to a trademark on `Java` (held originally by Sun and now by Oracle)

- JavaScript means the programming language
- ECMAScript is the name used by the language specification. The current version of JavaScript is ECMAScript 5; ECMAScript 6 is currently being developed

## The Language

### Identifiers and Variable names
All Variables and function names are case sensitive

### Statements vs Expressions

JavaScript has two major syntactic categories: statements and expressions:
- Statements "do things". **A program is a sequence of statements**, for example `var foo;`
- Expressions produce values. **They are function arguments, the right side of an assignment**, for example `3 * 7`

```js
// this is 'expression statement'
myFunc(7, 1);
```
The function call is an expression

### Values

JavaScript makes a somewhat arbitary distinction between values:
- the **primitive values** are `booleans`, `numbers`, `strings`, `null` and `undefined`
  - Booleans: `true`, `false`
  - Numbers: `1736`, `1.351`
  - Strings: `'abc'`, `"abc"`
  - Two "nonvalues": `undefined`, `null`
- all other values are `objects`

A major difference between them is how they are compared; each object has a unique identity and is only (strictly) equal to itself:
```js
var obj1 = {};
var obj2 = {};

obj1 === obj2 // false
obj1 === obj1 // true


var prim1 = 123;
var prim2 = 123;

prim1 === prim2 // true
```

Primitives are compared by **value**

Objects are compared by **reference**

### `undefined` and `null`

`undefined` means **'no value'**:
- uninitialized variables;
- missing parameters;
- nonexistent properties.

'null' means **'no object'**; it's used as a nonvalue whenever an object is expected (parameters, last in a chain of objects, etc)

### Enable Strict Mode
Strict Mode enables more warnings and makes JavaScript a cleaner language
```js
'use strict'; // put this line at the top of the file

// or function
function functionInStrictMode() {
  'use strict';
}
```

## callbacks
Callbacks are typically used to run a piece of code after a certain event has happened (mouse-click, data was written in db etc).
Typically it's an *anonymous function* (function declared without a name) that's passed directly into the receiving function as a parameter.

Callbacks are asynchronous

Callback doesn't inherit the scope of the function it's passed into

*A callback function inherits the scope in which it's defined*

You can also use **named callbacks** and pass the code as a *reference* to avoid **callback hell**

```js
// var myTimer = setTimeout(callback, delay);

var waitForIt = setTimeout(function() {
  console.log('This is callback function');
}, 2000);
// clearTimeout(waitForIt);
```

## Closures

The closure protects the value from outside interference.

The returned method has access to the scope in which it was created

```js
var user = {};

var setAge = function (myAge) {
  return {
    getAge: function () {
      return myAge;
    }
  };
};

user.age = setAge(30);
console.log(user.age); // Object {getAge: function}
console.log(user.age.getAge()); // 30

var usertwo = {};
usertwo.age = setAge(35);
console.log(usertwo.age.getAge()); // 35
console.log(user.age.getAge()); // 30
```


## References
- ["Getting MEAN with Mongo, Express, Angular, and Node" by Simon Holmes ][1]
- [freeCodeCamp][2]

[1]: https://www.manning.com/books/getting-mean-with-mongo-express-angular-and-node
[2]: http://freecodecamp.com/