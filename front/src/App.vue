<template>
  <div>
    <Menu></Menu>
    <Header></Header>
    <div class="container">
      <router-view :key="$route.fullPath" />
    </div>
  </div>
</template>

<script>
import Menu from "./components/Menu.vue";
import Header from "./components/Header.vue";

export default {
  components: {
    Menu,
    Header
  },
  mounted() {
    window.TEMPLATE_START();
  }
};
</script>
