function ValidateEmail(email) {
  if (
    /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(
      email
    )
  ) {
    return true;
  }

  return false;
}

document.getElementById("regForm").addEventListener("submit", function (event) {
  event.preventDefault();

  let firstName = document.getElementById("firstName").value;
  let lastName = document.getElementById("lastName").value;
  let mobile = document.getElementById("mobile").value;
  let email = document.getElementById("email").value;
  let address = document.getElementById("address").value;
  let city = document.getElementById("city").value;
  let state = document.getElementById("state").value;

  let firstNameError = document.getElementById("firstNameError");
  let lastNameError = document.getElementById("lastNameError");
  let mobileError = document.getElementById("mobileError");
  let emailError = document.getElementById("emailError");
  let addressError = document.getElementById("addressError");
  let cityError = document.getElementById("cityError");
  let stateError = document.getElementById("stateError");

  firstNameError.classList.add("hide");
  lastNameError.classList.add("hide");
  mobileError.classList.add("hide");
  emailError.classList.add("hide");
  addressError.classList.add("hide");
  cityError.classList.add("hide");
  stateError.classList.add("hide");

  if (firstName === "") {
    firstNameError.textContent = "First Name is required.";
    firstNameError.classList.remove("hide");
  }

  if (lastName === "") {
    lastNameError.textContent = "Last Name is required.";
    lastNameError.classList.remove("hide");
  }

  if (mobile === "") {
    mobileError.textContent = "Mobile is required.";
    mobileError.classList.remove("hide");
  }

  if (email === "") {
    emailError.textContent = "Email is required.";
    emailError.classList.remove("hide");
  } else {
    if (!ValidateEmail(email)) {
      emailError.textContent = "Email is invalid.";
      emailError.classList.remove("hide");
    }
  }

  if (address === "") {
    addressError.textContent = "Address is required.";
    addressError.classList.remove("hide");
  }

  if (city === "") {
    cityError.textContent = "City is required.";
    cityError.classList.remove("hide");
  }

  if (state === "") {
    stateError.textContent = "State is required.";
    stateError.classList.remove("hide");
  }

  console.log(firstName, lastName, mobile, address, city, state);
});

// function submitForm(elem) {
//   console.log(elem);
//   return false;
// }
