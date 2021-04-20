<template lang="html">
  <div>
    <div class="semester-accordion mb-3">
      <div class="semester-header">
        <div class="semester-title align-middle">
          <button
            @click="removeSemester()"
            @keyup.enter="removeSemester()"
            data-tooltip="Remove Semester"
            class="button-as-link remove-semester"
          >
            <i class="fas fa-trash"></i>
          </button>
          <div class="text-theme-whitest d-inline">
            <h2
              class="m-0"
              contenteditable
              @keyup.enter="getUserInput"
              @keydown.enter="endUserInput"
              @input="getUserInput"
            >
              {{ semester.semesterName }}
            </h2>
          </div>
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

    <div
      class="semester-body collapse mb-3"
      :class="{ show: hasCourses }"
      :id="targetName"
    >
      <div class="container">
        <div
          v-if="semester.semesterCourses.length > 0"
          class="row justify-content-center"
        >
          <div
            v-for="(course, index) in semester.semesterCourses"
            :key="index"
            class="d-flex col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3"
          >
            <CourseCard
              @openAddSemesterModal="showAddToSemesterModal"
              @openCourseInfoModal="showCourseInfoModal"
              :isRemovingCourse="true"
              :course="course"
            ></CourseCard>
          </div>
        </div>
        <div class="row text-center" v-else>
          <h5>You haven't added any courses to this semester yet.</h5>
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
      targetName: String,
      semester: Object
    },

    data() {
      return {
        semesterName: this.semester.semesterName,
      };
    },

    computed: {
      hasCourses() {
        return this.semester.semesterCourses.length > 0;
      }
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

        getUserInput(e) {
            this.semesterName = e.target.innerText;
        },

        endUserInput(e) {
            // remove focus from semester name
            e.srcElement.blur();

            // remove whitespace from both sides of semester name
            this.semesterName = this.semesterName.trim();

            if(this.semesterName < 1)
                e.target.innerText = this.semester.semesterName;
            else if(this.semesterName > 64)    // semester name max size in db
                e.target.innerText = this.semester.semesterName;
            else
              e.target.innerText = this.semesterName;

            if(this.semesterName !== this.semester.semesterName)
                this.$store.dispatch("semesters/editSemesterName", {
                    semesterId: this.semester.semesterId,
                    newName: this.semesterName
                })
        },

        removeSemester() {
          var removeSemester = confirm(
            "Are you sure you want to remove this semester and all its courses?"
          );

          if (removeSemester)
            this.$store.dispatch("semesters/removeSemester", this.semester.semesterId);

        }
    }
}
</script>

<style scoped lang="scss">
.semester-accordion {
  width: 100%;
}

.semester-title {
  width: 95%;
  margin: auto;
}

.semester-header {
  display: inline-block;
  width: 100%;
}

.remove-semester {
  position: relative;
  top: 4px;
  margin-right: 1rem;
  font-size: 1.2rem;
}

.semester-header h4,
h2,
i {
  display: inline-block;
  vertical-align: middle;
}

.edit-semester-name {
  cursor: pointer;

  &:active,
  &:focus {
    cursor: text;
  }
}
</style>
