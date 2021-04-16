<template lang="html">
  <Modal :useFooter="false" ref="changeProgramModalRef">
    <template v-slot:header>
      Change Program
    </template>

    <template v-slot:body>
      <div>
        <div v-if="addedPrograms.length > 0" class="mb-3">
          <h5 class="ms-3">Selected Programs</h5>
          <table class="table text-theme-whitest mt-3">
            <tbody>
              <tr
                class="program-row"
                v-for="(degree, index) in addedPrograms"
                :key="index"
              >
                <td>{{ degree.degreeType }}</td>
                <td>{{ degree.degreeName }}</td>
                <td>
                  <button
                    @click="removeProgram(degree)"
                    class="add-remove-link button-as-link"
                  >
                    <i class="fas fa-times-circle fa-lg"></i>
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="accordion accordion-flush" id="accordionExample">
          <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
              <button
                class="accordion-button"
                type="button"
                data-bs-toggle="collapse"
                data-bs-target="#collapseOne"
                aria-expanded="true"
                aria-controls="collapseOne"
              >
                Search Courses
              </button>
            </h2>
            <div
              id="collapseOne"
              class="accordion-collapse collapse"
              :class="{ show: openAccordion }"
              aria-labelledby="headingOne"
              data-bs-parent="#accordionExample"
            >
              <div class="accordion-body">
                <input
                  type="search"
                  class="form-control"
                  placeholder="Search Programs"
                  v-model.trim="keyword"
                  ref="searchPrograms"
                />

                <div v-if="programs.length > 0" class="mt-3 px-3">
                  <table class="table text-theme-whitest">
                    <tbody>
                      <tr
                        class="program-row"
                        v-for="(degree, index) in programs"
                        :key="index"
                      >
                        <td>{{ degree.degreeType }}</td>
                        <td>{{ degree.degreeName }}</td>
                        <td>
                          <button
                            @click="addProgram(degree)"
                            class="add-remove-link button-as-link"
                          >
                            <i class="fas fa-plus-circle fa-lg"></i>
                          </button>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
                <p class="mt-3" v-else>No programs found</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import { mapState } from "vuex";

export default {
  components: {
    Modal
  },

  data() {
    return {
      programs: [],
      keyword: "",
      openAccordion: false
    };
  },

  watch: {
    keyword: function() {
      this.programs = this.$store.getters["courses/searchPrograms"](
        this.keyword
      );
    }
  },

  computed: mapState({
    addedPrograms: state => state.courses.searchRequest.programs
  }),

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.changeProgramModalRef.openModal();

      if (this.openAccordion) {
        console.log("got here");
        // timeout is needed to wait for modal and accordion animation to finish
        setTimeout(() => {
          this.$refs.searchPrograms.focus();
        }, 750);
      }
    },

    closeModal() {
      this.$refs.changeProgramModalRef.closeModal();
    },

    addProgram(program) {
      this.$store.commit("courses/addProgram", program);
      this.$store.dispatch("courses/updatePagination", 1);
    },

    removeProgram(program) {
      this.$store.commit("courses/removeProgram", program);
      this.$store.dispatch("courses/updatePagination", 1);
    }
  },

  created() {
    this.openAccordion = this.addedPrograms.length === 0;

    this.$store.dispatch("courses/getPrograms").then(() => {
      this.programs = this.$store.state.courses.allPrograms;
    });
  }
};
</script>

<style lang="scss" scoped>
#search-results {
  background-color: var(--theme-dark-gray);
  position: absolute;
}

.fa-plus-circle {
  font-size: 1.35rem;
}

tr {
  border-color: var(--theme-black);

  &:last-child {
    border-color: transparent;
  }
}

@media (min-width: 576px) {
  td {
    padding: 1rem;
  }
}

td {
  padding-top: 1rem;
  padding-bottom: 1rem;
}

.table {
  margin-bottom: 0;
}

.accordion-item {
  background-color: transparent;
  border: 0;
}

.accordion-button {
  background-color: transparent;
  color: var(--theme-whitest);
}
</style>
