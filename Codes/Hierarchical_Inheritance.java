class Creature {
    String habitat;

    public Creature(String habitat) {
        this.habitat = habitat;
    }
}

class Dragon extends Creature {
    public Dragon() {
        super("Mountains"); 
    }

    void breatheFire() {
        System.out.println("Dragon breathes fire!");
    }
}

class Unicorn extends Creature {
    public Unicorn() {
        super("Forests"); 
    }

    void heal() {
        System.out.println("Unicorn uses healing magic!");
    }
}
class Hierarchical_Inheritance{
    public static void main(String[] args) {
        Unicorn N = new Unicorn();
        N.heal();
        Dragon X = new Dragon();
        X.breatheFire();
    }
}