import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import StatusCodes from 'http-status-codes';
import * as Toast from '../toast.js';

Vue.use(Vuex);

const defaultError = "An unexpected error has occurred. Please try again.";

export default new Vuex.Store({
  state: {
    isAuthenticated: false,
    userId: null,
    hasConfirmedEmail: null,
    authError: null
  },

  mutations: {
    authenticateUser(state, { userId, hasConfirmedEmail }) {
      state.isAuthenticated = true;
      state.userId = userId;
      state.authError = null;
      state.hasConfirmedEmail = hasConfirmedEmail;
    },

    unAuthenticateUser(state) {
      state.isAuthenticated = false;
      state.userId = null;
      state.authError = null;
      state.hasConfirmedEmail = null;
    },

    setAuthError(state, message = defaultError) {
      state.authError = message;
    },
  },

  actions: {
    logIn({ commit }, { email, password }) {
      return axios
        .post("/auth/login", {
          email: email,
          password: password
        })
        .then(function (response) {
          commit({
            type: "authenticateUser",
            userId: response.data.userId,
            hasConfirmedEmail: response.data.hasConfirmedEmail
          });

          if (!response.data.hasConfirmedEmail) {
            setTimeout(() => {
              Toast.showWarningMessage("You have not confirmed your email.");
            }, 3000);
          }
        })
        .catch(function (error) {
          console.log("error in login: ", error)
          if (!error.response)
            commit("setAuthError");
          else if (error.response.status == StatusCodes.BAD_REQUEST)
            commit("setAuthError", "Incorrect username or password.");
          else
            commit("setAuthError");
        });
    },

    // verify existing token from "userInfo" localStorage
    verifyAccessToken({ commit }) {
      return axios.get("/auth/verify/access")
        .then(function (response) {
          commit({
            type: "authenticateUser",
            userId: response.data.userId,
            hasConfirmedEmail: response.data.hasConfirmedEmail
          });
        })
        .catch(function (error) {
          console.log("error in verifyAccessToken: ", error)
          if (!error.response)
            commit("setAuthError");
          else if (error.response.status === StatusCodes.UNPROCESSABLE_ENTITY)
            commit(
              "setAuthError",
              "Your session has expired or is invalid. Please login again."
            );
        });
    },

    logOut({ commit }) {
      commit("unAuthenticateUser");

      return axios.post("/auth/logout")
        .catch(function () {
          commit("setAuthError");
          Toast.showErrorMessage(this.state.authError);
        });
    }
  }
});