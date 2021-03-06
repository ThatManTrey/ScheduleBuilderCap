<template lang="html">
  <div class="d-flex flex-grow-1">
    <PageSpinner :showSpinner="isLoading"></PageSpinner>

    <div
      v-if="!isLoading"
      class="container d-flex flex-grow-1 justify-content-center align-items-center mb-3 mt-3"
    >
      <transition name="fade-med">
        <div
          v-if="favCourses.length > 0"
          class="row w-100 justify-content-center mx-3"
        >
          <div
            class="d-flex col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
            v-for="(course, index) in favCourses"
            :key="index"
          >
            <CourseCard
              @openAddSemesterModal="showAddToSemesterModal"
              @openCourseInfoModal="showCourseInfoModal"
              v-bind:course="course"
            ></CourseCard>
          </div>
        </div>

        <div v-else id="no-fav-message">
          <h4 class="text-theme-whitest mb-3">
            You haven't favorited any courses yet.
          </h4>
          <p class="text-theme-light-gray">
            You can find some
            <router-link to="home" class="link">here</router-link>.
          </p>
        </div>
      </transition>
    </div>

    <CourseInfoModal
      @openAddRatingModal="showAddRatingModal"
      @openViewRatingModal="showViewRatingModal"
      ref="courseInfoModalFavorites"
    ></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalFavorites"></AddToSemesterModal>
    <AddRatingModal ref="addRatingModalFavorites"></AddRatingModal>
    <ViewRatingModal
      @openAddRatingModal="showAddRatingModal"
      ref="viewRatingModalFavorites"
    ></ViewRatingModal>
  </div>
</template>

<script lang="js">
import CourseCard from '../components/CourseCard.vue';
import PageSpinner from '../components/spinners/PageSpinner.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue';
import AddRatingModal from '../components/modals/AddRatingModal.vue';
import ViewRatingModal from '../components/modals/ViewRatingModal.vue';
import { mapState } from "vuex";

export default {
    components: {
        CourseCard,
        PageSpinner,
        CourseInfoModal,
        AddRatingModal,
        ViewRatingModal,
        AddToSemesterModal,
    },

     computed: mapState({
       favCourses: state => state.favorites.favoriteCourses,
       course: state => state.courses.currentCourse,
       isLoading: state => state.favorites.isLoadingFavorites
     }),

      methods: {
        showCourseInfoModal () {
          this.$store.dispatch("ratings/getCourseRatings", { course: this.course });
          this.$store.dispatch("ratings/getUserCourseRating", {
            course: this.course
          });
            this.$refs.courseInfoModalFavorites.openModal();
        },

        showAddToSemesterModal () {
            this.$refs.addToSemesterModalFavorites.openModal();
        },

        showAddRatingModal () {
          this.$refs.addRatingModalFavorites.openModal();
        },

        showViewRatingModal () {
          this.$refs.viewRatingModalFavorites.openModal();
        }
      },
};
</script>

<style scoped>
.container {
  padding-top: 3rem;
}

#no-fav-message {
  position: fixed;
  top: 45vh;
  width: 100%;
  text-align: center;
}
</style>
