<template lang="html">
  <div class="card justify-content-center course-card">
    <div class="card-body container-fluid text-theme-whiter">
      <div class="row text-theme-whitest">
        <h4 class="course-card-title m-1">{{ course.CourseName }}</h4>
      </div>

      <div class="row" :class="{ 'mb-2': !showSmallCard }">
        <div class="col-10 p-0">
          <span class="badge rounded-pill course-badge">
            <button class="button-as-link">{{ course.CourseID }}</button>
          </span>

          <span class="badge rounded-pill course-badge">
            <button class="button-as-link" v-if="course.CreditHours_Max == course.CreditHours_Min">{{ course.CreditHours_Max }} Credits</button>
            <button class="button-as-link" v-else >{{ course.CreditHours_Min }}-{{ course.CreditHours_Max }} Credits</button>
          </span>
        </div>

        <div v-if="showSmallCard" class="col-2 text-end">
          <a
            tabindex="0"
            @keyup.enter="showCourseInfoModal()"
            @click="showCourseInfoModal()"
          >
            <i class="fas fa-lg fa-info-circle"></i>
          </a>
        </div>
      </div>

      <div v-if="!showSmallCard" class="row mb-3">
        <p class="card-text">
          {{ course.CourseDesc }}
        </p>
      </div>

      <div v-if="!showSmallCard" class="row">
        <div class="col">
          <a tabindex="0"
            data-tooltip="Favorite Course"
            data-tooltip-location="bottom"
            ><i class="far fa-star fa-lg"></i
          ></a>
        </div>

        <div class="col text-center">
          <a
            tabindex="0"
            @keyup.enter="showCourseInfoModal()"
            @click="showCourseInfoModal()"
            class="link small"
            >View more</a>
          </div>

        <div class="col text-end">
          <a
            v-if="!isRemovingCourse"
            tabindex="0"
            @keyup.enter="showAddToSemesterModal()"
            @click="showAddToSemesterModal()"
            data-tooltip="Add to Semester"
            data-tooltip-location="bottom"
            >
            <i class="fas fa-plus-circle fa-lg"></i>
            </a>
          <a
            v-if="isRemovingCourse"
            tabindex="0"
            @keyup.enter="removeFromSemester()"
            @click="removeFromSemester()"
            data-tooltip="Remove from Semester"
            data-tooltip-location="bottom"
            ><i class="fas fa-times-circle fa-lg"></i
          ></a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    showSmallCard: {
      type: Boolean,
      default: false
    },

    /* true replaces the add semester button with a remove button (used on schedule page) */
    isRemovingCourse: {
      type: Boolean,
      default: false
    },

    course: {
      type: Object
    }
  },

  methods: {
    showAddToSemesterModal() {
      this.$emit("openAddSemesterModal");
    },
    showCourseInfoModal() {
      this.$emit("openCourseInfoModal");
    },

    removeFromSemester() {
      confirm("Are you sure you want to remove this course?");
    }
  }
};
</script>

<style scoped lang="scss">
div.course-card {
  background-color: var(--theme-blacker);
  transition: transform 0.2s;
}

div.course-card:hover,
div.course-card:focus-within {
  background-color: var(--theme-black);

  /* shadow taken from dark mode gmail hover styling */
  box-shadow: inset 1px 0 0 rgb(255 255 255 / 20%),
    inset -1px 0 0 rgb(255 255 255 / 20%), 0 0 4px 0 rgb(95 99 104 / 60%),
    0 0 6px 2px rgb(95 99 104 / 60%);
  z-index: 1;

  transform: scale(1.05);
}

.course-desc {
  min-height: 5rem;
}

/*
  limiting text displayed,
  referenced from: 
  https://stackoverflow.com/questions/3922739/limit-text-length-to-n-lines-using-css
*/
.card-text {
  overflow: hidden;
   text-overflow: ellipsis;
   display: -webkit-box;
   -webkit-line-clamp: 5; /* number of lines to show */
   -webkit-box-orient: vertical;
   min-height: 7.5rem;
}

span.course-badge {
  color: var(--theme-whiter);
  background-color: var(--theme-darkest-gray);
  margin-left: 0.5rem;
}

.course-badge button {
  font: inherit;
}

.course-card-title {
  font-family: "Source Sans Pro";
}

i.fa-info-circle {
  color: inherit;
  position: relative;
  top: 3px;
}

.link.small {
  font-size: 11pt;
}
</style>
