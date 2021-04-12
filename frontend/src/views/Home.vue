<template lang="html">
  <div class="d-flex flex-grow-1">
    <PageSpinner :showSpinner="isLoadingCourses"></PageSpinner>

    <div class="container d-flex flex-column flex-grow-1">
      <FilterCoursesBar
        @openChangeProgramModal="$refs.changeProgramModalHome.openModal()"
      ></FilterCoursesBar>

      <transition name="coursefade" mode="out-in">
        <div v-if="showCard && !isLoadingCourses && totalResults > 0" class="row justify-content-center align-items-center flex-grow-1 mx-3">
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

        <div
          v-if="!showCard && !isLoadingCourses && totalResults > 0"
          class="row flex-grow-1 mt-3 mt-md-5 mb-3 mx-3 mx-xl-1"
          id="table-container"
        >
          <table class="table">
            <colgroup>
              <col span="1" style="width: 10%;" />
              <col span="1" style="width: 30%;" />
              <col span="1" style="width: 55%;" />
              <col span="1" style="width: 5%;" />
            </colgroup>

            <tbody>
              <CourseTableRow
                v-for="(course, index) in allCourses"
                :key="index"
                :course="course"
                @openCourseInfoModal="showCourseInfoModal"
                @openAddSemesterModal="showAddToSemesterModal"
              ></CourseTableRow>
            </tbody>
          </table>
        </div>

        <div class="row text-theme-white" v-if="!isLoadingCourses && totalPages === 0">
          <h5 class="text-center mb-5" id="no-results-found">No results found. Try another keyword?</h5>
        </div>
      </transition>

      

      <!-- pagination buttons and total results -->
      <!-- SVG source: https://tablericons.com/ -->
      <div
        v-if="!isLoadingCourses && totalPages > 0"
        class="row mx-3 mt-3"
        style="margin-bottom: 5rem;"
      >
        <div class="col-4 text-theme-white">
          <h5>{{ totalResults }} Results</h5>
        </div>
        <div class="col-8 d-flex justify-content-end">
          <nav class="course-pagination" aria-label="Course pagination">
            <ul>
              <li>
                <button
                  class="button-as-link"
                  :disabled="isFirstPage()"
                  @click="firstPage()"
                  aria-label="First page"
                  data-tooltip="First Page"
                >
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
                </button>
              </li>
              <li>
                <button
                  class="button-as-link"
                  :disabled="isFirstPage()"
                  @click="prevPage()"
                  aria-label="Previous page"
                  data-tooltip="Previous Page"
                >
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
                </button>
              </li>
              <li>
                <button
                  class="button-as-link"
                  :disabled="isLastPage()"
                  @click="nextPage()"
                  aria-label="Next page"
                  data-tooltip="Next Page"
                >
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
                </button>
              </li>
              <li>
                <button
                  class="button-as-link"
                  :disabled="isLastPage()"
                  @click="lastPage()"
                  aria-label="Last page"
                  data-tooltip="Last Page"
                >
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
                </button>
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
      v-if="!isLoadingCourses && totalPages > 1"
    >
      <button
        class="button-as-link"
        :disabled="isFirstPage()"
        @click="prevPage()"
      >
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
      v-if="!isLoadingCourses && totalPages > 1"
    >
      <button
        class="button-as-link"
        :disabled="isLastPage()"
        @click="nextPage()"
      >
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

    <SemesterBar @showAddSemesterModal="showAddSemesterModal"></SemesterBar>

    <CourseInfoModal
      @openAddSemesterModal="showAddToSemesterModal"
      ref="courseInfoModalHome"
    ></CourseInfoModal>
    <AddToSemesterModal ref="addToSemesterModalHome"></AddToSemesterModal>
    <ChangeProgramModal ref="changeProgramModalHome"></ChangeProgramModal>
  </div>
</template>

<script lang="js">
import CourseCard from '../components/CourseCard.vue';
import CourseTableRow from '../components/CourseTableRow.vue';
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
        CourseCard,
        CourseInfoModal,
        AddToSemesterModal,
        PageSpinner,
        FilterCoursesBar,
        SemesterBar,
        ChangeProgramModal,
        CourseTableRow
    },

    computed: {
      ...mapState({
        allCourses: state => state.courses.allCourses,
        isLoadingCourses: state => state.courses.isLoadingCourses,
        viewOption: state => state.courses.searchRequest.viewOption,
        currentPage: state => state.courses.currentPage,
        totalPages: state => state.courses.totalPages,
        totalResults: state => state.courses.totalResults
      }),
      ...mapGetters('courses', {
        showCard: 'showCard'
      })
    },

    created() {
        // reset keyword if page has changed
        this.$store.commit('courses/setSearchKeyword', "");
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
        this.$store.dispatch('courses/updatePagination', 1);
      },

      prevPage() {
        this.$store.dispatch('courses/updatePagination', this.currentPage - 1);
      },

      nextPage() {
        this.$store.dispatch('courses/updatePagination', this.currentPage + 1);
      },

      lastPage() {
        this.$store.dispatch('courses/updatePagination', this.totalPages);
      },

      isFirstPage() {
        return this.currentPage === 1;
      },

      isLastPage() {
        return this.currentPage === this.totalPages;
      }
    },
};
</script>

<style scoped lang="scss">
.coursefade-enter-active {
  transition: all 0.5s;
}

.coursefade-leave-active {
  transition: all 0.5s;
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

button,
a {
  &[disabled] {
    opacity: 0.25;
    cursor: default;

    // hide tooltip
    &::before,
    &::after {
      display: none;
    }
  }

  &:not([disabled]) {
    svg:hover {
      stroke: var(--theme-primary-light);
    }
  }
}

@media (max-width: 576px) {
  #table-container {
    overflow-x: scroll;
  }
}

#no-results-found {
  position: fixed;
  top: 50vh;
  right: 0;
}
</style>
