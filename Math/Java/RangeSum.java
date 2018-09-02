// Imports Scanner Class
import java.util.Scanner;

class RangeSum {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);  
    
    // Gets number to start range
    System.out.println("Please enter a first integer");
    String input = sc.nextLine();
    int a = Integer.parseInt(input);
    
    // Gets number to end range
    System.out.println("Please enter a second integer");
    input = sc.nextLine();
    int b = Integer.parseInt(input);
    
    // Int declaration before statements
    int i = 0;
    int sum = 0;
    
    // Makes sure number is a valid range
    if (b < a){
      System.out.println("Please make sure b is greated than a.");
    } else
    
    // For Loop
    for (i = a; i <=b; i++,a++){
      sum = sum + a;
    }  
    System.out.println("The sum of the range is: " + sum);
  }
}


