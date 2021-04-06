<template lang="html">
  <Modal :useFooter="false" ref="changeProgramModalRef">
    <template v-slot:header>
      Change Program
    </template>

    <template v-slot:body>
  <div>
    <div>fixeefief oijef[ji]</div>
    <!-- <div v-if="addedPrograms.length > 0" class="mb-3">
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
              <a
                @click="addProgram(degree)"
                tabindex="0"
                class="add-remove-link"
                ><i class="fas fa-times-circle fa-lg"></i
              ></a>
            </td>
          </tr>
        </tbody>
      </table>
    </div> -->

    <input
      type="search"
      class="form-control"
      placeholder="Search Programs"
      v-model.trim="keyword"
    />

    <div v-if="searchResults && searchResults.length > 0" class="mt-3 px-3">
      <table class="table text-theme-whitest">
        <tbody>
          <tr
            class="program-row"
            v-for="(degree, index) in searchResults"
            :key="index"
          >
            <td>{{ degree.degreeType }}</td>
            <td>{{ degree.degreeName }}</td>
            <td>
              <a
                @click="addProgram(degree)"
                tabindex="0"
                class="add-remove-link"
                ><i class="fas fa-plus-circle fa-lg"></i
              ></a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <p class="mt-3" v-else>No programs found</p>
  </div>
  </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import axios from "axios";
import { mapState } from "vuex";

export default {
  components: {
    Modal,
  },

  data() {
    return {
      allDegrees: null,
      searchResults: null,
      keyword: "",
    };
  },

  computed: mapState({
    addedPrograms: (state) => state.courses.searchRequest.programs,
  }),

  watch: {
    keyword: function () {
      if (this.keyword.length > 0) this.searchPrograms();
    },
  },

  methods: {
    /* needed to open/close this modal from parent component */
    openModal() {
      this.$refs.changeProgramModalRef.openModal();
    },
    closeModal() {
      this.$refs.changeProgramModalRef.closeModal();
    },

    getDegrees() {
      axios.get("/degrees/all").then((res) => {
        this.allDegrees = res.data.degrees;
        if (this.keyword.length === 0) this.searchResults = this.allDegrees;
      });
    },

    searchPrograms() {
      this.searchResults = this.allDegrees.filter((degree) =>
        `${degree.degreeName.toLowerCase()} ${degree.degreeType.toLowerCase()}`.includes(
          this.keyword.toLowerCase()
        )
      );
    },

    addProgram(program) {
      this.$store.commit("courses/addProgram", program);
    },
  },

  created() {
    this.getDegrees();
  },
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

td {
  padding: 1rem;
}

.table {
  margin-bottom: 0;
}
</style>
