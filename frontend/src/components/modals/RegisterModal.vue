<template>
  <Modal ref="registerBaseModalRef">
    <template v-slot:header>
      Create An Account
      <span class="ms-2">
        <Spinner :showSpinner="isSubmittingForm" sizeInRem="1.5rem"></Spinner>
      </span>
    </template>

    <template v-slot:body>
      <transition name="fade">
        <SuccessAlert
          v-if="isRegisterSuccessful"
          :successMessage="successMessage"
        ></SuccessAlert>

        <ErrorAlert
          v-if="isRegisterSuccessful === false"
          :errorMessage="errorMessage"
        ></ErrorAlert>
      </transition>

      <form>
        <div class="mb-3 text-theme-white">
          <label for="userRegisterEmail" class="form-label">
            <h6>Email Address</h6>
          </label>

          <div class="input-container">
            <i class="fas fa-envelope fa-md text-theme-blacker" id="icon"></i>
            <input
              type="email"
              class="form-control"
              :class="{ 'form-error': emailField.error }"
              id="userRegisterEmail"
              placeholder="example@gmail.com"
              :disabled="isSubmittingForm"
              v-model.trim="emailField.email"
              ref="registerEmailField"
            />
          </div>

          <transition name="fade">
            <span v-if="emailField.error" class="form-error-text">
              <i class="fas fa-times-circle text-theme-warning-light"></i>
              {{ emailField.error }}
            </span>
          </transition>
        </div>

        <div class="mb-3 text-theme-white">
          <label for="userRegisterPass" class="form-label">
            <h6>Password</h6>
          </label>

          <div class="input-container">
            <i class="fas fa-key fa-md text-theme-blacker" id="icon"></i>
            <input
              type="password"
              class="form-control"
              :class="{ 'form-error': passField.error }"
              id="userRegisterPass"
              placeholder="Enter password..."
              :disabled="isSubmittingForm"
              v-model="passField.pass"
            />
          </div>

          <transition name="fade">
            <span v-if="passField.error" class="form-error-text">
              <i class="fas fa-times-circle text-theme-warning-light"></i>
              {{ passField.error }}
            </span>
          </transition>
        </div>

        <div class="mb-3 text-theme-white">
          <label for="userRegisterRetypePass" class="form-label">
            <h6>Retype Password</h6>
          </label>

          <div class="input-container">
            <i class="fas fa-key fa-md text-theme-blacker" id="icon"></i>
            <input
              type="password"
              class="form-control"
              :class="{ 'form-error': passVerifyField.error }"
              id="userRegisterRetypePass"
              placeholder="Re-enter password..."
              @keyup.enter="register()"
              :disabled="isSubmittingForm"
              v-model="passVerifyField.pass"
            />
          </div>

          <transition name="fade">
            <span v-if="passVerifyField.error" class="form-error-text">
              <i class="fas fa-times-circle text-theme-warning-light"></i>
              {{ passVerifyField.error }}
            </span>
          </transition>
        </div>
      </form>
    </template>

    <template v-slot:footer>
      <button
        type="button"
        class="btn btn-theme-blacker"
        :disabled="isSubmittingForm"
        @click="closeModal"
      >
        Close
      </button>

      <button
        class="btn btn-theme-primary-dark"
        :disabled="isSubmittingForm"
        @click="register()"
      >
        Sign Up
      </button>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import Spinner from "../spinners/Spinner.vue";
import SuccessAlert from "../alerts/SuccessAlert.vue";
import ErrorAlert from "../alerts/ErrorAlert.vue";
import {
  validateEmailField,
  validatePassField,
  validatePassVerifyField
} from "../../utils.js";

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
    passVerifyField: {
      pass: null,
      error: null
    },
    isSubmittingForm: false,
    isRegisterSuccessful: null,
    errorMessage: "An error occurred. Please try again.",
    successMessage: ""
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

    "passField.pass": function() {
      validatePassField(this.passField);
    },

    "passVerifyField.pass": function() {
      validatePassVerifyField(this.passVerifyField, this.passField);
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
      this.$refs.registerBaseModalRef.openModal();

      // timeout is needed to wait for modal opening to finish
      setTimeout(() => {
        this.$refs.registerEmailField.focus();
      }, 500);
    },

    closeModal() {
      this.$refs.registerBaseModalRef.closeModal();
      Object.assign(this.$data, initialState());
    },

    preventClosingModal() {
      this.$refs.registerBaseModalRef.preventClosingModal();
    },

    allowClosingModal() {
      this.$refs.registerBaseModalRef.allowClosingModal();
    },

    areFieldsValid() {
      // "Required field" and password not matching errors will
      // not be shown until user starts typing
      // set errors here if nothing has been entered yet
      if (this.emailField.email === null) this.emailField.email = "";
      if (this.passField.pass === null) this.passField.pass = "";
      if (this.passVerifyField.pass === null) this.passVerifyField.pass = "";

      validateEmailField(this.emailField);
      validatePassField(this.passField);
      validatePassVerifyField(this.passVerifyField, this.passField);

      return (
        !this.passField.error &&
        !this.emailField.error &&
        !this.passVerifyField.error
      );
    },

    register() {
      this.isSubmittingForm = true;
      this.isRegisterSuccessful = null;

      if (!this.areFieldsValid()) {
        this.isRegisterSuccessful = false;
        this.isSubmittingForm = false;
        this.errorMessage = "Please fix the errors below before continuing.";
        return;
      }

      this.preventClosingModal();

      this.$store
        .dispatch({
          type: "auth/register",
          email: this.emailField.email,
          password: this.passField.pass
        })
        .then(() => {
          if (this.$store.state.auth.authError) {
            this.isSubmittingForm = false;
            this.isRegisterSuccessful = false;
            this.errorMessage = this.$store.state.auth.authError;
            this.allowClosingModal();
          } else {
            this.$store
              .dispatch({
                type: "auth/logIn",
                email: this.emailField.email,
                password: this.passField.pass
              })
              .then(() => {
                if (this.$store.state.auth.authError) {
                  this.successMessage =
                    "Account created successfully! You can now log in.";
                } else {
                  this.successMessage =
                    "Account created successfully! Logging you in...";

                  setTimeout(() => {
                    this.closeModal();
                  }, 1000);
                }

                this.isSubmittingForm = false;
                this.isRegisterSuccessful = true;
                this.allowClosingModal();
              });
          }
        });
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

#userRegisterEmail {
  width: 100%;
}

#userRegisterPass {
  width: 100%;
}
</style>
