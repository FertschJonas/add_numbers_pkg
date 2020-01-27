#include "addnumbers.h"
#include <iostream>
#include <stdlib.h>

using namespace std;
int main(int argc, char * argv[]) {
	double a, b;
	if (argc ==3) {
		a = std::strtod(argv[1], nullptr); 
		b = std::strtod(argv[2], nullptr);
	}
	else {
		a = 5;
		b = 5;
	}
	for (int i = 0; i < argc; i++) {
		std::cout << "Argument " << i << " = " << argv[i] << std::endl;
	}
	std::cout << "Test des Packages:" << a << " + " << b << " = " << add_numbers(a, b) << std::endl;
	return 0;
}