//Declaring HTML Elements
const venueImageContainer = document.querySelector('.venue-image-container');
const uploadPhotoImage = document.querySelector('#venueimage');
const file = document.querySelector('#file');

//When user selects an image to upload
file.addEventListener('change',function(){
    const choosedFile = this.files[0];

    if (choosedFile) {
        const reader = new FileReader(); //FileReader is a predefined thing in javascript

        reader.addEventListener('load',function(){
            uploadPhotoImage.setAttribute('src',reader.result);
        });
        reader.readAsDataURL(choosedFile);
    }
})


/*Javascript for Search Venue By State Form*/
function removeAllPreviousOptions(city){
    for(var i=city.options.length-1;i>=0;i--){
        city.remove(i);
    }
  }
  
  function insertOptions(state,city){
    var state = document.getElementById('state');
    var city = document.getElementById('city');
    if (state.options[state.selectedIndex].value == "Bihar"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Patna";
      opt2.innerHTML = "Patna"
      removeAllPreviousOptions(city);
      city.options.add(opt1);  /*OR city.appendChild(opt1);*/
      city.options.add(opt2); 
    }
    else if (state.options[state.selectedIndex].value == "Delhi"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "New Delhi";
      opt2.innerHTML = "New Delhi"
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
    }
    else if (state.options[state.selectedIndex].value == "Haryana"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Chandigarh";
      opt2.innerHTML = "Chandigarh"
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
    }
    else if (state.options[state.selectedIndex].value == "Himachal Pradesh"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Shimla";
      opt2.innerHTML = "Shimla"
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
    }
    else if (state.options[state.selectedIndex].value == "Madhya Pradesh"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Bhopal";
      opt2.innerHTML = "Bhopal"
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
    }
    else if (state.options[state.selectedIndex].value == "Maharashtra"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      var opt3 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Mumbai";
      opt2.innerHTML = "Mumbai";
      opt3.value = "Pune";
      opt3.innerHTML = "Pune";
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
      city.options.add(opt3);
    }
    else if (state.options[state.selectedIndex].value == "Paschim Bengal"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Kolkata";
      opt2.innerHTML = "Kolkata"
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
    }
    else if (state.options[state.selectedIndex].value == "Punjab"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Chandigarh";
      opt2.innerHTML = "Chandigarh"
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
    }
    else if (state.options[state.selectedIndex].value == "Rajasthan"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      var opt3 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Jaipur";
      opt2.innerHTML = "Jaipur";
      opt3.value = "Udaipur";
      opt3.innerHTML = "Udaipur";
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
      city.options.add(opt3);
    }
    else if (state.options[state.selectedIndex].value == "Tamil Nadu"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Chennai";
      opt2.innerHTML = "Chennai"
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
    }
    else if (state.options[state.selectedIndex].value == "Uttar Pradesh"){
      var opt1 = document.createElement('option');
      var opt2 = document.createElement('option');
      opt1.value = "";
      opt1.innerHTML = "---Select Venue City---"
      opt2.value = "Lucknow";
      opt2.innerHTML = "Lucknow"
      removeAllPreviousOptions(city);
      city.options.add(opt1);
      city.options.add(opt2);
    }
  }
  