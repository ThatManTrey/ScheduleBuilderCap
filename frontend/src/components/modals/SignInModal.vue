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
        <!-- Login alerts -->
        <div v-if="!isResettingPassword">
          <SuccessAlert
            v-if="isLoginSuccessful"
            successMessage="Login Successful! Closing this window..."
          ></SuccessAlert>

          <ErrorAlert
            v-if="isLoginSuccessful === false"
            :errorMessage="errorMessage"
          ></ErrorAlert>
        </div>

        <!-- Password reset alerts -->
        <div v-else>
          <SuccessAlert
            v-if="isPasswordResetSuccessful"
            :successMessage="resetPassSuccessMessage"
          ></SuccessAlert>

          <ErrorAlert
            v-if="isPasswordResetSuccessful === false"
            :errorMessage="errorMessage"
          ></ErrorAlert>
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
            ref="signInEmailField"
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
            @keyup.enter="signIn()"
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
            <a
              tabindex="0"
              @keyup.enter="isResettingPassword = true"
              class="link"
              id="padding"
              @click="isResettingPassword = true"
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

        <label for="userResetPassEmail" class="visually-hidden form-label">
          <h6>Email Address</h6>
        </label>

        <input
          type="email"
          class="form-control"
          :class="{ 'form-error': resetPassEmailField.error }"
          id="userResetPassEmail"
          placeholder="Enter email..."
          @keyup.enter="resetPassword()"
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
        <button
          type="button"
          class="btn btn-theme-blacker"
          @click="closeModal"
          :disabled="isSubmittingForm"
        >
          Close
        </button>

        <button
          type="button"
          class="btn btn-theme-primary-dark ms-2"
          @click="signIn"
          :disabled="isSubmittingForm"
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
          :disabled="isSubmittingForm"
        >
          Go Back
        </button>

        <button
          type="button"
          class="btn btn-theme-primary-dark ms-2"
          @click="resetPassword()"
          :disabled="isSubmittingForm"
        >
          Reset My Password
        </button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import Spinner from "../spinners/Spinner.vue";
import SuccessAlert from "../alerts/SuccessAlert.vue";
import ErrorAlert from "../alerts/ErrorAlert.vue";
import { validateEmailField, validatePassField } from "../../utils";
import axios from "axios";

function initialState() {
  return {
    emailField: {
      email: null,
      error: null
    },
    passField: {
      pass: null,
      error: null
    },
    resetPassEmailField: {
      email: null,
      error: null
    },
    isSubmittingForm: false,
    isLoginSuccessful: null,
    isResettingPassword: false,
    isPasswordResetSuccessful: null,
    errorMessage: "",
    resetPassSuccessMessage: ""
  };
}

export default {
  data() {
    return initialState();
  },

  watch: {
    "emailField.email": function() {
      validateEmailField(this.emailField);
    },

    "resetPassEmailField.email": function() {
      validateEmailField(this.resetPassEmailField);
    },

    "passField.pass": function() {
      validatePassField(this.passField, false);
    }
  },

  components: {
    Modal,
    Spinner,
    SuccessAlert,
    ErrorAlert
  },

  methods: {
    openModal() {
      this.$refs.signInBaseModalRef.openModal();

      // timeout is needed to wait for modal opening to finish
      setTimeout(() => {
        this.$refs.signInEmailField.focus();
      }, 500);
    },
    closeModal() {
      this.$refs.signInBaseModalRef.closeModal();
      Object.assign(this.$data, initialState());
    },

    preventClosingModal() {
      this.$refs.signInBaseModalRef.preventClosingModal();
    },

    allowClosingModal() {
      this.$refs.signInBaseModalRef.allowClosingModal();
    },

    areLoginFieldsValid() {
      // "Required field" error will not be shown until user starts typing
      // set errors here if nothing has been entered yet
      if (this.emailField.email === null) this.emailField.email = "";
      if (this.passField.pass === null) this.passField.pass = "";

      validateEmailField(this.emailField);
      validatePassField(this.passField, false);

      return !this.passField.error && !this.emailField.error;
    },

    signIn() {
      this.isSubmittingForm = true;
      this.isLoginSuccessful = null;

      if (!this.areLoginFieldsValid()) {
        this.isLoginSuccessful = false;
        this.isSubmittingForm = false;
        this.errorMessage = "Please fix the errors below before continuing.";
        return;
      }

      this.preventClosingModal();

      this.$store
        .dispatch({
          type: "auth/logIn",
          email: this.emailField.email,
          password: this.passField.pass
        })
        .then(() => {
          this.isSubmittingForm = false;
          this.allowClosingModal();

          if (this.$store.state.auth.authError) {
            this.isLoginSuccessful = false;
            this.errorMessage = this.$store.state.auth.authError;
          } else {
            this.isLoginSuccessful = true;

            setTimeout(() => {
              this.closeModal();
            }, 1000);
          }
        });
    },

    isResetPasswordFieldValid() {
      if (this.resetPassEmailField.email === null)
        this.resetPassEmailField.email = "";
      validateEmailField(this.resetPassEmailField);

      return !this.resetPassEmailField.error;
    },

    resetPassword() {
      this.resetPassSuccessMessage = "A password reset link has been sent to ";
      this.isSubmittingForm = true;
      this.isPasswordResetSuccessful = null;

      if (!this.isResetPasswordFieldValid()) {
        this.isPasswordResetSuccessful = false;
        this.isSubmittingForm = false;
        this.errorMessage = "Please fix the errors below before continuing.";
        return;
      }

      this.preventClosingModal();

      axios
        .post("/auth/reset-pass-request", {
          email: this.resetPassEmailField.email
        })
        .then(
          () => {
            this.isPasswordResetSuccessful = true;
            this.isSubmittingForm = false;

            this.resetPassSuccessMessage += this.resetPassEmailField.email;
            this.allowClosingModal();
          },
          () => {
            this.isPasswordResetSuccessful = false;
            this.isSubmittingForm = false;

            this.errorMessage =
              "An unexpected error has occurred. Please try again.";
            this.allowClosingModal();
          }
        );
    }
  }
};
</script>

<style scoped>
.input-container {
  display: flex;
  width: 100%;
}

#icon {
  padding: 10px;
  min-width: 2.5rem;
  border: none;
  box-shadow: none;
  background: var(--theme-darkest-gray);
  text-align: center;
}

#userSignInEmail {
  width: 100%;
}

#userSignInPass {
  width: 100%;
}

#userSignInPassHelp {
  margin-top: 1rem;
}
</style>
