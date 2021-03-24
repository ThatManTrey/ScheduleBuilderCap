<template>
  <Modal ref="signInBaseModalRef">
    <template v-slot:header>
      <span v-if="!isResettingPassword">Sign In</span>
      <span v-else>Reset Password</span>
      <span class="ms-2">
        <Spinner :showSpinner="isSubmittingForm" sizeInRem="1.5rem"></Spinner>
      </span>
    </template>

    <template v-slot:body>
      <transition name="fade">
        <div v-if="hasSubmittedForm">
          <!-- Login alert -->
          <Alert
            v-if="!isResettingPassword"
            :isSuccess="isLoginSuccessful"
            :errorMessage="errorMessage"
            successMessage="Login Successful! Closing this window..."
          ></Alert>

          <!-- Password reset alert -->
          <Alert
            v-else
            :isSuccess="isPasswordResetSuccessful"
            :errorMessage="errorMessage"
            :successMessage="resetPassSuccessMessage"
          ></Alert>
        </div>
      </transition>

      <!-- Login form -->
      <form v-if="!isResettingPassword">
        <div class="mb-3 text-theme-white">
          <label for="userSignInEmail" class="form-label">
            <h6>Email Address</h6>
          </label>

          <input
            type="email"
            class="form-control"
            :class="{ 'form-error': emailField.error }"
            id="userSignInEmail"
            placeholder="example@gmail.com"
            :disabled="isSubmittingForm"
            v-model.trim="emailField.email"
          />

          <transition name="fade">
            <span v-if="emailField.error" class="form-error-text">
              <i class="fas fa-times-circle text-theme-warning-light"></i>
              {{ emailField.error }}
            </span>
          </transition>
        </div>

        <div class="text-theme-white">
          <label for="userSignInPass" class="form-label">
            <h6>Password</h6>
          </label>

          <input
            type="password"
            class="form-control"
            :class="{ 'form-error': passField.error }"
            id="userSignInPass"
            aria-describedby="userSignInPassHelp"
            placeholder="Enter password..."
            :disabled="isSubmittingForm"
            v-model="passField.pass"
          />

          <transition name="fade">
            <span v-if="passField.error" class="form-error-text">
              <i class="fas fa-times-circle text-theme-warning-light"></i>
              {{ passField.error }}
            </span>
          </transition>

          <div id="userSignInPassHelp" class="form-text">
            <a class="link" @click="isResettingPassword = true"
              >Forgot your password?</a
            >
          </div>
        </div>
      </form>

      <!-- Password reset form -->
      <form v-else>
        <p>
          Enter your email below and we'll send you a link to reset your
          password.
        </p>

        <label for="userResetPassEmail" class="form-label">
          <h6>Email Address</h6>
        </label>

        <input
          type="email"
          class="form-control"
          :class="{ 'form-error': resetPassEmailField.error }"
          id="userResetPassEmail"
          placeholder="Enter password..."
          :disabled="isSubmittingForm"
          v-model.trim="resetPassEmailField.email"
        />

        <span v-if="resetPassEmailField.error" class="form-error-text">
          <i class="fas fa-times-circle text-theme-warning-light"></i>
          {{ resetPassEmailField.error }}
        </span>
      </form>
    </template>

    <template v-slot:footer>
      <!-- Login buttons -->
      <div v-if="!isResettingPassword">
        <button type="button" class="btn btn-theme-blacker" @click="closeModal">
          Close
        </button>

        <button
          type="button"
          class="btn btn-theme-primary-dark ms-2"
          @click="signIn"
        >
          Continue
        </button>
      </div>

      <!-- Password reset buttons -->
      <div v-else>
        <button
          type="button"
          class="btn btn-theme-blacker"
          @click="isResettingPassword = false"
        >
          Go Back
        </button>

        <button
          type="button"
          class="btn btn-theme-primary-dark ms-2"
          @click="resetPassword()"
        >
          Reset My Password
        </button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import axios from "axios";
import Spinner from "../spinners/Spinner.vue";
import Alert from "../Alert.vue";
import * as Toast from "../../toast";

