<template lang="html">
  <div
    class="modal fade"
    tabindex="-1"
    aria-labelledby="modalLabel"
    aria-hidden="true"
    ref="modalRef"
  >
    <div
      class="modal-dialog"
      :class="{
        'modal-lg': useLargeModal,
        'modal-dialog-centered': centerVertically
      }"
    >
      <div class="modal-content">
        <div class="modal-header">
          <h4
            :class="{ 'm-auto': centerHeader }"
            class="modal-title"
            id="modalLabel"
          >
            <slot name="header" />
          </h4>

          <button
            id="close-modal-icon"
            type="button"
            class="button-as-link"
            @click="closeModal()"
            :disabled="isStatic"
          >
            <i class="fas fa-times fa-lg text-theme-lightest-gray"></i>
          </button>
        </div>

        <div class="modal-body">
          <slot name="body" />
        </div>

        <!-- only include if needed -->
        <div v-if="useFooter" class="modal-footer">
          <slot name="footer" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import bootstrap from "bootstrap/dist/js/bootstrap.bundle.min.js";

export default {
  props: {
    useFooter: {
      type: Boolean,
      default: true
    },
    centerHeader: {
      type: Boolean,
      default: false
    },
    useLargeModal: {
      type: Boolean,
      default: false
    },
    centerVertically: {
      type: Boolean,
      default: false
    }
  },

  data() {
    return {
      modal: null,
      isStatic: false
    };
  },

  methods: {
    openModal() {
      this.modal.show();
    },
    closeModal() {
      this.modal.hide();
    },
    preventClosingModal() {
      this.modal._config.backdrop = "static";
      this.modal._config.keyboard = false;
      this.isStatic = true;
    },
    allowClosingModal() {
      this.modal._config.backdrop = true;
      this.modal._config.keyboard = true;
      this.isStatic = false;
    }
  },

  // runs after element references are created so modal is not undefined
  mounted() {
    if (this.modal == null)
      this.modal = new bootstrap.Modal(this.$refs.modalRef);
  }
};
</script>

<style scoped lang="scss">
/* allows the header title to be centered */
#close-modal-icon {
  position: absolute;
  right: 20px;
}

/* bootstrap modal overrides */
div.modal-content {
  background-color: var(--theme-blackest);
  color: var(--theme-whiter);
}

div.modal-header {
  color: var(--theme-whitest);
  border: none;
}

div.modal-body {
  background-color: var(--theme-blacker);
}

div.modal-footer {
  border: none;
}
</style>
