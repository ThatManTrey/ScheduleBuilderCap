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
              id="newSemesterName2"
              class="form-control"
              placeholder="Enter a semester name..."
              v-model.trim="semesterName"
              @keyup.enter="addSemester()"
            />
            <span></span>
          </div>
        </div>
        <div class="row">
          <div class="col mt-2 mx-auto">
            <button
              class="btn btn-theme-confirm btn-sm w-100"
              @click="addSemester()"
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
    Modal
  },

  data() {
    return {
      semesterName: ""
    };
  },

  methods: {
    openModal() {
      this.$refs.addSemesterBaseModalRef.openModal();
    },

    closeModal() {
      this.$refs.addSemesterBaseModalRef.closeModal();
    },

    addSemester() {
      if (this.semesterName > 2) {
        console.log("add semester");

        this.$store.dispatch("semesters/addSemester", this.semesterName);
        this.closeModal();
      }
    }
  }
};
</script>
