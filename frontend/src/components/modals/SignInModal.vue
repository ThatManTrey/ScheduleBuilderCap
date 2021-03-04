<template>
  <Modal ref="signInBaseModalRef">
    <template v-slot:header> Sign In </template>

    <template v-slot:body>
      <form>
        <div class="mb-3 text-theme-white">
          <label for="userEmail" class="form-label">
            <h6>Email Address</h6>
          </label>
          <input
            type="email"
            class="form-control"
            id="userEmail"
            aria-describedby="passHelp"
          />
          <div id="passHelp" class="form-text">
            Don't have an account?
            <a class="link">Register here!</a>
          </div>
        </div>
        <div class="mb-3 text-theme-white">
          <label for="userPass" class="form-label">
            <h6>Password</h6>
          </label>
          <input
            type="password"
            class="form-control"
            id="userPass"
            aria-describedby="passHelp"
          />
          <div id="passHelp" class="form-text">
            <a class="link"
              >Forgot your password?</a
            >
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
        class="btn btn-theme-primary"
        @click="signIn"
      >
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
