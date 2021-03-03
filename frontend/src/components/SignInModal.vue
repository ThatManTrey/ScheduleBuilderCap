<template>
  <div
    class="modal fade"
    id="signInModal"
    tabindex="-1"
    aria-labelledby="signInModalLabel"
    aria-hidden="true"
    ref="signInModal"
  >
    <div class="modal-dialog">
      <div class="theme-modal-content">
        <div class="theme-modal-header">
          <h5 class="modal-title" id="signInModalLabel">Sign In</h5>

          <button type="button" class="button-as-link" data-bs-dismiss="modal">
            <i class="fas fa-times fa-lg text-theme-lightest-gray"></i>
          </button>
        </div>

        <div class="theme-modal-body">
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
                  Don't have an account? <a class="link" @click="openRegisterModal">Register here!</a>
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
                  <a class="link" @click="openResetPasswordModal">Forgot your password?</a>
              </div>
            </div>
          </form>
          </div>

        <div class="theme-modal-footer">
          <button
            type="button"
            class="btn btn-theme-black"
            data-bs-dismiss="modal"
          >
            Close
          </button>

          <button
            type="button"
            class="btn btn-theme-primary"
            data-bs-dismiss="modal"
            @click="signIn"
          >
            Continue
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import bootstrap from "bootstrap/dist/js/bootstrap.bundle.min.js";

export default {
  data() {
    return {
      modal: null,
    };
  },

  methods: {
    openModal() {
      this.modal.show();
    },

    signIn() {
      this.$emit('signIn');
    }
  },

  // runs after element references are created so modal is not undefined
  mounted() {
    this.modal = new bootstrap.Modal(this.$refs.signInModal);
  },
};
</script>
