import axios from "axios";
import * as Toast from "../../toast";

const state = () => ({
  // each semester object has
  //    semesterName
  //    semesterId
  //    semesterCourses - array of courses scheduled
  semesters: [],
  isLoadingSemesters: true
});

const mutations = {
  setSemesters(state, semesters) {
    state.semesters = semesters;
  },

  setIsLoadingSemesters(state, isLoading) {
    state.isLoadingSemesters = isLoading;
  },

  removeSemester(state, semesterId) {
    const index = state.semesters.findIndex(
      semester => semester.semesterId === semesterId
    );

    if (index > -1) state.semesters.splice(index, 1);
  },

  removeCourse(state, { semesterId, courseId }) {
    const semesterIndex = state.semesters.findIndex(
      semester => semester.semesterId === semesterId
    );

    const courseIndex = state.semesters[
      semesterIndex
    ].semesterCourses.findIndex(course => course.courseID === courseId);

    if (semesterIndex > -1 && courseIndex > -1)
      state.semesters[semesterIndex].semesterCourses.splice(courseIndex, 1);
  }
};

const getters = {
  isCourseScheduled: state => courseId => {
    let courseFound = false;

    state.semesters.forEach(semester => {
      if (hasCourseWithId(semester, courseId)) {
        courseFound = true;
        return;
      }
    });

    return courseFound;
  },

  getSemesterIdForCourse: state => courseId => {
    let semesterId = null;

    state.semesters.forEach(semester => {
      if (hasCourseWithId(semester, courseId)) {
        semesterId = semester.semesterId;
        return;
      }
    });

    return semesterId;
  }
};

const actions = {
  getSemesters({ commit, rootState, state }) {
    var url = "users/" + rootState.auth.userId + "/semesters";
    axios
      .get(url)
      .then(res => {
        commit("setSemesters", res.data.semesters);

        if (state.isLoadingSemesters) commit("setIsLoadingSemesters", false);
      })
      .catch(() => {
        if (state.isLoadingSemesters) commit("setIsLoadingSemesters", false);
      });
  },

  addSemester({ dispatch, rootState }, semesterName) {
    var url = "users/" + rootState.auth.userId + "/semesters";

    return axios.post(url, { semester_name: semesterName }).then(() => {
      dispatch("getSemesters");
    });
  },

  removeSemester({ rootState, dispatch, commit }, semesterId) {
    commit("removeSemester", semesterId);

    var url = "users/" + rootState.auth.userId + "/semesters/" + semesterId;
    axios
      .delete(url)
      .then(() => {
        Toast.showSuccessMessage("Semester removed successfully.");
      })
      .catch(() => {
        Toast.showErrorMessage(
          "An error occurred while trying to remove a semester.",
          10000
        );
        dispatch("getSemesters");
      });
  },

  editSemesterName({ dispatch, rootState }, { semesterId, newName }) {
    var url = "users/" + rootState.auth.userId + "/semesters/" + semesterId;
    axios.put(url, { semester_name: newName }).then(() => {
      dispatch("getSemesters");
    });
  },

  addCourseToSemester({ rootState, dispatch }, { semesterId, courseId }) {
    var url =
      "users/" +
      rootState.auth.userId +
      "/semesters/" +
      semesterId +
      "/courses/" +
      courseId;

    axios.post(url).then(() => {
      dispatch("getSemesters");
    });
  },

  removeCourseFromSemester({ rootState, getters, dispatch, commit }, courseId) {
    const semesterId = getters.getSemesterIdForCourse(courseId);
    commit("removeCourse", { semesterId: semesterId, courseId: courseId });

    var url =
      "users/" +
      rootState.auth.userId +
      "/semesters/" +
      semesterId +
      "/courses/" +
      courseId;

    axios.delete(url).catch(() => {
      Toast.showErrorMessage(
        "An error occurred while trying to delete a course.",
        10000
      );
      dispatch("getSemesters");
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

function hasCourseWithId(semester, courseId) {
  return semester.semesterCourses.some(course => course.courseID === courseId);
}
