// Contact Form Validation
function formvalidation() {
    // Get the data
    const name = document.getElementById("name").value;
    const phone_number = document.getElementById("phone_number").value;
    const email = document.getElementById("email").value;
    //const comment = document.getElementById("message").value;

    // Call the function
    if (!nameValidation(name) | !phone_numberValidation(phone_number) | !emailValidation(email)) {
        return false;
    }
}

// Functions
function nameValidation(name) {
    if (name === "") {
        document.getElementById("name_error").innerHTML = "Field can't be empty";
        return false;
    } else {
        document.getElementById("name_error").innerHTML = "";
        return true;
    }
}

function phone_numberValidation(phone_number) {
    if (phone_number === "") {
        document.getElementById("phone_number_error").innerHTML = "Field can't be empty";
        return false;
    } else if (phone_number.length != 10) {
        document.getElementById("phone_number_error").innerHTML = "Invalid phone number";
        return false;
    } else {
        document.getElementById("phone_number_error").innerHTML = "";
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
/*
function messageValidation(comment) {
    if (comment === "") {
        document.getElementById("message_error").innerHTML = "Field can't be empty";
        return false;
    } else {
        document.getElementById("message_error").innerHTML = "";
        return true;
    }
}
*/