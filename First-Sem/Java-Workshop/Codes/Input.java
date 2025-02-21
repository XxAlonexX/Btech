import java.util.Scanner;  // Import the Scanner class

class Input {
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);  // Create a Scanner object
    System.out.println("Enter username");

    String userName = myObj.nextLine();  // Read user input
	int num = myObj.nextInt(); 			// Read Input as Integer
    System.out.println("Username is: " + userName);  // Output user input
    System.err.println(num);            // Output for number
  }
}