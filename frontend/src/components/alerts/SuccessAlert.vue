<template lang="html">
  <div class="alert container text-theme-whitest bg-theme-primary-dark" role="alert">
    <div class="row">
      <div class="col-1 d-flex justify-content-center align-items-center">
        <i class="fas fa-check-circle" id="success-alert-check"></i>
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

<style scoped>
#success-alert-check {
  font-size: 1.5rem;
}
</style>
