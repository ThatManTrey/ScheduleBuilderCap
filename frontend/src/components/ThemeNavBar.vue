<template lang="html">
  <header>
    <nav class="navbar navbar-expand-md" id="app-nav">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="Home">
          KSU COURSE PLANNER
        </router-link>
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
          <ul class="navbar-nav flex-row flex-wrap me-auto mb-3 mb-md-0">
            <li class="nav-item col-6 col-md-auto">
              <router-link
                class="nav-link"
                to="Home"
                v-bind:class="{ 'nav-active': isCurrentRoute('Home') }"
              >
                <i class="fas fa-home"></i>Home
              </router-link>
            </li>

            <li v-if="isLoggedIn" class="nav-item col-6 col-md-auto">
              <router-link
                class="nav-link"
                to="schedule"
                v-bind:class="{ 'nav-active': isCurrentRoute('Schedule') }"
              >
                <i class="far fa-calendar "></i>Schedule
              </router-link>
            </li>

            <li v-if="isLoggedIn" class="nav-item col-6 col-md-auto">
              <router-link
                class="nav-link"
                to="favorites"
                v-bind:class="{ 'nav-active': isCurrentRoute('Favorites') }"
              >
                <i class="fas fa-bookmark "></i>Favorites
              </router-link>
            </li>

            <li class="nav-item col-6 col-md-auto">
              <router-link
                class="nav-link"
                to="about"
                v-bind:class="{ 'nav-active': isCurrentRoute('About') }"
              >
                <i class="fas fa-info-circle "></i>About
              </router-link>
            </li>
          </ul>

          <div class="d-flex">
            <button
              v-on:click="logout()"
              type="button"
              class="btn btn-theme-blacker"
              v-if="isLoggedIn"
            >
              Logout

              <i class="fas fa-sign-out-alt ms-1"></i>
            </button>
            <button
              type="button"
              class="btn btn-theme-blacker me-3"
              @click="$refs.signInModal.openModal()"
              v-if="!isLoggedIn"
            >
              Sign In
            </button>
            <button
              type="button"
              class="btn btn-theme-primary-dark"
              @click="$refs.registerModal.openModal()"
              v-if="!isLoggedIn"
            >
              Create An Account
            </button>
          </div>
        </div>
      </div>
    </nav>

    <SignInModal ref="signInModal"></SignInModal>
    <RegisterModal ref="registerModal"></RegisterModal>

    <transition name="fade-short">
      <div v-if="showScrollToTopButton" id="scroll-to-top">
        <a class="align-middle" @click="scrollToTop">
          <i class="fas fa-chevron-up fa-lg"></i>
        </a>
      </div>
    </transition>
  </header>
</template>

<script>
import SignInModal from "./modals/SignInModal.vue";
import RegisterModal from "./modals/RegisterModal.vue";
import { mapState } from "vuex";

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
      return this.$route.name === route;
    },

    checkScroll() {
      // shows scroll to top button past a certain number of px from the top
      if (
        document.body.scrollTop > this.SHOW_SCROLL_TOP_AFTER_PX ||
        document.documentElement.scrollTop > this.SHOW_SCROLL_TOP_AFTER_PX
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
      this.$store.dispatch("auth/logOut");
      if (!this.isCurrentRoute("Home")) this.$router.push("/home");
    }
  },

  computed: mapState({
    isLoggedIn: state => state.auth.isAuthenticated
  }),

  created() {
    this.SHOW_SCROLL_TOP_AFTER_PX = 200;

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
  z-index: 1;
  background-image: linear-gradient(
    180deg,
    rgba(255, 255, 255, 0.1),
    rgba(255, 255, 255, 0)
  );
  background-color: #000;
}

.nav-link {
  color: var(--theme-white);

  &:hover {
    color: var(--theme-whitest);
  }

  i {
    margin-right: 0.25rem;
    color: var(--theme-light-gray);
  }
}

.nav-active,
.nav-active i {
  color: var(--theme-whitest);
}

.navbar-brand {
  color: var(--theme-whiter);
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
  background-color: var(--theme-darkest-gray);

  &:hover {
    background-color: var(--theme-primary-dark);
  }
}

#scroll-to-top a i {
  position: relative;
  top: 7px;
  color: var(--theme-whitest);
}

</style>
