 // Comment
 console.log('hello world');

 let name = 'Mosh';
 console.log(name);

 // Should be meaningful, cannot be a reserved keyword, cannot start with a number, cannot containt a space of hyphen
 // case-sensitive 

 let firstName;
 let FirstName;
 let fiRstName = 'Mosh';
 let lastName = 'Hamedani';
 console.log(lastName);


 let interestRate = 0.3;
 interestRate = 1;
 console.log(interestRate);
// teve o valor alterado


 const interestrate = 1.2;
 console.log(interestRate);
 // nao pode ter seu valor alterado futuramente 


 let name1 = 'mosh' // String literal
 let age = 30; // Number Literal
 let isApproved = true; // Boolean Literal
 let firsstName; // undefined
 let firstNamee = undefined;
 let lastname = null;

 // reference types: object, array, function

// object
 let person = {
    name: 'rayssa',
    age: 18
 };
// Dot notation
person.name = 'Jonh';
person.age = 19;
// Bracket Notation (propridade entre aspas dentro de colchete igual a valor novo)
let selection = 'name';
person['name'] = 'Mary';
person[selection] = 'any';
console.log(person.name);
console.log(person);

//array (array is dinamic)
let selectedColors = ['red', 'blue', 'yellow'];
selectedColors[3] = 'Green';
console.log(selectedColors[0]);
console.log(selectedColors);
console.log(selectedColors.length); // existem outras funçoes q podem ser chamadas junto de uma array

// functions(performa tasks)

function greet() {
    console.log('hello world');
}
function greet() {
    return 1 + 1;
}
function greet(num1, num2) {
    console.log(num1 * num2);
}
greet(6,9);

function x(abc){
    return abc * abc ;
}
let number = x(27);
console.log(number);
console.log(x(10));
