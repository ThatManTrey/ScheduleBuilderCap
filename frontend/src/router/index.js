import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Favorites from "../views/Favorites.vue";
import Schedule from "../views/Schedule.vue";
import Theme from "../views/Theme.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import Ping from "../views/Ping.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
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
    component: Schedule
  },
  {
    path: "/favorites",
    name: "Favorites",
    component: Favorites
  },
  {
    path: "/theme",
    name: "Theme",
    component: Theme
  },
  {
    path: "/login",
    name: "Login",
    component: Login
  },
  {
    path: "/register",
    name: "Register",
    component: Register
  },
  {
    path: "/ping",
    name: "Ping",
    component: Ping
  }
];

const router = new VueRouter({
  routes
});

export default router;
