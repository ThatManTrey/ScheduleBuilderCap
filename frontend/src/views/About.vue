<template lang="html">
  <div>
    <div class="container mt-5" id="about-container">
      <div class="row">
        <nav
          id="sidenav"
          class="col-xl-2 d-xl-block d-none bg-theme-blackest sidebar collapse"
        >
          <div class="position-sticky pt-3">
            <ul class="nav flex-column">
              <li class="nav-item">
                <button
                  class="button-as-link"
                  @click="scrollToElement($refs.whatIsThis)"
                >
                  What Is This?
                </button>
              </li>
              <li class="nav-item">
                <button
                  class="button-as-link"
                  @click="scrollToElement($refs.disclaimers)"
                >
                  Disclaimers
                </button>
              </li>
              <li class="nav-item">
                <button
                  class="button-as-link"
                  @click="scrollToElement($refs.contributors)"
                >
                  Contributors
                </button>
              </li>
              <li class="nav-item">
                <button
                  class="button-as-link"
                  @click="scrollToElement($refs.contactUs)"
                >
                  Contact Us
                </button>
              </li>
            </ul>
          </div>
        </nav>

        <div class="col px-md-4 px-0">
          <div class="container-fluid">
            <div class="row about-block" ref="whatIsThis">
              <h3>What Is This?</h3>
              <p>
                Most Kent State University (KSU) students would agree that the
                current course searching tools available through the university
                are somewhat lacking in the user-friendliness department. So, we
                decided to create our own alternative.
              </p>

              <p>
                We've made the entire KSU course catalog, both undergraduate and
                graduate courses, available for viewing, including the ability
                to search courses, filter by programs, and sort them.
              </p>
              <p>
                By registering for an account above, you can create your own
                schedule that you can come back to as a reference throughout
                your college career.
              </p>
              <p>
                Confirming your email during the registration process will also
                allow you to rate a course based on its quality and difficulty
                for other users to see.
              </p>
            </div>

            <div class="row about-block" ref="disclaimers">
              <h3>Disclaimers</h3>
              <p>
                Specific semester availability for courses is not shown here, so
                always double check the official KSU catalog through Flashline
                when officially scheduling courses for a semester.
              </p>
            </div>
            <div
              class="row about-block justify-content-around"
              ref="contributors"
            >
              <h3>Contributors</h3>
              <div class="col-4 d-flex flex-column">
                <span class="mb-4"
                  >Jaimie Bowen
                  <a
                    href="https://github.com/jaimie453"
                    class="contributor-link"
                    ><i class="fab fa-github"></i></a
                ></span>
                <span
                  >Jaden Kandel
                  <a
                    href="https://github.com/JadenKandel"
                    class="contributor-link"
                    ><i class="fab fa-github"></i></a
                ></span>
              </div>
              <div class="col-4 d-flex flex-column">
                <span class="mb-4"
                  >Trey Phillips
                  <a
                    href="https://github.com/ThatManTrey"
                    class="contributor-link"
                    ><i class="fab fa-github"></i></a
                ></span>
                <span
                  >Daniel Stephan
                  <a href="https://github.com/dstepha3" class="contributor-link"
                    ><i class="fab fa-github"></i></a
                ></span>
              </div>
            </div>
            <div class="row about-block" ref="contactUs">
              <h3>Contact Us</h3>
              <p>
                Any questions or issues? Send us an email at
                <a class="link" href="mailto:ksucourseplanner@gmail.com"
                  >ksucourseplanner@gmail.com</a
                >
                and we'll get back to you soon.
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    scrollToElement(elementRef) {
      elementRef.scrollIntoView({ behavior: "smooth" });
    }
  }
};
</script>

<style lang="scss" scoped>
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
  animation: slidein 1s;
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

#sidenav button {
  padding: 1rem 1rem 1rem 2rem;
  text-decoration: none;
  font-size: 1.2rem;
  color: var(--theme-whiter);
  display: block;

  &:hover {
    color: var(--theme-primary-light);
  }
}

.about-body {
  margin: 2rem 6rem 3rem 10rem;
}

.about-block {
  margin-bottom: 5rem;

  h3 {
    text-align: center;
    padding-bottom: 1rem;
    margin-bottom: 2rem;
    border-bottom: solid 0.25pt var(--theme-black);
    color: var(--theme-whitest);
  }
}

#about-container {
  max-width: 800px;
}

p {
  color: var(--theme-white);
}

.contributor-link {
  float: right;

  i {
    font-size: 1.25rem;

    &:hover {
      color: var(--theme-primary-light);
    }
  }
}
</style>
