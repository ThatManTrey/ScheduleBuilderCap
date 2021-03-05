<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <div class="container mt-3 mb-5">
      <div v-for="n in 4" :key="n" class="row">
        <SemesterAccordion
          :targetName="'example' + n"
          @showCourseInfoModal="showCourseInfoModal"
          @showAddToSemesterModal="showAddToSemesterModal"
        ></SemesterAccordion>
      </div>

      <div class="row mt-3">
        <div class="col text-center">
          <button type="button" class="btn btn-theme-confirm" @click="showAddSemesterModal()">
            <i class="fas fa-plus-circle text-theme-blackest"></i> Add Another Semester
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
import ThemeNavBar from '../components/ThemeNavBar.vue';
import SemesterAccordion from '../components/SemesterAccordion.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue';
import AddSemesterModal from '../components/modals/AddSemesterModal.vue';

export default {
    name: 'schedule',
    props: [],
    components: {
        ThemeNavBar,
        SemesterAccordion,
        CourseInfoModal,
        AddToSemesterModal,
        AddSemesterModal
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
    }
}
</script>

<style scoped>
div.row {
  min-width: 100%;
}
</style>
