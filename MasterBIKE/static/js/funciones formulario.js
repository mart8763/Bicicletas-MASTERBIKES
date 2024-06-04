const form = document.getElementById('form');
const username = document.getElementById('username');
const username2 = document.getElementById('username2');
const email = document.getElementById('email');
const password = document.getElementById('password');



form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error')
    inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success')
    inputControl.classList.remove('error')
}

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
    const usernameValue = username.value.trim();
    const username2Value = username.value.trim();
    const emailValue = email.value.trim();
    const passwordValue = password.value.trim();

    if (usernameValue === '') {
        setError(username, 'Requiere un nombre');
    } else {
        setSuccess(username)
    }

    if (username2Value === '') {
        setError(username2, 'Requiere un apellido');
    } else {
        setSuccess(username2)
    }

    if (emailValue === '') {
        setError(email, 'Requiere el email')
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Ingrese un emial valido')
    } else {
        setSuccess(email);
    }

    if (passwordValue === '') {
        setError(password, 'Requiere la contraseña')
    } else if (passwordValue.length < 8) {
        setError(password, 'La contraseña debe tener al menos 8 caracteres')
    } else {
        setSuccess(password)
    }

};