class Rectangle {
    //used to setup your object
    constructor (_height, _width, _color) {
        console.log("The Rectangle is being created");
        this.width = _width;
        this.height = _height;
        this.color = _color;
    }

    getArea() {
        return this.width * this.height;
    }

    printDescription() {
        console.log(`I am a rectangle of ${this.width} x ${this.height} and I have an area of ${this.getArea()}`);
    }
}


class Square {
    constructor(_width) {
        this.width = _width;
        this.height = _width;
        this.numOfRequestsForArea = 0;
    }
    get area() {
        this.numOfRequestsForArea ++
        return this.width**2;
    }
    
    set area(num) {
        this.width = Math.sqrt(num);
    }

    //Static Method use the class as its base, not any particular object
    static equals (a, b) {
        return a.width**2 == b.width**2;
    }

    static isValidDimensions (width, height) {
        return width === height;
    }
}

let square1 = new Square(8);
let square2 = new Square(25);

//          see here we do square.equals because its a class method, not object method
console.log(Square.equals(square1, square2));

console.log(Square.isValidDimensions(8,8))



class Person {
    constructor (_name, _age){
        this.name = _name;
        this.age = _age;
    }

    describe() {
        console.log(`I am ${this.name} and I am ${this.age} years old.`);
    }
}
// use extends for inheritence. In this case, class Programmer all the stuff from Person
class Programmer extends Person {
    constructor (_name, _age, yearsExperience) {
        //super calls the this.x functions of the parent calss
        super(_name, _age)
        //Custom Behaviors
        this.yearsOfExperience = yearsExperience
    }

    code() {
        console.log(`${this.name} is coding.`);
    }
}

let person1 = new Person('Jeff', 45);
let programmer1 = new Programmer('Kevin', 25, 2);
programmer1.describe();
programmer1.code();

const programmers = [
    new Programmer('Ryan', 25, 2),
    new Programmer('Alex', 61, 12),
    new Programmer('Samantha', 23, 5),
    new Programmer('Ryan', 42, 7)

];


function developSoftware(progammers) {
    //Develop software
    for (let programmer of programmers) {
         programmer.code()
    }
}

developSoftware(programmers);