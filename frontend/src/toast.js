import Vue from "vue";

export function showErrorMessage(errorMessage) {
  Vue.$toast.open({
    message: errorMessage,
    type: "error"
  });
}

export function showSuccessMessage(successMessage) {
  Vue.$toast.open({
    message: successMessage,
    type: "success"
  });
}

export function showWarningMessage(warningMessage) {
  Vue.$toast.open({
    message: warningMessage,
    type: "warning"
  });
}