import axios from "axios";

const state = () => ({
  // each semester object has
  //    semesterName
  //    semesterID
  //    array of courses
  semesters: []
});

const mutations = {
  setSemesters(state, semesters) {
    state.semesters = semesters;
  }
};

const getters = {
  searchPrograms: state => courseId => {
    // i think this would work?
    return state.semesters.filter(semester =>
      semester.courses.includes(courseId)
    );
  }
};

const actions = {
  getSemesters({ commit, rootState }) {
    var url = "users/" + rootState.auth.userId + "/semesters";
    axios
      .get(url)
      .then(res => {
        console.log("received semesters: ", res.data.semesters);
        commit("setSemesters", res.data.semesters);
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },

  addSemester({ dispatch, rootState }, semesterName) {
    var url = "users/" + rootState.auth.userId + "/semesters";
    axios
      .post(url, { semester_name: semesterName })
      .then(() => {
        dispatch("getSemesters");
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },

  removeSemester({ dispatch, rootState }, { semesterId }) {
    var url = "users/" + rootState.auth.userId + "/semesters/" + semesterId;
    axios
      .delete(url)
      .then(() => {
        dispatch("getSemesters");
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },

  editSemesterName({ dispatch, rootState }, { semesterId, newName }) {
    var url = "users/" + rootState.auth.userId + "/semesters/" + semesterId;
    axios
      .put(url, { semester_name: newName })
      .then(() => {
        dispatch("getSemesters");
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },

  addCourseToSemester({ dispatch, rootState }, { semesterId, courseId }) {
    var url =
      "users/" +
      rootState.auth.userId +
      "/semesters/" +
      semesterId +
      "/courses/" +
      courseId;
    axios
      .post(url)
      .then(() => {
        dispatch("getSemesters");
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },

  removeCourseFromSemester({ dispatch, rootState }, { semesterId, courseId }) {
    var url =
      "users/" +
      rootState.auth.userId +
      "/semesters/" +
      semesterId +
      "/courses/" +
      courseId;
    axios
      .delete(url)
      .then(() => {
        dispatch("getSemesters");
      })
      .catch(error => {
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
