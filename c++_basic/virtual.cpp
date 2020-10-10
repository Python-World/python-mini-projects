#include<bits/stdc++.h>
using namespace std;

class A{
	int a,b;
public:
	void setdata(int a, int b){
		a = a,b = b;
	}
	virtual void display(){
		cout<<"hi"<<"a";
	}
	
};

class B: public A{
private:
	int a,b;
public:
	void display(){
		cout<<"hello";
	}
};

int main(){
	A *p;
	B obj2;
	p = &obj2;
	//It should be of A class;
	p->display();
}