function ValidatePhone(input) {
  var validRegex = /^[24795][0-9]{7}/;
  if (input.value.match(validRegex)) return true;
  return false;
}
function ValidateEmail(input) {
  var validRegex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
  if (input.value.match(validRegex)) return true;
  return false;
}

$('.email').on("change keyup paste",
  function(){
    let email = document.forms["Inscription"]["email"];
    if(ValidateEmail(email)){
      $('.email_paper').addClass("next");
    } else {
      $('.email_paper').removeClass("next");
    }
  }
);

$('.user').on("change keyup paste", 
 function(){
    if ($(this).val()){
      $('.user_paper').addClass("next");
    } else {
      $('.user_paper').removeClass("next");
    }
 }
);

$('.phone').on("change keyup paste", 
 function(){
    let phone = document.forms["Inscription"]["phone_number"];
    if (ValidatePhone(phone)){
      $('.phone_paper').addClass("next");
    } else {
      $('.phone_paper').removeClass("next");
    }
 }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.email').click(
  function(){
    console.log("Something");
    $('.email-section').addClass("fold-up");
    $('.password-section').removeClass("folded");
  }
);

$('.password').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-lock').addClass("next");
    } else {
      $('.icon-lock').removeClass("next");
    }
  }
);

$('.next-button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('button').hover(
  function(){
    $(this).css('cursor', 'pointer');
  }
);

$('.next-button.user').click(
  function(){
    console.log("Something");
    $('.password-section').addClass("fold-up");
    $('.repeat-password-section').removeClass("folded");
  }
);

$('.repeat-password').on("change keyup paste",
  function(){
    if($(this).val()){
      $('.icon-repeat-lock').addClass("next");
    } else {
      $('.icon-repeat-lock').removeClass("next");
    }
  }
);

$('.next-button.phone').click(
  function(){
    console.log("Something");
    $('.repeat-password-section').addClass("fold-up");
    $('.success').css("marginTop", 0);
  }
);

