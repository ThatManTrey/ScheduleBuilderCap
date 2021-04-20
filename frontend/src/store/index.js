import Vue from "vue";
import Vuex from "vuex";
import auth from "./modules/auth";
import courses from "./modules/courses";
import favorites from "./modules/favorites";
import semesters from "./modules/semesters";
import ratings from "./modules/ratings";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
    courses,
    favorites,
    semesters,
    ratings
  }
});
