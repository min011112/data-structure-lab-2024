#include "complex.h"
void main()
{
	Complex a, b, c;
	a.read("A =");
	b.read("B =");
	c.add(a, b);
	a.print("A = ");
	b.print("A = ");
	c.print("A+B = ");
}