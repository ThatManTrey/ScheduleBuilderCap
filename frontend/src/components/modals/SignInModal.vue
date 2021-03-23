<template>
  <Modal ref="signInBaseModalRef">
    <template v-slot:header>
      <span>Sign In</span>
      <!-- <span v-else>Reset My Password</span> -->
      <span class="ms-2">
        <Spinner :showSpinner="isSubmittingForm" sizeInRem="1.5rem"></Spinner>
      </span>
    </template>

    <template v-slot:body>
      <transition name="fade">
        <div v-if="hasSubmittedForm">
          <Alert
            :isSuccess="isLoginSuccessful"
            :errorMessage="errorMessage"
            successMessage="Login Successful! Closing this window..."
          ></Alert>
        </div>
      </transition>

      <!-- <div
        v-if="isPasswordReset"
        class="alert container bg-theme-success text-theme-whitest container"
        role="alert"
      >
        <div class="row">
          <div class="col-1">
            <i
              class="fas fa-check-circle fa-lg"
              style="vertical-align: -webkit-baseline-middle;"
            ></i>
          </div>
          <div class="col-11">
            Your password has been succesfully reset! Check your email for a
            link.
          </div>
        </div>
      </div> -->

      <form>
        <div class="mb-3 text-theme-white">
          <label for="userSignInEmail" class="form-label">
            <h6>Email Address</h6>
          </label>
          <input
            type="email"
            class="form-control"
            id="userSignInEmail"
            aria-describedby="userSignInEmailHelp"
            placeholder="example@gmail.com"
            :disabled="isSubmittingForm"
            v-model.trim="email"
          />
        </div>

        <div class="mb-3 text-theme-white">
          <label for="userSignInPass" class="form-label">
            <h6>Password</h6>
          </label>
          <span class="form-input-icon"><i class="fas fa-key" hidden></i></span>
          <input
            type="password"
            class="form-control"
            id="userSignInPass"
            aria-describedby="userSignInPassHelp"
            placeholder="Enter password..."
            :disabled="isSubmittingForm"
            v-model.trim="pass"
          />
          <!-- <div id="userSignInPassHelp" class="form-text">
            <a class="link" @click="isResettingPassword = true"
              >Forgot your password?</a
            >
          </div> -->
        </div>
      </form>

      <!-- Password reset -->
      <!-- <form v-else>
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
          id="userResetPassEmail"
          aria-describedby="userResetPassEmailHelp"
        />
        <div id="userResetPassEmailHelp" class="form-text">
          Please enter a valid email
        </div>
      </form> -->
    </template>
    <template v-slot:footer>
      <!-- Login -->
      <div>
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

      <!-- Password reset -->
      <!-- <div v-else>
        <button
          type="button"
          class="btn btn-theme-blacker"
          @click="isResettingPassword = false"
        >
          Cancel
        </button>

        <button
          type="button"
          class="btn btn-theme-primary-dark ms-2"
          @click="resetPassword()"
        >
          Reset My Password
        </button>
      </div> -->
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import axios from "axios";
import Spinner from "../spinners/Spinner.vue";
import Alert from "../Alert.vue";

export default {
  data() {
    return {
      // isResettingPassword: false,
      // isPasswordReset: false,
      email: "",
      pass: "",
      isSubmittingForm: false,
      hasSubmittedForm: false,
      isLoginSuccessful: null,
      errorMessage: "An error has occurred.",
    };
  },

  components: {
    Modal,
    Spinner,
    Alert,
  },

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      // reset login variables to default in case the user tries to login,
      // closes the modal, and then reopens it
      this.email = "";
      this.pass = "";
      (this.isSubmittingForm = false), (this.hasSubmittedForm = false);
      this.isLoginSuccessful = null;

      this.$refs.signInBaseModalRef.openModal();
    },
    closeModal() {
      this.$refs.signInBaseModalRef.closeModal();
    },

    signIn() {
      // add client-side validation checks here

      this.isSubmittingForm = true;
      this.hasSubmittedForm = false;
      this.isLoginSuccessful = null;

      var loginUrl = process.env.VUE_APP_API_URL + "/auth/login";

      axios
        .post(loginUrl, {
          email: this.email,
          password: this.pass,
        })
        .then(
          (response) => {
            this.isLoginSuccessful = true;
            this.isSubmittingForm = false;
            this.hasSubmittedForm = true;

            this.setAuthToken(response.data.access_token);

            setTimeout(() => {
              this.closeModal();
            }, 2000);
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
              this.isLoginSuccessful = false;
              this.isSubmittingForm = false;
              this.hasSubmittedForm = true;
            }
          }
        );
    },

    setAuthToken(token) {
      localStorage.setItem("user", token);
      // set axios default
      this.$emit("checkAuth");
    },

    // resetPassword() {
    //   this.isResettingPassword = false;
    //   this.isPasswordReset = true;
    // },
  },

  created() {
    this.isResettingPassword = false;
    this.isPasswordReset = false;
  },
};
</script>

<style scoped></style>
