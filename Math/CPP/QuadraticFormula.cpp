#include <iostream>
#include <cmath>

using namespace std;

int main() {
 	for( ; ; ) {
  		double a,b,c;
 	
  		// Gets coefficients
  		cout <<"Enter the coefficients starting with a then b then c \n";
		cin>>a>>b>>c;
  
 	 	if (a==0.0){
     		cout <<"Undefined \n";
  			return 1;
      }
      	// Quadratic Formula Finder
  		double x1, x2;
    	x1 =(-b + sqrt((b*b) - 4*a*c))/(2*a);
    	x2 =(-b - sqrt((b*b) - 4*a*c))/(2*a); 
   		cout <<"The roots are <>x1</b> = " << x1 << " and x2 = " << x2 << "\n \n";
   }
}
