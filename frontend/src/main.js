import "./assets/style.css";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";
import "@fortawesome/fontawesome-free/css/all.css";
import "vue-toast-notification/dist/theme-default.css";

import Vue from "vue";
import App from "./App.vue";
import VueToast from "vue-toast-notification";
import router from "./router";
import store from "./store/";
import axios from "axios";
import * as Toast from "./toast.js";

Vue.config.productionTip = false;

Vue.use(VueToast, {
  position: "top",
  duration: 10000
});

axios.defaults.baseURL = process.env.VUE_APP_API_URL;
if (process.env.NODE_ENV === "development")
  axios.defaults.headers.common["Api-Key"] = process.env.VUE_APP_API_KEY;

// verify access token on new session
if (localStorage.getItem("userInfo")) {
  store
    .dispatch({
      type: "verifyAccessToken",
      token: localStorage.getItem("userInfo")
    })
    .then(() => {
      if (store.state.authError) Toast.showErrorMessage(store.state.authError);
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
