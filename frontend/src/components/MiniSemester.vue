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
          @input="getUserInput"
          @keydown.enter="endUserInputAfterEnter"
          v-click-outside="endUserInputAfterClick"
          ref="editableSemesterName"
          >{{ semester.semesterName }}</span
        >
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
        <span 
          class="badge rounded-pill course-badge"
          tabindex="0"
          @keyup.enter="showCourseInfoModal(course)"
          @click="showCourseInfoModal(course)"
        >
          <button class="button-as-link">{{ course.courseID }}</button></span
        >
        <span 
          class="courseName" 
          tabindex="0"
          @keyup.enter="showCourseInfoModal(course)"
          @click="showCourseInfoModal(course)"
        >
          {{ course.courseName }}
        </span>
      </li>

      <li v-if="semester.semesterCourses.length == 0" id="emptySemester">
        <span class="text-theme-white">You haven't added any courses yet.</span>
      </li>
    </ul>
  </div>
</template>

<script lang="js">
import ClickOutside from 'vue-click-outside'

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
        showCourseInfoModal(course) {
          this.$store.commit("courses/setCurrentCourse", { course: course });
          this.$store.dispatch("ratings/getCourseRatings", { course: course });
          this.$store.dispatch("ratings/getUserCourseRating", {
            course: course
          });
          this.$emit("openCourseInfoModal");
        },

        getUserInput(e) {
            this.semesterName = e.target.innerText;
        },

        endUserInput(e) {
            // remove whitespace from both sides of semester name
            this.semesterName = this.semesterName.trim();

                                            // semester name max size in db
            if(this.semesterName.length < 1 || this.semesterName.length > 64) {
                e.innerText = this.semester.semesterName;
                this.semesterName = this.semester.semesterName;
                return;
            } else e.innerText = this.semesterName;

            if(this.semesterName !== this.semester.semesterName)
                this.$store.dispatch("semesters/editSemesterName", {
                    semesterId: this.semester.semesterId,
                    newName: this.semesterName
                })
        },

        endUserInputAfterClick() {
          this.endUserInput(this.$refs.editableSemesterName);
        },

        endUserInputAfterEnter(e) {
          // remove focus from semester name
          e.srcElement.blur();
          this.endUserInput(e.target);
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

      directives: {
      ClickOutside
    }

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

.list-group li.course:hover {
  background-color: var(--theme-blackest);
  cursor: pointer;
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
