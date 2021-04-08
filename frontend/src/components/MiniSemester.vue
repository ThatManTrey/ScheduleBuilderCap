<template lang="html">
  <div class="semester">
    <ul class="list-group">
      <li class="list-group-item header">
        <a
          @click="removeSemester()"
          @keyup.enter="removeSemester()"
          data-tooltip="Remove Semester"
          data-tooltip-location="bottom"
        >
          <i class="fas fa-trash fa-sm padding"></i
        ></a>
        <span id="semesterName" contenteditable="true">Spring 2021</span>
        <span class="badge rounded-pill course-badge float-right">
          <button class="button-as-link" id="semesterCredits">16</button>
        </span>
      </li>

      <li class="list-group-item course" v-for="n in 4" :key="n">
        <a
          @click="removeCourse()"
          @keyup.enter="removeCourse()"
          class="fas fa-times-circle fa-md text-theme-warning-dark"
          id="remove"
        ></a>
        <span class="badge rounded-pill course-badge">
          <button class="button-as-link">MATH 13013</button></span
        >
        <span id="courseName">Analytic Geometry...</span>
      </li>
    </ul>
  </div>
</template>

<script lang="js">
import * as Toast from '../toast.js';

export default {
    name: 'miniSemester',
    props: {
      targetName: String
    },
    methods: {
        removeSemester() {
            var removePromptResult = confirm(
                "Are you sure you want to remove this semester and all its courses?"
            );
        if (removePromptResult === true) {
            Toast.showSuccessMessage(
                "Semester was removed successfully."
            );
        }
        },
        removeCourse() {
            var removePromptResult = confirm(
                "Are you sure you want to remove this course?"
            );
        if (removePromptResult === true) {
            Toast.showSuccessMessage(
                "Course was removed successfully."
            );
        }
      },
    }
}
</script>

<style scoped>
div.container {
  padding: 10px;
}

.list-group {
  width: 16rem;
}

.list-group li {
  background-color: var(--theme-blacker);
  color: var(--theme-whiter);
  overflow: hidden;
}

.list-group li.course {
  height: 2.6rem;
  font-size: 10pt;
}

.list-group-item.header {
  font-size: 12pt;
  color: var(--theme-whitest);
  background-color: var(--theme-blackest);
}

#courseName {
  padding-left: 0.5rem;
}

span.course-badge {
  color: var(--theme-whiter);
  background-color: var(--theme-darkest-gray);
}

.course-badge button {
  font: inherit;
}

.padding {
  padding-right: 1rem;
}

.float-right {
  float: right;
  margin-top: 2px;
}

#semesterCredits {
  font-size: 10pt;
}

.semester {
  display: inline-block;
  margin-right: 1rem;
}

#remove {
  padding-right: 0.5rem;
  margin-left: -0.25rem;
}
</style>
