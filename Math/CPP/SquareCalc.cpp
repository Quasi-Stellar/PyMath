#include <iostream>
#include <cmath>

using namespace std;
int main() {
    for( ; ; ) {


		double sideLength;
  
 	 	double area;
  		double perimeter;
  	
      	std::cout << "Please enter the square's side length.\n";
  		std::cin >> sideLength;
        
      	// Following line requires ``#include <cmath>``. Squares double. 
      	area = ((double)pow(sideLength,2));
      	perimeter = ((double)sideLength*4);
      	char esc_char = 27;
      	cout <<"Area: " << area << " Perimeter: " << perimeter << "\n";
      	cout <<"\n";

  }
}
