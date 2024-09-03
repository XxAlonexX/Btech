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
### Modifiers (Access Modifiers)
- Public : It's a park which can be accessed by anyone in game (Class);
- Private : It's like a hideout which can be accessed only by same team members (same class members);
- Protected : It's like a GTA online Closed friends server;
- Default : Everyone in the packadge can easily access this.

### Packages
Packages are like folders which contains a specific assigned part of your code.
- Helps you code readablity
- Increase maintainabilty l
- Avoide name conflicts

### Method to run Java Files on Command line
```
- javac FileNameHere.java           //Will make a class compile form

- java FileNameHere                 // Will exicute the file directly here

```
## Method Overloading & Overriding
### Overloading
Method Overloading is where we use same method with diffrent parameters.
```java
class Player {
    void attack() { 
        System.out.println("Basic punch!"); 
    }

    void attack(String weapon) { 
        System.out.println("Attack with " + weapon + "!");
    }

    void attack(int powerLevel) {
        System.out.println("Supercharged attack with power level " + powerLevel + "!");
    }
}
```
### Overriding
Method Overriding is where we use same methods and parameters and the override the functions for that perticular class.
```java
class Character {
    void move() { 
        System.out.println("Generic movement"); 
    }
}

class Ninja extends Character {
    @Override 
    void move() {
        System.out.println("Ninja vanishes in a puff of smoke!"); 
    }
}

class Wizard extends Character {
    @Override
    void move() {
        System.out.println("Wizard teleports!");
    }
}
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
It is important to close scannes in java using `scanner.close();`

```java
import java.util.Scanner;  // Import the Scanner class

class Main {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);  // Create a Scanner object
    System.out.println("Enter username");

    String userName = myObj.nextLine();  // Read user input
	int num = myObj.nextInt(); 			// Read Input as Integer
    System.out.println("Username is: " + userName);  // Output user input
    myObj.close();
  }
}
```
### Rule Switch
```java
int dayOfWeek = 3;
String dayType = switch (dayOfWeek) {
    case 1, 7 -> "Weekend";
    case 2, 3, 4, 5, 6 -> "Weekday";
    default -> "Invalid day";
};
```

# OOPs
### Class &Objects
Class is a blueprint for the data which does not occupy any spaces in memory.
Objects are the entities of class which are stored under class.

## Principals of OOPs

## Accesibity Table                             
- Private 
- Public 
- Protected
- Default

