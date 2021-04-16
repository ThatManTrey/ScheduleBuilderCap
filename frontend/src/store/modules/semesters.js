import axios from "axios";

const state = () => ({
  // each semester object has
  //    semesterName
  //    semesterId
  //    semesterCourses - array of courses scheduled
  semesters: []
  // is adding semester
  // is loading semesters (set on inital app load)
});

const mutations = {
  setSemesters(state, semesters) {
    state.semesters = semesters;
  }

  // remove semester and add/remove course would also be clientside
  // can't do add semester since adding a new semester would require a new id from the db
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
  getSemesters({ commit, rootState }) {
    var url = "users/" + rootState.auth.userId + "/semesters";
    axios
      .get(url)
      .then(res => {
        commit("setSemesters", res.data.semesters);
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },

  addSemester({ dispatch, rootState }, semesterName) {
    var url = "users/" + rootState.auth.userId + "/semesters";

    return axios
      .post(url, { semester_name: semesterName })
      .then(() => {
        dispatch("getSemesters");
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },

  removeSemester({ rootState }, semesterId) {
    var url = "users/" + rootState.auth.userId + "/semesters/" + semesterId;
    axios
      .delete(url)
      .then(() => {
        //dispatch("getSemesters");
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

  addCourseToSemester({ rootState }, { semesterId, courseId }) {
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
        //dispatch("getSemesters");
      })
      .catch(error => {
        // eslint-disable-next-line
        console.error(error);
      });
  },

  removeCourseFromSemester({ rootState, getters }, courseId) {
    const semesterId = getters.getSemesterIdForCourse(courseId);

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
        //dispatch("getSemesters");
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

function hasCourseWithId(semester, courseId) {
  return semester.semesterCourses.some(course => course.courseID === courseId);
}
