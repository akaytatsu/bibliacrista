import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "./registerServiceWorker";

import VueResource from "vue-resource";
Vue.use(VueResource);

import Paginate from 'vuejs-paginate'
Vue.component('paginate', Paginate)

Vue.config.productionTip = false;

Vue.http.options.root = "http://localhost:8000/bible/";

new Vue({
  router,
  render: h => h(App)
}).$mount("#app");
