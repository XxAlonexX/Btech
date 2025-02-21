// class Test{
//     void show(String a){
//         System.out.println("Done");
//     }
// }
// class Txt extends Test{
//     void show(String a, int b){
//         System.out.println("Two");
//     }
// }
// public class overRidingBasicD6 {
//     public static void main(String[] args) {
//     Test t = new Test();
//     Txt n = new Txt();
//     t.show("ha");
//     n.show("ha",8);

//     }
// }

//  To overriding method must same written type or sub type?

// class Test{
//     String show (String a){
//         System.out.println("Done");
//         return a;
//     }
// }
// public class Txt extends Test{

//     @Override
//     String show(String a){
//         System.out.println("Two");
//         return a;
//     }
// }
// public class overRidingBasicD6 {
//     public static void main(String[] args) {
//     Test t = new Test();
//     Txt n = new Txt();
//     t.show("ha");
//     n.show("ha");

//     }
// }

// java compiler priortise the child over parent class so you cannot make a child protected and parent public. 

class Test{
    protected void show(){
        System.out.println("Done");
        
    }
}
 class Txt extends Test{

    @Override
    public void show(){
        System.out.println("Two");
        
    }
}
public class overRidingBasicD6 {
    public static void main(String[] args) {
    Test t = new Test();
    Txt n = new Txt();
    t.show();
    n.show();

    }
}