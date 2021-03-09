<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <PageSpinner
      v-if="!hasLoadedCourses"
      :showSpinner="!hasLoadedCourses"
    ></PageSpinner>

    <div class="container">
        <FilterCoursesBar></FilterCoursesBar>
        
        <transition name="coursefade">
        <div v-show="hasLoadedCourses" class="row mx-3">
          <div
            class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
            v-for="n in 20"
            :key="n"
          >
            <CourseCard
              @openAddSemesterModal="showAddToSemesterModal"
              @openCourseInfoModal="showCourseInfoModal"
            ></CourseCard>
          </div>
        </div>
      </transition>
    </div>

    <CourseInfoModal
      @openAddSemesterModal="showAddToSemesterModal"
      ref="courseInfoModalHome"
    ></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalHome"></AddToSemesterModal>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import CourseCard from '../components/CourseCard.vue';
import PageSpinner from '../components/spinners/PageSpinner.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue';
import FilterCoursesBar from '../components/FilterCoursesBar.vue';

export default {
    name: 'home',
    props: [],
    data() {
        return {
            hasLoadedCourses: false,
            isLoggedIn: false
        }
    },
    components: {
        ThemeNavBar,
        CourseCard,
        CourseInfoModal,
        AddToSemesterModal,
        PageSpinner,
        FilterCoursesBar
    },
    created() {
        // loading test
        setTimeout(() => {
            this.hasLoadedCourses = true;
        }, 2000);
    },
      methods: {
        showCourseInfoModal () {
            this.$refs.courseInfoModalHome.openModal();
        },
        showAddToSemesterModal () {
            this.$refs.addToSemesterModalHome.openModal();
        },
      },
};
</script>

<style scoped>
.coursefade-enter-active {
  transition: opacity 1.5s;
}

.coursefade-enter,
.coursefade-leave-to {
  opacity: 0;
}

</style>
