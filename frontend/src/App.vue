<template>
  <div id="app">
    <PageSpinner :showSpinner="!hasLoaded" sizeInRem="3rem"></PageSpinner>
    <router-view v-if="hasLoaded" />
  </div>
</template>

<script>
import axios from "axios";
import PageSpinner from "./components/spinners/PageSpinner";
import * as Toast from "./toast.js";

export default {
  data() {
    return {
      hasLoaded: false
    };
  },

  components: {
    PageSpinner
  },

  created() {
    axios.defaults.baseURL = process.env.VUE_APP_API_URL;

    // verify accessToken if user has it in localStorage before loading anything
    if (localStorage.getItem("userInfo")) {
      this.$store
        .dispatch({
          type: "verifyAccessToken",
          token: localStorage.getItem("userInfo")
        })
        .then(() => {
          if (this.$store.state.authError)
            Toast.showErrorMessage(this.$store.state.authError);

          this.hasLoaded = true;
        });
    } else {
      this.hasLoaded = true;
    }
  }
};
</script>
