<template lang="html">
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
          <button type="button" class="button-as-link" data-bs-dismiss="modal">
            <i class="fas fa-times fa-lg text-theme-lightest-gray"></i>
          </button>
        </div>
        <div class="theme-modal-body">
          <div style="text-align: center">
            <span class="badge rounded-pill course-badge">MATH13013</span>
            <span class="badge rounded-pill course-badge">4 Credits</span>
            <br /><br />
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
            <hr />
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
            <button
              type="button"
              class="btn btn-theme-secondary"
              style="justify-content:center"
            >
              Rate Course
            </button>
          </div>
        </div>
        <div class="row" style="margin:1rem">
          <div class="col">
            <a href="#"
              ><i class="far fa-star fa-lg star-unfilled-icon"></i
            ></a>
          </div>
          <div class="col" style="text-align: right;">
            <a
              data-bs-toggle="modal"
              data-bs-target="#add-to-semester-modal"
              @click="showCourseInfoModal"
              data-bs-dismiss="modal"
              style="cursor: pointer"
            >
              <i class="fas fa-plus-circle fa-lg plus-add-icon"></i
            ></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
