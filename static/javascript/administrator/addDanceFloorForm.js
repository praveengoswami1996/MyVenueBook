//Declaring HTML Elements
const danceFloorImageContainer = document.querySelector('.dancefloor-image-container');
const danceFloorImage = document.querySelector('#dancefloorimage');
const file = document.querySelector('#file');

//When user selects an image to upload
file.addEventListener('change',function(){
    const choosedFile = this.files[0];

    if (choosedFile) {
        const reader = new FileReader(); //FileReader is a predefined thing in javascript

        reader.addEventListener('load',function(){
            danceFloorImage.setAttribute('src',reader.result);
        });
        reader.readAsDataURL(choosedFile);
    }
})
//Add Dance Floor Form Validation
function validate(){
    let returnValue = true;
    let danceFloorTypeField = document.getElementById('dancefloortype');
    let danceFloorType = danceFloorTypeField.value.trim();
    let danceFloorDescriptionField = document.getElementById('dancefloordescription');
    let danceFloorDescription = danceFloorDescriptionField.value.trim();
    let danceFloorPriceField  = document.getElementById('dancefloorpriceperbooking');
    let danceFloorPrice = danceFloorPriceField.value.trim(); 
    let danceFloorCodeField = document.getElementById('dancefloorcode');
    let danceFloorCode = danceFloorCodeField.value.trim()

    let errorMsgSpan = document.getElementsByClassName('errormsg');
    //food name field validation
    if (danceFloorType == '' || danceFloorType == null){
        danceFloorTypeField.style.border = ".1rem solid red";
        errorMsgSpan[0].innerHTML = "Dance floor type cannot have only spaces"
        errorMsgSpan[0].style.color = "red";
        errorMsgSpan[0].style.fontSize = "1.5rem";
        errorMsgSpan[0].style.textTransform = "none";
        returnValue = false;
    }
    if (danceFloorDescription == '' || danceFloorDescription == null){
        danceFloorDescriptionField.style.border = ".1rem solid red";
        errorMsgSpan[1].innerHTML = "Dance floor description cannot have only spaces"
        errorMsgSpan[1].style.color = "red";
        errorMsgSpan[1].style.fontSize = "1.5rem";
        errorMsgSpan[1].style.textTransform = "none";
        returnValue = false;
    }
    if (isNaN(danceFloorPrice)){
        danceFloorPriceField.style.border = ".1rem solid red";
        errorMsgSpan[2].innerHTML = "Please enter a valid amount"
        errorMsgSpan[2].style.color = "red";
        errorMsgSpan[2].style.fontSize = "1.5rem";
        errorMsgSpan[2].style.textTransform = "none";
        returnValue = false;
    }
    else if(danceFloorPrice == '' || danceFloorPrice == null){
        danceFloorPriceField.style.border = ".1rem solid red";
        errorMsgSpan[2].innerHTML = "Please enter a valid amount"
        errorMsgSpan[2].style.color = "red";
        errorMsgSpan[2].style.fontSize = "1.5rem";
        errorMsgSpan[2].style.textTransform = "none";
        returnValue = false;
    }
    if (danceFloorCode == '' || danceFloorCode == null){
        danceFloorCodeField.style.border = ".1rem solid red";
        errorMsgSpan[3].innerHTML = "Dance floor code cannot have only spaces"
        errorMsgSpan[3].style.color = "red";
        errorMsgSpan[3].style.fontSize = "1.5rem";
        errorMsgSpan[3].style.textTransform = "none";
        returnValue = false;
    }
    return returnValue;
}