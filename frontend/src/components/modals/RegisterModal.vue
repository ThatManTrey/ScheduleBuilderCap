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
        <div class="mb-3" v-if="hasSubmittedForm">
          <div
            class="alert container bg-theme-success text-theme-whitest container"
            role="alert"
            v-if="isRegisterSuccessful"
          >
            <div class="row">
              <div class="col-1">
                <i class="fas fa-check-circle fa-lg"></i>
              </div>
              <div class="col-11">
                Account created successfully! Check your email for a
                confirmation link.
              </div>
            </div>
          </div>

          <div
            class="alert container bg-theme-warning-dark text-theme-whitest container"
            role="alert"
            v-if="!isRegisterSuccessful"
          >
            <div class="row">
              <div class="col-1">
                <i class="fas fa-times-circle fa-lg"></i>
              </div>
              <div class="col-11">
                {{ errorMessage }}
              </div>
            </div>
          </div>
        </div>
      </transition>

      <form @submit.prevent="register()">
        <div class="mb-3 text-theme-white">
          <label for="userRegisterEmail" class="form-label">
            <h6>Email Address</h6>
          </label>
          <input
            type="email"
            class="form-control"
            id="userRegisterEmail"
            placeholder="example@gmail.com"
            :disabled="isSubmittingForm"
            v-model="registerForm.email"
          />
        </div>

        <div class="mb-3 text-theme-white">
          <label for="userRegisterPass" class="form-label">
            <h6>Password</h6>
          </label>
          <input
            type="password"
            class="form-control"
            id="userRegisterPass"
            aria-describedby="userRegisterPassHelp"
            placeholder="Enter password..."
            :disabled="isSubmittingForm"
            v-model="registerForm.pass"
          />
          <div id="userRegisterPassHelp" class="form-text">
            Passwords must be more than x characters long
          </div>
        </div>

        <div class="mb-3 text-theme-white">
          <label for="userRegisterRetypePass" class="form-label">
            <h6>Retype Password</h6>
          </label>
          <input
            type="password"
            class="form-control"
            id="userRegisterRetypePass"
            aria-describedby="userRegisterRetypePassHelp"
            placeholder="Re-enter password..."
            :disabled="isSubmittingForm"
            v-model="registerForm.passVerify"
          />
          <div id="userRegisterRetypePassHelp" class="form-text">
            Passwords must match
          </div>
        </div>
      </form>
    </template>
    <template v-slot:footer>
      <button type="button" class="btn btn-theme-blacker" @click="closeModal">
        Close
      </button>

      <button
        type="button"
        class="btn btn-theme-primary-dark"
        @click="register"
        :disabled="isSubmittingForm"
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

export default {
  data() {
    return {
      registerForm: {
        email: "",
        pass: "",
        passVerify: ""
      },
      isSubmittingForm: false,
      hasSubmittedForm: false,
      isRegisterSuccessful: null,
      errorMessage: ""
    };
  },

  components: {
    Modal,
    Spinner
  },

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.registerBaseModalRef.openModal();
    },
    closeModal() {
      this.$refs.registerBaseModalRef.closeModal();
    },

    register() {
      this.isSubmittingForm = true;
      // hide previous alerts
      this.hasSubmittedForm = false;
      this.isRegisterSuccessful = null;

      var registerUrl = process.env.VUE_APP_API_URL + "/auth/register";

      if (this.registerForm.pass == this.registerForm.passVerify) {
        axios
          .post(registerUrl, {
            email: this.registerForm.email,
            password: this.registerForm.pass
          })
          .then(
            () => {
              this.isRegisterSuccessful = true;
              this.isSubmittingForm = false;
              this.hasSubmittedForm = true;
            },
            error => {
              this.isRegisterSuccessful = false;
              this.isSubmittingForm = false;
              this.hasSubmittedForm = true;
              // if the error response does not have a msg attribute, set a default error message
              try {
                if (
                  error.response.data.msg != null &&
                  error.response.data.msg != ""
                )
                  this.errorMessage = error.response.data.msg;
                else this.errorMessage = "An error has occurred.";
              } catch (err) {
                this.errorMessage = "An error has occurred.";
              }
            }
          );
      } else {
        console.log("Passwords do not match");
      }
    }
  }
};
</script>
