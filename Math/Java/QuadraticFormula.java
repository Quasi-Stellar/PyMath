import java.util.Scanner;

class QuadraticForumla {
  public static void main(String[] args) {
  	Scanner sc = new Scanner(System.in);
	
    System.out.println("Please enter your coefficient for a");
    String input = sc.nextLine();
    double a = Integer.parseInt(input);
    if (a == 0){
    	System.out.println("Undefined");
	
    } else {
	  
    System.out.println("Please enter your coefficient for b");
    input = sc.nextLine();
    double b = Integer.parseInt(input);
        
    System.out.println("Please enter your coefficient for c");
    input = sc.nextLine();
    double c = Integer.parseInt(input);
    
    double x1, x2;
    x1 =(-b + Math.sqrt((b*b) - 4*a*c))/(2*a);
    x2 =(-b - Math.sqrt((b*b) - 4*a*c))/(2*a);
    
    System.out.println("The roots are x1: " + x1 + " and x2: " + x2);
    }
  }
}

