<template lang="html">
  <div>
    
      <footer class="container" v-if="isLoggedIn">
        <button class="semesterBar-button" v-on:click="isOpen = !isOpen">
          <i class="far fa-calendar "></i>
        </button>
        <transition name="toggle">
          <div class="semesterBar-container" v-if="isOpen">
            <span v-for="(semester, index) in semesters" :key="index">
              <MiniSemester :semester="semester"></MiniSemester>
            </span>
            <div class="inline">
              <a
                tabindex="0"
                @keyup.enter="showAddSemesterModal()"
                @click="showAddSemesterModal()"
                data-tooltip="Add a Semester"
                data-tooltip-location="bottom"
              >
                <i class="fas fa-plus-circle fa-lg newSemester align-items-center"></i>
              </a>
            </div>
          </div>
          </transition>
      </footer>
    <AddSemesterModal ref="addSemesterModalSchedule"></AddSemesterModal>
    
  </div>
</template>

<script>
import MiniSemester from "../components/MiniSemester.vue";
import AddSemesterModal from "../components/modals/AddSemesterModal.vue";
import { mapState } from "vuex";

export default {
  name: "semester-bar",
  data() {
    return {
      isOpen: false
    };
  },

  props: {
    targetName: String
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
      this.$refs.addSemesterModalSchedule.openModal();
    }
  },
  components: {
    MiniSemester,
    AddSemesterModal
  }
};
</script>

<style scoped>
.container {
  width: 99%;
  display: block;
  position: fixed;
  bottom: 0;
  left: 0;
  z-index: 100;
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
  animation: slideup-mini 2s ease;
}
@keyframes slideup-mini {
  from {
    transform: translateY(100%);
    opacity: 25%;
  }
  to {
    transform: translateY(0%);
    opacity: 100%;
  }
}
.semesterBar-container {
  background: var(--theme-black);
  color: var(--theme-whiter);
  display: flex;
  width: 110%;
  min-height: 5rem;
  max-height: 15rem;
  text-align: left;
  margin-left: -1rem;
  border-top: solid 1pt var(--theme-primary-dark);
  border-top-right-radius: 10px;
  overflow-x: auto;
  overflow-y: auto;
  white-space: nowrap;
  padding: 1rem;
  -webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
  box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
}
@keyframes slide {
  0% {
    margin-bottom: -18%;
    
    
  }
  100% {
    margin-bottom: 0%;
  
  }
}

.toggle-enter-active {
  animation: slide 1s ease;
}
.toggle-leave-active {
  animation: slide 1s reverse;
}

.inline {
  display: inline-block;
  align-self: center;
}
.newSemester {
  padding-left: 1.5rem;
  padding-right: 3rem;
}


@media only screen and (max-width: 1280px) {
  .container {
    display: none;
  }
}
</style>
