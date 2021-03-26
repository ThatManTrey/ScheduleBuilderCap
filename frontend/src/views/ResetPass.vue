<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <PageSpinner
      v-if="isLoadingPage"
      :showSpinner="isLoadingPage"
    ></PageSpinner>
    <div v-else class="container mt-5">
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
import PageSpinner from '../components/spinners/PageSpinner.vue';
import Spinner from '../components/spinners/Spinner.vue';

export default {
    name: 'reset-pass',
    components: {
        ThemeNavBar,
        PageSpinner,
        Spinner
    },

    data() {
      return {
        resetPassToken: String,
        passField: {
          pass: "",
          error: null
        },
        passVerifyField: {
          pass: "",
          error: null
        },
        isLoadingPage: true,
        isSubmittingForm: false,
        hasSubmittedForm: false,
      }
    },

     watch: {

      "passField.pass": function() {
        if (this.passField.pass.length === 0)
          this.passField.error = "Required field";
        else if (this.passField.pass.length < 8)
          this.passField.error = "Password must be more than 8 characters long.";
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
      verifyResetToken() {

        if(this.resetPassToken) {
          var verifyUrl = process.env.VUE_APP_API_URL + "/auth/verify/reset-pass";
          axios
          .get(verifyUrl, { headers: { Authorization: "Bearer " + this.resetPassToken } })
          .then(() => {
            this.isLoadingPage = false;
          })
          .catch(() => {
            this.$router.push('home');
            Toast.showErrorMessage(
              "Invalid or expired authentication token. Request another reset link and try again."
            );
          });
        } else {
          this.$router.push('home');
          Toast.showErrorMessage("Invalid reset password token.");
        }
      },

      areFieldsValid() {
        if (this.passField.pass.length === 0)
          this.passField.error = "Required field";
        if (this.passVerifyField.pass.length === 0)
          this.passVerifyField.error = "Required field";

        return !this.passField.error && !this.passVerifyField.error;
      },

      resetPassword(){
        this.isSubmittingForm = true;
        this.hasSubmittedForm = false;

        if (!this.areFieldsValid()) {
          this.hasSubmittedForm = true;
          this.isSubmittingForm = false;
          Toast.showErrorMessage("Please fix the errors below before continuing.");
          return;
        }

      var resetPassUrl = process.env.VUE_APP_API_URL + "/auth/reset-pass";

      axios
        .post(resetPassUrl, {
          password: this.passField.pass
        },
        { headers: { Authorization: "Bearer " + this.resetPassToken } })
        .then(
          () => {
            this.isSubmittingForm = false;
            this.hasSubmittedForm = true;
            Toast.showSuccessMessage("Password reset successfully!")
          },
          error => {
            this.isSubmittingForm = false;
            this.hasSubmittedForm = true;
            Toast.showErrorMessage("Error resetting password: ", error);
          }
        );
      }
    },

    created() {
      this.resetPassToken = this.$route.query.token;
      this.verifyResetToken();
    }
};
</script>