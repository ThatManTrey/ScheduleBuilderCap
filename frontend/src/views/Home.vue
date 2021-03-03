<template lang="html">
  <div>
    <ThemeNavBar @isLoggedIn="isLoggedInUpdate"></ThemeNavBar>
    <PageSpinner
      v-if="!hasLoadedCourses"
      :showSpinner="!hasLoadedCourses"
    ></PageSpinner>

    <div class="container">
      <div class="row mt-3">
        <div class="col">
          <div class="dropdown course-dropdown">
            <button
              class="btn btn-theme-secondary dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Select a program
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li>
                <a class="dropdown-item" href="#">Computer Science (B. S.)</a>
              </li>
              <li><a class="dropdown-item" href="#">Biology (B. S.)</a></li>
              <li><a class="dropdown-item" href="#">English (B. A.)</a></li>
            </ul>
          </div>
          <div class="dropdown course-dropdown">
            <button
              class="btn btn-theme-primary dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Select a concentration
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li>
                <a class="dropdown-item" href="#">Computer Science (B. S.)</a>
              </li>
              <li><a class="dropdown-item" href="#">Biology (B. S.)</a></li>
              <li><a class="dropdown-item" href="#">English (B. A.)</a></li>
            </ul>
          </div>
          <div class="dropdown course-dropdown">
            <button
              class="btn btn-theme-primary dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Sort Courses
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <div class="course-search">
            <form class="d-flex">
              <input
                class="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              <button class="btn btn-theme-primary" type="submit">
                Search
              </button>
            </form>
          </div>
          <hr class="bg-theme-dark-gray" />
        </div>
      </div>

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
        PageSpinner
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

.course-search {
  max-width: 30rem;
  display: inline-block;
  position: relative;
  top: 0.1rem;
}

.course-dropdown {
  display: inline-block;
  margin-right: 1rem;
}
</style>
