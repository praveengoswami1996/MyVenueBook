$(document).ready(function(){

  $('.fa-bars').click(function(){
    $(this).toggleClass('fa-times');
    $('.navbar').toggleClass('nav-toggle');
  });

  $(window).on('load scroll',function(){

    $('.fa-bars').removeClass('fa-times');
    $('.navbar').removeClass('nav-toggle');

    if($(window).scrollTop() > 30){
      $('header').addClass('header-active');
    }else{
      $('header').removeClass('header-active');
    }

    $('section').each(function(){
      var id = $(this).attr('id');
      var height = $(this).height();
      var offset = $(this).offset().top - 200;
      var top = $(window).scrollTop();
      if(top >= offset && top < offset + height){
        $('.navbar ul li a').removeClass('active');
        $('.navbar').find('[data-scroll="' + id + '"]').addClass('active');
      }
    });

  });
});
/*Javascript for Search Venue By State Form*/

function removeAllPreviousOptions(city){
  for(var i=city.options.length-1;i>=1;i--){
      city.remove(i);
  }
}

function insertOptions(state,city){
  var state = document.getElementById('state');
  var city = document.getElementById('city');
  if (state.options[state.selectedIndex].value == "Bihar"){
    var opt1 = document.createElement('option');
    opt1.value = "Patna";
    opt1.innerHTML = "Patna"
    removeAllPreviousOptions(city);
    city.options.add(opt1);  /*OR city.appendChild(opt1);*/ 
  }
  else if (state.options[state.selectedIndex].value == "Delhi"){
    var opt1 = document.createElement('option');
    opt1.value = "New Delhi";
    opt1.innerHTML = "New Delhi"
    removeAllPreviousOptions(city);
    city.options.add(opt1);
  }
  else if (state.options[state.selectedIndex].value == "Haryana"){
    var opt1 = document.createElement('option');
    opt1.value = "Chandigarh";
    opt1.innerHTML = "Chandigarh"
    removeAllPreviousOptions(city);
    city.options.add(opt1);
  }
  else if (state.options[state.selectedIndex].value == "Himachal Pradesh"){
    var opt1 = document.createElement('option');
    opt1.value = "Shimla";
    opt1.innerHTML = "Shimla"
    removeAllPreviousOptions(city);
    city.options.add(opt1);
  }
  else if (state.options[state.selectedIndex].value == "Madhya Pradesh"){
    var opt1 = document.createElement('option');
    opt1.value = "Bhopal";
    opt1.innerHTML = "Bhopal"
    removeAllPreviousOptions(city);
    city.options.add(opt1);
  }
  else if (state.options[state.selectedIndex].value == "Maharashtra"){
    var opt1 = document.createElement('option');
    var opt2 = document.createElement('option');
    opt1.value = "Mumbai";
    opt2.value = "Pune";
    opt1.innerHTML = "Mumbai";
    opt2.innerHTML = "Pune";
    removeAllPreviousOptions(city);
    city.options.add(opt1);
    city.options.add(opt2);
  }
  else if (state.options[state.selectedIndex].value == "Paschim Bengal"){
    var opt1 = document.createElement('option');
    opt1.value = "Kolkata";
    opt1.innerHTML = "Kolkata"
    removeAllPreviousOptions(city);
    city.options.add(opt1);
  }
  else if (state.options[state.selectedIndex].value == "Punjab"){
    var opt1 = document.createElement('option');
    opt1.value = "Chandigarh";
    opt1.innerHTML = "Chandigarh"
    removeAllPreviousOptions(city);
    city.options.add(opt1);
  }
  else if (state.options[state.selectedIndex].value == "Rajasthan"){
    var opt1 = document.createElement('option');
    var opt2 = document.createElement('option');
    opt1.value = "Jaipur";
    opt2.value = "Udaipur";
    opt1.innerHTML = "Jaipur"
    opt2.innerHTML = "Udaipur"
    removeAllPreviousOptions(city);
    city.options.add(opt1);
    city.options.add(opt2);
  }
  else if (state.options[state.selectedIndex].value == "Tamil Nadu"){
    var opt1 = document.createElement('option');
    opt1.value = "Chennai";
    opt1.innerHTML = "Chennai"
    removeAllPreviousOptions(city);
    city.options.add(opt1);
  }
  else if (state.options[state.selectedIndex].value == "Uttar Pradesh"){
    var opt1 = document.createElement('option');
    opt1.value = "Lucknow";
    opt1.innerHTML = "Lucknow"
    removeAllPreviousOptions(city);
    city.options.add(opt1);
  }
}


