<template lang="html">
  <Modal
    :centerHeader="true"
    :useFooter="false"
    :centerVertically="true"
    ref="addSemesterBaseModalRef"
  >
    <template v-slot:header>
      Add a Semester
      <span class="ms-2">
        <Spinner :showSpinner="isLoading" sizeInRem="1.5rem"></Spinner>
      </span>
    </template>

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
import Spinner from "../spinners/Spinner";

export default {
  components: {
    Modal,
    Spinner,
  },

  data() {
    return {
      semesterName: "",
      isLoading: false,
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
      this.isLoading = true;

      if (this.semesterName.length === 0) {
        const semesterNumber = this.$store.state.semesters.semesters.length + 1;
        this.semesterName = "Semester " + semesterNumber;
      } else if (this.semesterName.length > 64) {
        this.semesterName = this.semesterName.slice(0, 64);
      }

      this.$store
        .dispatch("semesters/addSemester", this.semesterName)
        .then(() => {
          this.isLoading = false;
          this.semesterName = "";
          this.closeModal();
        });
    },
  },
};
</script>
