# node.js
**node.js** is a server side implementation of Google Chrome js engine that allows you to run it on your server. It's event driven and asynchronous which makes it perfect for writing network and I/O intense applications.

## Best practices
node.js differs a lot from conventional languages and frameworks, it doesn't require an http server to run (apache or nginx), instead you create your own http server inside your app and have full control of it. 

**Express** is a recommended option for implementing http server with node, because it's lightweight and supports a lot of cool features like routing and templating engines. But there are other options (`http` module for example)j