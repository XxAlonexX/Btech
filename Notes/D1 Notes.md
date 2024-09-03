# Basics
1. Weather class contains main() method or not and weather main() method is declared according to requirements or not these things won't checked by compiler. At runtime, JVM is responsible to check these things.

- All runtime if JVM is unable to find required main() method then we will get runtime exception saying `NoSuchMethodError.main`

```java
class Test{
}
java Test.java
java Test
RuntimeException : NoSuchMethodError.main
```
![fig1.jpeg]

2. We can declare `'String[]'`  in any acceptable form.
- `main(String []args)`
- `main(String[] args)`
- `main (String args[])`

3. Instead of `'args'` we can take any valid java identifier.

4. We can declare main() method with the following modifiers also.
- `final`
- `synchronized `
- `strictfp`

```java
class Test{
final static synchronized strictfp public void main(string args[]){
sopen("void main");
}
}
javac Test.java
java Test
output void main
```

### Method to run Java Files on Command line
```
- javac FileNameHere.java           //Will make a class compile form

- java FileNameHere                 // Will exicute the file directly here

```
## Constructers
```java
 package Firstapp;                      // Package Name

public class Student {
	public static void Dance() {
		System.out.println("Nacchiiiiii");
	}

	public static void main(String[] args) {
	   Student alex=new Student();
	   alex.Dance();
	}

}
```
## Input in Java

```java
import java.util.Scanner;  // Import the Scanner class

class Main {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);  // Create a Scanner object
    System.out.println("Enter username");

    String userName = myObj.nextLine();  // Read user input
	Int num = myObj.nextInt(); 			// Read Input as Integer
    System.out.println("Username is: " + userName);  // Output user input
  }
}
```

# OOPs
### Class &Objects
Class is a blueprint for the data which does not occupy any spaces in memory.
Objects are the entities of class which are stored under class.

## Principals of OOPs


