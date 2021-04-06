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

    <CourseInfoModal ref="courseInfoModalFavorites"></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalFavorites"></AddToSemesterModal>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import CourseCard from '../components/CourseCard.vue';
import PageSpinner from '../components/spinners/PageSpinner.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue'
import FilterCoursesBar from '../components/FilterCoursesBar.vue';
import axios from 'axios';

export default {
    name: 'favorites',
    props: [],
    components: {
        ThemeNavBar,
        CourseCard,
        PageSpinner,
        CourseInfoModal,
        AddToSemesterModal,
        FilterCoursesBar
    },
    created() {
        // loading test
        this.getCourses();
    },
    
    data () {
      return {
        isModalVisible: false,
        courses: [],
        hasLoadedCourses: false
      };
    },

      methods: {
        showCourseInfoModal () {
            this.$refs.courseInfoModalFavorites.openModal();
        },
        showAddToSemesterModal () {
            this.$refs.addToSemesterModalFavorites.openModal();
        },
        getCourses() {
          var baseUrl = process.env.VUE_APP_API_URL + "/user/" + this.$store.state.userId

          //AJAX request
          axios.get(baseUrl + "/favorites")
            .then((res) => {
              this.courses = res.data;
              this.hasLoadedCourses = true;
            })
            .catch((error) => {
              // eslint-disable-next-line
              console.error(error);
            });
        }
      },
};
</script>

<style scoped></style>
