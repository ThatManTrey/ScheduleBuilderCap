<template lang="html">
  <div>
    <div class="container-fluid">
      <div class="row justify-content-center">
        <div
          class="col-10 col-sm-8 col-md-6 col-lg-5 col-xl-4 vertical-center justify-content-center"
        >
          <div class="card signin-box bg-theme-blacker">
            <div class="card-body">
              <div>
                <h2 class="text-center text-theme-whitest">
                  KSU Course Planner
                </h2>
                <p class="slogan-subtext">A better way to plan your degree</p>
                <!-- put logo here maybe? -->
              </div>

              <div class="container mb-3">
                <div class="alert alert-success" role="alert" hidden>
                  Your password has been succesfully reset! Check your email for
                  a link.
                </div>

                <form>
                  <div class="mb-3 text-theme-white">
                    <label for="userEmail" class="form-label"
                      >Email Address</label
                    >
                    <input
                      type="email"
                      class="form-control"
                      id="userEmail"
                      aria-describedby="passHelp"
                    />
                    <div id="passHelp" class="form-text">
                      <router-link class="dropdown-item" to="register">
                        Don't have an account? Register here!
                      </router-link>
                    </div>
                  </div>
                  <div class="mb-3 text-theme-white">
                    <label for="userPass" class="form-label">Password</label>
                    <input
                      type="password"
                      class="form-control"
                      id="userPass"
                      aria-describedby="passHelp"
                    />
                    <div id="passHelp" class="form-text">
                      <button
                        type="button"
                        class="open-pass-modal"
                        data-bs-toggle="modal"
                        data-bs-target="#resetPasswordModal"
                      >
                        Forgot your password?
                      </button>
                    </div>
                  </div>
                  <div class="mb-3 text-center">
                    <!-- <button type="submit" class="btn btn-primary">Log in</button> -->
                    <router-link class="dropdown-item" to="home"
                      >Log In</router-link
                    >
                  </div>
                </form>
              </div>

              <div class="accordion" id="accordionExample">
                <div class="accordion-item">
                  <h2 class="accordion-header" id="headingOne">
                    <button
                      class="accordion-button"
                      type="button"
                      data-bs-toggle="collapse"
                      data-bs-target="#collapseOne"
                      aria-expanded="true"
                      aria-controls="collapseOne"
                    >
                      What's KSU Course Planner?
                    </button>
                  </h2>
                  <div
                    id="collapseOne"
                    class="accordion-collapse collapse"
                    aria-labelledby="headingOne"
                    data-bs-parent="#accordionExample"
                  >
                    <div class="accordion-body">
                      <p>
                        <strong
                          >KSU Course Planner is a free course scheduling and
                          degree planner app for Kent State University
                          students.</strong
                        >
                        Unlike services offered directly through the university
                        such as Visual Schedule Builder, KSU Course Planner
                        allows you to plan out your entire college career in
                        advance, no matter how many semesters you plan on
                        attending. Sign up now to give it a try!
                      </p>
                    </div>
                  </div>
                </div>
              </div>

              <!-- Reset Password Modal -->
              <div
                class="modal fade"
                id="resetPasswordModal"
                tabindex="-1"
                aria-labelledby="resetPasswordModalLabel"
                aria-hidden="true"
              >
                <div class="modal-dialog">
                  <div class="modal-content">
                    <form>
                      <div class="modal-header">
                        <h5 class="modal-title" id="resetPasswordModalLabel">
                          Reset My Password
                        </h5>
                        <button
                          type="button"
                          class="btn-close"
                          data-bs-dismiss="modal"
                          aria-label="Close"
                        ></button>
                      </div>
                      <div class="modal-body">
                        <p>
                          Enter your email address and we will send you a link
                          to reset your password.
                        </p>
                        <label for="userEmailToReset" class="form-label"
                          >Email Address</label
                        >
                        <input
                          type="email"
                          class="form-control"
                          id="userEmailToReset"
                          aria-describedby="emailHelp"
                        />
                        <div id="emailHelp" class="form-text text-danger">
                          Please enter a valid email.
                        </div>
                      </div>
                      <div class="modal-footer">
                        <button
                          type="button"
                          class="btn btn-secondary"
                          data-bs-dismiss="modal"
                        >
                          Cancel
                        </button>
                        <button type="button" class="btn btn-primary">
                          Reset Password
                        </button>
                      </div>
                    </form>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">

export default {
    name: 'login',
    props: [],
    components: {
    },
}
</script>

<style scoped></style>
