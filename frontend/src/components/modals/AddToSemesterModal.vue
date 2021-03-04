<template lang="html">
  <Modal :centerHeader="true" :useFooter="false" ref="addToSemesterBaseModalRef">
    <template v-slot:header>Add Course to Semester</template>
    <template v-slot:body>
        <h6 class="text-center">
            Select the semester you would like to add MATH 13013 to:
          </h6>
          <div class="list-group mt-3">
            <a class="list-group-item" v-for="n in 4" :key="n">
              <a><i class="fas fa-times-circle"></i></a> Fall 2021
              <span class="badge rounded-pill course-badge small">15 Credits</span>
            </a>
          </div>

          <!-- ignore this error lol, works fine -->
          <div class="text-center mt-3">
              <button type="button" class="btn btn-theme-confirm">
                Add Semester
              </button>
          </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";

export default {
  components: {
    Modal
  },

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.addToSemesterBaseModalRef.openModal();
    },
    closeModal() {
      this.$refs.addToSemesterBaseModalRef.closeModal();
    },
  }
};
</script>

<style scoped>

div.list-group {
  border-radius: 0.5rem;
}

a.list-group-item {
  color: var(--theme-whitest);
  font-weight: bold;
  border: 3px solid rgba(0, 0, 0, 0);
}

a.list-group-item, a.list-group-item a  {
  width: 100%;
  height: 100%;
}

a.list-group-item:hover {
  border: 3px solid rgba(2, 161, 145, 0.5);
}

a.list-group-item:nth-child(odd) {
    background-color: var(--theme-black);
}

a.list-group-item:nth-child(even) {
    background-color: var(--theme-darkest-gray);
}

a.list-group-item i {
  color: var(--theme-white);
  margin-right: .25rem;
}

a.list-group-item i:hover {
  color: #d54040;
}

.course-badge.small {
  background-color: var(--theme-primary);
  color: var(--theme-whitest);
  float: right;
}

</style>
