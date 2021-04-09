import axios from "axios";
import enums from "../../enums";

// const resultsPerPage =

const state = () => ({
  allCourses: [],
  currentCourse: {
    type: Object
  },
  isLoadingCourses: true,
  allPrograms: [],
  viewOption: enums.ViewOptions.normalCard,
  searchRequest: {
    programs: [],
    sortOption: {
      type: enums.SortTypes.courseId,
      isAscending: true
    },
    keyword: ""
  },
  currentPage: 1,
  totalPages: 5,
  totalResults: 100
});

const mutations = {
  setAllCourses(state, allCourses) {
    state.allCourses = allCourses;
    state.isLoadingCourses = false;
  },

  setCurrentCourse(state, course) {
    state.currentCourse = course;
  },

  setAllPrograms(state, allPrograms) {
    state.allPrograms = allPrograms;
  },

  setIsLoadingCourses(state, isLoading) {
    state.isLoadingCourses = isLoading;
  },

  addProgram(state, program) {
    // if program has not already been added
    if (state.searchRequest.programs.indexOf(program) === -1) {
      state.searchRequest.programs.push(program);
      updateLocalStoragePrograms(state.searchRequest.programs);
    }
  },

  removeProgram(state, program) {
    const index = state.searchRequest.programs.indexOf(program);
    if (index > -1) {
      state.searchRequest.programs.splice(index, 1);
      updateLocalStoragePrograms(state.searchRequest.programs);
    }
  },

  setSearchPrograms(state, programs) {
    state.searchRequest.programs = programs;
  },

  setSearchKeyword(state, keyword) {
    state.searchRequest.keyword = keyword;
  },

  setSortType(state, sortType) {
    if (state.searchRequest.sortOption.type === sortType)
      state.searchRequest.sortOption.isAscending = !state.searchRequest
        .sortOption.isAscending;
    else state.searchRequest.sortOption.type = sortType;

    updateLocalStorageSortOption(state.searchRequest.sortOption);
  },

  setSortOption(state, { sortType, isAscending = true }) {
    state.searchRequest.sortOption = {
      type: sortType,
      isAscending: isAscending
    };
  },

  setViewOption(state, viewOption) {
    state.viewOption = viewOption;
    updateLocalStorageViewOption(viewOption);
  },

  setPagination(state, newPage) {
    state.currentPage = newPage;
    console.log("current page: ", newPage);
  }
};

const getters = {
  showSmallCard: state => {
    return state.viewOption === enums.ViewOptions.smallCard;
  },

  showCard: state => {
    return (
      state.viewOption === enums.ViewOptions.normalCard ||
      state.viewOption === enums.ViewOptions.smallCard
    );
  },

  searchPrograms: state => keyword => {
    if (keyword.length === 0) return state.allPrograms;

    return state.allPrograms.filter(program =>
      `${program.degreeName.toLowerCase()} ${program.degreeType.toLowerCase()}`.includes(
        keyword.toLowerCase()
      )
    );
  }
};

const actions = {
  // change this to take pagination object once it's implemented
  getCourses({ commit }) {
    commit("setIsLoadingCourses", true);
    axios
      .get("courses/cs")
      .then(res => {
        // check if the result's page is the same as current page before commit
        commit("setAllCourses", res.data.deptCourses);
      })
      .catch(error => {
        // eslint-disable-next-line
                console.error(error);
      });
  },

  updatePagination({ commit, dispatch }, newPage) {
    commit("setPagination", newPage);
    dispatch("getCourses");
  },

  getPrograms({ commit }) {
    return axios.get("/degrees/all").then(res => {
      commit("setAllPrograms", res.data.degrees);
    });
  },

  getOptionsFromLocalStorage({ dispatch }) {
    var viewOption = parseInt(localStorage.getItem("viewOption"));
    var sortType = parseInt(localStorage.getItem("sortType"));
    var isAscending = localStorage.getItem("isAscending") === "true";
    var programs = JSON.parse(localStorage.getItem("programs"));

    dispatch("setOptionsFromLocalStorage", {
      viewOption,
      sortType,
      isAscending,
      programs
    });
  },

  setOptionsFromLocalStorage(
    { commit },
    { viewOption, sortType, isAscending, programs }
  ) {
    if (isValidViewOption(viewOption)) commit("setViewOption", viewOption);

    if (isValidSortType(sortType))
      commit("setSortOption", { sortType, isAscending });

    if (programs !== null && programs.length > 0)
      commit("setSearchPrograms", programs);

    //otherwise use default values defined in state
  }
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
};

function updateLocalStorageViewOption(viewOption) {
  localStorage.setItem("viewOption", viewOption);
}

function updateLocalStorageSortOption(sortOption) {
  localStorage.setItem("sortType", sortOption.type);
  localStorage.setItem("isAscending", sortOption.isAscending);
}

function updateLocalStoragePrograms(programs) {
  localStorage.setItem("programs", JSON.stringify(programs));
}

function isValidSortType(sortType) {
  return (
    sortType === enums.SortTypes.courseId ||
    sortType === enums.SortTypes.program ||
    sortType === enums.SortTypes.credits
  );
}

function isValidViewOption(viewOption) {
  return (
    viewOption === enums.ViewOptions.normalCard ||
    viewOption === enums.ViewOptions.smallCard ||
    viewOption === enums.ViewOptions.table
  );
}
