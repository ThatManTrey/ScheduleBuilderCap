<template lang="html">
  <Modal
    :useLargeModal="true"
    :useFooter="$store.state.auth.isAuthenticated"
    ref="courseInfoBaseModalRef"
  >
    <template v-slot:header v-if="course.course"
      >{{ course.course.courseID }} - {{ course.course.courseName }}</template
    >

    <template v-slot:body v-if="course.course">
      <div class="container-fluid">
        <div class="row">
          <h5>
            <strong>Description</strong
            ><span class="text-theme-white float-end">{{
              courseProgramName
            }}</span>
          </h5>
          <p>
            {{ course.course.courseDesc }}
          </p>
        </div>
        <div class="row">
          <p><strong>Prerequisite</strong>: {{ course.course.prereqs }}</p>
          <!-- <p><strong>Attributes</strong>: {{}}</p> -->
        </div>
        <div class="row">
          <div class="col-6">
            <p
              v-if="
                course.course.creditHoursMax == course.course.creditHoursMin
              "
            >
              <strong>Credits</strong>:
              <span id="creditHours">{{ course.course.creditHoursMax }}</span>
              Credit Hours
            </p>
            <p
              v-if="
                course.course.creditHoursMax != course.course.creditHoursMin
              "
            >
              <strong>Credits</strong>:
              <span id="creditHours">
                {{ course.course.creditHoursMin }}-{{
                  course.course.creditHoursMax
                }}</span
              >
              Credit Hours
            </p>
            <p>
              <strong>Schedule Type</strong>: {{ course.course.courseType }}
            </p>
          </div>
          <div class="col-6">
            <p
              v-if="
                course.course.contactHoursMin == course.course.contactHoursMax
              "
            >
              <strong> Contact Hours</strong>:
              <span> {{ course.course.creditHoursMax }}</span>
              Hours
            </p>
            <p
              v-if="
                course.course.contactHoursMin != course.course.contactHoursMax
              "
            >
              <strong> Contact Hours</strong>:
              <span>
                {{ course.course.contactHoursMin }}-{{
                  course.course.contactHoursMax
                }}</span
              >
              Hours
            </p>
            <p><strong>Grade Mode</strong>: {{ course.course.gradeType }}</p>
          </div>
        </div>

        <div class="row text-center">
          <hr class="bg-theme-darkest-gray" size="5" />
          <div class="col">
            Course Quality:
            <div
              class="avg-rating"
              v-if="!$store.state.ratings.isLoadingRatings"
            >
              <h3 v-if="courseRatings.currentQuality <= 1">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3
                v-if="
                  courseRatings.currentQuality > 1 &&
                    courseRatings.currentQuality <= 2
                "
              >
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3
                v-if="
                  courseRatings.currentQuality > 2 &&
                    courseRatings.currentQuality <= 3
                "
              >
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3
                v-if="
                  courseRatings.currentQuality > 3 &&
                    courseRatings.currentQuality <= 4
                "
              >
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="courseRatings.currentQuality > 4">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="!courseRatings.currentQuality">
                <p id="noRatings">This course has not been rated yet.</p>
              </h3>
            </div>
          </div>

          <div class="col">
            Course Difficulty:
            <div
              class="avg-rating"
              v-if="!$store.state.ratings.isLoadingRatings"
            >
              <h3
                v-if="courseRatings.currentDifficulty <= 1"
                class="text-theme-confirm"
              >
                Easy
              </h3>
              <h3
                v-if="
                  courseRatings.currentDifficulty > 1 &&
                    courseRatings.currentDifficulty <= 2
                "
                class="text-theme-secondary"
              >
                Average
              </h3>
              <h3
                v-if="courseRatings.currentDifficulty > 2"
                class="text-theme-warning-light"
              >
                Difficult
              </h3>
              <h3 v-if="!courseRatings.currentDifficulty">
                <p id="noRatings">This course has not been rated yet.</p>
              </h3>
            </div>
          </div>
        </div>
        <div v-if="$store.state.auth.hasConfirmedEmail" class="text-center">
          <button
            v-if="!isRated"
            type="button"
            @click="openAddRatingModal"
            class="btn btn-theme-primary-dark"
          >
            Add My Rating
          </button>
          <p v-if="isRated">
            You've already rated this course.
          </p>
          <button
            v-if="isRated"
            type="button"
            @click="openViewRatingModal"
            class="btn btn-theme-primary-dark"
          >
            View Rating
          </button>
        </div>
      </div>
    </template>

    <template v-if="isLoggedIn" v-slot:footer>
      <div class="d-flex" id="course-info-footer">
        <button
          v-if="!isFavorited"
          @click="addToFavorites(course)"
          data-tooltip="Favorite Course"
          data-tooltip-location="right"
          class="button-as-link"
        >
          <i class="far fa-bookmark fa-lg"></i>
        </button>
        <button
          v-else
          @click="removeFromFavorites(course)"
          data-tooltip="Unfavorite Course"
          data-tooltip-location="right"
          class="button-as-link"
        >
          <i class="fas fa-bookmark fa-lg"></i>
        </button>
        <button
          v-if="!isScheduled"
          class="ms-auto button-as-link"
          @click="openAddToSemesterModal"
          data-tooltip="Add to Semester"
          data-tooltip-location="left"
        >
          <i class="fas fa-plus-circle fa-lg plus-add-icon"></i>
        </button>
        <button
          v-if="isScheduled"
          @click="removeFromSemester()"
          data-tooltip="Remove from Semester"
          data-tooltip-location="left"
          class="ms-auto button-as-link"
        >
          <i class="fas fa-times-circle fa-lg"></i>
        </button>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import { mapState } from "vuex";

