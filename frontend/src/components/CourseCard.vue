<template lang="html">
  <div class="card justify-content-center bg-theme-blacker course-card">
    <div class="card-body container-fluid text-theme-whiter">
      <div class="row text-theme-whitest">
        <h4 class="course-card-title m-1">Analytic Geometry And Calculus I</h4>
      </div>

      <div class="row mb-2">
        <div class="p-0">
          <span class="badge rounded-pill course-badge">
            <button class="button-as-link">MATH 13013</button>
          </span>

          <span class="badge rounded-pill course-badge">
            <button class="button-as-link">4 Credits</button>
          </span>
        </div>
      </div>

      <div class="row mb-3">
        <p class="card-text">
          This course will introduce the state-of-art computing platforms with
          the focus on how to utilize them in processing (managing and
          analyzing) massive datasets...
          <a data-bs-toggle="modal" data-bs-target="#course-info-modal" @click="showCourseInfoModal"
            class="link"
          >View more</a>
        </p>
      </div>

      <div class="row">
        <div class="col">
          <a href="#"><i class="far fa-star fa-lg text-theme-secondary"></i></a>
        </div>

        <div class="col" style="text-align: right;">
          <a data-bs-toggle="modal" data-bs-target="#add-to-semester-modal" @click="showAddToSemesterModal"
            style="cursor: pointer"
            ><i class="fas fa-plus-circle fa-lg text-theme-confirm"></i
          ></a>
        </div>
      </div>
    </div>
<!--
    <div
          class="modal fade"
          id="course-info-modal"
          tabindex="-1"
          aria-labelledby="course-info-modal"
          aria-hidden="true"
        >
          <div class="modal-dialog">
            <div class="theme-modal-content">
              <div class="theme-modal-header">
                <h5 class="modal-title" id="course-info-modal">
                  Analytical Geometry And Calculus I
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
                <div style="text-align: center">
                  <span class="badge rounded-pill course-badge">MATH13013</span>
                  <span class="badge rounded-pill course-badge">4 Credits</span>
                  <br/><br/>
                </div>
                <p>
                  This course will introduce the state-of-art computing platforms with
                  the focus on how to utilize them in processing (managing and
                  analyzing) massive datasets...
                </p>
                <p>
                  Prerequisite:
                </p>
                <p>
                  Schedule Type:
                </p>
                <p>
                  Contact Hours:
                </p>
                <p>
                  Grade Mode:
                </p>
                <div class="row" style="text-align: center">
                   <hr/>
                  <div class="col">
                    <p>Course Quality:</p>
                    <p>
                      <i class="fas fa-star fa-lg text-theme-secondary"></i>
                      <i class="far fa-star fa-lg text-theme-secondary"></i>
                      <i class="far fa-star fa-lg text-theme-secondary"></i>
                      <i class="far fa-star fa-lg text-theme-secondary"></i>
                      <i class="far fa-star fa-lg text-theme-secondary"></i>
                    </p>
                  </div>
                  <div class="col">
                    <p>Course Difficulty:</p>
                    <p>
                      <i class="fas fa-star fa-lg text-theme-secondary"></i>
                      <i class="far fa-star fa-lg text-theme-secondary"></i>
                      <i class="far fa-star fa-lg text-theme-secondary"></i>
                      <i class="far fa-star fa-lg text-theme-secondary"></i>
                      <i class="far fa-star fa-lg text-theme-secondary"></i>
                    </p>
                  </div>
                </div>
                <div style="text-align: center">
                  <button type="button" class="btn btn-theme-secondary" style="justify-content:center">
                    Rate Course
                  </button>
                </div>
              </div>
              <div class="row" style="margin:1rem">
                <div class="col">
                    <a href="#"><i class="far fa-star fa-lg text-theme-secondary"></i></a>
                  </div>
                <div class="col" style="text-align: right;">
                  <a data-bs-toggle="modal" data-bs-target="#add-to-semester-modal" href="#add-to-semester-modal"
                      data-bs-dismiss="modal">
                    <i class="fas fa-plus-circle fa-lg text-theme-confirm"></i></a>
                </div>
              </div>
            </div>
          </div>
        </div> -->

   <!-- <div
          class="modal fade"
          id="add-to-semester-modal"
          data-backdrop="false">
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
        </div> -->


  </div>

</template>

<style lang="scss">
div.course-card {
  transition: transform 0.2s;
  box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.1) !important;
}

div.course-card:hover {
  background-color: var(--theme-black) !important;
  box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.75) !important;
  transform: scale(1.05);
}

.course-desc {
  min-height: 5rem;
}

span.course-badge {
  color: var(--theme-whiter);
  background-color: var(--theme-darkest-gray);
  margin-left: 0.5rem;
}

.course-badge button {
  font: inherit;
}

.course-card-title {
  font-family: "Source Sans Pro";
}
</style>
