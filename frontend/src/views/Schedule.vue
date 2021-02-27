<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <div class="container mt-3">
      <div v-for="n in 4" :key="n" class="row">
        <SemesterAccordion :targetName="'example' + n"></SemesterAccordion>
      </div>
    </div>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import SemesterAccordion from '../components/SemesterAccordion.vue';

export default {
    name: 'schedule',
    props: [],
    components: {
        ThemeNavBar,
        SemesterAccordion
    },
}
</script>

<style scoped>
div.row {
  min-width: 100%;
}
</style>
