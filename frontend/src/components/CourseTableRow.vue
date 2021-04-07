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
        <a @click="showAddToSemesterModal()"
          ><i class="fas fa-plus-circle text-theme-confirm"></i
        ></a>
      </div>
    </td>
  </tr>
</template>

<script lang="js">

export default {
    props: ['course'],

    methods: {
        showCourseInfoModal() {
            this.$store.commit("auth/setCourse", { course: this.course });
            this.$emit("openCourseInfoModal");
        },
        showAddToSemesterModal() {
            this.$emit("openAddSemesterModal");
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

.fa-plus-circle {
  font-size: 1.5rem;
}

.course-info-link {
  color: currentColor;
}
</style>
