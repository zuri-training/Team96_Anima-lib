$(document).ready(function() {
    $('#form').trigger("reset");
    $("form :input").attr("autocomplete", "off");
    $('#form').submit(function(e) {
      e.preventDefault();
      var fname = $('#fullname').val();
      var email = $('#email').val();
      var pass = $('#textarea').val();
  
      $(".error").remove();
  
      if (fname.length < 1) {
        $('#fullname').after('<span class="error">Enter your fullname here!</span>');
        $('#fullname').addClass('error-icon');
      } else {
          
        $('#fullname').removeClass('error-icon');
      
    }

      if (email.length < 1) {
        $('#email').after('<span class="error">Email cannot be empty</span>');
        $('#email').addClass('error-icon');
      } else {
        var regEx = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i;
        var validEmail = regEx.test(email);
        if (!validEmail) {
          $('#email').after('<span class="error">Looks like this is not an email</span>');
          $('#email').addClass('error-icon');
        }else {
          
            $('#email').removeClass('error-icon');
          
        }
      }
      if (pass.length < 1) {
        $('#textarea').after('<span class="error">Type your Request here!</span>');
        $('#textarea').addClass('error-icon');
      } else {
          
          $('#textarea').removeClass('error-icon');
        
      }
    });
  
  });
