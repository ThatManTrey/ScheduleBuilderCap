<template lang="html">
  <nav
    class="navbar navbar-expand-md navbar-light bg-theme-blackest"
    id="app-nav"
  >
    <div class="container-fluid">
      <!-- Put logo here -->
      <a class="navbar-brand text-theme-whitest" href="#">KSU COURSE PLANNER</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item nav-active">
            <router-link class="nav-link" to="home">
              <i class="fas fa-home text-theme-whitest"></i>Home
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="schedule">
              <i class="far fa-calendar text-theme-whitest"></i>My Schedule
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="favorites">
              <i class="fas fa-star text-theme-whitest"></i>Favorites
            </router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="about">
              <i class="fas fa-info-circle text-theme-whitest"></i>About
            </router-link>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle text-theme-white"
              href="#"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              More
            </a>
            <ul
              class="dropdown-menu bg-theme-black"
              aria-labelledby="navbarDropdown"
            >
              <li>
                <a class="dropdown-item text-theme-whiter" href="#"
                  >Contact Us</a
                >
              </li>
              <li>
                <a class="dropdown-item text-theme-whiter" href="#"
                  >Another action</a
                >
              </li>
              <li>
                <hr class="dropdown-divider text-theme-whiter" />
              </li>
              <li>
                <a class="dropdown-item text-theme-white" href="#"
                  >Delete My Account</a
                >
              </li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle text-theme-white"
              href="#"
              id="navbarDropdown"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              dev
            </a>
            <ul
              class="dropdown-menu bg-theme-black"
              aria-labelledby="navbarDropdown"
            >
              <li>
                <router-link class="dropdown-item" to="theme">
                  Theme page</router-link
                >
              </li>
              <li>
                <a
                  class="dropdown-item text-theme-whiter"
                  href="https://getbootstrap.com/docs/5.0/getting-started/introduction/"
                  target="_blank"
                  >Bootstrap doc</a
                >
              </li>
              <li>
                <a
                  class="dropdown-item text-theme-whiter"
                  href="https://uxdesign.cc/dark-mode-ui-design-the-definitive-guide-part-1-color-53dcfaea5129"
                  target="_blank"
                  >Theme ref</a
                >
              </li>
            </ul>
          </li>
        </ul>
        <div class="d-flex">
          <!-- <button type="submit" class="btn btn-primary">Logout</button> -->
          <router-link class="dropdown-item bg-theme-black" to="login">
            Logout
            <i
              class="fas fa-sign-out-alt text-theme-whitest"
              style="margin-left: 0.25rem;"
            ></i>
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>
