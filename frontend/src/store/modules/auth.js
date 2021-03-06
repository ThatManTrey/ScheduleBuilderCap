import Vue from "vue";
import axios from "axios";
import StatusCodes from "http-status-codes";
import * as Toast from "../../toast.js";

const defaultError = "An unexpected error has occurred. Please try again.";

const state = () => ({
  isAuthenticated: false,
  userId: null,
  hasConfirmedEmail: null,
  authError: null
});

const mutations = {
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

  confirmEmail(state, hasConfirmedEmail) {
    state.hasConfirmedEmail = hasConfirmedEmail;
  }
};

const actions = {
  logIn({ commit, dispatch }, { email, password }) {
    return axios
      .post("/auth/login", {
        email: email,
        password: password
      })
      .then(function(response) {
        commit({
          type: "authenticateUser",
          userId: response.data.userId,
          hasConfirmedEmail: response.data.hasConfirmedEmail
        });

        dispatch("favorites/getFavoriteCourses", null, { root: true });
        dispatch("semesters/getSemesters", null, { root: true });
        dispatch("ratings/getUserRatedCourses", null, { root: true });

        axios.defaults.headers.common["X-CSRF-TOKEN"] = Vue.$cookies.get(
          "csrf_access_token"
        );

        if (!response.data.hasConfirmedEmail) {
          setTimeout(() => {
            Vue.$toast.open({
              message:
                "You have not confirmed your account yet. Click here to send another email.",
              type: "success",
              duration: 10000,
              onClick: resendConfirmationEmail
            });
          }, 3000);
        }
      })
      .catch(function(error) {
        if (!error.response) commit("setAuthError");
        else if (error.response.status == StatusCodes.BAD_REQUEST)
          commit("setAuthError", "Incorrect username or password.");
        else commit("setAuthError");
      });
  },

  register({ commit }, { email, password }) {
    return axios
      .post("/auth/register", {
        email: email,
        password: password
      })
      .then(function() {
        commit("setAuthError", null);
      })
      .catch(function(error) {
        if (!error.response) commit("setAuthError");
        else if (error.response.status === StatusCodes.BAD_REQUEST)
          commit("setAuthError", "That email address is not available.");
        else commit("setAuthError");
      });
  },

  // verify token on new session
  verifyAccessToken({ commit, dispatch }) {
    return axios
      .get("/auth/verify/access")
      .then(function(response) {
        commit({
          type: "authenticateUser",
          userId: response.data.userId,
          hasConfirmedEmail: response.data.hasConfirmedEmail
        });

        dispatch("favorites/getFavoriteCourses", null, { root: true });
        dispatch("semesters/getSemesters", null, { root: true });
        dispatch("ratings/getUserRatedCourses", null, { root: true });
      })
      .catch(function(error) {
        if (!error.response) commit("setAuthError");
      });
  },

  logOut({ commit }) {
    commit("unAuthenticateUser");

    return axios.post("/auth/logout").catch(function() {
      commit("setAuthError");
    });
  }
};

function resendConfirmationEmail() {
  axios
    .post("/auth/resend-confirm")
    .then(function() {
      Toast.showSuccessMessage("Confirmation email has been sent!", 10000);
    })
    .catch(function() {
      Toast.showErrorMessage(
        "Error sending confirmation email. Please try again.",
        10000
      );
    });
}

export default {
  namespaced: true,
  state,
  actions,
  mutations
};
