<template lang="html">
  <div
    class="alert container text-theme-whitest bg-theme-warning-dark"
    role="alert"
  >
    <div class="row">
      <div class="col-1">
        <i class="fas fa-times-circle fa-lg"></i>
      </div>
      <div class="col-11">
        {{ errorMessage }}
      </div>
    </div>
  </div>
</template>

<script lang="js">

export default {
    name: 'error-alert',
    props: {
      errorMessage: String
    }
}
</script>
