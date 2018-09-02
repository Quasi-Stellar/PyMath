#include <iostream>
#include <cmath>

using namespace std;
int main() {
 	int option;
  	bool loopController = true;
  	while(loopController == true){
  		cout << "Please choose your option:\n";
 		cout << "\t 1) Addition\n";
  		cout << "\t 2) Subtraction\n";
  		cout << "\t 3) Multiplication\n";
  		cout << "\t 4) Division\n";
  		cout << "\t 5) Square\n";
  		cout << "\t 6) Square Root\n";
  		cout << "\t 7) Modulus\n";
  		cout << "\t 8) Quadratic Roots\n";

  		cin >> option;
  		if (option <= 8 && option >= 1){
  			if (option == 1){
    			double a,b;
    			cout << "Enter two numbers to add. \n";
  				cin >> a >> b;
  				cin >> b;
    			double sum = a+b;
    			cout << "The sum is: " << sum << "\n";
  			} else if (option == 2){
    			double a,b;
    			cout << "Enter two numbers to subtract. \n";
  				cin >> a >> b;
  				cin >> b;
    			double difference = a-b;
    			cout << "The difference is: " << difference << "\n";
  			} else if (option == 3){
    			double a,b;
    			cout << "Enter two numbers to multiply. \n";
  				cin >> a >> b;
  				cin >> b;
    			double product = a*b;
    			cout << "The product is: " << product << "\n";
  			} else if (option == 4){
    			double a,b;
  				cout <<"Enter two numbers to divide. \n";
    			cin >> a >> b;
    			double quotient = a/b;
    			cout << "The answer is: "<< quotient <<"\n";
  			} else if (option == 5){
    			double sideLength;
 				double area;
  				double perimeter;
   				cout << "Enter a side length or number you would like to square.\n";
  				cin >> sideLength;
    			// Following line requires ``#include <cmath>``. Squares double. 
    			area = ((double)pow(sideLength,2));
    			perimeter = ((double)sideLength*4);
    			char esc_char = 27;
    			cout <<"Area: " << area << " Perimeter: " << perimeter << "\n";
    			cout <<"\n";
 	 		} else if (option == 6){
   				double a;
   				cout << "Enter a number to take the square root of \n";
    			cin >> a;
    			double rootA = sqrt(a);
    			cout << "The answer is: " << rootA << "\n";
   			} else if (option == 7){
  				int a,b;
  				cout <<"Enter two numbers to divide (modulus). \n";
    			cin >> a >> b;
  	 			int modulus = a%b;
    			int num = a/b;
  	 			cout << "The modulus is: "<< num << "R" << modulus <<"\n";
 	 		} else if (option == 8){
   				double a,b,c;
    			cout << "Enter the value of the coefficients a, b and c.\n";
    			cin >>a>>b>>c;
   				if (a==0.0){
     				cout <<"Undefined \n";
  					return 1;
     	 	}
      			// Quadratic Formula Finder
  				double x1, x2;
    			x1 =(-b + sqrt((b*b) - 4*a*c))/(2*a);
    			x2 =(-b - sqrt((b*b) - 4*a*c))/(2*a); 
   				cout <<"The roots are x1 = " << x1 << " and x2 = " << x2 << "\n \n";
		 }
	

  			} else if (option > 8 || option < 1){
    			loopController = false;
          		int helpPrompt;
      			cout << "ERROR 1: Invalid option. For help type in 1, to skip this help prompt type in 0.\n";
        		cin >> helpPrompt;
      			if (helpPrompt == 1){
          			cout << "Please enter a number between 1 and 8. \n \n";
        		} else if (helpPrompt == 0){
          			cout << "Thank you for your input! \n \n";
        	}
    }
  }  
}
