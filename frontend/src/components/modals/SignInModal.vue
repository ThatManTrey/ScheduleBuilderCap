<template>
  <Modal ref="signInBaseModalRef">
    <template v-slot:header> Sign In </template>

    <template v-slot:body>
      <form>
        <div class="mb-3 text-theme-white">
          <label for="userSignInEmail" class="form-label">
            <h6>Email Address</h6>
          </label>
          <span class="form-input-icon" hidden><i class="fas fa-envelope"></i></span>
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
            <a class="link">Forgot your password?</a>
          </div>
        </div>
      </form>
    </template>
    <template v-slot:footer>
      <button type="button" class="btn btn-theme-blacker" @click="closeModal">
        Close
      </button>

      <button type="button" class="btn btn-theme-primary" @click="signIn">
        Continue
      </button>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";

export default {
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
    }
  }
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
