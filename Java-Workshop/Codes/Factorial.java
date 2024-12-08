import java.util.*;
public class Factorial {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        input.close();
        long Qt =1;
        for(int i=1;i<=num;i++){
           Qt *= i;
           System.out.println(Qt);   // Error
        }
        System.out.println(Qt);
    }
}
