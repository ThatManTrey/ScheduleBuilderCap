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

Vue.config.productionTip = false;

Vue.use(VueToast, {
  position: "top",
  duration: 10000
});

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
