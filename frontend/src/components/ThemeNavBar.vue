<template lang="html">
  <nav class="navbar navbar-expand-lg bg-theme-blackest" id="app-nav">
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

        <!-- <span class="navbar-toggler-icon"></span> -->
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

          <li class="nav-item col-6 col-lg-auto">
            <router-link
              class="nav-link"
              to="schedule"
              v-bind:class="{ 'nav-active': isCurrentRoute('Schedule') }"
            >
              <i class="far fa-calendar "></i>My Schedule
            </router-link>
          </li>

          <li class="nav-item col-6 col-lg-auto">
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

          <li class="nav-item col-6 col-lg-auto dropdown">
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
            v-on:click="logout"
            type="submit"
            class="btn btn-theme-blacker"
          >
            Logout
            <i class="fas fa-sign-out-alt " style="margin-left: 0.25rem;"></i>
          </button>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: "theme-nav-bar",
  methods: {
    logout: function(event) {
      if (event) {
        this.$router.push("login");
      }
    },
    isCurrentRoute: function(route) {
      return this.currentRouteName == route;
    }
  },
  computed: {
    currentRouteName: function() {
      return this.$route.name;
    }
  }
};
</script>

<style lang="scss" scoped>
#app-nav {
  font-family: "Source Sans Pro", sans-serif;
  z-index: 1;
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

ul.navbar-nav {
}
</style>
