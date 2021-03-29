<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>

    <div class="container mt-3">
      <div class="row course-container">
        <h3 class="text-theme-whitest">Theme guide</h3>

        <br /><br />

        <div class="row">
          <div
            class="col-sm-12 col-lg-6 mb-3 bg-theme-blacker text-theme-whitest"
          >
            <br />

            <h5 class="text-theme-whitest">Alerts/Modals</h5>

            <br />

            <p>
              Use alerts in modals when a success/error message is needed after
              hitting an API endpoint
            </p>

            <!-- turn these alerts into a component -->
            <div
              class="alert container bg-theme-success text-theme-whitest container"
              role="alert"
            >
              <div class="row">
                <div class="col-1">
                  <i class="fas fa-check-circle fa-lg"></i>
                </div>
                <div class="col-11">
                  Your password has been succesfully reset! Check your email for
                  a link.
                </div>
              </div>
            </div>

            <!-- probably wont use this -->
            <!-- <div
              class="alert container bg-theme-primary-dark text-theme-whitest container"
              role="alert"
            >
              <div class="row">
                <div class="col-1">
                  <Spinner
                    :showSpinner="true"
                    sizeInRem="1.5rem"
                    color="white"
                  ></Spinner>
                </div>
                <div class="col-11">
                  Attempting to login...
                </div>
              </div>
            </div> -->

            <div
              class="alert container bg-theme-warning-dark text-theme-whitest container"
              role="alert"
            >
              <div class="row">
                <div class="col-1">
                  <i class="fas fa-times-circle fa-lg"></i>
                </div>
                <div class="col-11">
                  An error occured oh no aaaaaaaaaaaaaaaaaaaaaaaaaa
                </div>
              </div>
            </div>

            <br />

            <p>
              Use toast messages outside of modals after hitting an API
              endpoint.
            </p>

            <button
              type="button"
              class="btn btn-theme-warning-dark"
              @click="error()"
            >
              Error toast message
            </button>
            &nbsp;
            <button
              type="button"
              class="btn btn-theme-confirm"
              @click="success()"
            >
              Success toast message
            </button>

            <br />
          </div>

          <div
            class="col-sm-12 col-lg-6 mb-3 bg-theme-blacker text-theme-whitest"
          >
            <br />
            <h5>Icons</h5>
            <br />
            <i class="fas fa-plus-circle fa-lg text-theme-confirm"></i>
            &nbsp; Adding
            <br />

            <i class="far fa-star fa-lg text-theme-secondary"></i>
            &nbsp; Favorites
            <br />

            <a>
              <i class="fas fa-star fa-lg text-theme-secondary"></i>
            </a>
            &nbsp; Favorites
            <br />

            <i class="fas fa-info-circle fa-lg text-theme-primary-light"></i>
            &nbsp; More info
            <br />

            <i class="fas fa-times-circle fa-lg text-theme-warning-dark"></i>
            &nbsp; Remove/error
            <br />

            <i
              class="fas fa-question-circle fa-lg text-theme-primary-light"
            ></i>
            Help &nbsp;
            <br />

            <i class="fas fa-check-circle fa-lg text-theme-success"></i> &nbsp;
            Success
            <br />

            <i class="fas fa-key fa-lg text-theme-whitest"></i> &nbsp; Password
            <br />

            <i class="fas fa-envelope fa-lg text-theme-whitest"></i> &nbsp;
            email
            <br />

            <i class="fas fa-sort-alpha-up fa-lg text-theme-whitest"></i> &nbsp;
            Sorting (if needed)
            <br />

            <i class="fas fa-times fa-lg text-theme-whitest"></i> &nbsp; Cancel
            <br />

            <i class="fas fa-search fa-lg text-theme-whitest"></i>
            Search (if needed)
            <br />
          </div>
        </div>

        <div class="row">
          <div class="col-sm-12 col-lg-6 mb-3 bg-theme-darkest-gray">
            <br />

            <h5 class="text-theme-whitest">Buttons</h5>

            <br />

            <div class="mb-3">
              <button type="button" class="btn btn-theme-black">
                Less important button
              </button>
              &nbsp;
              <button type="button" class="btn btn-theme-blacker">
                Less important button
              </button>

              <br />
              <br />

              <button type="button" class="btn btn-theme-primary-dark">
                Somewhat important button
              </button>
              &nbsp;
              <button type="button" class="btn btn-theme-secondary">
                Very Important button
              </button>

              <br />
              <br />

              <button type="button" class="btn btn-theme-warning-dark">
                Delete something
              </button>
              &nbsp;
              <button type="button" class="btn btn-theme-confirm">
                Add something
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
          <div class="col-md-12 col-lg-10 col-xl-8 mb-3">
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
      </div>
    </div>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import Spinner from '../components/spinners/Spinner.vue';
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
            // AJAX request
            axios.get("/colors/primary")
                .then((res) => {
                    this.primaryColors = res.data;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
            axios.get("/colors/accent")
                .then((res) => {
                    this.accentColors = res.data;
                })
                .catch((error) => {
                    // eslint-disable-next-line
                    console.error(error);
                });
        },
        error(){
          Toast.showErrorMessage("Test error message")
        },
        success(){
          Toast.showSuccessMessage("Test success message")
        }
    },
    created() {
        this.getColors();
        setTimeout(() => {
            this.hasLoaded = true;
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
