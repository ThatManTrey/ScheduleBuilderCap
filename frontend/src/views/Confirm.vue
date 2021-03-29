<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <PageSpinner :showSpinner="isLoadingPage"></PageSpinner>
    <div v-if="!isLoadingPage" class="container mt-5">
      <div class="row justify-content-center text-theme-whitest">
          <h2>Account confirmed successfully!</h2>
          <p>You can now sign in.</p>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import PageSpinner from '../components/spinners/PageSpinner.vue';
import axios from 'axios';
import * as Toast from '../toast.js';

export default {

    components: {
        ThemeNavBar,
        PageSpinner
    },

    data() {
        return {
            confirmationToken: null,
            isLoadingPage: true
        }
    },

    // TODO: move to router check
    methods: {
        verifyConfirmationToken() {

            if(this.confirmationToken) {
            axios
            .get("/auth/verify/confirm", { headers: { Authorization: "Bearer " + this.confirmationToken } })
            .then(() => {
                this.isLoadingPage = false;
            })
            .catch(() => {
                this.$router.push('home');
                Toast.showErrorMessage(
                    "You have already confirmed your email"
                );
            });
            } else {
            this.$router.push('home');
            Toast.showErrorMessage("Invalid reset confirmation token.");
            }
      },
    },

    created() {
      this.confirmationToken = this.$route.query.token;
      console.log(this.confirmationToken);
        this.verifyConfirmationToken();
    }
};
</script>
