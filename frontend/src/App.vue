<template>
  <div id="app">
    <PageSpinner v-if="!hasLoaded" :showSpinner="!hasLoaded" sizeInRem="3rem"></PageSpinner>
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

  methods: {
    verifyAccessToken() {
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
    },

    setAxiosDefaults() {
      axios.defaults.baseURL = process.env.VUE_APP_API_URL;
      if(process.env.NODE_ENV === "development") 
        axios.defaults.headers.common["Api-Key"] = process.env.VUE_APP_API_KEY;
    }
  },

  created() {
    this.setAxiosDefaults();

    // verify accessToken if user has it in localStorage before loading anything
    if (localStorage.getItem("userInfo")) 
      this.verifyAccessToken();
    else 
      this.hasLoaded = true;
  }
};
</script>
