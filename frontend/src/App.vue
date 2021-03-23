<template>
  <div id="app">
    <PageSpinner
      v-if="!hasLoaded"
      :showSpinner="!hasLoaded"
      sizeInRem="3rem"
    ></PageSpinner>
    <transition name="page-fade">
      <router-view v-if="hasLoaded" />
    </transition>
  </div>
</template>

<script>
import axios from "axios";
import * as Toast from "./toast";
import PageSpinner from "./components/spinners/PageSpinner";

export default {
  data() {
    return {
      hasLoaded: false,
    };
  },

  components: {
    PageSpinner,
  },

  methods: {
    checkToken(authToken) {
      console.log(authToken);
      var verifyUrl = process.env.VUE_APP_API_URL + "/auth/verify";
      axios
        .get(verifyUrl, { headers: { Authorization: "Bearer " + authToken } })
        .then(() => {
          this.$actions.login(authToken);
          this.hasLoaded = true;
        })
        .catch(() => {
          this.hasLoaded = true;
          Toast.showErrorMessage(
            "Invalid authentication token. Please login again."
          );
          this.localStorage.userInfo;
        });
    },
  },

  created() {
    if (localStorage.userInfo != null) 
      this.checkToken(localStorage.userInfo);
      
    else this.hasLoaded = true;
  },
};
</script>
