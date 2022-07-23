let date = new Date();
let todayDate = date.getDate();
let currentMonth = date.getMonth() + 1;
let currentYear = date.getFullYear();
if (todayDate < 10){
    todayDate = '0' + todayDate;
}
if (currentMonth < 10){
    currentMonth = '0' + currentMonth;
}
let minDate = currentYear+'-'+currentMonth+'-'+todayDate;
let bookingStartDate = document.getElementById('bookingstartdate');
let bookingEndDate = document.getElementById('bookingenddate');
bookingStartDate.setAttribute('min', minDate);
bookingEndDate.setAttribute('min', minDate);

let bookedDatesList = document.getElementById('bookeddates').value;
console.log(bookedDatesList)
console.log(typeof(bookedDatesList))


function calculateBookingDays(){
    let totalBookingDays = document.getElementById('totalbookingdays'); 
    let startDateField = document.getElementById('bookingstartdate');
    let endDateField = document.getElementById('bookingenddate');
    let date = new Date()
    let day = date.getDate()
    let month = date.getMonth() + 1;
    let year = date.getFullYear()
    if (day<10){
        day = '0'+day;
    }
    if (month<10){
        month = '0'+month;
    }
    let todayDate = year + '-' + month + '-' + day;
    let startDate = startDateField.value;
    let endDate = endDateField.value;
    endDateField.setAttribute('min', startDate)
    startDateField.setAttribute('max', endDate)
    if (endDate && startDate==''){
        startDateField.setAttribute('max', endDate)
        startDateField.setAttribute('value', todayDate)
    }
    startDate = startDateField.value;    
    let date1 = new Date(startDate);
    let date2 = new Date(endDate);
    let oneDayMS = 1000*60*60*24 /*milliseconds in one day */
    let diffrenceInMS = date2.getTime() - date1.getTime() //Difference In milliseconds
    totalBookingDays.value = (diffrenceInMS/oneDayMS)+1;
    if(!endDate){
        totalBookingDays.value = 1;
    }
    if (totalBookingDays.value < 1){
        endDateField.setAttribute('value', startDate)
        totalBookingDays.value = 1;
    }  
}

