import "./assets/style.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "@fortawesome/fontawesome-free/css/all.css";
import "vue-toast-notification/dist/theme-default.css";

import Vue from "vue";
import App from "./App.vue";
import VueToast from "vue-toast-notification";
import VueCookies from "vue-cookies";
import router from "./router";
import store from "./store/";
import axios from "axios";
import * as Toast from "./toast.js";
import HttpStatus from "http-status-codes";
import enums from "./enums.js";

Vue.config.productionTip = false;

Vue.use(VueCookies);

Vue.use(VueToast, {
  position: "top",
  duration: 10000
});

Vue.prototype.$enums = enums;

axios.defaults.baseURL = process.env.VUE_APP_API_URL;
if (process.env.NODE_ENV === "production")
  axios.defaults.headers.common["Api-Key"] = process.env.VUE_APP_API_KEY;

// allow each request to send and receive cookies
axios.interceptors.request.use(
  function(config) {
    config.withCredentials = true;
    return config;
  },
  function(error) {
    return Promise.reject(error);
  }
);

axios.interceptors.response.use(
  function(response) {
    return response;
  },
  function(error) {
    if (error.response.status === HttpStatus.UNAUTHORIZED) {
      Toast.showErrorMessage("Your session has expired. Please login again.");
      store.commit("auth/unAuthenticateUser");
      if (router.currentRoute.name != "Home") router.push("/home");
    } else if (error.response.status === 470) {
      // access token has been refreshed, update CSRF header and retry request
      // set new CSRF token for last request and all future requests
      var newCsrfToken = Vue.$cookies.get("csrf_access_token");
      error.config.headers["X-CSRF-TOKEN"] = newCsrfToken;
      axios.defaults.headers.common["X-CSRF-TOKEN"] = newCsrfToken;

      // retry last request
      return axios.request(error.config);
    }
    return Promise.reject(error);
  }
);

store.dispatch("courses/getOptionsFromLocalStorage");

// csrf token cookie isn't httponly, access token is
if (Vue.$cookies.get("csrf_access_token")) {
  store.dispatch("auth/verifyAccessToken").then(function() {
    if (store.state.auth.authError) console.log(store.state.auth.authError);
    // needed for validating POST, PUT, DELETE requests
    else
      axios.defaults.headers.common["X-CSRF-TOKEN"] = Vue.$cookies.get(
        "csrf_access_token"
      );

    initalizeApp();
  });
} else {
  initalizeApp();
}

function initalizeApp() {
  new Vue({
    router,
    store,
    render: h => h(App)
  }).$mount("#app");
}
