import axios from 'axios';
import * as Toast from '../../toast';

const state = () => ({
    // array of favorite objects, container favId and course object
    // could also make this a map where courseId is the key and favorite object is value 
    favorites: []
});

const mutations = {
    setFavorites(state, favorites) {
        state.favorites = favorites;
    }
};

const getters = {
    isFavorited: state => courseId => {
        // replace with favorites.has(courseId) if Map is implemented
        return state.favorites.filter(favorite => favorite.course.courseID === courseId);
    }
};

const actions = {
    getFavoriteCourses({ commit, rootState }) {
        var url = "users/" + rootState.auth.userId + "/favorites";
        axios.get(url)
            .then(res => {
                commit("setFavorites", res.data.favorites);
            })
            .catch(error => {
                // eslint-disable-next-line
                console.error(error);
            });
    },

    addFavorite({ dispatch, rootState }, courseId) {
        var url = "users/" + rootState.auth.userId + "/favorites/add";
        axios.post(url, { courseId: courseId })
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
        var url = "users/" + rootState.auth.userId + "/favorites/remove";
        axios.delete(url, { courseId: courseId })
            .then(() => {
                dispatch("getFavoriteCourses");
                Toast.showSuccessMessage("Favorite added successfully!");
            })
            .catch(error => {
                // eslint-disable-next-line
                console.error(error);
                Toast.showErrorMessage("Error removing favorite.");
            });
    },
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};

