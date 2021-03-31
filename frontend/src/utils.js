// takes object with two strings { pass: ..., error: ...}
export function validatePassField(passField, checkLength = true) {
  if (passField.pass === null) return;
  else if (passField.pass.length === 0)
    passField.error = "Required field";
  else if (checkLength && passField.pass.length < 8)
    passField.error = "Password must be at least 8 characters long.";
  else passField.error = null;
}

// takes object with two strings { pass: ..., error: ...}
export function validatePassVerifyField(passVerifyField, passField) {
  if (passVerifyField.pass === null) return;
  else if (passVerifyField.pass.length === 0)
    passVerifyField.error = "Required field";
  else if (passVerifyField.pass !== passField.pass)
    passVerifyField.error = "Passwords do not match";
  else passVerifyField.error = null;
}

// takes object with two strings { email: ..., error: ...}
export function validateEmailField(emailField) {
  if (emailField.email === null) return;
  else if (emailField.email.length === 0)
    emailField.error = "Required field";
  else if (!isEmailValid(emailField.email))
    emailField.error = "Please enter a valid email";
  else emailField.error = null;
}

// https://masteringjs.io/tutorials/fundamentals/email-validation
// checks if email roughly follows pattern xx@yy.zz
export function isEmailValid(email) {
  return /^[^@]+@\w+(\.\w+)+\w$/.test(email);
}
