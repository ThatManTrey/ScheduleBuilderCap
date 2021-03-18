<template lang="html">
  <div>
    <div class="semester-accordion mb-3">
      <div class="semester-header">
        <div class="semester-title align-middle">
          <a
            @click="removeSemester()"
            @keyup.enter="removeSemester()"
            data-tooltip="Remove Semester"
            data-tooltip-location="bottom"
          >
            <i class="fas fa-trash fa-lg"></i>
          </a>
          <h2 class="text-theme-whitest m-0">
            <span contenteditable="true">Fall 2021</span>
            (<span class="text-theme-secondary">16</span>)
          </h2>
          <button
            class="btn btn-theme-primary-dark float-end"
            type="button"
            data-bs-toggle="collapse"
            :data-bs-target="'#' + targetName"
            aria-expanded="false"
            :aria-controls="targetName"
          >
            <i class="fas fa-chevron-down"></i>
          </button>
        </div>
        <div class="semester-divider">
          <hr class="bg-theme-darkest-gray" size="5" />
        </div>
      </div>
    </div>

    <div class="semester-body collapse show mb-3" :id="targetName">
      <div class="container">
        <div class="row">
          <div
            v-for="n in 4"
            :key="n"
            class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
          >
            <CourseCard
              @openAddSemesterModal="showAddToSemesterModal"
              @openCourseInfoModal="showCourseInfoModal"
              :isRemovingCourse="true"
            ></CourseCard>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import CourseCard from '../components/CourseCard.vue';
import * as Toast from '../toast.js';

export default {
    name: 'semester-accordion',
    props: {
      targetName: String
    },
    components: {
      CourseCard,
    },
    methods: {
        showCourseInfoModal () {
            this.$emit("showCourseInfoModal");
        },
        showAddToSemesterModal () {
            this.$emit("showAddToSemesterModal")
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
    }
}
</script>

<style scoped lang="scss">
.semester-accordion {
  min-width: 100%;
}

.semester-title {
  width: 95%;
  margin: auto;
}

.semester-header {
  display: inline-block;
  width: 100%;
}

i.fa-trash {
  position: relative;
  top: 2px;
  margin-right: 1rem;
  font-size: 1.2rem;
}

.semester-header h4,
h2,
i {
  display: inline-block;
  vertical-align: middle;
}
</style>
