<template>
  <div id="app">
    <ThemeNavBar></ThemeNavBar>
    <transition name="fade-short" mode="out-in">
      <router-view />
    </transition>
  </div>
</template>

<script>
import ThemeNavBar from "./components/ThemeNavBar";

export default {
  components: {
    ThemeNavBar
  }
};
</script>

<style lang="scss" scoped>
#app {
  display: flex;
  min-height: 100vh;
  max-width: 100vw;
  flex-direction: column;
}
</style>
