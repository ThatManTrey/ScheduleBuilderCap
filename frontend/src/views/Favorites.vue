<template lang="html">
  <div class="d-flex flex-grow-1">
    <!-- <PageSpinner
      v-if="!hasLoadedCourses"
      :showSpinner="!hasLoadedCourses"
    ></PageSpinner> -->

    <div
      class="container d-flex flex-grow-1 justify-content-center align-items-center mb-3 mt-3"
    >
      <transition name="fade">
        <div v-if="favCourses.length !== 0" class="row w-100 justify-content-center align-items-center mx-3">
          <div
            class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
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
            You can find some <router-link to="home">here</router-link>.
          </p>
        </div>
      </transition>
    </div>

    <CourseInfoModal ref="courseInfoModalFavorites"></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalFavorites"></AddToSemesterModal>
  </div>
</template>

<script lang="js">
import CourseCard from '../components/CourseCard.vue';
//import PageSpinner from '../components/spinners/PageSpinner.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue';
import { mapState } from "vuex";

export default {
    components: {
        CourseCard,
        //PageSpinner,
        CourseInfoModal,
        AddToSemesterModal,
    },

     computed: mapState({
       favCourses: state => state.favorites.favoriteCourses,
     }),

      methods: {
        showCourseInfoModal () {
            this.$refs.courseInfoModalFavorites.openModal();
        },

        showAddToSemesterModal () {
            this.$refs.addToSemesterModalFavorites.openModal();
        },
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
