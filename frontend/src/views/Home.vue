<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <PageSpinner
      :showSpinner="isLoading"
    ></PageSpinner>

    <div v-if="!isLoading" class="container">
      <FilterCoursesBar
        @openChangeProgramModal="$refs.changeProgramModalHome.openModal()"
      ></FilterCoursesBar>

      <transition name="coursefade">
        <div v-if="showCard" class="row mx-3">
          <div
            class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
            v-for="(course, index) in allCourses"
            :key="index"
          >
            <CourseCard
              @openAddSemesterModal="showAddToSemesterModal"
              @openCourseInfoModal="showCourseInfoModal"
              v-bind:course="course"
            ></CourseCard>
          </div>
        </div>

        <div v-else class="row mx-3">
          <p class="text-theme-whitest">This is a table</p>
        </div>
      </transition>


      <!-- pagination buttons and total results -->
      <!-- SVG source: https://tablericons.com/ -->
      <div class="row mx-3 mt-3" style="margin-bottom: 5rem;">
        <div class="col-4 text-theme-white">
          <h5>168 Results</h5>
        </div>
        <div class="col-8 d-flex justify-content-end">
          <nav class="course-pagination" aria-label="Course pagination">
            <ul>
              <li>
                <a @click="firstPage()" class="page-button-disabled" aria-label="First page" data-tooltip="First Page">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="icon icon-tabler icon-tabler-chevrons-left"
                    width="36"
                    height="36"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="#B6B6B6"
                    fill="none"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <polyline points="11 7 6 12 11 17" />
                    <polyline points="17 7 12 12 17 17" />
                  </svg>
                </a>
              </li>
              <li>
                <a @click="prevPage()" class="page-button-disabled" aria-label="Previous page" data-tooltip="Previous Page">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="icon icon-tabler icon-tabler-chevron-left"
                    width="36"
                    height="36"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="#B6B6B6"
                    fill="none"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <polyline points="15 6 9 12 15 18" />
                  </svg>
                </a>
              </li>
              <li>
                <a @click="nextPage()" aria-label="Next page" data-tooltip="Next Page">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="icon icon-tabler icon-tabler-chevron-right"
                    width="36"
                    height="36"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="#B6B6B6"
                    fill="none"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <polyline points="9 6 15 12 9 18" />
                  </svg>
                </a>
              </li>
              <li>
                <a @click="lastPage()" aria-label="Last page" data-tooltip="Last Page">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    class="icon icon-tabler icon-tabler-chevrons-right"
                    width="36"
                    height="36"
                    viewBox="0 0 24 24"
                    stroke-width="1.5"
                    stroke="#B6B6B6"
                    fill="none"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <polyline points="7 7 12 12 7 17" />
                    <polyline points="13 7 18 12 13 17" />
                  </svg>
                </a>
              </li>
            </ul>
          </nav>
        </div>
      </div>
    </div>

    <!-- left previous page button -->
    <!-- SVG source: https://tablericons.com/ -->
    <div
      class="side-button-container d-none d-md-flex"
      id="prev-page-side-button-container"
      v-if="!isLoading"
    >
      <button class="button-as-link page-button-disabled" @click="prevPage()">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="icon icon-tabler icon-tabler-chevron-left"
          width="44"
          height="44"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="#B6B6B6"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path stroke="none" d="M0 0h24v24H0z" fill="none" />
          <polyline points="15 6 9 12 15 18" />
        </svg>
      </button>
    </div>

    <!-- right next page button -->
    <!-- SVG source: https://tablericons.com/ -->
    <div
      class="side-button-container d-none d-md-flex"
      id="next-page-side-button-container"
      v-if="!isLoading"
    >
      <button class="button-as-link" @click="nextPage()">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          class="icon icon-tabler icon-tabler-chevron-right"
          width="44"
          height="44"
          viewBox="0 0 24 24"
          stroke-width="1.5"
          stroke="#B6B6B6"
          fill="none"
          stroke-linecap="round"
          stroke-linejoin="round"
        >
          <path stroke="none" d="M0 0h24v24H0z" fill="none" />
          <polyline points="9 6 15 12 9 18" />
        </svg>
      </button>
    </div>

    <SemesterBar
      @showAddSemesterModal="showAddSemesterModal"
    ></SemesterBar>

    <CourseInfoModal
      @openAddSemesterModal="showAddToSemesterModal"
      ref="courseInfoModalHome"
    ></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalHome"></AddToSemesterModal>
    <ChangeProgramModal ref="changeProgramModalHome"></ChangeProgramModal>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import CourseCard from '../components/CourseCard.vue';
import PageSpinner from '../components/spinners/PageSpinner.vue';
import CourseInfoModal from '../components/modals/CourseInfoModal.vue';
import AddToSemesterModal from '../components/modals/AddToSemesterModal.vue';
import ChangeProgramModal from '../components/modals/ChangeProgramModal.vue';
import FilterCoursesBar from '../components/FilterCoursesBar.vue';
import SemesterBar from '../components/SemesterBar.vue';
import { mapState, mapGetters } from 'vuex';

export default {
    name: 'home',

    components: {
        ThemeNavBar,
        CourseCard,
        CourseInfoModal,
        AddToSemesterModal,
        PageSpinner,
        FilterCoursesBar,
        SemesterBar,
        ChangeProgramModal
    },

    computed: {
      ...mapState({
        allCourses: state => state.courses.allCourses,
        isLoading: state => state.courses.isLoadingCourses,
        viewOption: state => state.courses.searchRequest.viewOption
      }),
      ...mapGetters('courses', {
        showCard: 'showCard'
      })
    },

    created() {
        this.$store.dispatch('courses/getCourses');
    },

    methods: {
      showCourseInfoModal () {
        this.$refs.courseInfoModalHome.openModal();
      },

      showAddToSemesterModal () {
        this.$refs.addToSemesterModalHome.openModal();
      },
        
      showAddSemesterModal () {
        this.$refs.addSemesterModalHome.openModal();
      },

      firstPage() {

      },

      prevPage() {

      },

      nextPage() {

      },

      lastPage() {

      }
    },
};
</script>

<style scoped lang="scss">
.coursefade-enter-active {
  transition: opacity 1.5s;
}

.coursefade-enter,
.coursefade-leave-to {
  opacity: 0;
}

.side-button-container {
  position: fixed;
  height: 50vh;
  top: 25vh;
  z-index: 2;

  button {
    height: 50%;
    margin: auto;
    padding: 0 1rem;

    @media (min-width: 1700px) {
      padding: 0 5rem;
    }
  }
}

#prev-page-side-button-container {
  left: 0;
}

#next-page-side-button-container {
  right: 0;
}

.course-pagination {
  list-style-type: none;

  li {
    display: inline-block;
  }
}

svg:not(.page-button-disabled svg):hover {
    stroke: var(--theme-primary-light);
}

.page-button-disabled {
    opacity: 0.25;
    cursor: default;

    &::before,
    &::after {
      display: none;
    }
  }

</style>
