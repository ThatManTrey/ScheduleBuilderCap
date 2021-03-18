<template lang="html">
  <!-- Spinner that's fixed to the center of the screen when pages are loading  -->
  <div class="course-spinner-container ">
    <Spinner :showSpinner="showSpinner" sizeInRem="3rem"></Spinner>
  </div>
</template>

<script lang="js">
import Spinner from './Spinner.vue';

export default {
    name: 'page-spinner',
    props: {
      showSpinner: Boolean,
    },
    components: {
        Spinner
    }
}
</script>

<style scoped lang="scss">
.course-spinner-container {
  position: fixed;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  top: 0;
}

.course-spinner-container div {
  display: flex;
  margin: 0 auto;
}
</style>
