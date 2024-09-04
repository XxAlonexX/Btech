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
### Default Constructors 
```java
class Hero {
    String name;
    int health;
    int strength;
    String weapon;

    // Default Constructor
    public Hero() {
        this.name = "New Hero";
        this.health = 100;
        this.strength = 10;
        this.weapon = "Wooden Sword";
    }

    public void displayStats() {
        System.out.println("Name: " + name);
        System.out.println("Health: " + health);
        System.out.println("Strength: " + strength);
        System.out.println("Weapon: " + weapon);
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating a new hero using the default constructor
        Hero defaultHero = new Hero(); 
        defaultHero.displayStats(); 
    }
}
```
```java
public class Main {
    public static void main(String[] args) {
        // Creating a new hero using the default constructor
        Hero defaultHero = new Hero(); 
        defaultHero.displayStats(); 

        // Creating a new hero using the parameterized constructor
        Hero customHero = new Hero("Braveheart", 120, 15, "Iron Sword");
        customHero.displayStats();
    }
}
```
- Constructors does not have any return type.
- Exicutes automatically when we create a object.

### Input parameterized constructors
In order to make a program with both default and input parameterized constructor we either use ternory operators or (`Integer.parseInt();` -> It is used to convert string input into integer).
> We need to check input from user weather is empty or not so we use `VariableInput.isEmpty();`
```java
import java.util.*;
class Character {
    String name;
    String charClass;
    int level;
    int healthPoints;
    int manaPoints;

    // Default Constructor (Quick Start)
    public Character() {
        this.name = "Adventurer";
        this.charClass = "Warrior";
        this.level = 1;
        this.healthPoints = 100;
        this.manaPoints = 0; 
    }

    // Parameterized Constructor (Custom Character)
    public Character(String name, String charClass, int level, int healthPoints, int manaPoints) {
        this.name = name;
        this.charClass = charClass;
        this.level = level;
        this.healthPoints = healthPoints;
        this.manaPoints = manaPoints;
    }

    public void displayInfo() {
        System.out.println("Name: " + name);
        System.out.println("Class: " + charClass);
        System.out.println("Level: " + level);
        System.out.println("Health Points: " + healthPoints);
        System.out.println("Mana Points: " + manaPoints);
    }
}

public class Merge {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter character name (or press Enter for default): ");
        String name = scanner.nextLine();

        System.out.print("Enter character class (or press Enter for default): ");
        String charClass = scanner.nextLine();

        System.out.print("Enter character level (or press Enter for default): ");
        String levelInput = scanner.nextLine();
        int level = levelInput.isEmpty() ? 1 : Integer.parseInt(levelInput); // Default to 1 if empty
        System.out.print("Enter health points (or press Enter for default): ");
        String healthInput = scanner.nextLine();
        int healthPoints = healthInput.isEmpty() ? 100 : Integer.parseInt(healthInput); // Default to 100

        System.out.print("Enter mana points (or press Enter for default): ");
        String manaInput = scanner.nextLine();
        int manaPoints = manaInput.isEmpty() ? 0 : Integer.parseInt(manaInput); // Default to 0

        // Create character based on input
        Character character;
        if (name.isEmpty() && charClass.isEmpty()) {
            character = new Character(); // Use default constructor if no name or class provided
        } else {
            character = new Character(name, charClass, level, healthPoints, manaPoints);
        }

        System.out.println("\nCreated Character:");
        character.displayInfo();

        scanner.close();
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
### Abstraction
> Abstract methods have no body
 - A method must always be declared in an abstract class or we can say if class an abstract method it should declared abstract as well.
 - If a regular class extends an abstract class then the class must have to impliment all the abstract methods in abstract parent class or it has to be declared as abstrect.
 - Abstract class cannot be instancesiated, we can not create an object of abstraction class.
## Accesibity Table                             
- Private 
- Public 
- Protected
- Default

