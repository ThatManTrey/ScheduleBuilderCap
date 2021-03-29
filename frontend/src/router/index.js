import Vue from "vue";
import VueRouter from "vue-router";

import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Favorites from "../views/Favorites.vue";
import Schedule from "../views/Schedule.vue";
import Theme from "../views/Theme.vue";
import ResetPass from "../views/ResetPass.vue";

import VerifyAuth from './verifyAuth.js';
import VerifyResetToken from './verifyResetToken.js';
import verifyConfirmToken from './verifyConfirmToken.js';

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
    beforeEnter: VerifyAuth
  },
  {
    path: "/favorites",
    name: "Favorites",
    component: Favorites,
    beforeEnter: VerifyAuth
  },
  {
    path: "/reset",
    name: "Reset",
    component: ResetPass,
    beforeEnter: VerifyResetToken
  },
  {
    path: "/confirm",
    name: "Confirm",
    beforeEnter: verifyConfirmToken
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
