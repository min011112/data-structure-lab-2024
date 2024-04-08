#pragma once
#include <iostream>

class Rectangle {
private:
	double width;
	double height;
public:
	Rectangle(double w, double h) {
		width = w;
		height = h;
	}

	double getArea() {
		return width * height;
	}
	double getPerimeter() {
		return 2 * (width + height);
	}
	bool isSquare() {
		return(width == height);  //정사각형이면  true 반환/아니면  false 반환
	}
};