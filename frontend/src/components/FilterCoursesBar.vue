<template lang="html">
<div class="row mt-3">
        <div class="col">
          <div class="dropdown course-dropdown">
            <button
              class="btn btn-theme-secondary dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Select a program
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li>
                <a class="dropdown-item" href="#">Computer Science (B. S.)</a>
              </li>
              <li><a class="dropdown-item" href="#">Biology (B. S.)</a></li>
              <li><a class="dropdown-item" href="#">English (B. A.)</a></li>
            </ul>
          </div>
          <div class="dropdown course-dropdown">
            <button
              class="btn btn-theme-primary dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Select a concentration
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li>
                <a class="dropdown-item" href="#">Computer Science (B. S.)</a>
              </li>
              <li><a class="dropdown-item" href="#">Biology (B. S.)</a></li>
              <li><a class="dropdown-item" href="#">English (B. A.)</a></li>
            </ul>
          </div>
          <div class="dropdown course-dropdown">
            <button
              class="btn btn-theme-primary dropdown-toggle"
              type="button"
              id="dropdownMenuButton1"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              Sort Courses
            </button>
            <ul class="dropdown-menu" aria-labelledby="dropdownMenuButton1">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
            </ul>
          </div>
          <div class="course-search">
            <form class="d-flex">
              <input
                class="form-control me-2"
                type="search"
                placeholder="Search"
                aria-label="Search"
              />
              <button class="btn btn-theme-primary" type="submit">
                Search
              </button>
            </form>
          </div>
          <hr class="bg-theme-dark-gray" />
        </div>
      </div>
</template>

<style scoped>
.course-search {
  max-width: 30rem;
  display: inline-block;
  position: relative;
  top: 0.1rem;
}

.course-dropdown {
  display: inline-block;
  margin-right: 1rem;
}
</style>