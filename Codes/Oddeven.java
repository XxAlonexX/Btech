// College Code 

import java.util.*;
public class Oddeven {

	public static void main(String[] args) {
		//Create scanner object for input
		Scanner myobj = new Scanner(System.in);
		System.out.println("Enter a number: ");
		
		//read the input as an integer
		int number = myobj.nextInt();
		
		//check the number is even or odd
		if (number % 2 ==0) {
			System.out.print(number +"is even number ");
			
		}
		else {
			System.out.println(number + "is odd number");
		}

	}

}