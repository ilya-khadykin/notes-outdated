In this document I tried to gather best practices of writing good JavaScript code

## Variables, functions and scope: best practice

There are two types of scopes in JavaScript:
- global scope and
- function scope (local scope)

JavaScript also has `scope inheritance`, so if you declare a global variable it's accessible by everything, but if you declare a variable inside a function it's accessible only to that function and everything inside it.

In the browser the global scope is the object `window`, in Node.js it's `global`

### Best Practices

+ write variable names in `camelCase`
+ **always declare variables in the scope in which they belong**

+ When using global variable in local scope always use fully qualified reference:
```js
var firstname = 'Simon',
    fullname;
var addSurname = function() {
  var surname = 'Holmes';
  window.fullname = window.firstname + ' ' + surname;  // <-- explicitly referencing global scope
  console.log(window.fullname);
};
addSurname();
console.log(fullname);
```
+ Always use the `var` statement for variable declaration

+ **variable hoisting** - JavaScript 'hoists' all variable declarations to the top of their scope
```js
var firstname = 'Simon';
var addSurname = function () {
  var surname = 'Holmes';
  var fullname = firstname + ' ' + surname;  // <-- you expect this to use global variable
  var firstname = 'David';
  console.log(fullname);  // <-- but output is actually 'undefined Holmes'
};
addSurname();
```
You see an unexpected output because js 'hoists' all variable declarations to the top of their scope. Let's look at how js sees the code from the previous example:
```js
var firstname = 'Simon';
var addSurname = function () {
  var firstname, // <-- js moved all variable declarations to top
      surname,
      fullname;
  surname = 'Holmes';
  fullname = firstname + ' ' + surname; // <-- no value is assigned before it's used to 'firstname' so it's undefined
  firstname = 'David';
  console.log(fullname);  
};
addSurname();
```

+ There is no concept of a `block scope`

JavaScript doesn't have the concept of a 'block scope' within `if` statements or `for` loops etc. 

+ Using functions as variables, it's a good practice
```js
var addSurname = function () {};
```

+ Limit use of the global scope to avoid clashes with variables of the same names from imported third-party libraries and modules.
You can arrange all your variables into one object like so:
```js
var nameSetup = {  // <-- declare global variable as object
  firstname: 'Simon',
  fullname: '',
  addSurname: function () {
    var surname = 'Holmes';  // <-- local variables are still okay inside functions
    nameSetup.fullname = nameSetup.firstname + ' ' + surname;  // <-- always access values of object using fully qualified reference
    console.log(nameSetup.fullname)''
  }
};
nameSetup.addSurname();  // <-- always access values of object using fully qualified reference
console.log(nameSetup.fullname);
```
Using this approach you can add new properties to that object any time:
```js
nameSetup.addInitial = function (initial) {
  nameSetup.fullname = nameSetup.fullname.replace(" ", " " + initial + " ");
};
nameSetup.addInitial('D');
console.log(nameSetup.fullname);
```

### Logic flow and loops: best practice

+ Always use `{ }` in `if` statements
```js
var firstname = 'Simon', surname, initial = '', fullname;
if (firstname === 'Simon') {
  surname = 'Holmes';
} else if (firstname === 'Sally') {
  initial = 'J';
  surname = 'Panayiotou';
}
fullname = firstname + ' ' + initial + ' ' + surname;
console.log(fullname);
```

+ Always use the exact operator in conditional statements `===` and `!==` to avoid unexpected results due to type coercion

+ Declare utility variables right before loop statement in which they are used
```js
var i, myArray, arrayLength;  // <-- declare length variable
myArray = ["one", "two", "three"];
for (i = 0, arrayLength = myArray.length; i < arrayLength; i++) {  // <-- assign length of array to arrayLength when setting up loop to avoid checking array length property every time
  console.log(myArray[i]);
}
```

## References
- ["Getting MEAN with Mongo, Express, Angular, and Node" by Simon Holmes ][1]
- [freeCodeCamp][2]

[1]: https://www.manning.com/books/getting-mean-with-mongo-express-angular-and-node
[2]: http://freecodecamp.com/