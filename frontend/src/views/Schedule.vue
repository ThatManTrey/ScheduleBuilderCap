<template lang="html">
  <div class="d-flex flex-grow-1">
    <PageSpinner :showSpinner="isLoading"></PageSpinner>

    <div
      v-if="!isLoading"
      class="container mt-3 mb-5 d-flex flex-grow-1 flex-column"
    >
      <div
        v-for="(semester, index) in semesters"
        :key="index"
        class="row align-items-center flex-grow-1 my-3"
      >
        <SemesterAccordion
          :targetName="'semester' + index"
          :semester="semester"
          @showCourseInfoModal="showCourseInfoModal"
          @showAddToSemesterModal="showAddToSemesterModal"
          @openAddRatingModal="showAddRatingModal"
          @openViewRatingModal="showViewRatingModal"
        ></SemesterAccordion>
      </div>

      <div class="row align-items-center flex-grow-1 mt-3">
        <div class="col text-center">
          <button
            type="button"
            class="btn btn-theme-confirm"
            @click="showAddSemesterModal()"
          >
            <i class="fas fa-plus-circle text-theme-blackest"></i>
            Add Semester
          </button>
        </div>
      </div>
    </div>
    <CourseInfoModal
      @openAddSemesterModal="showAddToSemesterModal"
      @openAddRatingModal="showAddRatingModal"
      @openViewRatingModal="showViewRatingModal"
      ref="courseInfoModalSchedule"
    ></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalSchedule"></AddToSemesterModal>
    <AddSemesterModal ref="addSemesterModalSchedule"></AddSemesterModal>
    <AddRatingModal ref="addRatingModalSchedule"></AddRatingModal>
    <ViewRatingModal
      @openAddRatingModal="showAddRatingModal"
      ref="viewRatingModalSchedule"
    ></ViewRatingModal>
  </div>
</template>

<script lang="js">
import SemesterAccordion from '../components/SemesterAccordion.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue';
import AddSemesterModal from '../components/modals/AddSemesterModal.vue';
import AddRatingModal from '../components/modals/AddRatingModal.vue';
import ViewRatingModal from '../components/modals/ViewRatingModal.vue';
import PageSpinner from '../components/spinners/PageSpinner.vue';
import { mapState } from 'vuex';

export default {
    name: 'schedule',

    computed: mapState({
      semesters: state => state.semesters.semesters,
      isLoading: state => state.semesters.isLoadingSemesters,
      course: state => state.courses.currentCourse,
    }),

    components: {
        SemesterAccordion,
        CourseInfoModal,
        AddToSemesterModal,
        AddSemesterModal,
        AddRatingModal,
        ViewRatingModal,
        PageSpinner
    },

    methods: {
      showCourseInfoModal () {
            this.$store.dispatch("ratings/getCourseRatings", { course: this.course });
            this.$store.dispatch("ratings/getUserCourseRating", {
              course: this.course
            });
            this.$refs.courseInfoModalSchedule.openModal();
        },
        showAddToSemesterModal () {
            this.$refs.addToSemesterModalSchedule.openModal();
        },
        showAddSemesterModal () {
            this.$refs.addSemesterModalSchedule.openModal();
        },
        showAddRatingModal () {
          this.$refs.addRatingModalSchedule.openModal();
        },
        showViewRatingModal () {
          this.$refs.viewRatingModalSchedule.openModal();
        },
    },
}
</script>

<style scoped>
div.row {
  min-width: 100%;
}
</style>