export default {
  data() {
    return {
      emailField: {
        email: "",
        error: null
      },
      passField: {
        pass: "",
        error: null
      },
      resetPassEmailField: {
        email: "",
        error: null
      },
      isSubmittingForm: false,
      hasSubmittedForm: false,
      isLoginSuccessful: null,
      isResettingPassword: false,
      isPasswordResetSuccessful: null,
      errorMessage: "An error occurred. Please try again.",
      resetPassSuccessMessage: ""
    };
  },

  watch: {
    "emailField.email": function() {
      if (this.emailField.email.length === 0)
        this.emailField.error = "Required field";
      else if (!this.isEmailValid(this.emailField.email))
        this.emailField.error = "Please enter a valid email";
      else this.emailField.error = null;
    },

    "resetPassEmailField.email": function() {
      if (this.resetPassEmailField.email.length === 0)
        this.resetPassEmailField.error = "Required field";
      else if (!this.isEmailValid(this.resetPassEmailField.email))
        this.resetPassEmailField.error = "Please enter a valid email";
      else this.resetPassEmailField.error = null;
    },

    "passField.pass": function() {
      if (this.passField.pass.length === 0)
        this.passField.error = "Required field";
      else this.passField.error = null;
    }
  },

  components: {
    Modal,
    Spinner,
    Alert
  },

  methods: {
    openModal() {
      this.$refs.signInBaseModalRef.openModal();
    },
    closeModal() {
      this.$refs.signInBaseModalRef.closeModal();
    },

    // https://masteringjs.io/tutorials/fundamentals/email-validation
    // checks if email follows pattern xx@yy.zz
    isEmailValid(email) {
      return /^[^@]+@\w+(\.\w+)+\w$/.test(email);
    },

    areLoginFieldsValid() {
      // "Required field" error will not be shown until user starts typing
      // set errors here if nothing has been entered yet
      if (this.emailField.email.length === 0)
        this.emailField.error = "Required field";
      if (this.passField.pass.length === 0)
        this.passField.error = "Required field";

      return !this.passField.error && !this.emailField.error;
    },

    signIn() {
      this.isSubmittingForm = true;
      this.hasSubmittedForm = false;
      this.isLoginSuccessful = null;

      if (!this.areLoginFieldsValid()) {
        this.hasSubmittedForm = true;
        this.isLoginSuccessful = false;
        this.isSubmittingForm = false;
        this.errorMessage = "Please fix the errors below before continuing.";
        return;
      }

      var loginUrl = process.env.VUE_APP_API_URL + "/auth/login";
      axios
        .post(loginUrl, {
          email: this.emailField.email,
          password: this.passField.pass
        })
        .then(
          response => {
            this.isLoginSuccessful = true;
            this.isSubmittingForm = false;
            this.hasSubmittedForm = true;

            setTimeout(() => {
              this.closeModal();

              // should probably change closeModal to async instead of this
              setTimeout(() => {
                this.checkToken(response.data.access_token);
              }, 250);
            }, 1000);
          },
          error => {
            try {
              if (
                error.response.data.msg != null &&
                error.response.data.msg != ""
              )
                this.errorMessage = error.response.data.msg;
              // else use default errorMessage defined above
            } finally {
              this.isLoginSuccessful = false;
              this.isSubmittingForm = false;
              this.hasSubmittedForm = true;
            }
          }
        );
    },

    // delete this
    checkToken(authToken) {
      var verifyUrl = process.env.VUE_APP_API_URL + "/auth/verify/access";
      axios
        .get(verifyUrl, { headers: { Authorization: "Bearer " + authToken } })
        .then(() => {
          this.$actions.login(authToken);
        })
        .catch(() => {
          Toast.showErrorMessage(
            "Invalid authentication token. Please login again."
          );
        });
    },

    isResetPasswordFieldValid() {
      if (this.resetPassEmailField.email.length === 0)
        this.resetPassEmailField.error = "Required field";

      return !this.resetPassEmailField.error;
    },

    resetPassword() {
      this.resetPassSuccessMessage = "A password reset link has been sent to ";
      this.isSubmittingForm = true;
      this.hasSubmittedForm = false;
      this.isPasswordResetSuccessful = null;

      if (!this.isResetPasswordFieldValid()) {
        this.hasSubmittedForm = true;
        this.isPasswordResetSuccessful = false;
        this.isSubmittingForm = false;
        this.errorMessage = "Please fix the errors below before continuing.";
        return;
      }

      var resetPassUrl =
        process.env.VUE_APP_API_URL + "/auth/reset-pass-request";
      axios
        .post(resetPassUrl, {
          email: this.resetPassEmailField.email
        })
        .then(
          () => {
            this.resetPassSuccessMessage += this.resetPassEmailField.email;
            this.isPasswordResetSuccessful = true;
            this.isSubmittingForm = false;
            this.hasSubmittedForm = true;
          },
          error => {
            try {
              if (
                error.response.data.msg != null &&
                error.response.data.msg != ""
              )
                this.errorMessage = error.response.data.msg;
              // else use default errorMessage defined above
            } finally {
              this.isPasswordResetSuccessful = false;
              this.isSubmittingForm = false;
              this.hasSubmittedForm = true;
            }
          }
        );
    }
  }
};
</script>

<style scoped></style>
