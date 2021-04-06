<template lang="html">
  <div class="row mt-3 mb-4">
    <!-- filter bar for sm screens -->
    <div class="col-12 d-flex d-md-none align-items-center mb-3">
      <input
        type="text"
        class="form-control"
        placeholder="Search"
        @keyup.enter="searchCourses()"
        :value="keyword"
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
              :class="{ 'dropdown-active': isSortType($enums.SortTypes.courseId) }"
              @click="changeSort($enums.SortTypes.courseId)"
            >
              Division Level
              <div
                v-if="isSortType($enums.SortTypes.courseId)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType($enums.SortTypes.program) }"
              @click="changeSort($enums.SortTypes.program)"
            >
              Program
              <div
                v-if="isSortType($enums.SortTypes.program)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType($enums.SortTypes.credits) }"
              @click="changeSort($enums.SortTypes.credits)"
            >
              Credits
              <div
                v-if="isSortType($enums.SortTypes.credits)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending }"
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
                'dropdown-active': isViewOption($enums.ViewOptions.normalCard)
              }"
              @click="changeViewOption($enums.ViewOptions.normalCard)"
            >
              Standard Card
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{
                'dropdown-active': isViewOption($enums.ViewOptions.smallCard)
              }"
              @click="changeViewOption($enums.ViewOptions.smallCard)"
              >Small Card</a
            >
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isViewOption($enums.ViewOptions.table) }"
              @click="changeViewOption($enums.ViewOptions.table)"
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
      <h1 class="text-theme-whitest d-inline text-center text-md-start">
        {{ getProgramDisplayName() }}
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
              :class="{ 'dropdown-active': isSortType($enums.SortTypes.courseId) }"
              @click="changeSort($enums.SortTypes.courseId)"
            >
              Division Level
              <div
                v-if="isSortType($enums.SortTypes.courseId)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType($enums.SortTypes.program) }"
              @click="changeSort($enums.SortTypes.program)"
            >
              Program
              <div
                v-if="isSortType($enums.SortTypes.program)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending }"
                  class="fas fa-sort-down"
                ></i>
              </div>
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isSortType($enums.SortTypes.credits) }"
              @click="changeSort($enums.SortTypes.credits)"
            >
              Credits
              <div
                v-if="isSortType($enums.SortTypes.credits)"
                class="sort-icon-container"
              >
                <i
                  :class="{ 'sort-active': isAscending }"
                  class="fas fa-sort-up"
                ></i>
                <i
                  :class="{ 'sort-active': !isAscending }"
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
                'dropdown-active': isViewOption($enums.ViewOptions.normalCard)
              }"
              @click="changeViewOption($enums.ViewOptions.normalCard)"
            >
              Standard Card
            </a>
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{
                'dropdown-active': isViewOption($enums.ViewOptions.smallCard)
              }"
              @click="changeViewOption($enums.ViewOptions.smallCard)"
              >Small Card</a
            >
          </li>
          <li>
            <a
              class="dropdown-item"
              :class="{ 'dropdown-active': isViewOption($enums.ViewOptions.table) }"
              @click="changeViewOption($enums.ViewOptions.table)"
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
          :value="keyword"
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
import { mapState } from 'vuex';

export default {
    data() {
        return {
            isSearching: false
        }
    },

    computed: mapState({
      keyword: state => state.courses.searchRequest.keyword,
      isAscending: state => state.courses.searchRequest.sortOption.isAscending,
      programs: state => state.courses.searchRequest.programs
    }),

    methods: {
      changeSort(sortType) {
        this.$store.commit('courses/setSortType', sortType);
        // dispatch
      },

      isSortType(sortType) {
        return this.$store.state.courses.searchRequest.sortOption.type === sortType;
      },

      changeViewOption(viewOption) {
        this.$store.commit('courses/setViewOption', viewOption);
      },

      isViewOption(viewOption) {
        return this.$store.state.courses.viewOption == viewOption;
      },

      openChangeProgramModal(){
        this.$emit("openChangeProgramModal");
      },

      toggleSearch() {
        this.isSearching = !this.isSearching;
        if(this.isSearching) {
          // doesn't work without this timeout for some reason
          setTimeout(() => {
            this.$refs.searchCourses.focus();
          }, 10);
        } else {
          this.$store.commit('courses/setSearchKeyword', "");
        }
      },

      searchCourses() {
        this.$store.commit('courses/setSearchKeyword', this.keyword);
        // dispatch
      },

      getProgramDisplayName() {
        if (this.programs.length === 0)
          return "All Courses"
        else if (this.programs.length === 1)
          return this.programs[0].degreeName + " Courses";
        else if(this.programs.length <= 3) {
          var result = "";
          for(var i = 0; i < this.programs.length; i++) {
            result += this.programs[i].degreeType

            if(i === this.programs.length - 2)
              result += " and ";
            else if(i !== this.programs.length - 1)
                result += ", ";            
          }

          result += " Courses";
          return result;
        } else 
          return "Multiple Programs Selected";
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
