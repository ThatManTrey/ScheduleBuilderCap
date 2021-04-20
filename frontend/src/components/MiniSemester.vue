<template lang="html">
  <div class="semester me-4">
    <ul class="list-group">
      <li class="list-group-item header">
        <button
          @click="removeSemester()"
          data-tooltip="Remove Semester"
          data-tooltip-location="bottom"
          class="button-as-link"
        >
          <i class="fas fa-trash fa-sm padding"></i>
        </button>
        <span
          id="semesterName"
          contenteditable
          @keyup.enter="getUserInput"
          @keydown.enter="endUserInput"
          @input="getUserInput"
          >{{ semester.semesterName }}</span
        >
        <!--<span class="badge rounded-pill course-badge float-right">
          <button class="button-as-link" id="semesterCredits">16</button>
        </span>-->
      </li>

      <li
        class="list-group-item course"
        v-for="(course, index) in semester.semesterCourses"
        :key="index"
      >
        <button
          @click="removeCourse(course.courseID)"
          class="button-as-link"
          id="remove"
        >
          <i class="fas fa-times-circle fa-md"></i>
        </button>
        <span class="badge rounded-pill course-badge">
          <button class="button-as-link">{{ course.courseID }}</button></span
        >
        <span class="courseName">{{ course.courseName }}</span>
      </li>
      <li v-if="semester.semesterCourses.length == 0" id="emptySemester">
        <span class="text-theme-white">You haven't added any courses yet.</span>
      </li>
    </ul>
  </div>
</template>

<script lang="js">

export default {
    name: 'miniSemester',
    props: {
      targetName: String,
      semester: Object,
      course: Object
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

    methods: {
      getUserInput(e) {
            const input = e.target.innerText;

            if(input.length < 1)
                e.target.innerText = this.semester.semesterName;
            else if(input.length > 64)    // semester name max size in db
                e.target.innerText = this.semester.semesterName;
            else
                this.semesterName = input;
        },

        endUserInput(e) {
            // remove focus from semester name
            e.srcElement.blur();

            // remove whitespace from both sides of semester name
            this.semesterName = this.semesterName.trim();
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
        },

        removeCourse(courseID) {
            this.$store.dispatch(
              "semesters/removeCourseFromSemester", courseID
            );
        }
      },

}
</script>

<style scoped>
div.container {
  padding: 10px;
}

.list-group li {
  background-color: var(--theme-blacker);
  color: var(--theme-whiter);
  overflow: hidden;
}

.list-group li.course {
  font-size: 10pt;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.list-group-item.header {
  font-size: 12pt;
  color: var(--theme-whitest);
  background-color: var(--theme-blackest);
}

span.courseName {
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
  /* fix */
  /* overflow-y: auto; */
  width: 16rem;
  display: block;
}

#remove {
  padding-right: 0.5rem;
  margin-left: -0.25rem;
}

#emptySemester {
  list-style-type: none;
  font-size: 10pt;
  text-align: center;
  padding: 0.5rem;
}
</style>
