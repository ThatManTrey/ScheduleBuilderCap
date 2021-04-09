<template lang="html">
  <div>
    <PageSpinner
      v-if="!hasLoadedCourses"
      :showSpinner="!hasLoadedCourses"
    ></PageSpinner>

    <div class="container">
      <transition name="coursefade">
        <div v-show="hasLoadedCourses" class="row mx-3">
          <div
            class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
            v-for="(course, index) in courses.favCourses"
            :key="index"
          >
            <CourseCard
              @openAddSemesterModal="showAddToSemesterModal"
              @openCourseInfoModal="showCourseInfoModal"
              v-bind:course="course"
            ></CourseCard>
          </div>
          <div class=" text-theme-light-gray noFavMessage" v-if="!courses.favCourses.length">
            <p> You haven't favorited any courses.</p> 
          </div>
        </div>
      </transition>
    </div>

    <CourseInfoModal ref="courseInfoModalFavorites"></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalFavorites"></AddToSemesterModal>
  </div>
</template>

<script lang="js">
import CourseCard from '../components/CourseCard.vue';
import PageSpinner from '../components/spinners/PageSpinner.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue';
import { mapState } from "vuex";
import axios from 'axios';

export default {
    components: {
        CourseCard,
        PageSpinner,
        CourseInfoModal,
        AddToSemesterModal,
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

     computed: mapState({
      userID: state => state.auth.userId,
      currentCourse: state => state.courses.currentCourse
     }),

      methods: {
        showCourseInfoModal () {
            this.$refs.courseInfoModalFavorites.openModal();
        },
        showAddToSemesterModal () {
            this.$refs.addToSemesterModalFavorites.openModal();
        },
        getCourses() {
          var baseUrl = process.env.VUE_APP_API_URL + "/user/" + this.userID

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

<style scoped>

.container {
  padding-top: 3rem;
}

.noFavMessage {
  padding-top: 10rem;
  text-align: center;
}
</style>
