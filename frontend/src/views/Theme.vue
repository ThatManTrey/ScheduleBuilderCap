<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>

    <div class="container mt-3">
      <div class="row course-container">
        <h3 class="text-theme-whitest">Theme guide</h3>

        <br /><br />

        <div class="row">
          <div class="col-sm-12 col-lg-6 mb-3 bg-theme-blacker">
            <br />

            <h5 class="text-theme-whitest">Alerts</h5>

            <br />

            <div class="alert bg-theme-confirm" role="alert">
              <i class="fas fa-check-circle fa-lg text-theme-white"></i> &nbsp;
              Your password has been succesfully reset! Check your email for a
              link.
            </div>

            <div class="alert bg-theme-warning text-theme-whitest" role="alert">
              <i class="fas fa-times-circle fa-lg text-theme-white"></i> &nbsp;
              error error error erororororoor
            </div>
          </div>

          <div class="col-sm-12 col-lg-6 mb-3 bg-theme-blacker">
            <br />

            <h5 class="text-theme-whitest">Icons</h5>

            <br />

            <i class="fas fa-plus-circle fa-lg text-theme-confirm"></i> &nbsp;

            <i class="far fa-star fa-lg text-theme-secondary"></i> &nbsp;

            <i class="fas fa-star fa-lg text-theme-secondary"></i> &nbsp;

            <i class="fas fa-info-circle fa-lg text-theme-primary"></i> &nbsp;

            <i class="fas fa-times-circle fa-lg text-theme-warning"></i> &nbsp;

            <i class="fas fa-question-circle fa-lg text-theme-primary"></i>
            &nbsp; <i class="fas fa-home fa-lg text-theme-whitest"></i> &nbsp;

            <i class="far fa-calendar fa-lg text-theme-whitest"></i> &nbsp;

            <i class="fas fa-check-circle fa-lg text-theme-confirm"></i> &nbsp;

            <i class="fas fa-sign-out-alt fa-lg text-theme-whitest"></i> &nbsp;

            <i class="fas fa-key fa-lg text-theme-whitest"></i> &nbsp;

            <i class="fas fa-envelope fa-lg text-theme-whitest"></i> &nbsp;

            <i class="fas fa-sort-alpha-up fa-lg text-theme-whitest"></i> &nbsp;

            <i class="fas fa-edit fa-lg text-theme-whitest"></i> &nbsp;

            <i class="fas fa-times fa-lg text-theme-whitest"></i> &nbsp;

            <i class="fas fa-search fa-lg text-theme-whitest"></i>
          </div>
        </div>

        <div class="row">
          <div class="col-sm-12 col-lg-6 mb-3 bg-theme-blacker">
            <br />

            <h5 class="text-theme-whitest">modals/buttons</h5>

            <br />

            <div class="mb-3">
              <button
                type="button"
                class="btn btn-theme-black"
                data-bs-toggle="modal"
                data-bs-target="#exampleModalOne"
              >
                Standard modal
              </button>

              <button
                type="button"
                class="btn btn-theme-black"
                data-bs-toggle="modal"
                data-bs-target="#exampleModalTwo"
              >
                Launch demo modal
              </button>

              <br /><br />

              <button type="button" class="btn btn-theme-primary">
                Test button
              </button>

              <button type="button" class="btn btn-theme-secondary">
                Test button
              </button>

              <button type="button" class="btn btn-theme-warning">
                Test button
              </button>

              <button type="button" class="btn btn-theme-confirm">
                Test button
              </button>
            </div>
          </div>

          <div class="col-sm-12 col-lg-6 mb-3 bg-theme-blacker">
            <br />

            <h5 class="text-theme-whitest">CSS classes</h5>

            <br />

            <div class="mb-3 text-theme-white">
              <p><b>Background color</b>: &nbsp; bg-theme-{color}</p>

              <p><b>Text color</b>: &nbsp; text-theme-{color}</p>

              <p>
                <b>Button color</b>: &nbsp;
                btn-theme-{accent-color/black/blacker}
              </p>

              <p>
                <a class="link"
                  >Link color for &lt;a&gt; and &lt;router-link&gt; </a
                >: &nbsp; link
              </p>

              <p>
                <button class="link button-as-link">
                  Button that looks like link/text</button
                >: &nbsp; button-as-link
              </p>
            </div>
          </div>
        </div>

        <div class="row mt-3">
          <div class="col bg-theme-blacker">
            <br />

            <h5 class="text-theme-whitest">Spinner Test</h5>

            <br />

            <p class="text-theme-white">fades out and disappears after 5s</p>

            <Spinner :showSpinner="!hasLoaded"></Spinner>
          </div>
        </div>

        <div class="row justify-content-center">
          <div class="col-sm-12 col-md-10 col-lg-8 mb-3">
            <div class="container-fluid mb-3 text-white">
              <h5 class="text-theme-whitest">Main (neutral) colors</h5>

              <br />

              <div></div>

              <div
                class="row text-theme-whitest"
                v-for="(color, index) in primaryColors"
                :key="index"
              >
                <div class="col-2">{{ color.name }} &nbsp;</div>

                <div
                  class="col-6 color-test"
                  :class="'bg-theme-' + color.name"
                ></div>

                <div class="col-4">&nbsp; {{ color.uses }}</div>
              </div>
            </div>

            <div class="container-fluid">
              <h5 class="text-theme-whitest">Accent colors</h5>

              <br />

              <div
                class="row text-theme-whitest"
                v-for="(color, index) in accentColors"
                :key="index"
              >
                <div class="col-2">{{ color.name }} &nbsp;</div>

                <div
                  class="col-6 color-test"
                  :class="'bg-theme-' + color.name"
                ></div>

                <div class="col-4">&nbsp; {{ color.uses }}</div>
              </div>
            </div>
          </div>
        </div>

        <!-- modals -->

        <div
          class="modal fade"
          id="exampleModalOne"
          tabindex="-1"
          aria-labelledby="exampleModalLabelOne"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="theme-modal-content">
              <div class="theme-modal-header">
                <h5 class="modal-title" id="exampleModalLabelOne">
                  Standard modal
                </h5>

                <button
                  type="button"
                  class="button-as-link"
                  data-bs-dismiss="modal"
                >
                  <i class="fas fa-times fa-lg text-theme-lightest-gray"></i>
                </button>
              </div>

              <div class="theme-modal-body">
                <p>test modal</p>
              </div>

              <div class="theme-modal-footer">
                <button
                  type="button"
                  class="btn btn-theme-dark"
                  data-bs-dismiss="modal"
                >
                  Cancel
                </button>

                <button
                  type="button"
                  class="btn btn-theme-primary"
                  data-bs-dismiss="modal"
                >
                  Continue
                </button>
              </div>
            </div>
          </div>
        </div>

        <div
          class="modal fade"
          id="exampleModalTwo"
          tabindex="-1"
          aria-labelledby="exampleModalLabelTwo"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="theme-modal-content">
              <div class="theme-modal-header">
                <h5 class="modal-title" id="exampleModalLabelOne">
                  Modal w/ no footer
                </h5>

                <button
                  type="button"
                  class="button-as-link"
                  data-bs-dismiss="modal"
                >
                  <i class="fas fa-times fa-lg text-theme-lightest-gray"></i>
                </button>
              </div>

              <div class="theme-modal-body">
                <h6 class="text-theme-whiter">This modal has a header</h6>

                <p>
                  orem ipsum dolor sit amet, consectetur adipiscing elit, sed do
                  eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
                  enim ad minim veniam, quis nostrud exercitation ullamco
                  laboris nisi ut aliquip ex ea commodo consequat. Duis aute
                  irure dolor in reprehenderit in voluptate velit esse cillum
                  dolore eu fugiat nulla pariatur. Excepteur sint occaecat
                  cupidatat non proident, sunt in culpa qui officia deserunt
                  mollit anim id est laborum.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import Spinner from '../components/Spinner.vue';
import * as Toast from '../toast.js';
import axios from 'axios';

export default {
    name: 'Theme',
    data() {
        return {
            primaryColors: [],
            accentColors: [],
            hasLoaded: false,
        };
    },
    components: {
        ThemeNavBar,
        Spinner
    },
    methods: {
        getColors() {
            const path = 'http://localhost:5000/api/colors';
            // AJAX request
            axios.get(path + "/primary")
                .then((res) => {
                    this.primaryColors = res.data;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
            axios.get(path + "/accent")
                .then((res) => {
                    this.accentColors = res.data;
                    Toast.showSuccessMessage("This is a success message");
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        }
    },
    created() {
        this.getColors();
        setTimeout(() => {
            this.hasLoaded = true;
            Toast.showErrorMessage("This is an error message");
        }, 5000);
    },
};
</script>

<style scoped>
.color-test {
  border: 1px solid black;
  border-radius: 1rem;
  height: 3rem;
}
</style>
