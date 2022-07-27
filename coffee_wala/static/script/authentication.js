// Registration Validation
function loginValidation() {
    //Get the data
    const sic_number = document.getElementById("sic_number").value;
    const password1 = document.getElementById("password1").value;

    //Call the functions
    if (!sic_numberValidation(sic_number) | !password1Validation(password1)) {
        return false;
    }
}


// Registration Validation
function registrationValidation() {
    //Get the data
    const first_name = document.getElementById("first_name").value;
    const last_name = document.getElementById("last_name").value;
    const sic_number = document.getElementById("sic_number").value;
    const email = document.getElementById("email").value;
    const password1 = document.getElementById("password1").value;
    const password2 = document.getElementById("password2").value;

    //Call the functions
    if (!first_nameValidation(first_name) | !last_nameValidation(last_name) | !sic_numberValidation(sic_number) | !emailValidation(email) | !password1Validation(password1) | !password2Validation(password2, password1)) {
        return false;
    }
}


// Functions
function first_nameValidation(first_name) {
    if (first_name === "") {
        document.getElementById("first_name_error").innerHTML = "Field can't be empty";
        return false;
    } else {
        document.getElementById("first_name_error").innerHTML = "";
        return true;
    }
}

function last_nameValidation(last_name) {
    if (last_name === "") {
        document.getElementById("last_name_error").innerHTML = "Field can't be empty";
        return false;
    } else {
        document.getElementById("last_name_error").innerHTML = "";
        return true;
    }
}

function sic_numberValidation(sic_number) {
    if (sic_number === "") {
        document.getElementById("sic_number_error").innerHTML = "Field can't be empty";
        return false;
    } else if (sic_number.length != 8) {
        document.getElementById("sic_number_error").innerHTML = "Invalid SIC Number";
        return false;
    } else {
        document.getElementById("sic_number_error").innerHTML = "";
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


function password1Validation(password1) {
    if (password1 === "") {
        document.getElementById("password1_error").innerHTML = "Password can't be empty ";
        return false;
    } else if (password1.length <= 8) {
        document.getElementById("password1_error").innerHTML = "Password is too short";
        return false;
    } else if (!password1.match(/[a-z]/)) {
        document.getElementById("password1_error").innerHTML = "Password must contain a lowercase letter";
        return false;
    } else if (!password1.match(/[A-Z]/)) {
        document.getElementById("password1_error").innerHTML = "Password must contain a uppercase letter";
        return false;
    } else if (!password1.match(/[0-9]/)) {
        document.getElementById("password1_error").innerHTML = "Password must contain a number";
        return false;
    } else if (!password1.match(/[@,#,$,%]/)) {
        document.getElementById("password1_error").innerHTML = "Password must contain a special letter";
        return false;
    } else {
        document.getElementById("password1_error").innerHTML = "";
        return true;
    }
}

function password2Validation(password2, password1) {
    if (password2 === "") {
        document.getElementById("password2_error").innerHTML = "Field can't be empty";
        return false;
    }
    else if (password2 != password1) {
        document.getElementById("password2_error").innerHTML = "Both password doesn't match";
        return false;
    } else {
        document.getElementById("password2_error").innerHTML = "";
        return true;
    }
}