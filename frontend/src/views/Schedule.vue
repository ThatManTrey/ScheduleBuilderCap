<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <div class="container"></div>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';

export default {
    name: 'schedule',
    props: [],
    components: {
        ThemeNavBar,
    },
}
</script>

<style scoped></style>