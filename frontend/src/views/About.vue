<template lang="html">
  <div>
    <ThemeNavBar></ThemeNavBar>
    <div class="container">
      <div class="row">
          <nav id="sidenav" class="col-md-3 col-lg-2 d-md-block bg-theme-blacker sidebar collapse">
            <div class="position-sticky pt-3">
              <ul class="nav flex-column">
                <li class="nav-item"><a href="#instructions">Instructions</a></li>
                <li class="nav-item"><a href="#about">About Us</a></li>
                <li class="nav-item"><a href="#contact-us">Contact Us</a></li>
              </ul>
            </div>
          </nav>
        
        <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
          <div class=" row about-block" id="instructions">
            <h3 class="text-theme-white">How-To Use</h3>
            <p class="text-theme-light-gray"> words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words </p>
          </div>
          <div class="row about-block" id="about">
            <h3 class="text-theme-white">About Us</h3>
            <p class="text-theme-light-gray"> words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words </p>
          </div>
          <div class="row about-block" id="contact-us">
           <h3 class="text-theme-white">Contact Us</h3>
            <p class="text-theme-light-gray"> words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words words 
            words words words words words words words words words words words words words words words words words </p>
          </div>
        </div>
      </div>


    </div>
  </div>
</template>

<script lang="js">
import ThemeNavBar from '../components/ThemeNavBar.vue';

export default {
    name: 'about',
    props: [],
    components: {
        ThemeNavBar,
    },
}
</script>

<style scoped>

#sidenav {
  height: 100%;
  width: 14rem;
  position: fixed;
  z-index: 0;
  top: 0;
  left: 0;
  background-color: var(--theme-blacker);
  overflow-x: hidden;
  padding-top: 4rem;
  border-right: solid 1pt var(--theme-secondary);
}

#sidenav a {
  padding: 1rem 1rem 1rem 2rem;
  text-decoration: none;
  font-size: 1.2rem;
  color: var(--theme-light-gray);
  display: block;
}

#sidenav a:hover {
  color: var(--theme-secondary);
}

.about-body {
  margin: 2rem 6rem 3rem 10rem;
}

.about-block {
  background: var(--theme-black);
  padding: 2rem;
  margin: 2rem;
  border: 0.25pt solid var(--theme-darkest-gray);
}

.about-block h3 {
  text-align: center;
  margin-bottom: 1.5rem;
}

</style>
