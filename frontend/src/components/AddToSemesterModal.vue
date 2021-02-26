
<template lang="html">
<div
          class="modal fade"
          id="add-to-semester-modal"
          tabindex="-1"
          aria-labelledby="add-to-semester-modal"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="theme-modal-content">
              <div class="theme-modal-header">
                <h5 class="modal-title" id="exampleModalLabelOne">
                  Add to Semester
                </h5>
                <button
                  type="button"
                  class="button-as-link"
                  data-bs-dismiss="modal"
                >
                  <i class="fas fa-times fa-lg text-theme-lightest-gray"></i>
                </button>
              </div>
              <div class="theme-modal-body">
                <h6 class="text-theme-whiter" style="text-align: center">
                  Select semester you would like to add this course to:</h6>
                <div class="list-group">
                    <a href="#"><li class="list-group-item list-group-item-action" >
                      Semester 1
                      <span class="badge rounded-pill course-badge small">0</span></li></a>
                    <a href="#"><li class="list-group-item list-group-item-action" >
                      Semester 2
                      <span class="badge rounded-pill course-badge small">0</span></li></a>
                    <a href="#"><li class="list-group-item list-group-item-action" >
                      Semester 3
                      <span class="badge rounded-pill course-badge small">0</span></li></a>
                    <a href="#"><li class="list-group-item list-group-item-action" >
                      Semester 4
                      <span class="badge rounded-pill course-badge small">0</span></li></a>
                </div>

                <div style="text-align: center; padding-top: 1rem">
                  <a href="#">
                    <button type="button" class="btn btn-theme-primary">
                      Add Semester
                    </button>
                  </a>
                </div>

              </div>
            </div>
          </div>
        </div>
</template>