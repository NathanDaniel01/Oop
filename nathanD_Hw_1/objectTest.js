import{boat} from "./object.mjs"

const myBoat = new boat("NRS",13.0,0001,7);

console.assert(myBoat.brand == "NRS", "Failed Brand");
console.assert(myBoat.length == 13.0, "Failed length");
console.assert(myBoat.capacity == 7, "Failed Capasity");

