<template lang="html">
  <div>
    <div class="myContainer">
      <div class="row justify-content-center myRow">
        <div class="col-xxl-2 col-xl-3 col-lg-4 col-md-5 col-sm-8 col-10">
          <h3 class="text-theme-whitest mb-5 text-center">
            Reset Your Password
            <Spinner
              :showSpinner="isSubmittingForm"
              sizeInRem="1.5rem"
            ></Spinner>
          </h3>

          <form @submit.prevent="resetPassword">
            <div class="mb-3 text-theme-white">
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
              class="btn btn-theme-primary-dark w-100"
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
import * as Toast from '../toast.js';
import axios from 'axios';
import Spinner from '../components/spinners/Spinner.vue';
import { validatePassField, validatePassVerifyField, } from "../utils.js";

export default {
    name: 'reset-pass',
    components: {
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
        validatePassField(this.passField);
      },

      "passVerifyField.pass": function() {
        validatePassVerifyField(this.passVerifyField, this.passField);
      }
    },

    methods: {
      areFieldsValid() {
        validatePassField(this.passField);
        validatePassVerifyField(this.passVerifyField, this.passField);

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
          () => {
            this.isSubmittingForm = false;
            Toast.showErrorMessage("Error resetting password. Please try again.");
          }
        );
      }
    },
};
</script>

<style scoped>
.myContainer {
  min-height: 30rem;
  overflow: hidden;
}

.myRow {
  min-height: 100%;
  margin-top: 13%;
}
</style>
