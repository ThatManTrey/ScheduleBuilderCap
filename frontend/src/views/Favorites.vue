<template lang="html">
  <div>
    <!-- <PageSpinner
      v-if="!hasLoadedCourses"
      :showSpinner="!hasLoadedCourses"
    ></PageSpinner> -->

    <div class="container">
      <transition name="fade">
        <div v-if="favCourses.length !== 0" class="row mx-3">
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
      <div class=" text-theme-light-gray noFavMessage" v-else>
        <p>You haven't favorited any courses.</p>
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

.noFavMessage {
  padding-top: 10rem;
  text-align: center;
}
</style>
