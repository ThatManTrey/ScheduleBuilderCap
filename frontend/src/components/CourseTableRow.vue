<template lang="html">
  <tr class="text-theme-whitest">
    <td>
      <a class="course-info-link" @click="showCourseInfoModal()">
        <div class="cell-container">
          {{ course.courseID }}
        </div>
      </a>
    </td>
    <td>
      <a class="course-info-link" @click="showCourseInfoModal()">
        <div class="cell-container">
          <span v-if="course.creditHoursMax === course.creditHoursMin">
            {{ course.creditHoursMax }}
          </span>
          <span v-if="course.creditHoursMax !== course.creditHoursMin">
            {{ course.creditHoursMin }} - {{ course.creditHoursMax }}
          </span>
          Credits
        </div>
      </a>
    </td>
    <td>
      <a class="course-info-link" @click="showCourseInfoModal()">
        <div class="cell-container">
          {{ course.courseName }}
        </div>
      </a>
    </td>
    <td>
      <a class="course-info-link" @click="showCourseInfoModal()">
        <div class="cell-container">
          {{ course.courseDesc }}
        </div>
      </a>
    </td>
    <td>
      <div class="cell-container center p-1">
        <button
            v-if="!isScheduled"
            @click="showAddToSemesterModal()"
            class="button-as-link"
          >
            <i class="fas fa-plus-circle fa-lg table-icon"></i>
          </button>
        <button
            v-if="isScheduled"
            @click="removeFromSemester()"
            class="button-as-link"
          >
          <i class="fas fa-times-circle fa-lg table-icon"></i>
        </button>
      </div>
    </td>
  </tr>
</template>

<script lang="js">

export default {
    props: ['course'],

    computed: {
      isScheduled() {
        return this.$store.getters["semesters/isCourseScheduled"](
          this.course.courseID
        );
      }
    },

    methods: {
        showCourseInfoModal() {
            this.$store.commit("courses/setCurrentCourse", { course: this.course });
            this.$emit("openCourseInfoModal");
        },

        showAddToSemesterModal() {
            this.$store.commit("courses/setCurrentCourse", { course: this.course });
            this.$emit("openAddSemesterModal");
        },

        removeFromSemester() {
      this.$store.dispatch(
        "semesters/removeCourseFromSemester",
        this.course.courseID
      );
    },
    }
}
</script>

<style lang="scss" scoped>
tr {
  border-color: var(--theme-black);

  &:last-child {
    border-color: transparent;
  }
}

td {
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.cell-container {
  height: 50px;
  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;

  &.center {
    display: flex;
    align-items: center;
  }
}

.table-icon {
  font-size: 1.5rem;
}

.course-info-link {
  color: currentColor;
}
</style>
