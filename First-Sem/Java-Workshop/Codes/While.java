import java.util.*;
public class While {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num = input.nextInt();
        int i=1;
        input.close();
        long Qt =1;
        while(i <= num){
           Qt *= i;
           i++;
        }
        System.out.println(Qt);
    }

}