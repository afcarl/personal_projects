#include <iostream>
using namespace std;

void Printing()
{
  cout << "Printing stuff\n";
}

int adder(int x,int y)
{
  return x + y;
}

int main()
{
  int x,y;
  Printing();
  cout << "Input x: ";
  cin >> x;
  cout << "Input y: ";
  cin >> y;
  cout << adder(x,y) << endl;
  return 0;
}
