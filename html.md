`HTML` is a markup language which is rendered by browsers to display web content

1. [Basic principles](basic-principles)
2. [Standart structure of HTML document](standart-structure-of-html-document)

![html5](./img/html5.png)

## Basic principles

Browsers to be able to render contents of a web page should parse it's content and determine how elements are separated from one another on a page. To help them do that `HTML` has a concept of pair tags, one piece opens the element and the other closes it. Here is an example of creating a 'header' element:
```html
<h1>Your title here</h1>
```
There are 6 levels of heading in HTML (from 1 to 6, decreasing its importance), visually they differ from one another by font size and 'logical meaning' (the higher the level the more important it is, it's used by search engines to rank pages among other things). Header text is placed between the opening and closing tags allowing browsers easily find them.

Almost all tags in HTML are paired and there are a lot of them with different purposes. 

In order to change the look or settings of HTML elements **attributes** are used, they should be inserted in tag itself:
```html
<a href="[URI]">[Anchor text or image tag]</a>
<h2 style="color: blue">Level 2</h2>
```
`href` attribute specifies the URL link to a resource.

You can find a full list of HTML elements and their attributes here:
- [HTML Elements][1]
- [HTML(5) Tutorial from W3Scools][2]

Every HTML document should have [standart structure](standart-structure-of-html-document)

## Standart structure of HTML document
```html
 <!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>This is a Heading</h1>
<p>This is a paragraph.</p>

</body>
</html> 
```

[1]: http://docs.webplatform.org/wiki/html/elements
[2]: http://www.w3schools.com/html/default.asp