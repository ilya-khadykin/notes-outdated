# Java IO Libraries

## java.io

Abstract Classes:
- InputStream
- OutputStream
- Reader
- Writer

```java
package readfile;

  public class ReadAFile {
    public static void main(String[] args) throws Throwable {
        FileReader fr = new FileReader("text.txt");
        BufferedReader br = new BufferedReader(fr);

        String line;
        while((line = br.readLine()) != null) {
            System.out.println("Read: " + line);
        }
    }
  }
```

## References
1. [Java Programming Basics by Simon Roberts][1]

[1]: https://www.safaribooksonline.com/library/view/java-programming-basics/9780133975154/