<template lang="html">
  <div class="row mt-3 mb-4">
    <!-- filter bar for sm screens -->
    <div class="col-12 d-flex d-md-none align-items-center mb-3">
      <input
        type="text"
        class="form-control"
        placeholder="Search"
        @keyup.enter="searchCourses()"
        v-model="searchRequest.keyword"
      />

      <a class="d-block d-md-none filter-button" @click="openChangeProgramModal()" data-tooltip="Select Program">
        <i class="fas fa-pencil-alt"></i>
      </a>

      <div class="dropdown">
        <button
          class="button-as-link filter-button"
          type="button"
          id="sortOptions"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          data-tooltip="Sort Courses"
        >
          <i class="fas fa-sort-amount-up-alt"></i>
        </button>
        <ul class="dropdown-menu" aria-labelledby="sortOptions">
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType(SortTypes.courseId) }"
              @click="changeSort(SortTypes.courseId)"
            >
              Division Level
              <div
                v-if="isSortType(SortTypes.courseId)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending() }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending() }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType(SortTypes.program) }"
              @click="changeSort(SortTypes.program)"
            >
              Program
              <div
                v-if="isSortType(SortTypes.program)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending() }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending() }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType(SortTypes.credits) }"
              @click="changeSort(SortTypes.credits)"
            >
              Credits
              <div
                v-if="isSortType(SortTypes.credits)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending() }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending() }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
        </ul>
      </div>

      <div class="dropdown">
        <button
          class="button-as-link filter-button"
          type="button"
          id="viewOptions"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          data-tooltip="View Options"
        >
          <i class="fas fa-eye"></i>
        </button>
        <ul class="dropdown-menu" aria-labelledby="viewOptions">
          <li>
            <a
              class="dropdown-item"
              :class="{
                'dropdown-active': viewOption === ViewOptions.normalCard
              }"
              @click="viewOption = ViewOptions.normalCard"
            >
              Standard Card
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{
                'dropdown-active': viewOption === ViewOptions.smallCard
              }"
              @click="viewOption = ViewOptions.smallCard"
              >Small Card</a
            >
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': viewOption === ViewOptions.table }"
              @click="viewOption = ViewOptions.table"
              >Table</a
            >
          </li>
        </ul>
      </div>
    </div>

    <!-- search title -->
    <div
      class="col d-flex align-items-center justify-content-center justify-content-md-start"
    >
      <h1 class="text-theme-whitest d-inline">
        CS Courses
      </h1>
    </div>

    <!-- filter bar for screens md and up -->
    <div class="col d-none d-md-flex align-items-center justify-content-end">
      <a @click="openChangeProgramModal()" data-tooltip="Select Program" class="filter-button">
        <i class="fas fa-pencil-alt"></i>
      </a>

      <div class="dropdown">
        <button
          class="button-as-link filter-button"
          type="button"
          id="sortOptions"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          data-tooltip="Sort Courses"
        >
          <i class="fas fa-sort-amount-up-alt"></i>
        </button>
        <ul class="dropdown-menu" aria-labelledby="sortOptions">
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType(SortTypes.courseId) }"
              @click="changeSort(SortTypes.courseId)"
            >
              Division Level
              <div
                v-if="isSortType(SortTypes.courseId)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending() }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending() }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType(SortTypes.program) }"
              @click="changeSort(SortTypes.program)"
            >
              Program
              <div
                v-if="isSortType(SortTypes.program)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending() }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending() }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType(SortTypes.credits) }"
              @click="changeSort(SortTypes.credits)"
            >
              Credits
              <div
                v-if="isSortType(SortTypes.credits)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending() }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending() }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
        </ul>
      </div>

      <div class="dropdown">
        <button
          class="button-as-link filter-button"
          type="button"
          id="viewOptions"
          data-bs-toggle="dropdown"
          aria-expanded="false"
          data-tooltip="View Options"
        >
          <i class="fas fa-eye"></i>
        </button>
        <ul class="dropdown-menu" aria-labelledby="viewOptions">
          <li>
            <a
              class="dropdown-item"
              :class="{
                'dropdown-active': viewOption === ViewOptions.normalCard
              }"
              @click="viewOption = ViewOptions.normalCard"
            >
              Standard Card
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{
                'dropdown-active': viewOption === ViewOptions.smallCard
              }"
              @click="viewOption = ViewOptions.smallCard"
              >Small Card</a
            >
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': viewOption === ViewOptions.table }"
              @click="viewOption = ViewOptions.table"
              >Table</a
            >
          </li>
        </ul>
      </div>

      <transition name="fade">
        <input
          v-show="isSearching"
          type="text"
          class="form-control ms-3"
          id="search"
          placeholder="Search"
          ref="searchCourses"
          @keyup.enter="searchCourses()"
          v-model="searchRequest.keyword"
        />
      </transition>

      <a v-if="!isSearching" @click="toggleSearch()" data-tooltip="Search Courses" class="filter-button">
        <i class="fas fa-search"></i>
      </a>
      <a v-else @click="toggleSearch()" data-tooltip="Cancel Search" class="filter-button">
        <i class="fas fa-times"></i>
      </a>
    </div>
  </div>
</template>

<script lang="js">

const ViewOptions = Object.freeze({
  normalCard: 1,
  smallCard: 2,
  table: 3
});

const SortTypes = Object.freeze({
  courseId: 1,
  credits: 2,
  program: 3
});

export default {
    data() {
        return {
            ViewOptions,
            SortTypes,
            degrees: [],
            isSearching: false,
            searchRequest: {
              keyword: null,
              program: null,
              sortOption: {
                type: SortTypes.courseId,
                isAscending: true
              }
            },
            viewOption: ViewOptions.normalCard
        }
    },

    watch: {
      viewOption: function() {
          console.log(this.viewOption)
      },
    },

      methods: {
        changeSort(sortType) {
          if(this.isSortType(sortType))
            this.searchRequest.sortOption.isAscending = !this.searchRequest.sortOption.isAscending;
          else
            this.searchRequest.sortOption.type = sortType;

          this.searchCourses();
        },

        isSortType(sortType) {
          return this.searchRequest.sortOption.type === sortType;
        },

        isAscending() {
          return this.searchRequest.sortOption.isAscending;
        },

        openChangeProgramModal(){
          this.$emit("openChangeProgramModal");
        },

        toggleSearch() {
          this.isSearching = !this.isSearching;
          if(this.isSearching) {
            // doesn't work without this timeout
            setTimeout(() => {
              this.$refs.searchCourses.focus();
            }, 10);
          } else {
            this.searchRequest.keyword = null;
          }
        },

        searchCourses() {
          console.log("search request: ", this.searchRequest)
        }
      },
};
</script>

<style lang="scss" scoped>
.filter-button {
  margin-left: 1rem;

  @media (min-width: 576px) {
    margin-left: 1.5rem;
  }

  i {
    font-size: 1.6rem;
    color: var(--theme-white);

    &:hover {
      color: var(--theme-primary-light);
    }
  }
}

.dropdown-active {
  border-left: 3px solid var(--theme-primary-dark);
}

a.dropdown-item {
  display: flex;
  align-items: center;
}

.sort-icon-container {
  display: flex;
  flex-direction: column;
  margin-left: 1rem;

  i {
    font-size: 1.25rem;
    color: var(--theme-dark-gray);

    &:first-child {
      height: 1px; // makes the top sort icon sit directly above the bottom icon
    }

    &.sort-active {
      color: var(--theme-whitest);
    }
  }
}
</style>
