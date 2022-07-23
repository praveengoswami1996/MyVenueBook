const profileImageContainer = document.querySelector('.profile-image-container');
const profileImage = document.querySelector('#customerprofileimage');
const file = document.querySelector('#file');

//When user selects an image to upload
file.addEventListener('change',function(){
    const choosedFile = this.files[0];

    if (choosedFile) {
        const reader = new FileReader(); //FileReader is a predefined thing in javascript

        reader.addEventListener('load',function(){
            profileImage.setAttribute('src',reader.result);
        });
        reader.readAsDataURL(choosedFile);
    }
})

function validateEmail(){
    let errorMsgLabel = document.getElementsByClassName('errormsg');
    let emailPattern = /^[a-zA-Z0-9\.-_]+@[a-zA-Z0-9-]+.[a-zA-Z]{2,8}.[a-zA-Z]{2,8}?$/
    let customerEmailField = document.getElementById('customeremail');
    let customerEmail = customerEmailField.value;
    if (!emailPattern.test(customerEmail)){
        customerEmailField.style.border = ".1rem solid red";
        errorMsgLabel[1].innerHTML = "Invalid Email"
        errorMsgLabel[1].style.fontSize = "1.5rem"
        errorMsgLabel[1].style.color = "red";
        errorMsgLabel[1].style.textTransform = "none";
    }
    else{
        customerEmailField.style.border = ".1rem solid green";
        errorMsgLabel[1].innerHTML = "Valid Email"
        errorMsgLabel[1].style.fontSize = "1.5rem"
        errorMsgLabel[1].style.color = "green";
        errorMsgLabel[1].style.textTransform = "none";
    }
}
function validateUsername(){
    //Customer Username Field Validation
    let errorMsgLabel = document.getElementsByClassName('errormsg');
    let usernamePattern = /^[a-zA-Z0-9\._@-]{8,16}$/
    let customerUsernameField = document.getElementById('customerusername');
    let customerUsername = customerUsernameField.value;
    if (usernamePattern.test(customerUsername)){
        customerUsernameField.style.border = ".1rem solid green";
        errorMsgLabel[7].innerHTML = "Valid username format"
        errorMsgLabel[7].style.fontSize = "1.5rem"
        errorMsgLabel[7].style.color = "green";
        errorMsgLabel[7].style.textTransform = "none";
    }
    else{
        customerUsernameField.style.border = ".1rem solid red";
        errorMsgLabel[7].innerHTML = "Invalid username format"
        errorMsgLabel[7].style.fontSize = "1.5rem"
        errorMsgLabel[7].style.color = "red";
        errorMsgLabel[7].style.textTransform = "none";
    }
}

