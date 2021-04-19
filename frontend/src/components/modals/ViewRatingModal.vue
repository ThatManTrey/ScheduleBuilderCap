<template lang="html">
  <Modal :centerHeader="true" :useFooter="true" ref="viewRatingBaseModalRef">
    <template v-slot:header v-if="course.course"
      >Your ratings for {{ course.course.courseID }}</template
    >
    <template v-slot:body v-if="course.course">
      <div class="text-center mt-3">
        <div>
          <h6>
            You rated {{ course.course.courseID }} in terms of
            <strong>quality</strong>:
          </h6>
          <div class="avg-rating" v-if="userQuality">
            <h3 v-if="userQuality <= 1">
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
            </h3>
            <h3
              v-if="userQuality > 1 && userQuality <= 2"
            >
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
            </h3>
            <h3
              v-if="userQuality > 2 && userQuality <= 3"
            >
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
            </h3>
            <h3
              v-if="userQuality > 3 && userQuality <= 4"
            >
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="far fa-star fa-lg text-theme-secondary"></i>
            </h3>
            <h3 v-if="userQuality > 4">
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
            </h3>
            <h3 v-if="!userQuality">
              <p id="noRatings">error</p>
            </h3>
            <p v-if="userQuality" id="creditHours">
              {{ userQuality }} / 5
            </p>
          </div>
        </div>
        <div class="padding">
          <h6>
            You rated {{ course.course.courseID }} in terms of
            <strong>difficulty</strong>:
          </h6>
          <div class="avg-rating" v-if="userDifficulty">
            <h3
              v-if="userDifficulty <= 1"
              class="text-theme-confirm"
            >
              Easy
            </h3>
            <h3
              v-if="
                userDifficulty> 1 &&
                  userDifficulty <= 2
              "
              class="text-theme-secondary"
            >
              Average
            </h3>
            <h3
              v-if="userDifficulty > 2"
              class="text-theme-warning-light"
            >
              Difficult
            </h3>
            <h3 v-if="!userDifficulty">
              <p id="noRatings">error</p>
            </h3>
          </div>
      </div>
    </div>
    </template>

    <template v-slot:footer v-if="course.course">
      <div class="d-flex justify-content-between" id="ratings-footer">
        <a
          @click="removeRating(course)"
          @keyup.enter="removeRating(course)"
          data-tooltip="Remove Rating"
          data-tooltip-location="right"
        >
          <i class="fas fa-trash fa-md"></i
        ></a>
        <a
          @click="editRating(course)"
          @keyup.enter="editRating(course)"
          data-tooltip="Edit Rating"
          data-tooltip-location="left"
        >
          <i class="fas fa-edit fa-md"></i
        ></a>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import { mapState } from "vuex";

export default {

  computed: mapState({
    course: state => state.courses.currentCourse,
    userQuality: state => state.ratings.currentUserRating.rating[0].ratingQuality,
    userDifficulty: state => state.ratings.currentUserRating.rating[0].ratingDifficulty
  }),

  components: {
    Modal
  },

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.viewRatingBaseModalRef.openModal();
    },

    closeModal() {
      this.$refs.viewRatingBaseModalRef.closeModal();
    },

    editRating() {
      this.$store.dispatch("ratings/removeRating", this.course.course);
      this.openAddRatingModal();
    },

    removeRating() {
      this.$store.dispatch("ratings/removeRating", this.course.course);
      this.closeModal();
    },

    openAddRatingModal() {
      this.closeModal();

      setTimeout(() => {
        this.$emit("openAddRatingModal");
      }, 320);
    }
  }
};
</script>

<style scoped>
#ratings-footer {
  width: 100%;
  font-size: 1.15rem;
}

.avg-rating {
  margin-top: 1rem;
  margin-bottom: 1.25rem;
}

.padding {
  margin-top: 3rem;
}

#noRatings {
  font-size: 12pt;
  color: var(--theme-warning-light);
}

#easy {
  color: var(--theme-success);
  font-weight: bold;
  font-size: 12pt;
}

#average {
  color: var(--theme-secondary);
  font-weight: bold;
  font-size: 12pt;
}

#diffuclt {
  color: var(--theme-warning-light);
  font-weight: bold;
  font-size: 12pt;
}
</style>
