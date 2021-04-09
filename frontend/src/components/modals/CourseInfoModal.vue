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
            </p>
            <p
              v-if="
                course.course.contactHoursMin != course.course.contactHoursMax
              "
            >
              <strong> Contact Hours</strong>:
              <span id="creditHours">
                {{ course.course.contactHoursMin }} -
                {{ course.course.contactHoursMax }}</span
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
              <h3 v-if="ratings.quality >= 1 && ratings.quality < 3">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.quality >= 3 && ratings.quality < 5">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.quality >= 5 && ratings.quality < 7">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.quality >= 7 && ratings.quality < 9">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.quality >= 9 && ratings.quality <= 10">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="!ratings.quality || ratings.quality < 1">
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <p v-if="!ratings.quality" id="creditHours">0 / 10</p>
              <p v-else id="creditHours">{{ ratings.quality }} / 10</p>
            </div>
          </div>

          <div class="col">
            Course Difficulty:
            <div class="avg-rating">
              <h3 v-if="ratings.difficulty >= 1 && ratings.difficulty < 3">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.difficulty >= 3 && ratings.difficulty < 5">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.difficulty >= 5 && ratings.difficulty < 7">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.difficulty >= 7 && ratings.difficulty < 9">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="ratings.difficulty >= 9 && ratings.difficulty <= 10">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-if="!ratings.difficulty || ratings.difficulty < 1">
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <p v-if="!ratings.difficulty" id="creditHours">0 / 10</p>
              <p v-else id="creditHours">{{ ratings.difficulty }} / 10</p>
            </div>
          </div>
        </div>
        <div class="text-center">
          <button
            v-if="$store.state.auth.hasConfirmedEmail"
            type="button"
            class="btn btn-theme-primary-dark"
          >
            Add My Rating
          </button>
        </div>
      </div>
    </template>

    <template v-if="$store.state.auth.isAuthenticated" v-slot:footer>
      <div class="d-flex" id="course-info-footer">
        <a
          tabindex="0"
          v-if="!isAFavorite"
          @keyup.enter="addToFavorites(course)"
          @click="addToFavorites(course)"
          data-tooltip="Favorite Course"
          data-tooltip-location="bottom"
          ><i class="far fa-bookmark fa-lg"></i
        ></a>
        <a
          tabindex="0"
          v-if="isAFavorite"
          @keyup.enter="removeFromFavorites(course)"
          @click="removeFromFavorites(course)"
          data-tooltip="Unfavorite Course"
          data-tooltip-location="bottom"
          ><i class="fas fa-bookmark fa-lg"></i
        ></a>
        <a
          class="ms-auto"
          @click="openAddToSemesterModal"
          data-tooltip="Add to Semester"
          data-tooltip-location="bottom"
        >
          <i class="fas fa-plus-circle fa-lg plus-add-icon"></i>
        </a>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import axios from "axios";
import * as Toast from "../../toast.js";

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
    // loading test
    this.getRatings();
  },

  computed: mapState({
    userID: state => state.auth.userId,
    course: state => state.courses.currentCourse
  }),

  methods: {
    /* needed to open/close this modal from parent component */
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

    getRatings() {
      var baseUrl =
        process.env.VUE_APP_API_URL + "/courses/" + this.course.course.courseID;

      //AJAX request
      axios
        .get(baseUrl + "/ratings")
        .then(res => {
          this.ratings = res.data;
          this.hasLoadedRatings = true;
        })
        .catch(error => {
          // eslint-disable-next-line
              console.error(error);
        });
    },
    addToFavorites(course) {
      var baseUrl = process.env.VUE_APP_API_URL + "/user/" + this.userID;

      //AJAX request
      axios
        .post(baseUrl + "/favorites/add", {
          course_id: course.course.courseID
        })
        .then(res => {
          console.log(res);
          this.displaySuccess(res);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          Toast.showErrorMessage("Unable to add course.");
        });
    },

    removeFromFavorites(course) {
      var baseUrl = process.env.VUE_APP_API_URL + "/user/" + this.userID;

      //AJAX request
      axios
        .delete(baseUrl + "/favorites/remove", {
          course_id: course.courseID
        })
        .then(res => {
          console.log(res);
          this.displaySuccess(res);
        })
        .catch(error => {
          // eslint-disable-next-line
          console.error(error);
          Toast.showErrorMessage("Unable to remove course.");
        });
    },

    displaySuccess(res) {
      if (res.status >= 200 || res.status < 300) {
        Toast.showSuccessMessage("Course added successfully!");
      }
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
</style>
