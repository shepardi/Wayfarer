let btnSignIn = $('#btn-sign-in');
let btnSignUp = $('#btn-sign-up');
let formSignIn = $('#form-sign-in');
let formSignUp = $('#form-sign-up');
let formSignIn2 = $('#form-sign-in2');
let formSignUp2 = $('#form-sign-up2');

btnSignIn.on('click', () => {
  formSignUp.addClass('hidden');
  formSignUp2.addClass('hidden');
  formSignIn.removeClass('hidden');
  formSignIn2.removeClass('hidden');
});

btnSignUp.on('click', () => {
  formSignIn.addClass('hidden');
  formSignIn2.addClass('hidden');
  formSignUp.removeClass('hidden');
  formSignUp2.removeClass('hidden');
});


