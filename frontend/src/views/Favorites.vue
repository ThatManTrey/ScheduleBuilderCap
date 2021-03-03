<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
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
                class="form-control theme-search me-2"
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

      <div class="row course-container">
        <div
          class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
          v-for="n in 2"
          :key="n"
        >
          <CourseCard></CourseCard>
        </div>
      </div>
    </div>

    <CourseInfoModal></CourseInfoModal>
    <AddToSemesterModal></AddToSemesterModal>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import CourseCard from '../components/CourseCard.vue';
import CourseInfoModal from '../components/CourseInfoModal.vue';
import AddToSemesterModal from '../components/AddToSemesterModal.vue'

export default {
    name: 'favorites',
    props: [],
    components: {
        ThemeNavBar,
        CourseCard,
        CourseInfoModal,
        AddToSemesterModal
    },

data () {
      return {
        isModalVisible: false,
      };
    },
      methods: {
        showCourseInfoModal () {
            this.modalVisible = true;
        },
        showAddToSemesterModal () {
            this.modalVisible = true;
        }
      },
};
</script>

<style scoped></style>
