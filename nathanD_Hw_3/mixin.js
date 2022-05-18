export class Breakfast {
    constructor(foo) {
        this._foo = foo;
    }
}
export class Smoothie extends Strawberry
{
    constructor(foo, calories, size, color, blenderOK,smoothieType) {
        super(foo, calories, size, color);
        this._blenderOK = blenderOK;
        this._smoothieType = smoothieType;
    }
}
function mixin(target, ...src) {
    for (let mixed of src) {
        for (var property of Object.getOwnPropertyNames(mixed.prototype)) {
            if (property != 'constructor') {
                target.prototype[property] = mixed.prototype[property]
            }
        }
    }
}
export class Strawberry extends Breakfast {
    constructor(foo, calories, size, color) {
        super(foo);
        this._calories = null;
        this.calories = calories;
        this._size = null;
        this.size = size;
        this._color = null;
        this.color = color; 
    }

    get calories() {
        return this._calories;
    }

    set calories(value) {
            this._calories = value;
    }
    get size() {
        return this._size;
    }

    set size(value) {
            this._size = value;
    }

    get color() {
        return this._color;
    }

    set color(value) {
            this._color = value;
    }
    compatible(banana) {
        return this.color >= banana.consumption
            && this.opposite == banana.size;
    }
}

// Mix In
export class Blender extends Breakfast {
    get blenderOK() {
        return this._blenderOK;
    }
    stop() {
        this._blenderOK = false;
    }
    start() {
        this._blenderOK = true;
    }
}

mixin(Smoothie,Blender);


let myBlender = new Smoothie("Fruit",10,"large","Red",true,"Bannana Strawberry");

myBlender.start();

myBlender.blenderOK

console.log(`myBlender is Smoothie: ${myBlender instanceof Smoothie}`);
console.log(`myBlender is Strawberry: ${myBlender instanceof Strawberry}`);
console.log(`myBlender is Breakfast: ${myBlender instanceof Breakfast}`);
console.log(`myBlender is Blender: ${myBlender instanceof Blender}`);


export default {
    Strawberry,
    Blender,
    Smoothie
}