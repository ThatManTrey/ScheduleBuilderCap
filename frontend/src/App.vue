<template>
  <div id="app">
    <ThemeNavBar></ThemeNavBar>
    <transition name="fade" mode="out-in">
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
