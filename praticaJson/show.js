// JSON = (JavaScript Object Notation) data -interchange format
//          Used for exchanging data between a server and a web application
//          JSON files {key:value} OR [value1, value2, value3]

//          JSON.stringify() = converts a JS obect to a JSON string
//          JSON.parse() = converts a JSON string to a JS object

const person = {
    "name": "Spongebob",
    "age": 30,
    "isEmployed": true,
    "hobbies": ["karate", "pesca", "luta"]
}

const jsonperson = `{
    "name": "Spongebob",
    "age": 30,
    "isEmployed": true,
    "hobbies": ["karate", "pesca", "luta"]
}`

// convertendo objeto JavaScript pra JSON string 
const jsonString = JSON.stringify(person)
console.log(person);

// convertendo String JSON pra JavaScript 
const jsonpraJs = JSON.parse(jsonperson)
console.log(jsonpraJs)

// A tecla [] possui o assento `` para transformar um objeto JS em JSON string. 

// fetch = buscar
fetch("persons.js")
    .then(Response => Response.json())
    .then(value  => console.log(value))