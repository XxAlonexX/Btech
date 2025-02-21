

class Hero {
    String name;
    int health;
    int strength;
    String weapon;
    

    // Parameters Constructors 
    public Hero(String name, int health, int strength, String weapon) {
        this.name = name;
        this.health = health;
        this.strength = strength;
        this.weapon = weapon;
    }

    // Default Constructor
    public Hero(){
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

public class Constructors {
    public static void main(String[] args) {
        
        // Creating a new hero using the default constructor
        Hero defaultHero = new Hero(); 
        Hero Alone = new Hero("XxAlonexX",500,24,"Golden");
        defaultHero.displayStats(); 
        Alone.displayStats();
        
    }
}