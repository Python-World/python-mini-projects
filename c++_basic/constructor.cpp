#include<bits/stdc++.h>
using namespace std;

class A{
  private:
	int a,b;
  public:
  	A(){

  	}
  	A(int x, int y){
  		a = x;
  		b = y;
  	}
  	void show(){
  		cout<<a<<" "<<b<<endl;
  	}
};


int main(){
	A *a1 = new A[10];
	for(int i=0;i<10;i++){
		a1[i] = A(3,4);
	}
	a1[0].show();
	A a2(4,5);
	a2.show();
}