import Vue from 'vue'
import App from './App.vue'
import './assets/style.css'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.js';
import '@fortawesome/fontawesome-free/js/all.js';

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
