<template>
  <div>
    <div class="row">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
        <div class="clients-grid">
          <ul class="cat-list-bg-style align-center sorting-menu">
            <li
              class="cat-list__item active"
              v-for="cap in capitulos"
              v-bind:key="cap.ver_capitulo"
            >
              <router-link
                :to="{
                  name: 'Versicle',
                  query: get_query_params({ capitulo: cap.ver_capitulo }, false, ['versiculo'])
                }"
                >{{ ("" + cap.ver_capitulo).padStart(2, "0") }}</router-link
              >
            </li>
          </ul>

          <div
            class="row sorting-container"
            id="clients-grid-1"
            data-layout="masonry"
          >
            <div
              class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-xs-12 sorting-item ecommerce natural"
              v-for="ver in versiculos"
              v-bind:key="ver.ver_id"
            >
              <div class="ui-block">
                <article class="hentry post">
                  <div class="post__author author vcard inline-items">
                    <div class="author-date">
                      <router-link
                        :to="{
                          name: 'Versicle',
                          query: get_query_params(
                            { livro_id: ver.ver_liv.liv_id },
                            false
                          )
                        }"
                        >{{ ver.ver_liv.liv_nome }}</router-link
                      >&nbsp;
                      <router-link
                        :to="{
                          name: 'Versicle',
                          query: get_query_params(
                            {
                              livro_id: ver.ver_liv.liv_id,
                              capitulo: ver.ver_capitulo
                            },
                            false
                          )
                        }"
                        >{{ ver.ver_capitulo }}</router-link
                      >&nbsp;:&nbsp;
                      <router-link
                        :to="{
                          name: 'Versicle',
                          query: get_query_params(
                            {
                              livro_id: ver.ver_liv.liv_id,
                              capitulo: ver.ver_capitulo,
                              versiculo: ver.ver_versiculo
                            },
                            false
                          )
                        }"
                        >{{ ver.ver_versiculo }}</router-link
                      >
                    </div>

                    <div class="more">
                      <svg class="olymp-three-dots-icon">
                        <use
                          xlink:href="icons/icons.svg#olymp-three-dots-icon"
                        ></use>
                      </svg>
                      <ul class="more-dropdown">
                        <li
                          v-for="versao in versoes"
                          v-bind:key="versao.vrs_id"
                        >
                          <router-link
                            :to="{
                              name: 'Versicle',
                              query: get_query_params(
                                { versao_id: versao.vrs_id },
                                false
                              )
                            }"
                            >{{ versao.vrs_nome }}</router-link
                          >
                        </li>
                      </ul>
                    </div>
                  </div>

                  <p>{{ ver.ver_texto }}</p>

                  <div class="post-additional-info inline-items">
                    <div class="names-people-likes">
                      {{ ver.ver_vrs.vrs_nome }}
                    </div>

                    <!-- <div class="comments-shared">
                        <a href="#" class="post-add-icon inline-items">
                          <svg class="olymp-speech-balloon-icon"><use xlink:href="icons/icons.svg#olymp-speech-balloon-icon"></use></svg>
                          <span>17</span>
                        </a>

                        <a href="#" class="post-add-icon inline-items">
                          <svg class="olymp-share-icon"><use xlink:href="icons/icons.svg#olymp-share-icon"></use></svg>
                          <span>24</span>
                        </a>
                    </div>-->
                  </div>

                  <!-- <div class="control-block-button post-control-button">
                      <a href="#" class="btn btn-control featured-post">
                        <svg class="olymp-trophy-icon">
                          <use xlink:href="icons/icons.svg#olymp-trophy-icon"></use>
                        </svg>
                      </a>
                      
                      <a href="#" class="btn btn-control">
                        <svg class="olymp-like-post-icon">
                          <use xlink:href="icons/icons.svg#olymp-like-post-icon"></use>
                        </svg>
                      </a>
                      
                      <a href="#" class="btn btn-control">
                        <svg class="olymp-comments-post-icon">
                          <use xlink:href="icons/icons.svg#olymp-comments-post-icon"></use>
                        </svg>
                      </a>
                      
                      <a href="#" class="btn btn-control">
                        <svg class="olymp-share-icon">
                          <use xlink:href="icons/icons.svg#olymp-share-icon"></use>
                        </svg>
                      </a>
                  </div>-->
                </article>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Versicle",
  data() {
    return {
      versiculos: {},
      capitulos: [],
      versoes: []
    };
  },
  components: {},
  mounted() {
    this.get_versoes();
    this.get_versicles();
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
    get_cap_from_book() {
      var params = {};

      params["livro_id"] = 1;
      params["versao_id"] = 1;

      if (
        this.$route.query.livro_id != undefined &&
        this.$route.query.livro_id != null
      ) {
        params["livro_id"] = this.$route.query.livro_id;
      }

      if (
        this.$route.query.versao_id != undefined &&
        this.$route.query.versao_id != null
      ) {
        params["versao_id"] = this.$route.query.versao_id;
      }

      this.$http.get("capitulos_livro", { params: params }).then(
        response => {
          // get body data
          this.capitulos = response.body;
        },
        () => {
          // error callback
        }
      );
    },
    get_cap_params(capitulo) {
      var params = {};

      // Deffault
      params["livro_id"] = 1;
      params["versao_id"] = 1;
      params["capitulo"] = capitulo;

      if (
        this.$route.query.livro_id != undefined &&
        this.$route.query.livro_id != null
      ) {
        params["livro_id"] = this.$route.query.livro_id;
      }

      if (
        this.$route.query.versao_id != undefined &&
        this.$route.query.versao_id != null
      ) {
        params["versao_id"] = this.$route.query.versao_id;
      }

      return params;
    },
    get_versoes() {
      this.$http.get("get_versoes").then(
        response => {
          // get body data
          this.versoes = response.body;
        },
        () => {
          // error callback
        }
      );
    },
    get_versicles() {
      var params = {};

      // Deffault
      params["livro_id"] = 1;
      params["versao_id"] = 1;
      params["capitulo"] = 1;
      // params['vesiculo'] = 1

      if (
        this.$route.query.livro_id != undefined &&
        this.$route.query.livro_id != null
      ) {
        params["livro_id"] = this.$route.query.livro_id;
      }

      if (
        this.$route.query.versao_id != undefined &&
        this.$route.query.versao_id != null
      ) {
        params["versao_id"] = this.$route.query.versao_id;
      }

      if (
        this.$route.query.versiculo != undefined &&
        this.$route.query.versiculo != null
      ) {
        params["versiculo"] = this.$route.query.versiculo;
      }

      if (
        this.$route.query.capitulo != undefined &&
        this.$route.query.capitulo != null
      ) {
        params["capitulo"] = this.$route.query.capitulo;
      }

      this.$http.get("versiculos", { params: params }).then(
        response => {
          // get body data
          this.get_cap_from_book();
          this.versiculos = response.body.results;
        },
        () => {
          // error callback
        }
      );
    }
  }
};
</script>
