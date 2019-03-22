<template>
  <div>
    <!-- Header -->
    <header class="header" id="site-header">
      <div class="page-title">
        <router-link :to="{ name: 'SimpleBooks'}">
          <h6 style="color: #FFFFFF;">BibliaCristã</h6>
        </router-link>
      </div>

      <div class="header-content-wrapper">
        <div class="search-bar w-search notification-list friend-requests">
          <div class="form-group with-button">
            <input
              class="form-control"
              placeholder="Pesquisar Versiculo"
              type="text" v-model="search"/>

            <router-link tag="button" :to="{ name: 'VersicleSearch', query: get_query_params({search: this.search}, true )}">
              <svg class="olymp-magnifying-glass-icon">
                <use
                  xlink:href="icons/icons.svg#olymp-magnifying-glass-icon"
                ></use>
              </svg>
            </router-link>
          </div>
        </div>

      </div>
    </header>

    <!-- ... end Header -->
    <!-- Responsive Header -->
    <header class="header header-responsive" id="site-header-responsive">
      <div class="header-content-wrapper">
        <ul class="nav nav-tabs mobile-app-tabs" role="tablist">

          <li class="nav-item">
            <a class="nav-link" data-toggle="tab" href="#search" role="tab">
              <svg class="olymp-magnifying-glass-icon">
                <use
                  xlink:href="icons/icons.svg#olymp-magnifying-glass-icon"
                ></use>
              </svg>
              <svg class="olymp-close-icon">
                <use xlink:href="icons/icons.svg#olymp-close-icon"></use>
              </svg>
            </a>
          </li>
        </ul>
      </div>

      <!-- Tab panes -->
      <div class="tab-content tab-content-responsive">
        <div class="tab-pane" id="search" role="tabpanel">
          <div class="search-bar w-search notification-list friend-requests">
            <div class="form-group with-button">
              <input
                class="form-control"
                placeholder="Pesquisar Versiculo"
                type="text" v-model="search"/>
            </div>
          </div>
        </div>
      </div>
      <!-- ... end  Tab panes -->
    </header>

    <!-- ... end Responsive Header -->
    <div class="header-spacer"></div>
  </div>
</template>

<script>
export default {
  name: "Header",
  data(){
    return {
      search: ""
    }
  },
  methods: {
    isInArray(value, array) {
      return array.indexOf(value) > -1;
    },
    get_query_params(news = {}, clear = false, exclude = []) {
      var params = {};
      var aux_new = news;
      if (clear == true) {
        params = {};
      } else {
        params = { ...this.$route.query };
      }

      if (Object.keys(aux_new).length > 0) {
        for (var key in aux_new) {
          params[key] = aux_new[key];
          
        }
      }

      for(var key in params){
        if(this.isInArray(key, exclude)){
            delete params[key];
          }
      }

      return params;
    },
  }
};
</script>
