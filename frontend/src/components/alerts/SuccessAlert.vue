<template lang="html">
  <div class="alert container text-theme-whitest bg-theme-success" role="alert">
    <div class="row">
      <div class="col-1">
        <i class="fas fa-check-circle fa-lg"></i>
      </div>
      <div class="col-11">
        {{ successMessage }}
      </div>
    </div>
  </div>
</template>

<script lang="js">

export default {
    name: 'success-alert',
    props: {
      successMessage: String
    }
}
</script>
