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
          successMessage="Account created successfully! Check your email for confirmation link."
        ></SuccessAlert>

        <ErrorAlert
          v-if="isRegisterSuccessful == false"
          :errorMessage="errorMessage"
        ></ErrorAlert>
      </transition>

      <form>
        <div class="mb-3 text-theme-white">
          <label for="userRegisterEmail" class="form-label">
            <h6>Email Address</h6>
          </label>

          <input
            type="email"
            class="form-control"
            :class="{ 'form-error': emailField.error }"
            id="userRegisterEmail"
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

        <div class="mb-3 text-theme-white">
          <label for="userRegisterPass" class="form-label">
            <h6>Password</h6>
          </label>

          <input
            type="password"
            class="form-control"
            :class="{ 'form-error': passField.error }"
            id="userRegisterPass"
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
        </div>

        <div class="mb-3 text-theme-white">
          <label for="userRegisterRetypePass" class="form-label">
            <h6>Retype Password</h6>
          </label>
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
      <button type="button" class="btn btn-theme-blacker" @click="closeModal">
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
import axios from "axios";
import Spinner from "../spinners/Spinner.vue";
import SuccessAlert from "../alerts/SuccessAlert.vue";
import ErrorAlert from "../alerts/ErrorAlert.vue";

export default {
  data() {
    return {
      emailField: {
        email: "",
        error: null,
      },
      passField: {
        pass: "",
        error: null,
      },
      passVerifyField: {
        pass: "",
        error: null,
      },
      isSubmittingForm: false,
      isRegisterSuccessful: null,
      errorMessage: "An error occurred. Please try again.",
    };
  },

  watch: {
    "emailField.email": function () {
      if (this.emailField.email.length === 0)
        this.emailField.error = "Required field";
      else if (!this.isEmailValid())
        this.emailField.error = "Please enter a valid email";
      else this.emailField.error = null;
    },

    "passField.pass": function () {
      if (this.passField.pass.length === 0)
        this.passField.error = "Required field";
      else if (this.passField.pass.length < 8)
        this.passField.error = "Password must be more than 8 characters long.";
      else this.passField.error = null;
    },

    "passVerifyField.pass": function () {
      if (this.passVerifyField.pass.length === 0)
        this.passVerifyField.error = "Required field";
      else if (this.passVerifyField.pass != this.passField.pass)
        this.passVerifyField.error = "Passwords do not match";
      else this.passVerifyField.error = null;
    },
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
    },
    closeModal() {
      this.$refs.registerBaseModalRef.closeModal();
    },

    // https://masteringjs.io/tutorials/fundamentals/email-validation
    // checks if email follows pattern xx@yy.zz
    isEmailValid() {
      return /^[^@]+@\w+(\.\w+)+\w$/.test(this.emailField.email);
    },

    areFieldsValid() {
      // "Required field" and password not matching errors will
      // not be shown until user starts typing
      // set errors here if nothing has been entered yet
      if (this.passVerifyField.pass != this.passField.pass)
        this.passVerifyField.error = "Passwords do not match";

      if (this.emailField.email.length === 0)
        this.emailField.error = "Required field";
      if (this.passField.pass.length === 0)
        this.passField.error = "Required field";
      if (this.passVerifyField.pass.length === 0)
        this.passVerifyField.error = "Required field";

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

      var registerUrl = process.env.VUE_APP_API_URL + "/auth/register";

      axios
        .post(registerUrl, {
          email: this.emailField.email,
          password: this.passField.pass,
        })
        .then(
          () => {
            this.isRegisterSuccessful = true;
            this.isSubmittingForm = false;
          },
          (error) => {
            try {
              if (
                error.response.data.msg != null &&
                error.response.data.msg != ""
              )
                this.errorMessage = error.response.data.msg;
              // else use default errorMessage defined above
            } finally {
              this.isRegisterSuccessful = false;
              this.isSubmittingForm = false;
            }
          }
        );
    },
  },
};
</script>
