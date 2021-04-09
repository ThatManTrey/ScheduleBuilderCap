import axios from "axios";
import * as Toast from "../../toast";

const state = () => ({
  // array of courses that have been favorited
  favoriteCourses: []
});

const mutations = {
  setFavorites(state, favoriteCourses) {
    state.favoriteCourses = favoriteCourses;
  }
};

const getters = {
  isCourseFavorited: state => courseId => {
    // replace with favorites.has(courseId) if Map is implemented
    return state.favoriteCourses.some(course => course.courseID === courseId);
  }
};

const actions = {
  getFavoriteCourses({ commit, rootState }) {
    var url = "users/" + rootState.auth.userId + "/favorites";
    axios
      .get(url)
      .then(res => {
        commit("setFavorites", res.data.favCourses);
      })
      .catch(error => {
        // eslint-disable-next-line
                console.error(error);
      });
  },

  addFavorite({ dispatch, rootState }, courseId) {
    var url = "users/" + rootState.auth.userId + "/favorites/" + courseId;
    axios.post(url)
      .then(() => {
        dispatch("getFavoriteCourses");
        Toast.showSuccessMessage("Favorite added successfully!");
      })
      .catch(error => {
        // eslint-disable-next-line
                console.error(error);
        Toast.showErrorMessage("Error adding favorite.");
      });
  },

  removeFavorite({ dispatch, rootState }, courseId) {
    var url = "users/" + rootState.auth.userId + "/favorites/" + courseId;
    axios.delete(url)
      .then(() => {
        dispatch("getFavoriteCourses");
        Toast.showSuccessMessage("Favorite has been removed.");
      })
      .catch(error => {
        // eslint-disable-next-line
                console.error(error);
        Toast.showErrorMessage("Error removing favorite.");
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
