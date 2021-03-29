import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import StatusCodes from "http-status-codes";
import jwt_decode from "jwt-decode";

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
    authenticateUser(state, userId) {
      state.isAuthenticated = true;
      state.userId = userId;
      state.hasConfirmedEmail = true;
      state.authError = null;
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

    setUnconfirmedEmail(state) {
      state.hasConfirmedEmail = false;
    }
  },
  actions: {
    // get new accessToken if credentials are valid
    logIn({ commit }, { email, password }) {
      return axios
        .post("/auth/login", {
          email: email,
          password: password
        })
        .then(
          response => {
            var token = response.data.accessToken;

            localStorage.setItem("userInfo", token);
            axios.defaults.headers.common["Authorization"] = "Bearer " + token;

            commit("authenticateUser", getUserIdFromToken(token));
          },
          error => {
            // server timeout
            if (!error.response) {
              commit("setAuthError");
              return;
            }

            switch (error.response.status) {
              case StatusCodes.UNAUTHORIZED:
                commit(
                  "setAuthError",
                  "Your session has expired or is invalid. Please login again."
                );
                break;

              case StatusCodes.BAD_REQUEST:
                commit("setAuthError", "Incorrect username or password.");
                break;

              case StatusCodes.FORBIDDEN:
                commit("setUnconfirmedEmail");
                commit(
                  "setAuthError",
                  "Please confirm your email before logging in."
                );
                break;

              default:
                commit("setAuthError");
            }
          }
        );
    },

    // verify existing token from "userInfo" localStorage
    verifyAccessToken({ commit }, { token }) {
      return axios
        .get("/auth/verify/access", {
          headers: { Authorization: "Bearer " + token }
        })
        .then(
          () => {
            axios.defaults.headers.common["Authorization"] = "Bearer " + token;
            commit("authenticateUser", getUserIdFromToken(token));
          },
          error => {
            // server timeout
            if (!error.response) commit("setAuthError");
            else if (
              error.response.status == StatusCodes.UNAUTHORIZED ||
              error.response.status == StatusCodes.UNPROCESSABLE_ENTITY
            )
              commit(
                "setAuthError",
                "Your session has expired or is invalid. Please login again."
              );
            else commit("setAuthError");

            localStorage.removeItem("userInfo");
          }
        );
    },

    logOut({ commit }) {
      localStorage.removeItem("userInfo");
      delete axios.defaults.headers.common["Authorization"];

      commit("unAuthenticateUser");
    }
  }
});

function getUserIdFromToken(token) {
  var decodedToken = jwt_decode(token);
  return decodedToken.sub;
}
