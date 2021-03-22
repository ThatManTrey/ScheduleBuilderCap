
<template lang="html">
    <div>
    <footer class="container">
        <button class="semesterBar-button" v-on:click="toggle()">
            <i class="far fa-calendar "></i>
            <!-- My Schedule -->
            </button>
        <div class="semesterBar-container" v-show="isOpen">
            <span 
            v-for="n in 4"
            :key="n">
                <MiniSemester></MiniSemester>
            </span>
            <div class="inline">
                <a 
                    v-if="!isRemovingCourse"
                    tabindex="0"
                    @keyup.enter="showAddSemesterModal()"
                    @click="showAddSemesterModal()"
                    data-tooltip="Add a Semester"
                    data-tooltip-location="bottom"
                    >
                    <i class="fas fa-plus-circle fa-lg newSemester"></i>
                    </a>
          
            </div>
        </div>
    </footer>

    <AddSemesterModal ref="addSemesterModalSchedule"></AddSemesterModal>
    </div>
</template>

<script>

import MiniSemester from '../components/MiniSemester.vue'
import AddSemesterModal from '../components/modals/AddSemesterModal.vue';
import * as Toast from '../toast.js';

export default ({
    name: 'semester-bar',
    data() {
        return {
            isOpen: false,
            isRemovingCourse: ""
        }
    },
    methods: {
        toggle: function() {
            this.isOpen = !this.isOpen
        },
        showAddSemesterModal () {
            this.$refs.addSemesterModalSchedule.openModal();
        },
        removeSemester() {
            var removePromptResult = confirm(
                "Are you sure you want to remove this semester and all its courses?"
            );
            if (removePromptResult == true) {
                Toast.showSuccessMessage(
                "Semester was removed successfully."
                );
            }
        },
    },
    components: {
        MiniSemester,
        AddSemesterModal
    }
})
</script>


<style scoped>

.container {
  width:99%;
  position:fixed;
  bottom:0;
  z-index: 100;
}

.semesterBar-button {
  cursor: pointer;
  display: block;
  min-width: 5rem;
  margin-left: 0.90rem;
  padding:15px 0;
  background:var(--theme-black);
  color:var(--theme-whiter);
  border:0;
  text-align:center;
  border-top-left-radius:10px;
  border-top-right-radius:10px;
  border-top: solid 1pt var(--theme-primary-dark);
  animation: slideup-mini 5s ease;
}

@keyframes slideup-mini {
  from {
    margin-bottom: -100%;
    opacity: 25%;
  }
  to {
    margin-bottom: 0%;
    opacity: 100%;
  }
}

.semesterBar-container {
  background: var(--theme-black);
  color: var(--theme-whiter);
  width:110%;
  min-height:5rem;
  text-align:left;
  margin-left: -1rem;
  border-top: solid 1pt var(--theme-primary-dark);
  border-top-right-radius:10px;
  overflow-x: auto;
  overflow-y: hidden;
  white-space: nowrap;
  padding: 1rem;
  -webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
  box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
  animation: slideIn 1s ease;
}

.semesterBar-containter.slideIn {
    animation: slideIn 1s ease;
}

.semesterBar-container.slideOut {
    animation: slideOut 1s ease;
}

@keyframes slideIn {
  0% {
    margin-bottom: -18%;
    opacity: 100%;
  }
    100% {
    margin-bottom: 0%;
    opacity: 100%;
  }
}

@keyframes slideOut {
    100% {
    margin-bottom: 0%;
    opacity: 100%;
  }
    0% {
    margin-bottom: -18%;
    opacity: 100%;
  }
}

.inline {
    display: inline-block;
}

.newSemester {
    position: absolute;
    top: 6rem;
    padding-left: 1.5rem;
    padding-right: 3rem;
}

/* Tooltip Styling */ 
[data-tooltip-location="bottom"]:before,
[data-tooltip-location="bottom"]:after {
  top: calc(100% + 95px);
  left: 29px;
  bottom: auto;
}

@media only screen and (max-width:1280px) {
    .container {
        display: none;
    }
}

</style>