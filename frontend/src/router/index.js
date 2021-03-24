import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Favorites from "../views/Favorites.vue";
import Schedule from "../views/Schedule.vue";
import Theme from "../views/Theme.vue";
import ResetPass from "../views/ResetPass.vue";
import * as Toast from "../toast.js";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    redirect: "/home"
  },
  {
    path: "/home",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    component: About
  },
  {
    path: "/schedule",
    name: "Schedule",
    component: Schedule,
    beforeEnter: (to, from, next) => {
      if (!localStorage.userInfo) {
        next("/home");
        Toast.showErrorMessage(
          "You'll need to login before you can view that page."
        );
      } else next();
    }
  },
  {
    path: "/favorites",
    name: "Favorites",
    component: Favorites,
    beforeEnter: (to, from, next) => {
      if (!localStorage.userInfo) {
        next("/home");
        Toast.showErrorMessage(
          "You'll need to login before you can view that page."
        );
      } else next();
    }
  },
  {
    path: "/reset",
    name: "Reset",
    component: ResetPass
  },
  {
    path: "/theme",
    name: "Theme",
    component: Theme
  }
];

const router = new VueRouter({
  routes
});

export default router;
