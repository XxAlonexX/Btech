
// class Test{
//     protected void show(){
//         System.out.println("Done");
        
//     }
// }
//  class Txt extends Test{

//     @Override
//     public void show() throws ArithmeticException{
//         System.out.println("Two");
        
//     }
// }
// public class exceptionError {
//     public static void main(String[] args) {
//     Test t = new Test();
//     Txt n = new Txt();
//     t.show();
//     n.show();

//     }
// }

// -------------------------------------------------------------------------------------------------------------------------

// abstract class A {
//     abstract void show() throws RuntimeException;
//     abstract void display();
// }

// class xyx extends A {
//     void display() { 
//         System.out.println("x");
//     }
    
//     @Override 
//     void show() throws RuntimeException { 
//         System.out.println("Welcome");
//     }
// }

// public class exceptionError {
//     public static void main(String[] args) {
//         A b = new xyx(); 
//         b.show();
//     }
// }

// -------------------------------------------------------------------------------------------------------------------------


// abstract class A {
//     abstract void show() throws RuntimeException;
//     abstract void display();
// }

// class xyx extends A {
//     void display() { 
//         System.out.println("x");
//     }
    
//     @Override 
//     void show() throws RuntimeException { 
//         System.out.println("Welcome");
//     }
// }
// interface Xyyx{
    
// }

// public class exceptionError {
//     public static void main(String[] args) {
//         A b = new xyx(); 
//         b.show();
//     }
// }


// -------------------------------------------------------------------------------------------------------------------------
class Test{
    void show(){
        System.out.println("1");
    }
}
class xyz extends Test{
    void show(){
        super.show();
        System.out.println("");
    }
}
public class exceptionError{
    public static void main(String[] args) {
        xyz t = new xyz();
        t.show();
    }
}
