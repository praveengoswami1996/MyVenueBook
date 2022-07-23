/*Javascript code for billingPageWithBookingDetails.html File Starts*/
document.addEventListener("DOMContentLoaded", function(event) { 
    var scrollpos = localStorage.getItem('scrollpos');
    if (scrollpos) window.scrollTo(0, scrollpos);
});
    
window.onbeforeunload = function(e) {
    localStorage.setItem('scrollpos', window.scrollY);
};


let foodAmountTotalPerDay = document.querySelector('.perdaytotal'); //Global Variable
let foodAmountTotalWholeBooking = document.querySelector('.completetotal-food'); //Global Variable
let foodTotalPerDay=0; //Global Variable
let foodTotalWholeBooking=0; //Global Variable
let danceFloorTotalWholeBooking = document.querySelector('.completetotal-floor'); //Global Variable
let myDanceFloorTotal = 0

function calculateTotalFoodAmount(id){
    x='foodpriceperserving'+id;
    y='foodamountperday'+id
    z='totalamount'+id;
    let foodPricePerServing = parseFloat(document.getElementById(x).innerHTML);
    let numberOfServingsField = document.getElementById(id); 
    let numberOfServings = parseInt(document.getElementById(id).value);
    if (isNaN(numberOfServings)){
        numberOfServings=0;
    }
    if (numberOfServings<1){
        numberOfServingsField.value = 0;
        numberOfServings = numberOfServingsField.value;
    }
    let foodAmountPerDay = document.getElementById(y);
    let totalAmount = document.getElementById(z);
    let totalBookingDays = parseInt(document.getElementById('bookingdays').innerHTML);

    let previousAmountPerDay = parseFloat(foodAmountPerDay.value)
    
    /*Calculating Food Amount Total per day according to the number of servings required*/

    if (isNaN(previousAmountPerDay)){
        foodAmountPerDay.value = foodPricePerServing*numberOfServings;
    }
    else{
        foodTotalPerDay=foodTotalPerDay-previousAmountPerDay;
        foodAmountPerDay.value = foodPricePerServing*numberOfServings;
    }
    foodTotalPerDay=foodTotalPerDay+parseFloat(foodAmountPerDay.value)
    foodAmountTotalPerDay.value=foodTotalPerDay;

    /*Calculating Food Amount Total for the whole booking*/
    previousTotalAmount = parseFloat(totalAmount.value)
    if (isNaN(previousTotalAmount)){
        totalAmount.value = parseFloat(foodAmountPerDay.value)*totalBookingDays;    
    }
    else{
        foodTotalWholeBooking = foodTotalWholeBooking - previousTotalAmount;
        totalAmount.value = parseFloat(foodAmountPerDay.value)*totalBookingDays;
    } 
    foodTotalWholeBooking=foodTotalWholeBooking+parseFloat(totalAmount.value)
    foodAmountTotalWholeBooking.value=foodTotalWholeBooking
}
/*Calculating Dance Floor Total Amount*/

function calculateDanceFloorTotal(id){
    x='dancefloorprice'+id;
    y='danceflooramount'+id;
    let daysField = document.getElementById(id); 
    let days = parseInt(document.getElementById(id).value);
    let totalBookingDays = parseInt(document.getElementById('bookingdays').innerHTML);
    if (isNaN(days)){
        days=0;
    }
    if (days>totalBookingDays){
        daysField.value = totalBookingDays;
        days = daysField.value  
    }
    if (days<1){
        daysField.value = 1;
        days = daysField.value 
    }
    let danceFloorPricePerDay = parseFloat(document.getElementById(x).innerHTML);

    let danceFloorTotalAmount = document.getElementById(y); 

    let previousDanceFloorTotalAmount = parseFloat(danceFloorTotalAmount.value);

    console.log(previousDanceFloorTotalAmount)

    if (isNaN(previousDanceFloorTotalAmount) || previousDanceFloorTotalAmount==0){
        danceFloorTotalAmount.value = danceFloorPricePerDay*days;
        myDanceFloorTotal = myDanceFloorTotal+parseFloat(danceFloorTotalAmount.value)
    }
    else{
        myDanceFloorTotal = myDanceFloorTotal - previousDanceFloorTotalAmount;
        danceFloorTotalAmount.value = danceFloorPricePerDay*days;
        myDanceFloorTotal = myDanceFloorTotal+parseFloat(danceFloorTotalAmount.value)
    }
    danceFloorTotalWholeBooking.value = myDanceFloorTotal;
}

/*Generating Amount Payable*/
function generateAmountPayable(){
    let venuePrice = parseFloat(document.getElementById('venueprice').innerHTML);
    let totalBookingDays = parseInt(document.getElementById('bookingdays').innerHTML);
    let venueBookingCharge = document.getElementById('venuebookingcharge');
    let totalAddOnFoodAmount = document.querySelector('.completetotal-food').value;
    let totalAddOnDanceFloorAmount = document.querySelector('.completetotal-floor').value;
    let addOnFoodCharge = document.getElementById('addonfoodcharge');
    let addOnDanceFloorCharge = document.getElementById('addondancefloorcharge');
    let amountPayable = document.getElementById('amountpayable');
    
    if (isNaN(totalAddOnFoodAmount) ||  totalAddOnFoodAmount==""){
        totalAddOnFoodAmount=0;
    }
    if (isNaN(totalAddOnDanceFloorAmount) || totalAddOnDanceFloorAmount==""){
        totalAddOnDanceFloorAmount=0;
    }
    venueBookingCharge.value = venuePrice*totalBookingDays;
    addOnFoodCharge.value = totalAddOnFoodAmount;
    addOnDanceFloorCharge.value = totalAddOnDanceFloorAmount;
    amountPayable.value = parseFloat(venueBookingCharge.value)+parseFloat(addOnFoodCharge.value)+parseFloat(addOnDanceFloorCharge.value) 
}

/*Javascript code for billingPageWithBookingDetails.html File Ends*/

function validate(){
    let returnValue = true;
    /*Card Number Field Validation*/
    let cardNumber = document.getElementById('cardnumber').value;
    let cvvNumber = document.getElementById('cvvnumber').value; 
    if (isNaN(cardNumber) || cardNumber.length!=16){
        alert("Invalid Card Number");
        returnValue = false;
    }

    if (isNaN(cvvNumber) || cvvNumber.length!=3){
        alert("Invalid CVV Number")
        returnValue = false;
    }

    /*Checkbox Validation*/
    let isChecked = document.getElementById('checkbox').checked;
    if (!isChecked){
        alert("Please check the box to proceed further")
        returnValue = false;
    }
    return returnValue;
}