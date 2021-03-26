<template lang="html">
  <div class="d-inline">
    <div class="d-inline" v-if="useAnimation">
      <transition name="fade">
        <div
          v-if="showSpinner"
          class="spinner-border"
          v-bind:style="styleObject"
          role="status"
        >
          <span class="visually-hidden">Loading...</span>
        </div>
      </transition>
    </div>
    <div class="d-inline" v-else>
      <div
        v-if="showSpinner"
        class="spinner-border"
        v-bind:style="styleObject"
        role="status"
      >
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </div>
</template>

<script lang="js">
export default {
    name: 'spinner',
    props: {
        showSpinner: Boolean,
        sizeInRem: {
            type: String,
            default: "2rem"
        },
        color: {
          type: String,
          default: "primary-dark"
        },
        useAnimation: {
          type: Boolean,
          default: true
        }
    },

    data() {
        return {
            styleObject: {
                height: this.sizeInRem,
                width: this.sizeInRem,
                'border-width': this.calcBorderWidth(),
                color: this.calcColor()
            }
        }
    },

    methods: {
      calcBorderWidth() {
        var borderSize = parseFloat(this.sizeInRem) * 0.1
        return borderSize.toString() + "em";
      },
      calcColor() {
        return "var(--theme-" + this.color + ")";
      }
    }
}
</script>
