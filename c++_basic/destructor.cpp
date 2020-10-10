#include<bits/stdc++.h>
using namespace std;


class A{
	int *a;
public:
	A(){
		a = new int;
		*a = 4;
		cout<<*a<<endl;
	}
	void show(){
		cout<<*a;
	}
	~A(){
		delete a;
		cout<<"hello";
	}
};



int main(){
	//In this destructir is not called when memory is created using new keyword then one need to delete it using delete keyword
	A *a= new A;
	a->show();
	delete a;
	a->show();
}