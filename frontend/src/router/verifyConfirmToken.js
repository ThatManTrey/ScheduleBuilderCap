import axios from "axios";
import * as Toast from "../toast.js";
import HttpStatus from "http-status-codes";
import store from "../store";

export default (to, from, next) => {
  var confirmationToken = to.query.token;

  if (confirmationToken) {
    axios
      .get("/auth/verify/confirm", {
        headers: { Authorization: "Bearer " + confirmationToken }
      })
      .then(() => {
        store.commit("auth/confirmEmail", true);
        next("/home");
        Toast.showSuccessMessage(
          "Your email has been confirmed successfully!",
          8000
        );
      })
      .catch(error => {
        if (!error.response) store.commit("auth/setAuthError");

        if (error.response.status == HttpStatus.BAD_REQUEST)
          store.commit(
            "auth/setAuthError",
            "You have already confirmed your email."
          );
        else
          store.commit("auth/setAuthError", "Invalid email confirmation link.");

        next("/home");
        Toast.showErrorMessage(store.state.auth.authError);
      });
  } else {
    next("/home");
    Toast.showErrorMessage("Invalid email confirmation link.");
  }
};
