/* eslint-disable */
<template lang="html">
  <Modal
    :centerHeader="true"
    :useFooter="false"
    ref="addToSemesterBaseModalRef"
  >
    <template v-slot:header>Add Course to Semester</template>
    <template v-slot:body v-if="course.course">
      <div>
        <h6 class="text-center">
          Select the semester you would like to add
          {{ course.course.courseID }} to:
        </h6>
        <div class="list-group mt-3">
          <!-- list of semesters -->
          <div
            tabindex="0"
            class="list-group-item add-course"
            @click="addCourse(semester.semesterId)"
            @keyup.enter="addCourse(semester.semesterId)"
            v-for="(semester, index) in semesters"
            :key="index"
          >
            <!-- @click.stop and @keyup.enter.stop prevents parent element's click from happening -->
            <a
              tabindex="0"
              @keyup.enter.stop
              @keyup.enter="removeSemester(semester)"
              @click.stop
              @click="removeSemester(semester)"
            >
              <i class="fas fa-trash"></i>
            </a>
            {{ semester.semesterName }}
            <span class="badge rounded-pill"
              >{{ semester.semesterCourses.length }} Courses</span
            >
          </div>

          <!-- add a new semester -->
          <div class="list-group-item">
            <div v-show="isAddingSemester" class="container-fluid">
              <div class="row">
                <div class="col-12">
                  <input
                    type="text"
                    class="form-control"
                    placeholder="Enter a semester name..."
                    v-model.trim="semesterName"
                    ref="newSemesterName"
                    @keyup.enter="addSemester()"
                  />
                </div>
                <div class="col-12 mt-2">
                  <button
                    type="submit"
                    class="btn btn-theme-confirm btn-sm me-3"
                    id="add-semeste-btn"
                    @click="addSemester()"
                  >
                    Add Semester
                  </button>
                  <button
                    class="button-as-link"
                    @click="isAddingSemester = false"
                  >
                    <i class="fas fa-times" id="cancel-add"></i>
                  </button>
                </div>
              </div>
            </div>
            <div v-show="!isAddingSemester" id="add-semester-link">
              <button class="button-as-link" @click="openAddSemesterInput">
                <i class="fas fa-plus-circle plus-add-icon"></i>
                <span> Add Semester</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import { mapState } from "vuex";

export default {
  data() {
    return {
      isAddingSemester: false,
      semesterName: ""
    };
  },

  computed: mapState({
    course: state => state.courses.currentCourse,
    semesters: state => state.semesters.semesters
  }),

  components: {
    Modal
  },

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.addToSemesterBaseModalRef.openModal();
    },

    closeModal() {
      this.$refs.addToSemesterBaseModalRef.closeModal();
    },

    openAddSemesterInput() {
      this.isAddingSemester = true;
      setTimeout(() => {
        this.$refs.newSemesterName.focus();
      }, 10);
    },

    addSemester() {
      this.isAddingSemester = false;

      if (this.semesterName.length === 0) {
        const semesterNumber = this.$store.state.semesters.semesters.length + 1;
        this.semesterName = "Semester " + semesterNumber;
      } else if (this.semesterName.length > 64) {
        this.semesterName = this.semesterName.slice(0, 64);
      }

      this.$store
        .dispatch("semesters/addSemester", this.semesterName)
        .then(() => {
          this.semesterName = "";
        });
    },

    removeSemester(semester) {
      var removeSemester = confirm(
        "Are you sure you want to remove " +
          semester.semesterName +
          " and all its courses?"
      );
      if (removeSemester) {
        this.$store.dispatch("semesters/removeSemester", semester.semesterId);
      }
    },

    addCourse(semesterId) {
      this.$store.dispatch("semesters/addCourseToSemester", {
        semesterId: semesterId,
        courseId: this.course.course.courseID
      });
      this.closeModal();
    }
  }
};
</script>

<style scoped>
div.list-group {
  border-radius: 0.5rem;
}

div.list-group-item {
  padding: 0.75rem 1.5rem;
  border: none;
}

div.add-course {
  color: var(--theme-whitest);
  font-weight: bold;
  cursor: pointer;
}

div.add-course:hover,
div.add-course:focus {
  /*border: 3px solid rgba(2, 161, 145, 0.5);*/
  box-shadow: inset 1px 0 0 rgba(2, 161, 145, 0.2),
    inset -1px 0 0 rgba(2, 161, 145, 0.2), 0 0 4px 0 rgba(2, 161, 145, 0.6),
    0 0 6px 2px rgba(2, 161, 145, 0.6);
  outline: none;
  z-index: 1;
}

div.list-group-item:nth-child(odd) {
  background-color: var(--theme-black);
}

div.list-group-item:nth-child(even) {
  background-color: var(--theme-darkest-gray);
}

div.list-group-item i {
  margin-right: 0.25rem;
}

span.badge {
  background-color: var(--theme-dark-gray);
  color: var(--theme-whitest);
  float: right;
}

/* add semester */

#cancel-add {
  position: relative;
  top: 3px;
  font-size: 1.2rem;
}

#add-semester-link {
  font-weight: 400;
  font-size: 0.9rem;
}

#add-semester-link a:hover,
#add-semester-link a:focus {
  color: var(--theme-confirm);
}

#add-semeste-btn {
  margin-bottom: 0;
}
</style>
