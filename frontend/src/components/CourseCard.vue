<template lang="html">
  <div class="card justify-content-center course-card">
    <div class="card-body container-fluid text-theme-whiter">
      <a
        tabindex="0"
        @keyup.enter="showCourseInfoModal()"
        @click="showCourseInfoModal()"
      >
        <div>
          <div class="row text-theme-whitest">
            <h4 class="course-card-title m-1">{{ course.courseName }}</h4>
          </div>

          <div class="row" :class="{ 'mb-2': !showSmallCard }">
            <div class="col-10 p-0">
              <span class="badge rounded-pill course-badge">
                {{ course.courseID }}
              </span>

              <span
                v-if="course.creditHoursMax == course.creditHoursMin"
                class="badge rounded-pill course-badge"
              >
                {{ course.creditHoursMax }} Credits
              </span>
              <span v-else class="badge rounded-pill course-badge">
                {{ course.creditHoursMin }} - {{ course.creditHoursMax }}
                Credits
              </span>
            </div>
          </div>

          <div v-if="!showSmallCard" class="row mb-3">
            <p class="card-text">
              {{ course.courseDesc }}
            </p>
          </div>
        </div>
      </a>

      <div v-if="!showSmallCard" class="row">
        <div v-if="isLoggedIn" class="col">
          <button
            tabindex="0"
            v-if="!isFavorited"
            @click="addToFavorites()"
            data-tooltip="Favorite Course"
            class="button-as-link"
          >
            <i class="far fa-bookmark fa-lg"></i>
          </button>
          <button
            tabindex="0"
            v-else
            @click="removeFromFavorites()"
            data-tooltip="Unfavorite Course"
            class="button-as-link"
          >
            <i class="fas fa-bookmark fa-lg"></i>
          </button>
        </div>

        <div v-if="isLoggedIn" class="col text-end">
          <button
            v-if="!isScheduled"
            tabindex="0"
            @click="showAddToSemesterModal()"
            data-tooltip="Add to Semester"
            class="button-as-link"
          >
            <i class="fas fa-plus-circle fa-lg"></i>
          </button>
          <button
            v-if="isScheduled"
            tabindex="0"
            @click="removeFromSemester()"
            data-tooltip="Remove from Semester"
            class="button-as-link"
          >
            <i class="fas fa-times-circle fa-lg"></i>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from "vuex";

export default {
  props: {
    course: {
      type: Object
    }
  },

  computed: {
    ...mapGetters("courses", {
      showSmallCard: "showSmallCard"
    }),

    ...mapState({
      isLoggedIn: state => state.auth.isAuthenticated,
      userID: state => state.auth.userId,
      currentCourse: state => state.courses.currentCourse
    }),

    isFavorited() {
      return this.$store.getters["favorites/isCourseFavorited"](
        this.course.courseID
      );
    },

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

    addToFavorites() {
      this.$store.dispatch("favorites/addFavorite", this.course);
    },

    removeFromFavorites() {
      this.$store.dispatch("favorites/removeFavorite", this.course);
    }
  }
};
</script>

<style scoped lang="scss">
div.course-card {
  background-color: var(--theme-blacker);
  //transition: transform 0.2s;
}

div.course-card:hover,
div.course-card:focus-within {
  background-color: var(--theme-black);

  box-shadow: inset 1px 0 0 rgb(255 255 255 / 20%),
    inset -1px 0 0 rgb(255 255 255 / 20%), 0 0 4px 0 rgb(95 99 104 / 60%),
    0 0 6px 2px rgb(95 99 104 / 60%);
  z-index: 1;

  // disabling since it messes with the tooltip
  //transform: scale(1.05);
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
  margin-top: 0.75rem;
}

.course-badge button {
  font: inherit;
}

.course-card-title {
  font-size: 17pt;
  min-height: 3.5rem;
  display: flex;
  justify-content: center;
  align-items: center;

  overflow: hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-line-clamp: 2; /* number of lines to show */
  -webkit-box-orient: vertical;
}

.link.small {
  font-size: 11pt;
}
</style>
