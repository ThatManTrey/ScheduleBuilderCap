<template lang="html">
  <div>
    <div class="semester-accordion mb-3">
      <div class="semester-header">
        <div class="semester-title align-middle">
          <i class="fas fa-edit text-theme-extra-light edit-semester-icon"></i>
          &nbsp;
          <h2 class="text-theme-whitest m-0">Fall 2021</h2>
          <span class="badge bg-theme-black text-theme-white"
            >16 credit hours</span
          >
          <button
            class="btn btn-theme-primary float-end"
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
          <hr class="bg-theme-dark-gray" style="height: 3px;" />
        </div>
      </div>
    </div>

    <div class="semester-body collapse mb-3" :id="targetName">
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
            ></CourseCard>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import CourseCard from '../components/CourseCard.vue';

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

.edit-semester-icon {
  position: relative;
  top: 2px;
}

.semester-header h4,
h2,
i {
  display: inline-block;
  vertical-align: middle;
}
</style>
