<template lang="html">
  <Modal
    :useLargeModal="true"
    :useFooter="$store.state.isAuthenticated"
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
          <p><strong>Attributes</strong>: {{}}</p>
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
              {{ course.course.contactHoursMax }} Hours
            </p>
            <p
              v-if="
                course.course.contactHoursMin != course.course.contactHoursMax
              "
            >
              <strong> Contact Hours</strong>:
              {{ course.course.contactHoursMin }}-{{
                course.course.contactHoursMax
              }}
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
              <h3 v-if="course.quality >= 1 || course.quality < 3">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else-if="course.quality >= 3 || course.quality < 5">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else-if="course.quality >= 5 || course.quality < 7">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else-if="course.quality >= 7 || course.quality < 9">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else-if="course.quality >= 9 || course.quality <= 10">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
            </div>
          </div>

          <div class="col">
            Course Difficulty:
            <div class="avg-rating">
              <h3 v-if="course.difficulty >= 1 || course.difficulty < 3">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else-if="course.difficulty >= 3 || course.difficulty < 5">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else-if="course.difficulty >= 5 || course.difficulty < 7">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else-if="course.difficulty >= 7 || course.difficulty < 9">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else-if="course.difficulty >= 9 || course.difficulty <= 10">
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
                <i class="fas fa-star fa-lg text-theme-secondary"></i>
              </h3>
              <h3 v-else>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
                <i class="far fa-star fa-lg text-theme-secondary"></i>
              </h3>
            </div>
          </div>
        </div>
        <div class="text-center">
          <button
            v-if="$store.state.hasConfirmedEmail"
            type="button"
            class="btn btn-theme-primary-dark"
          >
            Add My Rating
          </button>
        </div>
      </div>
    </template>

    <template v-if="$store.state.isAuthenticated" v-slot:footer>
      <div class="d-flex" id="course-info-footer">
        <a
          href="#"
          data-tooltip="Favorite Course"
          data-tooltip-location="bottom"
        >
          <i class="far fa-bookmark fa-lg bookmark-unfilled-icon"></i
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

  computed: mapState(["course"]),

  created() {
    // loading test
    this.getRatings();
  },

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
      var baseUrl = process.env.VUE_APP_API_URL + "/courses/" + "CS49999";
      // hard coded for now, having trouble passing courseID

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
}

#course-info-footer {
  width: 100%;
  font-size: 1.15rem;
}

.avg-rating {
  margin-top: 1rem;
  margin-bottom: 2rem;
}
</style>
