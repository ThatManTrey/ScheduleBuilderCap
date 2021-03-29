<template lang="html">
  <Modal
    :useLargeModal="true"
    :useFooter="$store.state.isAuthenticated"
    ref="courseInfoBaseModalRef"
  >
    <template v-slot:header
      >MATH 13013 - Analytic Geometry And Calculus I</template
    >

    <template v-slot:body>
      <div class="container-fluid">
        <div class="row">
          <h5><strong>Description</strong></h5>
          <p>
            Concepts of limit, continuity and derivative, and the indefinite and
            definite integral for functions of one real variable. Maximization,
            related rates, fundamental theorem of calculus. No credit earned
            toward a degree for this course if the student already earned credit
            for MATH 12011 and MATH 12012.
          </p>
        </div>
        <div class="row">
          <p>
            <strong>Prerequisite</strong>: Minimum 78 ALEKS math score; or MATH
            11022 with a minimum C grade.
          </p>
          <p>
            <strong>Attributes</strong>: Kent Core Mathematics and Critical
            Reasoning, Transfer Module Mathematics
          </p>
        </div>
        <div class="row">
          <div class="col-6">
            <p>
              <strong>Credits</strong>: <span id="creditHours">5</span> Credit
              Hours
            </p>
            <p><strong>Schedule Type</strong>: Lecture</p>
          </div>
          <div class="col-6">
            <p><strong>Contact Hours</strong>: 5 lecture</p>
            <p><strong>Grade Mode</strong>: Standard Letter</p>
          </div>
        </div>

        <div class="row text-center">
          <hr class="bg-theme-darkest-gray" size="5" />
          <div class="col">
            Course Quality:
            <h1 class="avg-rating">
              7 / 10
            </h1>
          </div>
          <div class="col">
            Course Difficulty:
            <h1 class="avg-rating">
              5 / 10
            </h1>
          </div>
        </div>
        <div class="text-center">
          <button
            v-if="$store.state.hasConfirmedEmail"
            type="button"
            class="btn btn-theme-primary-dark"
          >
            Add My Rating
          </button>
        </div>
      </div>
    </template>

    <template v-if="$store.state.isAuthenticated" v-slot:footer>
      <div class="d-flex" id="course-info-footer">
        <a
          href="#"
          data-tooltip="Favorite Course"
          data-tooltip-location="bottom"
        >
          <i class="far fa-star fa-lg star-unfilled-icon"></i
        ></a>
        <a
          class="ms-auto"
          @click="openAddToSemesterModal"
          data-tooltip="Add to Semester"
          data-tooltip-location="bottom"
        >
          <i class="fas fa-plus-circle fa-lg plus-add-icon"></i>
        </a>
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

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.courseInfoBaseModalRef.openModal();
    },
    closeModal() {
      this.$refs.courseInfoBaseModalRef.closeModal();
    },
    openAddToSemesterModal() {
      /* avoids nested modals */
      this.closeModal();

      /* needed to prevent scroll bar from showing when switching modals, idk why */
      setTimeout(() => {
        this.$emit("openAddSemesterModal");
      }, 320);
    }
  }
};
</script>

<style scoped>
strong {
  color: var(--theme-whitest);
}

p {
  color: var(--theme-white);
}

#creditHours {
  color: var(--theme-secondary);
  font-weight: 700;
}

#course-info-footer {
  width: 100%;
  font-size: 1.15rem;
}
</style>
