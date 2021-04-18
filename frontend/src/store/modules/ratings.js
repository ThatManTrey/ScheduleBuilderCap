import axios from "axios";
import * as Toast from "../../toast";

const state = () => ({
  ratings: [],
  userRatedCourses: [],
  isLoadingRatings: true,
  isRatedCourse: false
});

const mutations = {
  setUserRatings(state, userRatedCourses) {
    state.userRatedCourses = userRatedCourses;
  },

  setCourseRatings(state, ratings) {
    state.ratings = ratings;
  },

  addRating(state, course) {
    state.userRatedCourses.push(course);
  },

  removeRating(state, courseId) {
    const index = state.userRatedCourses.findIndex(
      course => course.courseID === courseId
    );
    if (index > -1) state.userRatedCourses.splice(index, 1);
  }
};

const getters = {
  isUserRatedCourse: state => courseId => {
    return state.userRatedCourses.some(course => course.courseID === courseId);
  }
};

const actions = {
  getUserRatedCourses({ commit, rootState, state }) {
    var url = "users/" + rootState.auth.userId + "/ratings";

    axios
      .get(url)
      .then(res => {
        commit("setUserRatings", res.data.userRatedCourses);
        if (state.isLoadingRatings) commit("setIsLoadingRatings", false);
      })
      .catch(error => {
        // eslint-disable-next-line
          console.error(error);

        if (state.isLoadingRatings) commit("setIsLoadingRatings", false);
      });
  },

  getCourseRatings({ commit, state }, course) {
    var baseUrl = process.env.VUE_APP_API_URL + "/courses/" + course.courseID;

    //AJAX request
    axios
      .get(baseUrl + "/ratings")
      .then(res => {
        commit("setCourseRating", res.data.ratings);
        if (state.isLoadingRatings) commit("setIsLoadingRatings", false);
      })
      .catch(error => {
        // eslint-disable-next-line
              console.error(error);
      });
  },

  addRating({ commit, rootState }, course, quality, difficulty) {
    commit("addRating", course);

    var url = "users/" + rootState.auth.userId + "/ratings/";
    axios
      .post(url, {
        course_id: course.courseID,
        quality: quality,
        difficulty: difficulty
      })
      .then(() => {
        Toast.showSuccessMessage("Rating added successfully!");
      })
      .catch(error => {
        // revert client side addition
        commit("removeRating", course.courseID);
        Toast.showErrorMessage("Error adding rating.");

        // eslint-disable-next-line
          console.error(error);
      });
  },

  removeRating({ commit, rootState }, course) {
    commit("removeRating", course.courseID);

    var url = "users/" + rootState.auth.userId + "/ratings/" + course.courseID;
    axios
      .delete(url)
      .then(() => {
        Toast.showSuccessMessage("Rating has been removed.");
      })
      .catch(error => {
        // revert client-side removal
        commit("addRating", course);
        Toast.showErrorMessage("Error removing rating.");

        // eslint-disable-next-line
          console.error(error);
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
