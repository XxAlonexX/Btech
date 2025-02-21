import  java.util.*;
public class Ternaroy {
    public static void main(String[] args) {
       Scanner s = new Scanner(System.in);
       int num = s.nextInt();
       s.close();
       String result = (num%2 == 0) ? "even" : "odd";
       System.out.println(result);
    }
    
}

/*
   int a = 2 , b = 4;
    int max = (2>4) ? a : b;
    System.out.println(max);
 */
