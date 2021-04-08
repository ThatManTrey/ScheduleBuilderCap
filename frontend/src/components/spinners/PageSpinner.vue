<template lang="html">
  <!-- Spinner that's fixed to the center of the screen when pages are loading  -->
  <div class="page-spinner">
    <Spinner :showSpinner="showSpinner" sizeInRem="3rem"></Spinner>
  </div>
</template>

<script lang="js">
import Spinner from './Spinner.vue';

export default {
    name: 'page-spinner',
    props: {
      showSpinner: Boolean
    },
    components: {
        Spinner
    }
}
</script>

<style scoped lang="scss">
// https://stackoverflow.com/questions/2005954/center-a-positionfixed-element?answertab=active#tab-top
// vertically centered fixed element
.page-spinner {
  position: fixed;
  top: 50vh;
  top: 50%;
  left: 50vw;
  left: 50%;
  margin-top: -25px; // half the spinner's height/width
  margin-left: -25px;
  z-index: 3;
}
</style>
