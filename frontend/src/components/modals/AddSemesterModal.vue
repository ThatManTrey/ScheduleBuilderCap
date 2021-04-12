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

        <span v-if="validationError" class="form-error-text mb-2">
          <i class="fas fa-times-circle text-theme-warning-light"></i>
          {{ validationError }}
        </span>
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
    Spinner
  },

  data() {
    return {
      semesterName: "",
      isLoading: false,
      validationError: null
    }
  },

  methods: {
    openModal() {
      this.$refs.addSemesterBaseModalRef.openModal();
    },

    closeModal() {
      this.$refs.addSemesterBaseModalRef.closeModal();
    },

    addSemester() {
      if (this.semesterName.length > 0 && this.semesterName.length < 64) {
        this.isLoading = true;
        this.validationError = null;

        this.$store.dispatch("semesters/addSemester", this.semesterName).then(() =>  {
          this.isLoading = false;
          this.semesterName = "";
          this.closeModal();
        });  
      } else if(this.semesterName.length < 1) {
        this.validationError = "Please a semester name.";
      } else {
        this.validationError = "Please enter a shorter semester name.";
      }    
    }
  }
};
</script>
