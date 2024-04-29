#pragma once

struct Location2D {
	int row;
	int col;

	//structure ������ row�� col 0���� �ʱ�ȭ
	Location2D(int r = 0, int c = 0) {
		row = r;
		col = c;
	 }
	//��ġ p�� �ڽ��� �̿����� �˻��ϴ� �Լ�
	bool isNeighbor(Location2D& p) {
		return((row == p.row && (col == p.col - 1 || col == p.col + 1))
			|| (col == p.col && (row == p.row - 1 || row == p.row + 1)));
	}
	//p�� �ڽŰ� ���� ��ġ������ �˻�(������ �����ε� ���)
	bool operator==(Location2D& p) {
		return row == p.row && col == p.col;
	}
};