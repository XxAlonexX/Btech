abstract  class NPC{
    String weapon;
    int Attack;
    abstract void Attack();
     void run(){
        System.out.println("Player Runs");
    }
    public NPC(String weapon, int Attack){
        this.weapon = weapon;
        this.Attack = Attack;
    }
}

class Kratos extends NPC{
    public Kratos(String weapon,int Attack){
        super(weapon, Attack);
    }
    
    void Attack(){
        System.out.println("Attacks with" +weapon);
    }
}
class Dante extends NPC{
    public Dante(String weapon,int Attack){
        super(weapon, Attack);
    }
    
    void Attack(){
        System.out.println("Attacks with" +weapon);
    }
}

public class Abstraction_test {
        public static void main(String[] args) {
            Kratos kratos = new Kratos("Stormbreaker", 473);
            Dante dante = new Dante("Sword", 444);
            kratos.Attack();
            kratos.run();
            dante.Attack();
            dante.run();
        }
}