
<template lang="html">
    <div>
    <footer class="container">
        <button class="semesterBar-button" v-on:click="toggle()">
            <i class="far fa-calendar "></i>
            <!-- My Schedule -->
            </button>
        <div class="semesterBar-container" v-show="isOpen" >
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
    </div>
</template>

<script>

import MiniSemester from '../components/MiniSemester.vue'

export default ({
    name: 'semester-bar',
    data() {
        return {
            isOpen: false
        }
    },
    methods: {
        toggle: function() {
            this.isOpen = !this.isOpen
        }
    },
    components: {
        MiniSemester
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

@media only screen and (max-width:1280px) {
    .container {
        display: none;
    }
}

</style>