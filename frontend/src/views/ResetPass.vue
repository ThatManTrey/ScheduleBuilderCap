<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-lg-4 col-md-6 col-sm-8 col-10">
          <h3 class="text-theme-whitest mb-3">
            Reset Your Password
            <Spinner
              :showSpinner="isSubmittingForm"
              sizeInRem="1.5rem"
            ></Spinner>
          </h3>

          <form @submit.prevent="resetPassword">
            <div class="mb-3 text-theme-white">
              <label for="resetPass" class="form-label">
                <h6>Password</h6>
              </label>

              <input
                type="password"
                class="form-control"
                :class="{ 'form-error': passField.error }"
                id="resetPass"
                placeholder="Enter new password..."
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
              <label for="resetPassVerify" class="form-label">
                <h6>Retype Password</h6>
              </label>
              <input
                type="password"
                class="form-control"
                :class="{ 'form-error': passVerifyField.error }"
                id="resetPassVerify"
                placeholder="Re-enter new password..."
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

            <button
              type="submit"
              :disabled="isSubmittingForm"
              class="btn btn-theme-primary-dark"
              role="submit"
            >
              Reset Password
            </button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import * as Toast from '../toast.js';
import axios from 'axios';
import Spinner from '../components/spinners/Spinner.vue';

export default {
    name: 'reset-pass',
    components: {
        ThemeNavBar,
        Spinner
    },

    data() {
      return {
        resetPassToken: this.$route.query.token,
        passField: {
          pass: "",
          error: null
        },
        passVerifyField: {
          pass: "",
          error: null
        },
        isSubmittingForm: false
      }
    },

     watch: {

      "passField.pass": function() {
        if (this.passField.pass.length === 0)
          this.passField.error = "Required field";
        else if (this.passField.pass.length < 8)
          this.passField.error = "Password must be at least 8 characters long.";
        else this.passField.error = null;
      },

      "passVerifyField.pass": function() {
        if (this.passVerifyField.pass.length === 0)
          this.passVerifyField.error = "Required field";
        else if (this.passVerifyField.pass != this.passField.pass)
          this.passVerifyField.error = "Passwords do not match";
        else this.passVerifyField.error = null;
      }
    },

    methods: {
      areFieldsValid() {
        if (this.passField.pass.length === 0)
          this.passField.error = "Required field";
        if (this.passVerifyField.pass.length === 0)
          this.passVerifyField.error = "Required field";

        return !this.passField.error && !this.passVerifyField.error;
      },

      resetPassword(){
        this.isSubmittingForm = true;

        if (!this.areFieldsValid()) {
          this.isSubmittingForm = false;
          Toast.showErrorMessage("Please fix the errors below before continuing.");
          return;
        }

        axios.post("/auth/reset-pass", 
          { password: this.passField.pass },
          { headers: { Authorization: this.resetPassToken } })
        .then(
          () => {
            this.isSubmittingForm = false;
            this.$router.push('/home');
            Toast.showSuccessMessage("Password reset successfully!")
          },
          error => {
            this.isSubmittingForm = false;
            Toast.showErrorMessage("Error resetting password: ", error);
          }
        );
      }
    },
};
</script>
