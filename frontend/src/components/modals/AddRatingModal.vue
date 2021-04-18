<template lang="html">
  <Modal :centerHeader="true" :useFooter="false" ref="addRatingBaseModalRef">
    <template v-slot:header v-if="course.course"
      >Add Rating to {{ course.course.courseID }}</template
    >
    <template v-slot:body v-if="course.course">
      <div class="text-center">
        <div class="row mt-4 mb-4">
          <h6>
            How would you rate {{ course.course.courseID }} in terms of <strong>quality</strong>?
          </h6>
          <div class="sliderContainer text-center">
            <input
              type="range"
              min="1"
              max="5"
              v-model="rating.quality"
              class="slider"
              id="qualitySlider"
            />
            <p
              class="displayVal text-theme-light-gray"
              v-text="rating.quality"
            ></p>
          </div>
        </div>
        <div class="row mt-3 mb-4">
          <h6>
            How would you rate {{ course.course.courseID }} in terms of
            <strong>difficulty</strong>?
          </h6>
          <div class="sliderContainer text-center">
            <input
              type="range"
              min="1"
              max="3"
              v-model="rating.difficulty"
              class="slider"
              id="difficultySlider"
            />
            <p
              class="displayVal text-theme-confirm"
              v-if="rating.difficulty == 1"
            >
              Easy
            </p>
            <p
              class="displayVal text-theme-secondary"
              v-if="rating.difficulty == 2"
            >
              Average
            </p>
            <p
              class="displayVal text-theme-warning-light"
              v-if="rating.difficulty == 3"
            >
              Difficult
            </p>
          </div>
        </div>
        <div class="mb-2">
          <button
            type="button"
            @click="addRating(course, rating)"
            class="btn btn-theme-primary-dark"
          >
            Submit My Rating
          </button>
        </div>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import { mapState } from "vuex";

export default {
  data() {
    return {
      rating: {
        quality: 3,
        difficulty: 2
      }
    };
  },

  computed: {
    ...mapState({
      course: state => state.courses.currentCourse
    })
  },

  components: {
    Modal
  },

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.addRatingBaseModalRef.openModal();
    },

    closeModal() {
      this.$refs.addRatingBaseModalRef.closeModal();
    },

    addRating() {
      this.$store.dispatch(
        "ratings/addRating",
        this.course.course,
        this.rating.quality,
        this.rating.difficulty
      );

      this.closeModal();
    }
  }
};
</script>

<style scoped>
.sliderContainer {
  margin: auto;
  padding-top: 1rem;
  padding-bottom: 1rem;
  width: 75%;
}

.slider {
  appearance: none;
  width: 100%;
  height: 5px;
  background: var(--theme-light-gray);
  outline: none;
  opacity: 0.5;
  -webkit-transition: 0.2s;
  transition: 0.2s;
}

.slider:hover {
  opacity: 1;
}

.slider::-webkit-slider-thumb {
  appearance: none;
  border: var(--theme-primary-light);
  width: 15px;
  height: 15px;
  background: var(--theme-primary-light);
  cursor: pointer;
}

.slider::-moz-range-thumb {
  border: var(--theme-primary-light);
  width: 15px;
  height: 15px;
  background: var(--theme-primary-light);
  cursor: pointer;
}

.displayVal {
  font-size: 14pt;
  margin-top: 0.25rem;
}
</style>
