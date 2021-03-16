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

  {
    name: "Mohit",
    designation: "Junior Developer",
    salary: 15000,
    address: {
      address_ln1: "13, Jaitpur",
      city: "New Delhi",
      state: "Delhi",
      pincode: 110101,
    },
  },

  {
    name: "Gaurav",
    designation: "Junior Developer",
    salary: 10000,
    address: {
      address_ln1: "13, Jaitpur",
      city: "New Delhi",
      state: "Delhi",
      pincode: 110101,
    },
  },

  {
    name: "Rajan",
    designation: "Junior Developer",
    salary: 10000,
    address: {
      address_ln1: "13, Jaitpur",
      city: "New Delhi",
      state: "Delhi",
      pincode: 110101,
    },
  },

  {
    name: "Teju",
    designation: "Junior Developer",
    salary: 30000,
    address: {
      address_ln1: "14, Jaitpur",
      city: "New Delhi",
      state: "Delhi",
      pincode: 110101,
    },
  },
];

// let jsonString = JSON.stringify(objArray);
// let jsonObject = JSON.parse(jsonString);

// let jsonString = `[{"name":"John","designation":"Developer","salary":25000,"address":{"address_ln1":"11, Jaitpur","city":"New Delhi","state":"Delhi","pincode":110101}},{"name":"Alex","designation":"Developer","salary":35000,"address":{"address_ln1":"12, Jaitpur","city":"New Delhi","state":"Delhi","pincode":110101}}]`;

// let jsonObject = JSON.parse(jsonString);
// console.log(jsonObject[0].name);

// console.log(JSON.stringify(objArray));

// old method
// for (let i = 0; i < objArray.length; i++) {
//   console.log(objArray[i].name);
//   console.log(objArray[i].address.city);
// }

// es method
// objArray.forEach(function (obj, index) {
//   console.log(obj.name);
// });

// objArray.forEach((obj) => {
//   console.log(obj.name);
// });

// objArray = objArray.map(function (obj, index) {
//   obj.salary = 50000;
//   return obj;
// });

// objArray = objArray.filter(function (obj) {
//   if (obj.salary > 10000) {
//     return obj;
//   }
// });

console.log(objArray);
