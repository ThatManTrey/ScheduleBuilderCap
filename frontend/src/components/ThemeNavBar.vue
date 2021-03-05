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
            <li class="nav-item col-6 col-lg-auto">
              <router-link
                class="nav-link"
                to="Home"
                v-bind:class="{ 'nav-active': isCurrentRoute('Home') }"
              >
                <i class="fas fa-home"></i>Home
              </router-link>
            </li>

            <li v-if="isLoggedIn" class="nav-item col-6 col-lg-auto">
              <router-link
                class="nav-link"
                to="schedule"
                v-bind:class="{ 'nav-active': isCurrentRoute('Schedule') }"
              >
                <i class="far fa-calendar "></i>My Schedule
              </router-link>
            </li>

            <li v-if="isLoggedIn" class="nav-item col-6 col-lg-auto">
              <router-link
                class="nav-link"
                to="favorites"
                v-bind:class="{ 'nav-active': isCurrentRoute('Favorites') }"
              >
                <i class="fas fa-star "></i>Favorites
              </router-link>
            </li>

            <li class="nav-item col-6 col-lg-auto">
              <router-link
                class="nav-link"
                to="about"
                v-bind:class="{ 'nav-active': isCurrentRoute('About') }"
              >
                <i class="fas fa-info-circle "></i>About
              </router-link>
            </li>

            <li v-if="isLoggedIn" class="nav-item col-6 col-lg-auto dropdown">
              <a
                class="nav-link dropdown-toggle "
                href="#"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                More
              </a>

              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <a class="dropdown-item" href="#">Contact Us</a>
                </li>

                <li>
                  <a class="dropdown-item" href="#">Another action</a>
                </li>

                <li>
                  <a class="dropdown-item" href="#">Delete My Account</a>
                </li>
              </ul>
            </li>

            <li class="nav-item col-6 col-lg-auto dropdown">
              <a
                class="nav-link dropdown-toggle "
                href="#"
                id="navbarDropdown"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                dev
              </a>

              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li>
                  <router-link
                    class="dropdown-item"
                    to="theme"
                    v-bind:class="{ 'nav-active': isCurrentRoute('Theme') }"
                  >
                    Theme page</router-link
                  >
                </li>

                <li>
                  <a
                    class="dropdown-item"
                    href="https://getbootstrap.com/docs/5.0/getting-started/introduction/"
                    target="_blank"
                    >Bootstrap doc</a
                  >
                </li>

                <li>
                  <a
                    class="dropdown-item"
                    href="https://uxdesign.cc/dark-mode-ui-design-the-definitive-guide-part-1-color-53dcfaea5129"
                    target="_blank"
                    >Theme ref</a
                  >
                </li>
              </ul>
            </li>
          </ul>

          <div class="d-flex">
            <button
              v-if="isLoggedIn"
              v-on:click="logout"
              type="submit"
              class="btn btn-theme-blacker"
            >
              Logout

              <i class="fas fa-sign-out-alt " style="margin-left: 0.25rem;"></i>
            </button>
            <button
              v-if="!isLoggedIn"
              type="submit"
              class="btn btn-theme-blacker me-3"
              @click="$refs.signInModal.openModal()"
            >
              Sign In
            </button>
            <button
              v-if="!isLoggedIn"
              type="submit"
              class="btn btn-theme-primary"
              @click="$refs.registerModal.openModal()"
            >
              Create An Account
            </button>
          </div>
        </div>
      </div>
    </nav>

    <SignInModal ref="signInModal" @signIn="signIn"></SignInModal>
    <RegisterModal ref="registerModal" @register="register"></RegisterModal>

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
      showScrollToTopButton: false,
      isLoggedIn: false,
      showSignInModal: false,
      test: false
    };
  },

  methods: {
    isCurrentRoute: function(route) {
      return this.currentRouteName == route;
    },

    checkScroll: function() {
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

    signIn() {
      this.isLoggedIn = true;
      this.$emit("isLoggedIn", this.isLoggedIn);
    },

    register() {
      console.log("registered");
    },

    logout: function(event) {
      if (event) {
        this.isLoggedIn = false;
        this.$emit("isLoggedIn", this.isLoggedIn);
      }
    }
  },

  computed: {
    currentRouteName: function() {
      return this.$route.name;
    }
  },

  created() {
    this.$emit("isLoggedIn", this.isLoggedIn);
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
