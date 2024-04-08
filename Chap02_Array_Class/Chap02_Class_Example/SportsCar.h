#pragma once
#include "Car.h"

class SportsCar : public Car
{
public:
	bool bTurbo; //boolÇü½ÄÀº TRUE/FALSE
	void setTurbo(bool bTur) { 
		bTurbo = bTur; 
	}
	void speedUp() {
		if (bTurbo) speed += 20;
		else Car::speedup();
	}
};
