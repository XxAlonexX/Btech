import java.util.*;

public class Switch_case {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("What's Your character max Health");
        int num;
        num = s.nextInt();
        switch(num){
            case 100:
            System.out.println("A");
            break;
            case 90:
            System.out.println("B");
            break;
            case 80:
            System.out.println("C");
            break;
            case 70:
            System.out.println("D");
            break;
            case 60:
            System.out.println("E");
            break;
            default:
            System.out.println("Grind a little");
        }

    }
}
