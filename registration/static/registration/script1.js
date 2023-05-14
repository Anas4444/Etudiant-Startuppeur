const form = document.getElementById('inscription');
const fullname = document.getElementById('prenom');
const email = document.getElementById('email');
const phone = document.getElementById('numero');
const specialite = document.getElementById('specialite');
const faculte = document.getElementById('faculte');

form.addEventListener('submit', e => {
  e.preventDefault();

  validateInputs();
});

const setError = (element, message) => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');

  errorDisplay.innerText = message;
  inputControl.classList.add('error');
  inputControl.classList.remove('success')
}

const setSuccess = element => {
  const inputControl = element.parentElement;
  const errorDisplay = inputControl.querySelector('.error');

  errorDisplay.innerText = '';
  inputControl.classList.add('success');
  inputControl.classList.remove('error');
};

const isValidEmail = email => {
  const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
  const fullnameValue = fullname.value.trim();
  const specialiteValue = specialite.value.trim();
  const emailValue = email.value.trim();
  const phoneValue = phone.value.trim();
  const faculteValue = faculte.value.trim();

  let isFormValid = false;
  if (fullnameValue === '') {
    isFormValid = false;
    setError(fullname, 'FullName is required');
  } else {
    isFormValid = true;
    setSuccess(fullname);
  }

  if (faculteValue === '') {
    isFormValid = false;
    setError(faculte, 'Faculté is required');
  } else {
    isFormValid = true;
    setSuccess(faculte);
  }

  if (specialiteValue === '') {
    isFormValid = false;
    setError(specialite, 'Specialité is required')
  }
  else {
    isFormValid = true;
    setSuccess(fullname);
  }

  if (emailValue === '') {
        setError(email, 'Email is required');
    } else if (!isValidEmail(emailValue)) {
        isFormValid = false;
        setError(email, 'Provide a valid email address');
    } else {
        isFormValid = true;
        setSuccess(email);
  }

  if (phoneValue === '') {
        isFormValid = false;
        setError(phone, 'Phone is required');
    } else if (!isValidPhone(phoneValue)) {
        isFormValid = false;
        setError(phone, 'Provide a valid phone number');
    } else {
        isFormValid = true;
        setSuccess(phone);
  }
  if (isFormValid) form.submit();
};

const isValidPhone = phone => {
    const re = /^[24795][0-9]{7}/;
    return re.test(String(phone));
}