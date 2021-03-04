<template lang="html">
  <div>
    <ThemeNavBar @isLoggedIn="isLoggedInUpdate"></ThemeNavBar>
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
            v-for="n in 12"
            :key="n"
          >
            <CourseCard></CourseCard>
          </div>
                
        </div>
        </transition>
    </div>

    <CourseInfoModal></CourseInfoModal>
    <AddToSemesterModal></AddToSemesterModal>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import CourseCard from '../components/CourseCard.vue';
import PageSpinner from '../components/PageSpinner.vue';
import CourseInfoModal from '../components/CourseInfoModal.vue';
import AddToSemesterModal from '../components/AddToSemesterModal.vue';
import FilterCoursesBar from '../components/FilterCoursesBar.vue';

export default {
    name: 'home',
    props: [],
    data() {
        return {
            hasLoadedCourses: false,
            isModalVisible: false,
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
            this.modalVisible = true;
        },
        showAddToSemesterModal () {
            this.modalVisible = true;
        },
        isLoggedInUpdate(data){
          this.isLoggedIn = data;
        }
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
