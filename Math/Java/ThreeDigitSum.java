import java.util.Scanner;
class ThreeDigitSum {
  public static void main(String[] args) {
  	Scanner sc = new Scanner(System.in);
    
    System.out.println("Please enter a three digit number.");
    String input = sc.nextLine();
    int num = Integer.parseInt(input);
    
    int a = num/100;
  	int answer1 = num-a*100;
    int b = answer1/10;
    int c = num%10;
    int sum = a+b+c;
    System.out.println("The sum of your three digits is " + sum);
  }
}

