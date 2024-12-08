interface Warrior {
    void swingSword();
    void blockAttack();
}

interface Mage {
    void castSpell();
    void meditate();
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

public class multipalinheri { 
    public static  void main(String[] args) {
        HybridHero Alone = new HybridHero();
        Alone.castSpell();
        Alone.swingSword();
    }
}