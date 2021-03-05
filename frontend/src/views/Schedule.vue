<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <div class="container mt-3">
      <div v-for="n in 4" :key="n" class="row">
        <SemesterAccordion
          :targetName="'example' + n"
          @showCourseInfoModal="showCourseInfoModal"
          @showAddToSemesterModal="showAddToSemesterModal"
        ></SemesterAccordion>
      </div>
    </div>

    <CourseInfoModal
      @openAddSemesterModal="showAddToSemesterModal"
      ref="courseInfoModalSchedule"
    ></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalSchedule"></AddToSemesterModal>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import SemesterAccordion from '../components/SemesterAccordion.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue';

export default {
    name: 'schedule',
    props: [],
    components: {
        ThemeNavBar,
        SemesterAccordion,
        CourseInfoModal,
        AddToSemesterModal
    },
    methods: {
      showCourseInfoModal () {
            this.$refs.courseInfoModalSchedule.openModal();
        },
        showAddToSemesterModal () {
            this.$refs.addToSemesterModalSchedule.openModal();
        },
    }
}
</script>

<style scoped>
div.row {
  min-width: 100%;
}
</style>
