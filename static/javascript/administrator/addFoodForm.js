//Declaring HTML Elements
const foodImageContainer = document.querySelector('.food-image-container');
const profileImage = document.querySelector('#foodimage');
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
//Add Food Form Validation
function validate(){
    let returnValue = true;
    let foodNameField = document.getElementById('foodname');
    let foodName = foodNameField.value.trim();
    let foodPriceField = document.getElementById('foodpriceperserving');
    let foodPrice = foodPriceField.value;
    let foodCodeField = document.getElementById('foodcode');
    let foodCode = foodCodeField.value.trim()
    let errorMsgSpan = document.getElementsByClassName('errormsg');
    //food name field validation
    if (foodName == '' || foodName == null){
        foodNameField.style.border = ".1rem solid red";
        errorMsgSpan[0].innerHTML = "A name cannot have only spaces"
        errorMsgSpan[0].style.color = "red";
        errorMsgSpan[0].style.fontSize = "1.5rem";
        errorMsgSpan[0].style.textTransform = "none";
        returnValue = false;
    }
    //food price field validation
    if (isNaN(foodPrice)){
        foodPriceField.style.border = ".1rem solid red";
        errorMsgSpan[1].innerHTML = "Please enter a valid amount";
        errorMsgSpan[1].style.color = "red";
        errorMsgSpan[1].style.fontSize = "1.5rem";
        errorMsgSpan[1].style.textTransform = "none";
        returnValue = false;
    }
    //food code field validation
    if (foodCode == '' || foodCode == null){
        foodCodeField.style.border = ".1rem solid red";
        errorMsgSpan[2].innerHTML = "food code cannot have only spaces"
        errorMsgSpan[2].style.color = "red";
        errorMsgSpan[2].style.fontSize = "1.5rem";
        errorMsgSpan[2].style.textTransform = "none";
        returnValue = false;
    }
    return returnValue;
}