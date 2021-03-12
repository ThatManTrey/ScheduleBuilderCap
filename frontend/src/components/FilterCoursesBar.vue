<template lang="html">
  <div class="row mt-3"> 
      <form class="center" method="#" action="#">
        <div class="course-dropdown">
          <select class="form-control theme-secondary" id="selectProgram">
            <option selected>Select a Program</option>
            <option>Computer Science (B.S.)</option>
            <option>Biology (B.S.)</option>
            <option>English (B.A.)</option>
          </select>
          <i class="fas fa-chevron-down fa-sm text-theme-blackest icon-css"></i>
        </div>
        <div class="course-dropdown">
          <select class="form-control theme-primary" id="selectConcentration">
            <option selected>Select a Concentration</option>
            <option>Computer Science (B.S.)</option>
            <option>Biology (B.S.)</option>
            <option>English (B.A.)</option>
          </select>
          <i class="fas fa-chevron-down fa-sm text-theme-whiter icon-css"></i>
        </div>
        <div class="course-dropdown">
          <select class="form-control theme-primary" id="selectSort">
            <option selected>Sort Courses</option>
            <option>Action</option>
            <option>Another Action</option>
            <option>Something else here</option>
          </select>
          <i class="fas fa-chevron-down fa-sm text-theme-whiter icon-css"></i>
        </div>
        <div class="course-search">
          <input type="text" class="form-control" id="search" placeholder="Search">
        </div>
        <button class="btn-sm btn-theme-primary" type="submit">
          Search
        </button>
      </form>

      <hr class="bg-theme-dark-gray" />
  </div>
</template>

<style scoped>
.course-search {
  width: 18rem;
  display: inline-block;
  margin-left: 0.5rem;
  margin-right: 1rem;
}

.course-dropdown {
  display: inline-block;
  margin: 0.5rem;
  margin-top: 0;
  width: 15rem;
}

.center {
  text-align: center;
}

.icon-css {
  position: relative;
  float: right;
  top: -23px;
  left: -14px;
}
</style>
