// Imports Scanner Class
import java.util.Scanner;

class Factorial {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);  
    
    // Gets number to take factorial of
    System.out.println("Please enter an integer to take the factorial of.");
    String input = sc.nextLine();
    int number = Integer.parseInt(input);
    
    // Int declaration before statements
    int i = number;
    int factorial = number;
    
    // Makes sure number is positive
    if (number < 1){
      System.out.println("Please make sure the number is positive.");
    } else
    
    // For Loop
    for (i = number; i > 1;){
      i--;
      factorial=factorial*i;
    }  
    System.out.println("The factorial is: " + factorial);
  }
}

