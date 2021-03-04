<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <div class="container">
      <FilterCoursesBar></FilterCoursesBar>
      <div class="row course-container">
        <div
          class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
          v-for="n in 2"
          :key="n"
        >
          <CourseCard></CourseCard>
        </div>
      </div>
    </div>

    <CourseInfoModal></CourseInfoModal>
    <AddToSemesterModal></AddToSemesterModal>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import CourseCard from '../components/CourseCard.vue';
import CourseInfoModal from '../components/CourseInfoModal.vue';
import AddToSemesterModal from '../components/AddToSemesterModal.vue'
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
            this.modalVisible = true;
        },
        showAddToSemesterModal () {
            this.modalVisible = true;
        }
      },
};
</script>

<style scoped></style>
