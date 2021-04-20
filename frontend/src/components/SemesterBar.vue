<template lang="html">
  <footer id="semesterBar" class="d-lg-block d-none">
    <div class="container-fluid p-0" :class="{ 'slide': !isOpen }" v-if="isLoggedIn">
      <button class="semesterBar-button" @click="isOpen = !isOpen">
        <i class="far fa-calendar "></i>
      </button>
        <div class="semesterBar-container">
            <MiniSemester v-for="(semester, index) in semesters" :key="index" :semester="semester"></MiniSemester>  

          <div v-if="semesters.length === 0" class="d-flex w-100 flex-column justify-content-center align-items-center">
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
          <div v-else>
            <button
            class="mb-0 button-as-link"
            @click="showAddSemesterModal()"
            >
            <span class="text-theme-white">
              <i class="fas fa-plus-circle"></i>
              Add semester
            </span>
            </button>
          </div>
        </div>
    </div>
  </footer>
</template>

<script>
import MiniSemester from "../components/MiniSemester.vue";
import { mapState } from "vuex";

export default {
  name: "semester-bar",
  data() {
    return {
      isOpen: false,
    };
  },

  computed: {
    ...mapState({
      isLoggedIn: (state) => state.auth.isAuthenticated,
      semesters: (state) => state.semesters.semesters,
    }),
  },

  methods: {
    toggle: function () {
      this.isOpen = !this.isOpen;
    },

    showAddSemesterModal() {
      this.$emit("showAddSemesterModal");
    },
  },
  components: {
    MiniSemester,
  },
};
</script>

<style scoped>
#semesterBar {
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 100;
  width: 100%;
}

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
  overflow-y: hidden;
  white-space: nowrap;
  padding: 1rem 1.5rem;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}

.container-fluid {
  transition: 0.5s ease;
}

.slide {
  transform: translateY(175px);
}

</style>
