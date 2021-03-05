<template>
  <Modal ref="signInBaseModalRef">
    <template v-slot:header>
      <span v-if="!isResettingPassword">Sign In</span>
      <span v-else>Reset My Password</span>
    </template>

    <template v-slot:body>
      <!-- Login -->

      <div v-if="isPasswordReset" class="alert bg-theme-success text-theme-blackest" role="alert">
        <i class="fas fa-check-circle fa-lg"></i> &nbsp;
        Your password has been succesfully reset! Check your email for a link.
      </div>

      <form v-if="!isResettingPassword">
        <div class="mb-3 text-theme-white">
          <label for="userSignInEmail" class="form-label">
            <h6>Email Address</h6>
          </label>
          <span class="form-input-icon" hidden
            ><i class="fas fa-envelope"></i
          ></span>
          <input
            type="email"
            class="form-control"
            id="userSignInEmail"
            aria-describedby="userSignInEmailHelp"
          />
          <div id="userSignInEmailHelp" class="form-text">
            Please enter a valid email
          </div>
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
          />
          <div id="userSignInPassHelp" class="form-text">
            <a class="link" @click="isResettingPassword = true"
              >Forgot your password?</a
            >
          </div>
        </div>
      </form>

      <!-- Password reset -->
      <form v-else>
        <p>Enter your email below and we'll send you a link to reset your password.</p>

        <label for="userResetPassEmail" class="form-label">
            <h6>Email Address</h6>
          </label>
          <span class="form-input-icon" hidden
            ><i class="fas fa-envelope"></i
          ></span>
          <input
            type="email"
            class="form-control"
            id="userResetPassEmail"
            aria-describedby="userResetPassEmailHelp"
          />
          <div id="userResetPassEmailHelp" class="form-text">
            Please enter a valid email
          </div>

      </form>

    </template>
    <template v-slot:footer>
      <!-- Login -->
      <div v-if="!isResettingPassword">
        <button type="button" class="btn btn-theme-blacker" @click="closeModal">
          Close
        </button>

        <button type="button" class="btn btn-theme-primary ms-2" @click="signIn">
          Continue
        </button>
      </div>

      <!-- Password reset -->
      <div v-else>
        <button type="button" class="btn btn-theme-blacker" @click="isResettingPassword = false">
          Cancel
        </button>

        <button type="button" class="btn btn-theme-primary ms-2" @click="resetPassword()">
          Reset My Password
        </button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";

export default {
  data() {
    return {
      isResettingPassword: false,
      isPasswordReset: false
    }
  },

  components: {
    Modal
  },

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.signInBaseModalRef.openModal();
    },
    closeModal() {
      this.$refs.signInBaseModalRef.closeModal();
    },

    signIn() {
      this.$emit("signIn");
      this.closeModal();
    },

    resetPassword() {
      this.isResettingPassword = false;
      this.isPasswordReset = true;
    }
  },
};
</script>

<style scoped>
/* 
.form-input-icon {
  position: absolute;
  top: 56px;
  left: 30px;
  font-size: 1.25rem;
} */
</style>
