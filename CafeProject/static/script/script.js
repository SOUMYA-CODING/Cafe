//For Registration page validation
function formvalidation() {
    //Get the data
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const phone_number = document.getElementById("phone_number").value;
    const message = document.getElementById("message").value;

    //Call the functions
    if (!nameValidation(name) | !emailValidation(email) | !phonenumberValidation(phone_number) | !messageValidation(message)) {
        return false;
    }
}

function nameValidation(name) {
    if (name === "") {
        document.getElementById("name_error").innerHTML = "Field can't be empty";
        return false;
    } else {
        document.getElementById("name_error").innerHTML = "";
        return true;
    }
}

function emailValidation(email) {
    let mailFormat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (email === "") {
        document.getElementById("email_error").innerHTML = "Field can't be empty";
        return false;
    } else if (!email.match(mailFormat)) {
        document.getElementById("email_error").innerHTML = "Please enter correct email address";
        return false;
    } else {
        document.getElementById("email_error").innerHTML = "";
        return true;
    }
}

function phonenumberValidation(phone_number) {
    if (phone_number === "") {
        document.getElementById("phone_error").innerHTML = "Field can't be empty";
        return false;
    } else if (phone_number.length != 10) {
        document.getElementById("phone_error").innerHTML = "Invalid Phone Number";
        return false;
    } else {
        document.getElementById("phone_error").innerHTML = "";
        return true;
    }
}

function messageValidation(message) {
    if (message === "") {
        document.getElementById("message_error").innerHTML = "Field can't be empty";
        return false;
    } else {
        document.getElementById("message_error").innerHTML = "";
        return true;
    }
}