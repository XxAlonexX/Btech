import java.util.*;
public class Numbers {
    public static void main(String[]args){
        int a;
        Scanner s = new Scanner(System.in);
        a = s.nextInt();

    if(a>90){
        System.out.println("Case1");
        if(a>96){     // Nested ifelse
            System.out.println("GRADE A");
        }
        else{
            System.out.println("B");
        }
    }
    else if (a>80) {        // else if
        System.out.println("Case ");
    }
    else if (a>70) {
        System.out.println("Case ");
    }
    else {
        System.out.println("Fail");
    }
    }
}


