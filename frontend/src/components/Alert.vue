<template lang="html">
  <div
    class="alert container text-theme-whitest"
    v-bind:class="{
      'bg-theme-success': isSuccess,
      'bg-theme-warning-dark': !isSuccess
    }"
    role="alert"
  >
    <div class="row">
      <div class="col-1">
        <span v-if="isSuccess">
          <i class="fas fa-check-circle fa-lg"></i>
        </span>
        <span v-else>
          <i class="fas fa-times-circle fa-lg"></i>
        </span>
      </div>
      <div class="col-11">
        <span v-if="isSuccess">
          {{ successMessage }}
        </span>
        <span v-else>
          {{ errorMessage }}
        </span>
      </div>
    </div>
  </div>
</template>

<script lang="js">

export default {
    name: 'alert',
    props: {
      isSuccess: Boolean,
      errorMessage: String,
      successMessage: String
    }
}
</script>