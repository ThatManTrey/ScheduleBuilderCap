<template lang="html">
    <div>
        <ThemeNavBar></ThemeNavBar>
        <PageSpinner v-if="!hasLoadedCourses" :showSpinner=!hasLoadedCourses></PageSpinner>
    
        <div class="container">
            <div class="row mt-3">
                <div class="col">
                    <div class="dropdown course-dropdown">
                        <button class="btn btn-theme-secondary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
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
                        <button class="btn btn-theme-primary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
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
                        <button class="btn btn-theme-primary dropdown-toggle" type="button" id="dropdownMenuButton1" data-bs-toggle="dropdown" aria-expanded="false">
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
                            <input class="form-control theme-search me-2" type="search" placeholder="Search" aria-label="Search" />
                            <button class="btn btn-theme-primary" type="submit">
                                                            Search
                                                          </button>
                        </form>
                    </div>
                    <hr class="bg-theme-dark-gray" />
                </div>
            </div>
            <transition name="coursefade">
                <div v-show="hasLoadedCourses" class="row mx-3">
                    <div class="col-sm-12 col-md-6 col-lg-4 col-xl-3 mb-3" v-for="n in 12" :key="n">
                        <CourseCard></CourseCard>
                    </div>
                </div>
            </transition>
    
            <!-- Additional requirements -->
            <div class="row" hidden>
                <div class="accordion" id="accordionExample">
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingOne">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                                          View Additional Graduation Requirements
                                                        </button>
                        </h2>
                        <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th scope="col">Add</th>
                                            <th scope="col">Category</th>
                                            <th class="text-center" scope="col">Credits Needed</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>
                                                <a href="#"><i class="fas fa-plus-circle fa-lg"></i></a>
                                            </td>
                                            <td>Foreign Language</td>
                                            <td class="text-center">8</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <a href="#"><i class="fas fa-plus-circle fa-lg"></i></a>
                                            </td>
                                            <td>Kent Core Composition</td>
                                            <td class="text-center">6</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <a href="#"><i class="fas fa-plus-circle fa-lg"></i></a>
                                            </td>
                                            <td>
                                                Kent Core Humanities and Fine Arts (minimum one course from each)
                                            </td>
                                            <td class="text-center">9</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <a href="#"><i class="fas fa-plus-circle fa-lg"></i></a>
                                            </td>
                                            <td>
                                                Kent Core Humanities and Fine Arts (minimum one course from each)
                                            </td>
                                            <td class="text-center">9</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <a href="#"><i class="fas fa-plus-circle fa-lg"></i></a>
                                            </td>
                                            <td>
                                                Kent Core Humanities and Fine Arts (minimum one course from each)
                                            </td>
                                            <td class="text-center">9</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <a href="#"><i class="fas fa-plus-circle fa-lg"></i></a>
                                            </td>
                                            <td>
                                                Kent Core Humanities and Fine Arts (minimum one course from each)
                                            </td>
                                            <td class="text-center">9</td>
                                        </tr>
                                        <tr>
                                            <td>
                                                <a href="#"><i class="fas fa-plus-circle fa-lg"></i></a>
                                            </td>
                                            <td>
                                                Computer Science (CS) Upper-Division Electives (30000 or 40000 level)
                                            </td>
                                            <td class="text-center">6</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- ensures all the courses can be seen when schedule is collapsed -->
        <br /><br /><br />
    
        <!-- <div class="semester-bar bg-light">
                                                    <div class="accordion" id="accordionExample" style="width: 100vw;">
                                                        <div class="accordion-item">
                                                            <h2 class="accordion-header" id="headingOne">
                                                                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne"
                                                                    aria-expanded="true" aria-controls="collapseOne" style="padding-right: 2rem;">
                                                                    My Schedule
                                                                </button>
                                                            </h2>
                                                            <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne"
                                                                data-bs-parent="#accordionExample">
                                                                <div class="accordion-body">
                                                                    <strong>This is the first item's accordion body.</strong> It is hidden by default, until the
                                                                    collapse plugin adds the appropriate classes that we use to style each element. These classes
                                                                    control the overall appearance, as well as the showing and hiding via CSS transitions. You can
                                                                    modify any of this with custom CSS or overriding our default variables. It's also worth noting that
                                                                    just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit
                                                                    overflow.
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div> -->
    </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';
import CourseCard from '../components/CourseCard.vue';
import PageSpinner from '../components/PageSpinner.vue';

export default {
    name: 'home',
    props: [],
    data() {
        return {
            hasLoadedCourses: false
        }
    },
    components: {
        ThemeNavBar,
        CourseCard,
        PageSpinner
    },
    created() {
        // loading test
        setTimeout(() => {
            this.hasLoadedCourses = true;
        }, 2000);
    }
}
</script>

<style scoped>

.coursefade-enter-active {
    transition: opacity 2s;
}

.coursefade-enter,
.coursefade-leave-to {
    opacity: 0;
}

</style>
