// https://masteringjs.io/tutorials/fundamentals/email-validation
// checks if email roughly follows pattern xx@yy.zz
export function isEmailValid(email) {
  return /^[^@]+@\w+(\.\w+)+\w$/.test(email);
}
