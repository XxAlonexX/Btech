// // Interface representing common character traits
// interface Character {
//     void attack(); 
//     void defend(); 
// }

// public class Warrior implements Character {
//     public int strength = 10;
//     private int health = 100; 

//     public void attack() {
//         System.out.println("Warrior attacks with a powerful sword!");
//     }

//     public void defend() {
//         System.out.println("Warrior raises a shield for defense!");
//     }

//     public int getHealth() { 
//         return health;
//     }
// }

// protected class Mage implements Character {
//     protected int mana = 50; 
//     private int spellPower = 8;

//     public void attack() {
//         if (mana >= 10) {
//             System.out.println("Mage casts a fireball!");
//             mana -= 10;
//         } else {
//             System.out.println("Mage is out of mana!");
//         }
//     }

//     public void defend() {
//         System.out.println("Mage creates a magical barrier!");
//     }
// }
// public class ClassCode {
//     public static void main(String[] args) {
//         Warrior warrior = new Warrior();
//         warrior.attack(); 
   
//     }
// }

// --------------------------------------------------------------------------------------------------------------------------

interface Warrior {
    public abstract void swingSword();
    public abstract void blockAttack();
}

interface Mage {
    public abstract void castSpell();
    public abstract void meditate();
}

class HybridHero implements Warrior, Mage {
    

    @Override
    public void swingSword() {
        System.out.println("Hero swings their mighty sword!");
    }

    @Override
    public void blockAttack() {
        System.out.println("Hero skillfully blocks an incoming attack!");
    }

    @Override
    public void castSpell() {
        System.out.println("Hero unleashes a powerful spell!");
    }

    @Override
    public void meditate() {
        System.out.println("Hero focuses their mind, restoring mana.");
    }
}

public class Warriorr { 
    public static  void main(String[] args) {
        HybridHero Alone = new HybridHero();
        Alone.castSpell();
        Alone.swingSword();
    }
}