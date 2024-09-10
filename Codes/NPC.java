// public class Abstract {
    
// }
abstract class NPC{
    abstract void start();
}
class Player extends NPC{
    void start(){
        System.out.println("Started");
    }
}
class Character extends NPC{
    void start(){
        System.out.println("Start's Car");
    }
    public static void main(String[] args) {
        Character x=new Character();
        Player y = new Player();
        x.start(); 
        y.start(); 
    }
}