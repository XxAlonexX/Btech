abstract class Character { // Abstract class representing a generic character
    protected int health;
    protected String name;

    public Character(String name, int health) {
        this.name = name;
        this.health = health;
    }

    public abstract void attack(); // Abstract method, subclasses must provide implementation

    public void displayInfo() {
        System.out.println("Name: " + name + ", Health: " + health);
    }
}

class Warrior extends Character {
    public Warrior(String name, int health) {
        super(name, health);
    }

    @Override
    public void attack() {
        System.out.println(name + " swings their sword!");
    }
}

class Mage extends Character {
    public Mage(String name, int health) {
        super(name, health);
    }

    @Override
    public void attack() {
        System.out.println(name + " casts a fireball!");
    }
}

public class PlayerCharacter {
    public static void main(String[] args) {
        Character warrior = new Warrior("Conan", 120);
        Character mage = new Mage("Merlin", 80);

        warrior.displayInfo();
        warrior.attack();

        mage.displayInfo();
        mage.attack();
    }
}