export default {
  components: {
    Modal
  },

  data() {
    return {
      ratings: [],
      hasLoadedRatings: false
    };
  },

  computed: {
    ...mapState({
      course: state => state.courses.currentCourse,
      courseRatings: state => state.ratings,
      isLoggedIn: state => state.auth.isAuthenticated
    }),

    isFavorited() {
      if (!this.course.course) return false;
      return this.$store.getters["favorites/isCourseFavorited"](
        this.course.course.courseID
      );
    },

    isRated() {
      if (!this.course.course) return false;
      return this.$store.getters["ratings/isUserRatedCourse"](
        this.course.course.courseID
      );
    },

    isScheduled() {
      if (!this.course.course) return false;
      return this.$store.getters["semesters/isCourseScheduled"](
        this.course.course.courseID
      );
    },

    courseProgramName() {
      return this.$store.getters["courses/getProgramNameForCourse"](
        this.course.course.courseIDType
      );
    }
  },

  methods: {
    openModal() {
      this.$refs.courseInfoBaseModalRef.openModal();
    },

    closeModal() {
      this.$refs.courseInfoBaseModalRef.closeModal();
    },

    openAddToSemesterModal() {
      /* avoids nested modals */
      this.closeModal();

      /* needed to prevent scroll bar from showing when switching modals, idk why */
      setTimeout(() => {
        this.$emit("openAddSemesterModal");
      }, 320);
    },

    openAddRatingModal() {
      this.closeModal();

      setTimeout(() => {
        this.$emit("openAddRatingModal");
      }, 320);
    },

    openViewRatingModal() {
      this.closeModal();

      setTimeout(() => {
        this.$emit("openViewRatingModal");
      }, 320);
    },

    addToFavorites() {
      this.$store.dispatch("favorites/addFavorite", this.course.course);
    },

    removeFromFavorites() {
      this.$store.dispatch("favorites/removeFavorite", this.course.course);
    },

    removeFromSemester() {
      this.$store.dispatch(
        "semesters/removeCourseFromSemester",
        this.course.course.courseID
      );
    }
  }
};
</script>

<style scoped>
strong {
  color: var(--theme-whitest);
}

p {
  color: var(--theme-white);
}

#course-info-footer {
  width: 100%;
  font-size: 1.15rem;
}

.avg-rating {
  margin-top: 1rem;
  margin-bottom: 1.25rem;
}

#noRatings {
  font-size: 12pt;
}
</style>
