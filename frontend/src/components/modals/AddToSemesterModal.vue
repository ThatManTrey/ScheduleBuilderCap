/* eslint-disable */
<template lang="html">
  <Modal
    :centerHeader="true"
    :useFooter="false"
    ref="addToSemesterBaseModalRef"
  >
    <template v-slot:header>Add Course to Semester</template>
    <template v-slot:body>
      <div>
        <h6 class="text-center">
          Select the semester you would like to add MATH 13013 to:
        </h6>
        <div class="list-group mt-3">
          <!-- list of semesters -->
          <div
            tabindex="0"
            class="list-group-item add-course"
            @click="addCourse()"
            @keyup.enter="addCourse()"
            v-for="n in semesters"
            :key="n"
          >
            <!-- @click.stop and @keyup.enter.stop prevents parent element's click from happening -->
            <i
              class="fas fa-times-circle remove-icon"
              tabindex="0"
              @keyup.enter.stop
              @keyup.enter="removeSemester(n)"
              @click.stop
              @click="removeSemester(n)"
            ></i>
            Semester {{ n }}
            <span class="badge rounded-pill course-badge small">
              15 Credits</span
            >
          </div>

          <!-- add a new semester -->
          <div class="list-group-item">
            <div v-show="isAddingSemester" class="container-fluid">
              <div class="row">
                <div class="col-12">
                  <input
                    type="text"
                    id="newSemesterName1"
                    class="form-control"
                    placeholder="Enter a semester name..."
                  />
                </div>
                <div class="col-6 mt-2">
                  <button
                    type="submit"
                    class="btn btn-theme-confirm btn-sm"
                    @click="test"
                  >
                    Add Semester
                  </button>
                  <a
                    tabindex="0"
                    @keyup.enter="isAddingSemester = false"
                    @click="isAddingSemester = false"
                  >
                    <i class="fas fa-times" id="cancel-add"></i>
                  </a>
                </div>
              </div>
            </div>
            <div v-show="!isAddingSemester" id="add-semester">
              <a
                tabindex="0"
                @keyup.enter="isAddingSemester = true"
                @click="isAddingSemester = true"
              >
                <i class="fas fa-plus-circle plus-add-icon"></i>
                <span> Add Another Semester</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </template>
  </Modal>
</template>

<script>
import Modal from "./Modal.vue";
import * as Toast from "../../toast.js";

export default {
  data() {
    return {
      isAddingSemester: false,
      semesters: 4
    };
  },

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
    test() {
      this.isAddingSemester = false;
      this.semesters++;
    },
    removeSemester(n) {
      var removePromptResult = confirm(
        "Are you sure you want to remove semester " +
          n +
          " and all its courses?"
      );
      if (removePromptResult == true) {
        Toast.showSuccessMessage(
          "Semester " + n + " was removed successfully."
        );
      }
    },

    addCourse() {
      Toast.showSuccessMessage("Course added successfully.");
      this.closeModal();
    }
  }
};
</script>

<style scoped>
div.list-group {
  border-radius: 0.5rem;
}

div.list-group-item {
  padding: 0.75rem 1.5rem;
  border: none;
}

div.add-course {
  color: var(--theme-whitest);
  font-weight: bold;
  cursor: pointer;
}

div.add-course:hover,
div.add-course:focus {
  /*border: 3px solid rgba(2, 161, 145, 0.5);*/
  box-shadow: inset 1px 0 0 rgba(2, 161, 145, 0.2),
    inset -1px 0 0 rgba(2, 161, 145, 0.2), 0 0 4px 0 rgba(2, 161, 145, 0.6),
    0 0 6px 2px rgba(2, 161, 145, 0.6);
  outline: none;
  z-index: 1;
}

div.list-group-item:nth-child(odd) {
  background-color: var(--theme-black);
}

div.list-group-item:nth-child(even) {
  background-color: var(--theme-darkest-gray);
}

div.list-group-item i {
  margin-right: 0.25rem;
}

.course-badge.small {
  background-color: var(--theme-primary-dark);
  color: var(--theme-whitest);
  float: right;
}

/* add semester link */

#cancel-add {
  position: relative;
  margin-left: 1rem;
  top: 3px;
  font-size: 1.2rem;
}

#add-semester {
  font-weight: 400;
  font-size: 0.9rem;
}

#add-semester a:hover,
#add-semester a:focus {
  color: var(--theme-confirm);
}
</style>
