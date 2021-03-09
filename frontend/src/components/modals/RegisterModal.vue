<template>
  <Modal ref="registerBaseModalRef">
    <template v-slot:header> Create An Account </template>

    <template v-slot:body>
      <form>
        <div class="mb-3 text-theme-white">
          <label for="userRegisterEmail" class="form-label">
            <h6>Email Address</h6>
          </label>
          <input type="email" class="form-control" id="userRegisterEmail" />
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

      <button type="button" class="btn btn-theme-primary" @click="register">
        Sign Up
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
      this.$refs.registerBaseModalRef.openModal();
    },
    closeModal() {
      this.$refs.registerBaseModalRef.closeModal();
    },

    register() {
      this.$emit("register");
      this.closeModal();
    }
  }
};
</script>