function validateForm(){
    let returnValue = true;
    let errorMsgLabel = document.getElementsByClassName('errormsg');

    //Customer Name Field Validation
    let customerNameField = document.getElementById('customername');
    let customerName = customerNameField.value.trim();
    if (customerName == '' || customerName == null){
        customerNameField.style.border = ".1rem solid red";
        errorMsgLabel[0].innerHTML = "***Name cannot have only spaces."
        errorMsgLabel[0].style.fontSize = "1.5rem"
        errorMsgLabel[0].style.color = "red";
        errorMsgLabel[0].style.textTransform = "none";
        returnValue = false;
    }

    //Customer Email Field Validation
    let emailPattern = /^[a-zA-Z0-9\.-_]+@[a-zA-Z0-9-]+.[a-zA-Z]{2,8}.[a-zA-Z]{2,8}?$/
    let customerEmailField = document.getElementById('customeremail');
    let customerEmail = customerEmailField.value;
    if (!emailPattern.test(customerEmail)){
        customerEmailField.style.border = ".1rem solid red";
        errorMsgLabel[1].innerHTML = "***Please enter a valid email id."
        errorMsgLabel[1].style.fontSize = "1.5rem"
        errorMsgLabel[1].style.color = "red";
        errorMsgLabel[1].style.textTransform = "none";
        returnValue = false;
    }

    //Customer Mobile Number Field Validation
    let customerMobileNumberField = document.getElementById('customermobilenumber');
    let customerMobileNumber = customerMobileNumberField.value.trim()
    if (isNaN(customerMobileNumber) || customerMobileNumber.length!=10){
        customerMobileNumberField.style.border = ".1rem solid red";
        errorMsgLabel[2].innerHTML = "***Invalid mobile number format."
        errorMsgLabel[2].style.fontSize = "1.5rem"
        errorMsgLabel[2].style.color = "red";
        errorMsgLabel[2].style.textTransform = "none";
        returnValue = false;
    }

    //Customer Address Field Validation
    let customerAddressField = document.getElementById('customeraddress');
    let customerAddress = customerAddressField.value.trim()
    if (customerAddress == '' || customerAddress == null){
        customerAddressField.style.border = ".1rem solid red";
        errorMsgLabel[3].innerHTML = "***Address field cannot be empty."
        errorMsgLabel[3].style.fontSize = "1.5rem"
        errorMsgLabel[3].style.color = "red";
        errorMsgLabel[3].style.textTransform = "none";
        returnValue = false;
    }

    //Customer City and State Field Validation
    let customerCityField = document.getElementById('customercity');
    let customerCity = customerCityField.value.trim();
    let customerStateField = document.getElementById('customerstate');
    let customerState = customerStateField.value.trim()
    if (customerCity == '' || customerCity == null){
        customerCityField.style.border = ".1rem solid red";
        errorMsgLabel[4].innerHTML = "***City field cannot be empty."
        errorMsgLabel[4].style.fontSize = "1.5rem"
        errorMsgLabel[4].style.color = "red";
        errorMsgLabel[4].style.textTransform = "none";
        returnValue = false;
    }
    if (customerState == '' || customerState == null){
        customerStateField.style.border = ".1rem solid red";
        errorMsgLabel[5].innerHTML = "***State field cannot be empty."
        errorMsgLabel[5].style.fontSize = "1.5rem"
        errorMsgLabel[5].style.color = "red";
        errorMsgLabel[5].style.textTransform = "none";
        returnValue = false;
    }

    //Customer Pincode Field Validation
    let customerPincodeField = document.getElementById('customerpincode');
    let customerPincode = customerPincodeField.value.trim()
    if (customerPincode == '' || customerPincode == null){
        customerPincodeField.style.border = ".1rem solid red";
        errorMsgLabel[6].innerHTML = "***Pincode field cannot be empty."
        errorMsgLabel[6].style.fontSize = "1.5rem"
        errorMsgLabel[6].style.color = "red";
        errorMsgLabel[6].style.textTransform = "none";
        returnValue = false;
    }
    else if (isNaN(customerPincode)){
        customerPincodeField.style.border = ".1rem solid red";
        errorMsgLabel[6].innerHTML = "***Only numbers are allowed."
        errorMsgLabel[6].style.fontSize = "1.5rem"
        errorMsgLabel[6].style.color = "red";
        errorMsgLabel[6].style.textTransform = "none";
        returnValue = false;
    }
    else if (customerPincode.length!=6){
        customerPincodeField.style.border = ".1rem solid red";
        errorMsgLabel[6].innerHTML = "***Pincode must be of 6-digits only."
        errorMsgLabel[6].style.fontSize = "1.5rem"
        errorMsgLabel[6].style.color = "red";
        errorMsgLabel[6].style.textTransform = "none";
        returnValue = false;
    }

    //Customer Username Field Validation
    let usernamePattern = /^[a-zA-Z0-9\._@-]{8,16}$/
    let customerUsernameField = document.getElementById('customerusername');
    let customerUsername = customerUsernameField.value;
    let confirmUsernameField = document.getElementById('confirmusername');
    let confirmUsername = confirmUsernameField.value;

    if (!usernamePattern.test(customerUsername)){
        customerUsernameField.style.border = ".1rem solid red";
        errorMsgLabel[7].innerHTML = "***Invalid username format."
        errorMsgLabel[7].style.fontSize = "1.5rem"
        errorMsgLabel[7].style.color = "red";
        errorMsgLabel[7].style.textTransform = "none";
        return false;
    }
    if (confirmUsername != customerUsername){
        confirmUsernameField.style.border = ".1rem solid red";
        errorMsgLabel[8].innerHTML = "***Username did not match."
        errorMsgLabel[8].style.fontSize = "1.5rem"
        errorMsgLabel[8].style.color = "red";
        errorMsgLabel[8].style.textTransform = "none";
        returnValue = false;
    }

    //Customer Password Field Validation
    let customerPassword = document.getElementById('customerpassword').value;
    let confirmPasswordField = document.getElementById('confirmpassword');
    let confirmPassword = confirmPasswordField.value;
    if (confirmPassword != customerPassword){
        confirmPasswordField.style.border = ".1rem solid red";
        errorMsgLabel[9].innerHTML = "***Password did not match."
        errorMsgLabel[9].style.fontSize = "1.5rem"
        errorMsgLabel[9].style.color = "red";
        errorMsgLabel[9].style.textTransform = "none";
        returnValue = false;
    }
    return returnValue;   
}


