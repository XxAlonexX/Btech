class Parent {  
    // superclass
    private  String privateField = "This is a private Field";

    public  String getPrivateField() {  
        return privateField;
    }
}

// subclass
class Child2 extends Parent {  
    public void displayPrivateField() {
        // System.out.println(privateField);
        // Accessing privateField using the getter method
        System.out.println("Accessing private Field using getter: " + getPrivateField());
    }
}

public class AccessingPrivateModifiers {
    public static void main(String[] args) {
        Child2 child = new Child2();
        child.displayPrivateField();
    }
}