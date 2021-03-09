<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <div class="container">
      <FilterCoursesBar></FilterCoursesBar>
      <div class="row course-container">
        <div
          class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
          v-for="n in 8"
          :key="n"
        >
          <CourseCard
            @openAddSemesterModal="showAddToSemesterModal"
            @openCourseInfoModal="showCourseInfoModal"
          ></CourseCard>
        </div>
      </div>
    </div>

    <CourseInfoModal ref="courseInfoModalFavorites"></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalFavorites"></AddToSemesterModal>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import CourseCard from '../components/CourseCard.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue'
import FilterCoursesBar from '../components/FilterCoursesBar.vue';

export default {
    name: 'favorites',
    props: [],
    components: {
        ThemeNavBar,
        CourseCard,
        CourseInfoModal,
        AddToSemesterModal,
        FilterCoursesBar
    },

data () {
      return {
        isModalVisible: false,
      };
    },
      methods: {
        showCourseInfoModal () {
            this.$refs.courseInfoModalFavorites.openModal();
        },
        showAddToSemesterModal () {
            this.$refs.addToSemesterModalFavorites.openModal();
        }
      },
};
</script>

<style scoped></style>
