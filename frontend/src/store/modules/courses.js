import axios from "axios";
import enums from '../../enums';

// const resultsPerPage =

const state = () => ({
    allCourses: [],
    isLoadingCourses: true,
    viewOption: enums.ViewOptions.normalCard,
    searchRequest: {
        programs: [],
        sortOption: {
            type: enums.SortTypes.courseId,
            isAscending: true
        },
        keyword: ""
    }
});

const mutations = {
    setAllCourses(state, allCourses){
        state.allCourses = allCourses;
        state.isLoadingCourses = false;
    },

    setIsLoadingCourses(state, isLoading){
        state.isLoadingCourses = isLoading;
    },

    addProgram(state, program) {
        // if program has not already been added
        if(state.searchRequest.programs.indexOf(program) === -1) 
            state.searchRequest.programs.push(program);
        
        console.log("added program: ", state.searchRequest.programs);
    },

    removeProgram(state, program) {
        var index = state.searchRequest.programs.indexOf(program);
        if (index > -1)
            state.searchRequest.programs.splice(index, 1)

        console.log("removed program: ", state.searchRequest.programs);
    },

    setSearchKeyword(state, keyword) {
        state.searchRequest.keyword = keyword;
    },

    setSortType(state, sortType) {
        if(state.searchRequest.sortOption.type === sortType)
          state.searchRequest.sortOption.isAscending = !state.searchRequest.sortOption.isAscending;
        else
          state.searchRequest.sortOption.type = sortType;
    },

    setViewOption(state, viewOption) {
        state.viewOption = viewOption;
    }
};

const getters = {
    showSmallCard: state => {
        return state.viewOption === enums.ViewOptions.smallCard;
    },
    showCard: state => {
        return state.viewOption === enums.ViewOptions.normalCard || state.viewOption === enums.ViewOptions.smallCard;
    }
};

const actions = {
    // change this to take pagination object once it's implemented
    getCourses({ commit }) {
        commit('setIsLoadingCourses', true);
        axios.get("courses/cs")
            .then((res) => {
                commit('setAllCourses', res.data.deptCourses);
            })
            .catch((error) => {
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
}