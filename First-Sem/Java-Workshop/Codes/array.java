import java.util.*;

/*/
public class array {

    public static void main(String[] args) {
        int[] letters = {5, 66, 4, -6,9};
        int a = 0;

        System.out.print("Letters: ");
        System.out.println("Your inventory: " + Arrays.toString(letters));
        // for (int i = 0; i < letters.length; i++) {
        for (int i = letters.length-1;i>= 0;i-- ){
            System.out.println(letters[i]);
            if (a < letters[i]) {
                a = letters[i];
            } else {
                // System.out.println("Largest number " + a);
            }
        }
    }
}
*/
//  -----------------------------------------------------------------------------------------------------------------------------------------
/*
public class array{
    public static void main(String[] args) {
        int number[] = {1,3,4,55,6,6,77};
        int count = 0;
        int e;
        Scanner scanner = new Scanner(System.in);
        e = scanner.nextInt();
        for(int i = 0; i< number.length; i++){
            if(number[i]==e){
                count++;
                System.out.println("The number " + e + " appears " + count + " times in the array.");
                }
                }
                }
                }
                // For(DataType VariableName : Array/Collection)
                */
                
//  -----------------------------------------------------------------------------------------------------------------------------------------
/*
public class array{
    public static void main(String[] args) {
        int score[] [] ={
            {1,4,5,6},
            {3,5,2,5}
            };
            // System.out.println(score[1][3]);
            for (int i = 0; i < score.length; i++) {
                System.out.print("Player " + (i + 1) + ": ");
                for (int j = 0; j < score[i].length; j++) {
                    System.out.print(score[i][j] + " ");
                }
                System.out.println();
            }
    }
}
*/
/*
public class array {

    public static void main(String[] args) {

        int[][] matrix1 = { {1, 2, 3, 4},
                            {5, 6, 7, 8},
                            {9, 10, 11, 12} };

        int[][] matrix2 = { {13, 14, 15, 16},
                            {17, 18, 19, 20},
                            {21, 22, 23, 24} };

        int[][] result = new int[matrix1.length][matrix1[0].length];

        for (int i = 0; i < matrix1.length; i++) {
            for (int j = 0; j < matrix1[i].length; j++) {
                result[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }

        System.out.println("Sum:");
        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result[i].length; j++) {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}
*/

/*
// Single array with input 

public class array {

    public static void main(String[] args) {


        Scanner s = new Scanner(System.in);
        int size = s.nextInt();
        int[] matrix = new int[size];
        for (int i = 0; i < size; i++) {
             matrix[i] = s.nextInt();
            }
            for(int i = 0 ; i < matrix.length;i++){
                System.out.println("Matrix" + matrix[i]);
            }
        }
     }
  */

