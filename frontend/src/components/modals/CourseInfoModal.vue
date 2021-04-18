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
          <h5><strong>Description</strong></h5>
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
              <span id="creditHours"> {{ course.course.creditHoursMax }}</span>
              Hours
            </p>
            <p
              v-if="
                course.course.contactHoursMin != course.course.contactHoursMax
              "
            >
              <strong> Contact Hours</strong>:
              <span id="creditHours">
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
            <div class="avg-rating">
              <h3 v-if="ratings.quality <= 1">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.quality > 1 && ratings.quality <= 2">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.quality > 2 && ratings.quality <= 3">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.quality > 3 && ratings.quality <= 4">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.quality > 4">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="!ratings.quality">
                <p id="noRatings">This course has not been rated yet.</p>
              </h3>
              <p v-if="ratings.quality" id="creditHours">
                {{ ratings.quality }} / 5
              </p>
            </div>
          </div>

          <div class="col">
            Course Difficulty:
            <div class="avg-rating">
              <h3 v-if="ratings.difficulty <= 1" class="text-theme-success">
                Easy
              </h3>
              <h3
                v-if="ratings.difficulty > 1 && ratings.difficulty <= 2"
                class="text-theme-secondary"
              >
                Average
              </h3>
              <h3
                v-if="ratings.difficulty > 2"
                class="text-theme-warning-light"
              >
                Difficult
              </h3>
              <h3 v-if="!ratings.difficulty">
                <p id="noRatings">This course has not been rated yet.</p>
              </h3>
            </div>
          </div>
        </div>
        <div v-if="$store.state.auth.hasConfirmedEmail" class="text-center">
          <button
            v-if="!$store.state.ratings.isRatedCourse"
            type="button"
            @click="openAddRatingModal"
            class="btn btn-theme-primary-dark"
          >
            Add My Rating
          </button>
          <p v-if="$store.state.ratings.isRatedCourse">
            You've already rated this course.
          </p>
          <button
            v-if="$store.state.ratings.isRatedCourse"
            type="button"
            @click="openViewRatingModal"
            class="btn btn-theme-secondary"
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
      hasLoadedRatings: false,
      isAFavorite: null
    };
  },

  isAFavorite: {
    type: Boolean,
    default: true
  },

  created() {
    if (this.course.course)
      this.$store.dispatch("ratings/getCourseRatings"), this.course.course;
  },

  computed: {
    ...mapState({
      course: state => state.courses.currentCourse,
      isLoggedIn: state => state.auth.isAuthenticated
      //isSendingFavorites: state => state.favorites.isSendingFavorite
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

#creditHours {
  color: var(--theme-secondary);
  font-weight: 700;
  padding-top: 0.25rem;
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
