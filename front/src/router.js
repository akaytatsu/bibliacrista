import Vue from "vue";
import Router from "vue-router";
import SimpleBooks from "./views/SimpleBooks.vue";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: "/",
      name: "SimpleBooks",
      component: SimpleBooks
    }
  ]
});
