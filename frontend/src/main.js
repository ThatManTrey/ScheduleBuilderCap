import "./assets/style.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "@fortawesome/fontawesome-free/css/all.css";
import "vue-toast-notification/dist/theme-default.css";

import Vue from "vue";
import App from "./App.vue";
import VueToast from "vue-toast-notification";
import VueCookies from 'vue-cookies';
import router from "./router";
import store from "./store/";
import axios from "axios";
import * as Toast from './toast.js';
import HttpStatus from 'http-status-codes';

// change this?
Vue.config.productionTip = false;

Vue.use(VueCookies);

Vue.use(VueToast, {
  position: "top",
  duration: 10000
});

axios.defaults.baseURL = process.env.VUE_APP_API_URL;
if (process.env.NODE_ENV === "development")
  axios.defaults.headers.common["Api-Key"] = process.env.VUE_APP_API_KEY;

// allow each request to send and receive cookies
axios.interceptors.request.use(
  function (config) {
    config.withCredentials = true;
    return config;
  },
  function (error) {
    return Promise.reject(error);
  }
);

// access token cookies is HttpOnly so can't check if it exists, have to run on every page refresh
store.dispatch("verifyAccessToken")
  .then(function () {
    if (store.state.authError)
      Toast.showErrorMessage(store.state.authError)
    else
      // needed for validating POST, PUT, DELETE requests
      axios.defaults.headers.common["X-CSRF-TOKEN"] = Vue.$cookies.get('csrf_access_token');
  
    initalizeApp();
  });

axios.interceptors.response.use(function (response) {
  return response;
}, function (error) {
  // redirect to home if access token has been removed by server 
  if (error.response.status == HttpStatus.UNPROCESSABLE_ENTITY) {
    Toast.showErrorMessage("Your session has expired or is invalid. Please login again.");
    store.commit("unAuthenticateUser");
    if(router.currentRoute.name != "Home")
      router.push("/home");
  }

  return Promise.reject(error);
});


function initalizeApp() {
  new Vue({
    router,
    store,
    render: h => h(App)
  }).$mount("#app");
}