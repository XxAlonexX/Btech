import java.util.*;

public class Calculator {

    public int add(int a, int b) { 
        int sum = a + b;
        return sum;
    }
}

class Cal { 
    public static void main(String args[]) {
        Calculator cal = new Calculator();
        Scanner s = new Scanner(System.in);
        int a = s.nextInt();
        int b = s.nextInt();
        s.close();
        int result = cal.add(a, b);  
        System.out.println("Sum: " + result); 
    }
}