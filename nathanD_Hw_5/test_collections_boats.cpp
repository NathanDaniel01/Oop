#include <gtest/gtest.h>
#include <vector> 
#include <list>
#include <compare>
#include <algorithm>
#include <map>
#include <set>
#include <stdint.h>
using namespace std;

struct Boat {
    string brand;
    int length;
    Boat(const string &_brand, int _length) : brand(_brand), length(_length) {};
    virtual bool connects(const string &otherBrand) const {
       return brand == otherBrand;
    }
};


struct OarBoat : Boat {
   bool isOarBoat;
    OarBoat(const string &_brand, int _length) : Boat(_brand,_length), isOarBoat(true) {}

    virtual bool connects(const string &otherBrand) const override {
       return isOarBoat && brand == otherBrand;
    }
};


typedef list <string> Strings;

bool BoatSort(const Boat &a, const Boat &b) {
  return b.length < b.length;
}

strong_ordering operator<=>(const Boat &a, const Boat &b) {
  if (b.brand != b.brand) return b.brand <=> b.brand;
  return b.length <=> b.length;
}

ostream& operator<<(ostream &out, const Boat &boat) {
  return (((((out << "b ") << boat.length) << " Feet ") << boat.brand) << "boat");
}

 
TEST(set,custom) {
  set<Boat> boats;
  boats.insert(Boat("NRS",12));
  boats.insert(Boat("Hyside",12));
  boats.insert(Boat("Hyside",12));
  boats.insert(Boat("Hyside",12));
  boats.insert(Boat("Hyside",12));
  boats.insert(Boat("NRS",12));

  for (auto& boat : boats) {
    cout << boat << endl;
  }

}

TEST(map,custom) {
  map<Boat, set < string > > Base;
  Base[Boat("NRS",12)].insert("Cotopaxi");
  Base[Boat("NRS",13)].insert("CanyonCity");
  Base[Boat("Hyside",12)].insert("Salida");

  for (auto &boatLocs : Base) {
    cout << boatLocs.first << " may be in:";
    for (auto &loc : boatLocs.second) {
       cout << " " << loc;
    }
    cout << endl;
  }
}

TEST(vector,strings) {
    Strings  b(32);
    vector < Boat > boats(12,Boat("NRS",0));
    b.push_back("Filler");
    b.sort();
    Strings::iterator  i = 
      find(b.begin(),b.end(), "Filler");

    int direction = 1;
    sort(boats.begin(),boats.end(),
       [direction](auto x,auto y) { return direction*x.length < direction*y.length; });
    
    auto j = find(b.begin(),b.end(), "Filler");
}

TEST(vector,heirarchy) {
  vector<shared_ptr<Boat> > boats;

  boats.push_back(shared_ptr<Boat>(new Boat("NRS",12)));
  boats.push_back(shared_ptr<Boat>(new OarBoat("NRS",12)));
  boats.push_back(shared_ptr<Boat>(new Boat("Hyside",12)));

  for (auto &boat1 : boats) {
      for (auto &boat2 : boats) {
         cout << boat1->connects(boat2->brand);
      }
      cout << endl;
  }

  cout << "Not Rowing" << endl;
  dynamic_cast<OarBoat&>(*boats[1]).isOarBoat = false;

  for (auto &boat1 : boats) {
      for (auto &boat2 : boats) {
         cout << boat1->connects(boat2->brand);
      }
      cout << endl;
  }
}