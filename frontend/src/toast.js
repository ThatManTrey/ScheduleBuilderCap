import Vue from "vue";

export function showErrorMessage(errorMessage, duration = 3000) {
  Vue.$toast.open({
    message: errorMessage,
    duration: duration,
    type: "error"
  });
}

export function showSuccessMessage(successMessage, duration = 3000) {
  Vue.$toast.open({
    message: successMessage,
    duration: duration,
    type: "success"
  });
}
