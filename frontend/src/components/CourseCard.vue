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
          <a
            data-bs-toggle="modal"
            data-bs-target="#course-info-modal"
            @click="showCourseInfoModal"
            class="link"
            >View more</a
          >
        </p>
      </div>

      <div class="row">
        <div class="col">
          <a href="#"><i class="far fa-star fa-lg star-unfilled-icon"></i></a>
        </div>

        <div class="col" style="text-align: right;">
          <a
            data-bs-toggle="modal"
            data-bs-target="#add-to-semester-modal"
            @click="showAddToSemesterModal"
            style="cursor: pointer"
            ><i class="fas fa-plus-circle fa-lg plus-add-icon"></i
          ></a>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
div.course-card {
  transition: transform 0.2s;
  box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.1);
}

div.course-card:hover {
  background-color: var(--theme-black);
  box-shadow: 0 1rem 3rem rgba(0, 0, 0, 0.75);
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
