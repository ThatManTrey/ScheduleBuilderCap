<template lang="html">
  <div
    class="container-fluid p-0 d-lg-block d-none"
    id=""
    :class="{ slide: !isOpen }"
    v-if="isLoggedIn"
  >
    <button class="semesterBar-button" @click="isOpen = !isOpen">
      <i class="far fa-calendar "></i>
    </button>
    <div class="semesterBar-container">
      <MiniSemester
        @openCourseInfoModal="showCourseInfoModal"
        v-for="(semester, index) in semesters"
        :key="index"
        :semester="semester"
      ></MiniSemester>

      <div
        v-if="semesters.length === 0"
        class="d-flex w-100 flex-column justify-content-center align-items-center"
      >
        <h3 class="mb-3">You don't have any semesters yet.</h3>
        <button
          class="mb-0 mx-5 button-as-link"
          @click="showAddSemesterModal()"
        >
          <span class="text-theme-lightest-gray">
            <i class="fas fa-plus-circle"></i>
            Add semester
          </span>
        </button>
      </div>
      <div v-else class="pe-4">
        <button class="mb-0 button-as-link" @click="showAddSemesterModal()">
          <span class="text-theme-white">
            <i class="fas fa-plus-circle"></i>
            Add semester
          </span>
        </button>
      </div>
    </div>

    <CourseInfoModal
      @openAddSemesterModal="showAddToSemesterModal"
      @openAddRatingModal="showAddRatingModal"
      @openViewRatingModal="showViewRatingModal"
      :isRemovingCourse="true"
      ref="courseInfoModalHome"
    ></CourseInfoModal>

    <AddRatingModal ref="addRatingModalHome"></AddRatingModal>
    <ViewRatingModal
      @openAddRatingModal="showAddRatingModal"
      ref="viewRatingModalHome"
    ></ViewRatingModal>
  </div>
</template>

<script>
import CourseInfoModal from "../components/modals/CourseInfoModal.vue";
import MiniSemester from "../components/MiniSemester.vue";
import AddRatingModal from "../components/modals/AddRatingModal.vue";
import ViewRatingModal from "../components/modals/ViewRatingModal.vue";
import { mapState } from "vuex";

export default {
  name: "semester-bar",
  data() {
    return {
      isOpen: false
    };
  },

  computed: {
    ...mapState({
      isLoggedIn: state => state.auth.isAuthenticated,
      semesters: state => state.semesters.semesters
    })
  },

  methods: {
    toggle: function() {
      this.isOpen = !this.isOpen;
    },

    showAddSemesterModal() {
      this.$emit("showAddSemesterModal");
    },

    showCourseInfoModal() {
      this.$refs.courseInfoModalHome.openModal();
    },

    showAddToSemesterModal() {
      this.$refs.addToSemesterModalFavorites.openModal();
    },

    showAddRatingModal() {
      this.$emit("showAddRatingModal");
    },

    showViewRatingModal() {
      this.$emit("showViewRatingModal");
    }
  },
  components: {
    MiniSemester,
    CourseInfoModal,
    AddRatingModal,
    ViewRatingModal
  }
};
</script>

<style scoped>
.semesterBar-button {
  cursor: pointer;
  display: block;
  min-width: 5rem;
  margin-left: 0.9rem;
  padding: 15px 0;
  background: var(--theme-black);
  color: var(--theme-whiter);
  border: 0;
  text-align: center;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-top: solid 1pt var(--theme-primary-dark);
}

.semesterBar-container {
  background: var(--theme-black);
  color: var(--theme-whiter);
  min-height: 175px;
  max-height: 175px;
  display: flex;
  text-align: left;
  border-top: solid 1pt var(--theme-primary-dark);
  border-top-right-radius: 10px;
  overflow-x: auto;
  overflow-y: auto;
  white-space: nowrap;
  padding: 1rem 1.5rem;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}

.container-fluid {
  transition: 0.5s ease;
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 1000;
  width: 100%;
}

.container-fluid.slide {
  transform: translateY(175px);
  z-index: 0;
}
</style>
