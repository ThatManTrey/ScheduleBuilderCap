import axios from "axios";
import * as Toast from "../../toast";

const state = () => ({
  favoriteCourses: [],
  isSendingFavorite: false  // disables button until response is received (prevents button spam)
});

const mutations = {
  setFavorites(state, favoriteCourses) {
    state.favoriteCourses = favoriteCourses;
  },

  // these next two mutations need to exist for the favorite icon to change without getting a response first from the server
  // favoriting functionality will operate based on the array of favorite courses from the client side
  // getFavorites will only be dispatched on app load
  // if there's an error from the server after a favorite has been set locally, the favorite will be reset client-side

  addFavorite(state, course) {
    state.favoriteCourses.push(course);
  },

  removeFavorite(state, courseId) {
    const index = state.favoriteCourses.findIndex(course => course.courseID === courseId);
    if (index > -1)
      state.favoriteCourses.splice(index, 1);
  },

  setIsSendingFavorite(state, isSending) {
    state.isSendingFavorite = isSending;
  }
};

const getters = {
  isCourseFavorited: state => courseId => {
    return state.favoriteCourses.some(course => course.courseID === courseId);
  }
};

const actions = {
  getFavoriteCourses({ commit, rootState }) {
    var url = "users/" + rootState.auth.userId + "/favorites";
    axios.get(url)
      .then(res => {
        commit("setFavorites", res.data.favCourses);
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },

  addFavorite({ commit, rootState }, course) {
    commit("setIsSendingFavorite", true);
    commit("addFavorite", course);

    var url = "users/" + rootState.auth.userId + "/favorites/" + course.courseID;
    axios.post(url)
      .then(() => {
        Toast.showSuccessMessage("Favorite added successfully!");
        commit("setIsSendingFavorite", false);
      })
      .catch(error => {
        // revert client side addition
        commit("removeFavorite", course.courseID);
        Toast.showErrorMessage("Error adding favorite.");
        commit("setIsSendingFavorite", false);

        // eslint-disable-next-line
        console.error(error);
      });
  },

  removeFavorite({ commit, rootState }, course) {
    commit("setIsSendingFavorite", true);
    commit("removeFavorite", course.courseID);

    var url = "users/" + rootState.auth.userId + "/favorites/" + course.courseID;
    axios.delete(url)
      .then(() => {
        Toast.showSuccessMessage("Favorite has been removed.");
        commit("setIsSendingFavorite", false);
      })
      .catch(error => {
        // revert client-side removal
        commit("addFavorite", course);
        Toast.showErrorMessage("Error removing favorite.");
        commit("setIsSendingFavorite", false);

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
