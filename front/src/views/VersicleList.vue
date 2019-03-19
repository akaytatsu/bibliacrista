<template>
  <div>
    <Chapters/>
    <Versicle/>
  </div>
</template>

<script>

import Versicle from "../components/Versicle.vue"
import Chapters from "../components/Chapters.vue"

export default {
  name: "VersicleList",
  components: {
    Versicle,
    Chapters,
  }
};
</script>
