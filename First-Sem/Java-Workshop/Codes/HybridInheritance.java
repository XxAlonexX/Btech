class Human {
    void fight() {
        System.out.println("Engages in hand-to-hand combat!");
    }
}

interface Robot {
    void enhanceStrength();
}

class Cyborg extends Human implements Robot {
    @Override
    public void enhanceStrength() {
        System.out.println("Strength enhanced by cybernetics!");
    }
}
public class HybridInheritance {
    public static void main(String[] args) {
        Cyborg n = new Cyborg();
        n.enhanceStrength();
        n.fight();
    }
}