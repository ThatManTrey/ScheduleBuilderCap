/* eslint-disable */
<template lang="html">
  <Modal
    :centerHeader="true"
    :useFooter="false"
    :centerVertically="true"
    ref="addSemesterBaseModalRef"
  >
    <template v-slot:header>Add a Semester</template>
    <template v-slot:body>
      <div class="container">
          <div class="row">
            <div class="col mx-auto">
              <input
                type="text"
                id="newSemesterName"
                class="form-control"
                placeholder="Enter a semester name..."
              />
            </div>
          </div>
          <div class="row">
            <div class="col mt-2 mx-auto">
              <button
                type="submit"
                class="btn btn-theme-confirm btn-sm"
                style="width: 100%;"
              >
                Add Semester
              </button>
            </div>
          </div>
        </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";

export default {
  components: {
    Modal,
  },

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.addSemesterBaseModalRef.openModal();
    },
    closeModal() {
      this.$refs.addSemesterBaseModalRef.closeModal();
    },

  },
};
</script>