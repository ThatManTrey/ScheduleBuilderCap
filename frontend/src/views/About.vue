<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <div class="container" id="display-block">
      <div class="row">
        <nav
          id="sidenav"
          class="col-md-3 col-lg-2 d-md-block bg-theme-blacker sidebar collapse"
        >
          <div class="position-sticky pt-3">
            <ul class="nav flex-column">
              <li class="nav-item"><a href="#instructions">Instructions</a></li>
              <li class="nav-item"><a href="#about">About Us</a></li>
              <li class="nav-item"><a href="#contact-us">Contact Us</a></li>
            </ul>
          </div>
        </nav>

        <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <div class="row about-block" id="instructions">
            <h3 class="text-theme-white">How-To Use</h3>
            <p class="text-theme-light-gray">This is how to use the app:</p>
          </div>
          <div class="row about-block" id="about">
            <h3 class="text-theme-white">About Us</h3>
            <p class="text-theme-light-gray">
              The KSU Course Planner provides a convenient and easy-to-use
              application for Kent State University (KSU) students to plan their
              future course work at the university. The application provides a
              rating system, providing insight into the course's quality and
              difficulty.
            </p>
            <p class="text-theme-light-gray">
              This application was created for CS49999 Capstone Project at Kent
              State University.
            </p>
            <div class="text-theme-white table-responsive">
              <table class="creator-info">
                <tr>
                  <td colspan="2">This application was created by:</td>
                </tr>

                <tr>
                  <td>Jaimie Bowen</td>
                  <td>Jaden Kandel</td>
                </tr>
                <tr>
                  <td>Trey Phillips</td>
                  <td>Daniel Stephan</td>
                </tr>
              </table>
            </div>
          </div>
          <div class="row about-block" id="contact-us">
            <h3 class="text-theme-white">Contact Us</h3>
            <p class="text-theme-light-gray" style="text-align:center">
              Complete the form below and one of our representatives will be in
              touch.
            </p>
            <form method="#" action="#">
              <div class="mb-3 text-theme-white">
                <label for="contactName" class="form-label">
                  <h6>Name:</h6>
                </label>
                <input
                  type="text"
                  class="form-control"
                  id="contactName"
                  aria-describedby="contactName"
                />
              </div>
              <div class="mb-3 text-theme-white">
                <label for="contactEmail" class="form-label">
                  <h6>Email Address:</h6>
                </label>
                <input
                  type="email"
                  class="form-control"
                  id="contactEmail"
                  aria-describedby="contactEmail"
                />
              </div>
              <div class="mb-3 text-theme-white">
                <label for="contactMessage" class="form-label">
                  <h6>Message:</h6>
                </label>
                <textarea
                  type="text"
                  class="form-control"
                  id="contactMessage"
                  aria-describedby="contactMessage"
                  rows="3"
                />
              </div>
              <div>
                <button type="reset" class="btn btn-theme-blacker">
                  Reset
                </button>
                <button
                  type="submit"
                  class="btn btn-theme-primary"
                  style="float:right"
                >
                  Submit
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';

export default {
    name: 'about',
    props: [],
    components: {
        ThemeNavBar,
    },
}
</script>

<style scoped>
#sidenav {
  height: 100%;
  width: 14rem;
  position: fixed;
  z-index: 0;
  top: 0;
  left: 0;
  background-color: var(--theme-blacker);
  overflow-x: hidden;
  padding-top: 4rem;
  border-right: solid 1pt var(--theme-darkest-gray);
  animation: slidein 3s;
}

@keyframes slidein {
  from {
    margin-left: -100%;
    width: 100%;
    opacity: 25%;
  }
  to {
    margin-left: 0%;
    width: 14rem;
    opacity: 100%;
  }
}

#sidenav a {
  padding: 1rem 1rem 1rem 2rem;
  text-decoration: none;
  font-size: 1.2rem;
  color: var(--theme-light-gray);
  display: block;
}

#sidenav a:hover {
  color: var(--theme-secondary);
}

.about-body {
  margin: 2rem 6rem 3rem 10rem;
}

.about-block {
  background: var(--theme-black);
  padding: 2rem;
  margin: 2rem;
  border: 0.25pt solid var(--theme-darkest-gray);
  animation: fade 3s ease;
}

@keyframes fade {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.about-block h3 {
  text-align: center;
  padding-bottom: 1rem;
  margin-bottom: 1.25rem;
  border-bottom: solid 0.25pt var(--theme-secondary);
}

.about-block h5 {
  text-align: center;
}

td {
  text-align: center;
  padding: 0.5rem;
}

.creator-info {
  margin-left: auto;
  margin-right: auto;
  width: 50%;
}
</style>
