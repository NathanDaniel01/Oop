#include <iostream>
#include <string> 
using namespace std;
/*
Idea:
         Car
       /     \
      /       \
  Electric    Gas
      \       /
       \     /
       Hybrid
*/
class Car
{
  public:
    string make;
    int year;
    Car()
    {
      cout << "Car" <<endl;
    }
    virtual ~Car() { cout << "~Car()" << endl; }
};

class Electric : virtual public Car
{
  public:
    bool isElectric;
    Electric(){ cout << "electric boogaloo" << endl; } 
   
    virtual ~Electric() { cout << "~Electric()" << endl; }
};
class Gasoline : virtual public Car
{
  public:
    string fuelType;
    Gasoline(){ cout << "Gasoline" << endl; } 
    virtual string SfuelType() const{return fuelType;}
    virtual void SfuelType(const string &value ){ fuelType = fuelType; }
    virtual ~Gasoline() { cout << "~Gasoline()" << endl; }
};
class Hybrid : public Electric , public Gasoline
{
  public:
    Hybrid(bool isElectric, string fuelType, string make, int year) 
    { 
        Electric();
        Gasoline();
        cout << "Hybrid" << endl; 
    }
    ~Hybrid() { cout << "~Hybrid()" << endl; }
};
void maintwo()
{
  Hybrid Hybrid(true, "Diesle", "ford", 2001);
}
int main() 
{
  maintwo();
  return 0;
}