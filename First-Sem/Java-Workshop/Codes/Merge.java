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