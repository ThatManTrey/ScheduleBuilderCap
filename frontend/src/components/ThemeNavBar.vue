<template lang="html">
  <div>
    <nav class="navbar navbar-expand-lg" id="app-nav">
      <div class="container-fluid">
        <!-- Put logo here -->

        <a class="navbar-brand" href="#">KSU COURSE PLANNER</a>

        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <i class="fas fa-bars"></i>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav flex-row flex-wrap me-auto mb-3 mb-lg-0">
            <li class="nav-item col-6 col-md-4 col-lg-auto">
              <router-link
                class="nav-link"
                to="Home"
                v-bind:class="{ 'nav-active': isCurrentRoute('Home') }"
              >
                <i class="fas fa-home"></i>Home
              </router-link>
            </li>

            <li hidden class="nav-item col-6 col-md-4 col-lg-auto">
              <router-link
                class="nav-link"
                to="schedule"
                v-bind:class="{ 'nav-active': isCurrentRoute('Schedule') }"
              >
                <i class="far fa-calendar "></i>My Schedule
              </router-link>
            </li>

            <li hidden class="nav-item col-6 col-md-4 col-lg-auto">
              <router-link
                class="nav-link"
                to="favorites"
                v-bind:class="{ 'nav-active': isCurrentRoute('Favorites') }"
              >
                <i class="fas fa-star "></i>Favorites
              </router-link>
            </li>

            <li class="nav-item col-6 col-md-4 col-lg-auto">
              <router-link
                class="nav-link"
                to="about"
                v-bind:class="{ 'nav-active': isCurrentRoute('About') }"
              >
                <i class="fas fa-info-circle "></i>About
              </router-link>
            </li>

            <li class="nav-item col-6 col-md-4 col-lg-auto">
              <router-link
                class="nav-link"
                to="theme"
                v-bind:class="{ 'nav-active': isCurrentRoute('Theme') }"
              >
                <i class="fas fa-question-circle"></i>Theme ref</router-link
              >
            </li>
          </ul>

          <div class="d-flex">
            <button
              hidden
              v-on:click="logout"
              type="submit"
              class="btn btn-theme-blacker"
            >
              Logout

              <i class="fas fa-sign-out-alt ms-1"></i>
            </button>
            <button
              type="submit"
              class="btn btn-theme-blacker me-3"
              @click="$refs.signInModal.openModal()"
            >
              Sign In
            </button>
            <button
              type="submit"
              class="btn btn-theme-primary-dark"
              @click="$refs.registerModal.openModal()"
            >
              Create An Account
            </button>
          </div>
        </div>
      </div>
    </nav>

    <SignInModal ref="signInModal"></SignInModal>
    <RegisterModal ref="registerModal"></RegisterModal>

    <transition name="fade">
      <div v-if="showScrollToTopButton" id="scroll-to-top">
        <a class="align-middle" @click="scrollToTop">
          <i class="fas fa-chevron-up fa-lg"></i>
        </a>
      </div>
    </transition>
  </div>
</template>

<script>
import * as Constants from "@/const.js";
import SignInModal from "./modals/SignInModal.vue";
import RegisterModal from "./modals/RegisterModal.vue";

export default {
  name: "theme-nav-bar",
  props: {
    useScrollToTopButton: {
      type: Boolean,
      default: true
    }
  },

  components: {
    SignInModal,
    RegisterModal
  },

  data() {
    return {
      showScrollToTopButton: false
    };
  },

  methods: {
    isCurrentRoute(route) {
      return this.currentRouteName == route;
    },

    checkScroll() {
      // shows scroll to top button past a certain number of px from the top
      if (
        document.body.scrollTop > Constants.SHOW_SCROLL_TOP_AFTER_PX ||
        document.documentElement.scrollTop > Constants.SHOW_SCROLL_TOP_AFTER_PX
      ) {
        this.showScrollToTopButton = true;
      } else {
        this.showScrollToTopButton = false;
      }
    },
    scrollToTop() {
      window.scroll(0, 0);
    },

    logout() {
      // remove token in localStorage
    }
  },

  computed: {
    currentRouteName() {
      return this.$route.name;
    }
  },

  created() {
    if (this.useScrollToTopButton) {
      window.addEventListener("scroll", this.checkScroll);
    }
  },

  destroyed() {
    if (this.useScrollToTopButton) {
      window.removeEventListener("scroll", this.checkScroll);
    }
  }
};
</script>

<style lang="scss" scoped>
/* navbar */

#app-nav {
  font-family: "Source Sans Pro", sans-serif;
  z-index: 1;
  background-image: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.1),
    rgba(255, 255, 255, 0)
  );
  background-color: #070707;
}

.nav-link i {
  margin-right: 0.25rem;
}

i.fa-star {
  color: var(--theme-whitest);
}

.nav-link {
  color: var(--theme-white);
}

.nav-link:hover {
  color: var(--theme-whitest);
}

a.navbar-brand {
  color: var(--theme-whiter);
}

a.nav-active {
  color: #d29241;
}

a.nav-active:hover {
  color: #d29241;
}

.navbar-toggler i {
  font-size: 1.75rem;
  color: var(--theme-light-gray);
}

/* scroll to top button */

#scroll-to-top {
  $radius: 2.5rem;
  $bottomRightOffset: 1.5rem;
  height: $radius;
  width: $radius;
  bottom: $bottomRightOffset;
  right: $bottomRightOffset;
  position: fixed;
  z-index: 99;
}

#scroll-to-top a {
  display: block;
  height: 100%;
  width: 100%;
  text-align: center;
  border-radius: 50%;
  background-color: #3f256d;
}

#scroll-to-top a i {
  position: relative;
  top: 7px;
  color: var(--theme-whiter);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
