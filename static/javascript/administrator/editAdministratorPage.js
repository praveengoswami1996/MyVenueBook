const profileImageContainer = document.querySelector('.profile-image-container');
const profileImage = document.querySelector('#adminprofileimage');
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
    let adminEmailField = document.getElementById('adminemail');
    let adminEmail = adminEmailField.value;
    if (!emailPattern.test(adminEmail)){
        adminEmailField.style.border = ".1rem solid red";
        errorMsgLabel[1].innerHTML = "Invalid Email"
        errorMsgLabel[1].style.fontSize = "1.5rem"
        errorMsgLabel[1].style.color = "red";
        errorMsgLabel[1].style.textTransform = "none";
    }
    else{
        adminEmailField.style.border = ".1rem solid green";
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
    let adminUsernameField = document.getElementById('adminusername');
    let adminUsername = adminUsernameField.value;
    if (usernamePattern.test(adminUsername)){
        adminUsernameField.style.border = ".1rem solid green";
        errorMsgLabel[4].innerHTML = "Valid username format"
        errorMsgLabel[4].style.fontSize = "1.5rem"
        errorMsgLabel[4].style.color = "green";
        errorMsgLabel[4].style.textTransform = "none";
    }
    else{
        adminUsernameField.style.border = ".1rem solid red";
        errorMsgLabel[4].innerHTML = "Invalid username format"
        errorMsgLabel[4].style.fontSize = "1.5rem"
        errorMsgLabel[4].style.color = "red";
        errorMsgLabel[4].style.textTransform = "none";
    }
}

function validateForm(){
    let returnValue = true;
    let errorMsgLabel = document.getElementsByClassName('errormsg');

    //Customer Name Field Validation
    let adminNameField = document.getElementById('adminname');
    let adminName = adminNameField.value.trim();
    if (adminName == '' || adminName == null){
        adminNameField.style.border = ".1rem solid red";
        errorMsgLabel[0].innerHTML = "***Name cannot have only spaces."
        errorMsgLabel[0].style.fontSize = "1.5rem"
        errorMsgLabel[0].style.color = "red";
        errorMsgLabel[0].style.textTransform = "none";
        returnValue = false;
    }

    //Customer Email Field Validation
    let emailPattern = /^[a-zA-Z0-9\.-_]+@[a-zA-Z0-9-]+.[a-zA-Z]{2,8}.[a-zA-Z]{2,8}?$/
    let adminEmailField = document.getElementById('adminemail');
    let adminEmail = adminEmailField.value;
    if (!emailPattern.test(adminEmail)){
        adminEmailField.style.border = ".1rem solid red";
        errorMsgLabel[1].innerHTML = "***Please enter a valid email id."
        errorMsgLabel[1].style.fontSize = "1.5rem"
        errorMsgLabel[1].style.color = "red";
        errorMsgLabel[1].style.textTransform = "none";
        returnValue = false;
    }

    //Admin Mobile Number Field Validation
    let adminMobileNumberField = document.getElementById('adminmobilenumber');
    let adminMobileNumber = adminMobileNumberField.value.trim()
    if (isNaN(adminMobileNumber) || adminMobileNumber.length!=10){
        adminMobileNumberField.style.border = ".1rem solid red";
        errorMsgLabel[2].innerHTML = "***Invalid mobile number format."
        errorMsgLabel[2].style.fontSize = "1.5rem"
        errorMsgLabel[2].style.color = "red";
        errorMsgLabel[2].style.textTransform = "none";
        returnValue = false;
    }

    //Admin Address Field Validation
    let adminAddressField = document.getElementById('adminaddress');
    let adminAddress = adminAddressField.value.trim()
    if (adminAddress == '' || adminAddress == null){
        adminAddressField.style.border = ".1rem solid red";
        errorMsgLabel[3].innerHTML = "***Address field cannot be empty."
        errorMsgLabel[3].style.fontSize = "1.5rem"
        errorMsgLabel[3].style.color = "red";
        errorMsgLabel[3].style.textTransform = "none";
        returnValue = false;
    }

    //Admin Username Field Validation
    let usernamePattern = /^[a-zA-Z0-9\._@-]{8,16}$/
    let adminUsernameField = document.getElementById('adminusername');
    let adminUsername = adminUsernameField.value;

    if (!usernamePattern.test(adminUsername)){
        adminUsernameField.style.border = ".1rem solid red";
        errorMsgLabel[4].innerHTML = "***Invalid username format."
        errorMsgLabel[4].style.fontSize = "1.5rem"
        errorMsgLabel[4].style.color = "red";
        errorMsgLabel[4].style.textTransform = "none";
        return false;
    }
    return returnValue;   
}

/*Create date string of previous date of birth--starts*/
let previousDobDateField = document.getElementById('previousdobdate');
let previousDob = document.getElementById('previousdob').value;
let previousDate = new Date(previousDob)

let date = previousDate.getDate();
if (date<10){
    date = '0'+date;
}
let month = previousDate.getMonth() + 1;
if (month<10){
    month = '0'+month;
}
let year = previousDate.getFullYear();

let dateString = year+'-'+month+'-'+date;
previousDobDateField.value = dateString;
/*Create date string of previous date of birth--ends*/

