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
        ></SemesterAccordion>
      </div>

      <div class="row align-items-center flex-grow-1 mt-3">
        <div class="col text-center">
          <button
            type="button"
            class="btn btn-theme-confirm"
            @click="showAddSemesterModal()"
          >
            <i class="fas fa-plus-circle text-theme-blackest"></i> Add Another
            Semester
          </button>
        </div>
      </div>
    </div>
    <CourseInfoModal
      @openAddSemesterModal="showAddToSemesterModal"
      ref="courseInfoModalSchedule"
    ></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalSchedule"></AddToSemesterModal>
    <AddSemesterModal ref="addSemesterModalSchedule"></AddSemesterModal>
  </div>
</template>

<script lang="js">
import SemesterAccordion from '../components/SemesterAccordion.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue';
import AddSemesterModal from '../components/modals/AddSemesterModal.vue';
import PageSpinner from '../components/spinners/PageSpinner.vue';
import { mapState } from 'vuex';

export default {
    name: 'schedule',

    computed: mapState({
      semesters: state => state.semesters.semesters,
      isLoading: state => state.semesters.isLoadingSemesters
    }),

    components: {
        SemesterAccordion,
        CourseInfoModal,
        AddToSemesterModal,
        AddSemesterModal,
        PageSpinner
    },

    methods: {
      showCourseInfoModal () {
            this.$refs.courseInfoModalSchedule.openModal();
        },
        showAddToSemesterModal () {
            this.$refs.addToSemesterModalSchedule.openModal();
        },
        showAddSemesterModal () {
            this.$refs.addSemesterModalSchedule.openModal();
        },
    },
}
</script>

<style scoped>
div.row {
  min-width: 100%;
}
</style>
