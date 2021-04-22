import axios from "axios";
import * as Toast from "../../toast";

const state = () => ({
  ratings: [],
  currentUserRating: {
    currentUserRatingQuality: null,
    currentUserRatingDifficulty: null
  },
  currentQuality: "",
  currentDifficulty: "",
  userRatedCourses: [],
  isLoadingRatings: true,
  isRatedCourse: false
});

const mutations = {
  setIsLoadingRatings(state, isLoading) {
    state.isLoadingRatings = isLoading;
  },

  setUserRatings(state, userRatedCourses) {
    state.userRatedCourses = userRatedCourses;
  },

  setIsUserRatedCourse(state, isRatedCourse) {
    state.isRatedCourse = isRatedCourse;
  },

  setCourseRatings(state, result) {
    state.ratings = result.ratings;
    state.currentQuality = result.quality;
    state.currentDifficulty = result.difficulty;
  },

  setCurrentUserRating(state, rating) {
    state.currentUserRating.currentUserRatingQuality =
      rating.rating[0].ratingQuality;
    state.currentUserRating.currentUserRatingDifficulty =
      rating.rating[0].ratingDifficulty;
  },

  addRating(state, rating) {
    state.userRatedCourses.ratedCourses.push(rating);
  },

  removeRating(state, courseId) {
    const index = state.userRatedCourses.ratedCourses.findIndex(
      course => course.courseID === courseId
    );
    if (index > -1) state.userRatedCourses.ratedCourses.splice(index, 1);
  }
};

const getters = {
  isUserRatedCourse: state => courseId => {
    return state.userRatedCourses.ratedCourses.some(
      course => course.courseID === courseId
    );
  }
};

const actions = {
  getUserRatedCourses({ commit, rootState, state }) {
    var url = "users/" + rootState.auth.userId + "/ratings";

    axios.get(url).then(res => {
      commit("setUserRatings", res.data);
      if (state.isLoadingRatings) commit("setIsLoadingRatings", false);
    });
  },

  getUserCourseRating({ rootState, commit }, { course }) {
    var url = "users/" + rootState.auth.userId + "/ratings/" + course.courseID;

    //AJAX request
    axios.get(url).then(res => {
      commit("setCurrentUserRating", res.data);
    });
  },

  getCourseRatings({ commit, state }, { course }) {
    var baseUrl = process.env.VUE_APP_API_URL + "/courses/" + course.courseID;

    //AJAX request
    axios
      .get(baseUrl + "/ratings")
      .then(res => {
        commit("setCourseRatings", res.data);
        if (state.isLoadingRatings) commit("setIsLoadingRatings", false);
      })
      .catch(() => {
        Toast.showErrorMessage("Error getting course ratings.", 10000);
      });
  },

  addRating(
    { dispatch, commit, rootState },
    { course, qualityVal, difficultyVal }
  ) {
    var rating = {
      courseID: rootState.courses.currentCourse.course.courseID,
      ratingDifficulty: difficultyVal,
      ratingQuality: qualityVal,
      userID: rootState.auth.userId
    };
    commit("addRating", rating);

    var url = "users/" + rootState.auth.userId + "/ratings";
    axios
      .post(url, {
        course_id: rootState.courses.currentCourse.course.courseID,
        quality: qualityVal,
        difficulty: difficultyVal,
        user_id: rootState.auth.userId
      })
      .then(() => {
        Toast.showSuccessMessage("Your rating was added successfully!");
        dispatch("getUserCourseRating", { course: course });
      })
      .catch(() => {
        // revert client side addition
        commit("removeRating", course.courseID);
        Toast.showErrorMessage("Error adding your rating.");
      });
  },

  removeRating({ commit, rootState }, course) {
    commit("removeRating", course.courseID);

    var url = "users/" + rootState.auth.userId + "/ratings/" + course.courseID;
    axios
      .delete(url)
      .then(() => {
        Toast.showSuccessMessage("Your rating has been removed.");
      })
      .catch(() => {
        // revert client-side removal
        commit("addRating", course);
        Toast.showErrorMessage("Error removing your rating.");
      });
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};
