<template lang="html">
  <transition name="spinnerfade">
    <div
      v-if="showSpinner"
      class="spinner-border text-theme-primary"
      v-bind:style="styleObject"
      role="status"
    >
      <span class="visually-hidden">Loading...</span>
    </div>
  </transition>
</template>

<script lang="js">
export default {
    name: 'spinner',
    props: {
        showSpinner: Boolean,
        sizeInRem: {
            type: String,
            default: "2rem"
        }
    },
    data() {
        return {
            styleObject: {
                height: this.sizeInRem,
                width: this.sizeInRem
            }
        }
    },
    created() {
        //this.styleObject.height = this.sizeInRem;
        //this.styleObject.width = this.sizeInRem;
    }
}
</script>

<style scoped lang="scss">
.spinnerfade-enter-active,
.spinnerfade-leave-active {
  transition: opacity 0.75s;
}

.spinnerfade-enter,
.spinnerfade-leave-to {
  opacity: 0;
}
</style>
