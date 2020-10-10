#include<bits/stdc++.h>
using namespace std;

class A
{
	int a;
public:
	virtual  void fun(){
		cout<<"I am in A";
	}
	virtual  void fun1(){
		cout<<"I am in A";
	}
};
class B: public A{
	//int b;
public:
	void fun(){

	}
	void fun1(){

	}
};


int main(){
	A o1;
	B o2;
	cout<<sizeof(o1)<<" "<<sizeof(o2);
	return 0;
}