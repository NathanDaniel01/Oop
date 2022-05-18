  function Boat(brand,  length, id, capacity) {
    this.brand = brand;
    this.length = length;
    this.id = id;
    this.capacity = capacity;
    this.getBrand = function() {
      return this.brand;
    };
    this.setBrand = function(brand) {
      this.brand = brand;
    };
    this.getLength = function() {
      return this.length;
    };
    this.setLength = function(length){
      this.length = length;;
    };
    this.getId = function() {
      return this.id;
    };
    this.setId = function(id){
      this.id = id;
    };
    this.getCapacity = function() {
      return this.capacity;
    };
    this.setCapacity = function(capacity){
      this.capacity = capacity;
    };
  
  }
  
function main(){
    const boat1 = new Boat("NRS",13.0,0001,7);
    console.log("Brand:    should be NRS    And we got: " + boat1.getBrand());
    boat1.setBrand("Hyside");
    console.log("Brand:    should be Hyside And we got: " + boat1.getBrand());
    console.log("Length:   should be 13.0   And we got: " + boat1.getLength());
    console.log("Id:       should be 1      And we got: " + boat1.getId());
    console.log("Capacity: should be 7      And we got: " + boat1.getCapacity());
}
main();
