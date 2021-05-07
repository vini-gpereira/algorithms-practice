var signUpForm = document.getElementById('sign-up-form');

function isPasswordValid(password, confirmation) {
    const validLettersRegex = /[\w@_\-\!]+/
    return password.length >= 5 && validLettersRegex.test(password) && password !== confirmation;
}

function submit(event) {
    event.preventDefault();
    const password = signUpForm.password.value;
    const passwordConfirmation = signUpForm.passwordconfirmation.value;
    const response = isPasswordValid(password, passwordConfirmation);

    if (response) {
        console.log('Form is valid!');
    } else {
        console.log('Form is not valid');
    }

    return response;
}

signUpForm.addEventListener('submit', submit)