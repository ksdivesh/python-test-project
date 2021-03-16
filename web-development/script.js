let inputCtrl = document.querySelector("#firstName");
// let inputCtrl = document.getElementById("firstName");
console.log(inputCtrl.value);
inputCtrl.value = "Mahendra";

// var divTag = document.querySelector("div");
// console.log(divTag);

var divTags = document.querySelectorAll("div");

// for (var i = 0; i < divTags.length; i++) {
//     console.log(divTags[i]);
// }

// divTags.forEach(function (div, index) {
//     console.log(div);
// });

divTags.forEach((div, index) => {
  // let heading = div.querySelector("h1");
  // heading.textContent = "Test Content " + index;

  // var elem = "<h2>Test heading 2</h2><p>sdfasdfasdfasdfasd sadfasdfasdf</p>";
  // div.innerHTML = elem;

  div.innerHTML = "";

  let elem = document.createElement("h2");
  elem.classList.add("test-heading", "test-heading-2");
  elem.setAttribute("id", "heading-" + index);
  elem.textContent = "Heading 2 " + index;

  div.appendChild(elem);
});

// const sum = (a, b) => {
//     return a + b;
// }

// function sum(a, b) {
//     return a + b;
// }

// var a = 10;
// var b = 20;

// console.log('sum is  ', sum(a, b));

document.querySelector("#idfjdf");
document.querySelector(".test-classs");
document.querySelectorAll(".test-class"); //return array
document.querySelectorAll("div"); //return array

//ES6 Module
document.getElementsByClassName("test-class"); //return array
document.getElementById("test-id"); //single element
document.getElementsByName("div"); //multile elements

// Class declaration
class Product {
  constructor(name, qty, price) {
    this.name = name;
    this.qty = qty;
    this.price = price;
  }

  create() {
    console.log(this.name, this.qty, this.price);
  }
}

const product = new Product("T-shirt", 10, 100);
console.log(product.name);
product.create();
// end of class

//funtion declaration

//old fashion
function createProduct(name, price) {
  let tax = 10; //scope is inside the function
}

//es6 module
const createProduct2 = (name, price) => {};

createProduct2("T-shirt", 1000);

/*
var => variable declaration 
let => variable declaration | scope limited to function 
const => constant declaration 
*/

/* Explicit conversion */

let price = "100";
price = parseInt(price);
price = parseFloat(price);

//es6 module
price = +price; //integer conversion

price = price.toString(); //to convert to string

let studentName = "John Doe";
studentName = studentName.toUpperCase();
studentName = studentName.toLowerCase();

//objects in javascript

let obj = {
  name: "John",
  designation: "Developer",
  salary: 25000,
  address: {
    address_ln1: "11, Jaitpur",
    city: "New Delhi",
    state: "Delhi",
    pincode: 110101,
  },
};

console.log(obj.name);
console.log(obj.address.city);

//array of objects
// let objArray = ["product1", "product2"];
let objArray = [
  {
    name: "John",
    designation: "Developer",
    salary: 25000,
    address: {
      address_ln1: "11, Jaitpur",
      city: "New Delhi",
      state: "Delhi",
      pincode: 110101,
    },
  },
  {
    name: "Alex",
    designation: "Developer",
    salary: 35000,
    address: {
      address_ln1: "12, Jaitpur",
      city: "New Delhi",
      state: "Delhi",
      pincode: 110101,
    },
  },
];

// let objArray = [obj1, obj2]

objArray[1].name;
objArray[0].address.city;

// JSON : Javascript Object Notation
//used to data transfer


let jsonString =  {
    "name": "Alex",
    "designation": "Developer",
    "salary": 35000,
    "address": {
      "address_ln1": "12, Jaitpur",
      "city": "New Delhi",
      "state": "Delhi",
      "pincode": 110101,
    },
  },