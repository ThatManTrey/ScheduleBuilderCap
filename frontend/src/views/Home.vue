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
            v-for="(course, index) in courses.deptCourses"
            :key="index"
            
          >
            <CourseCard
              @openAddSemesterModal="showAddToSemesterModal"
              @openCourseInfoModal="showCourseInfoModal"
              v-bind:course="course"
            ></CourseCard>
          </div>
        </div>
      </transition>
    </div>

    <SemesterBar></SemesterBar>

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
import SemesterBar from '../components/SemesterBar.vue';
import axios from 'axios';

export default {
    name: 'home',
    props: [],
    data() {
        return {
            courses: [],
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
        FilterCoursesBar,
        SemesterBar
    },
    created() {
        // loading test
        this.getCourses();
          setTimeout(() => {
            this.hasLoadedCourses = true;
        }, 2000)
    },
      methods: {
        showCourseInfoModal () {
            this.$refs.courseInfoModalHome.openModal();
        },
        showAddToSemesterModal () {
            this.$refs.addToSemesterModalHome.openModal();
        },
        getCourses() {
          var baseUrl = process.env.VUE_APP_API_URL + "/courses"

          //AJAX request
          axios.get(baseUrl + "/cs")
            .then((res) => {
              this.courses = res.data;
            })
            .catch((error) => {
              // eslint-disable-next-line
              console.error(error);
            });

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
