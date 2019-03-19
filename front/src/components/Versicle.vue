<template>
  <div>
    <div class="row">
      <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
        <div class="clients-grid">
          


          <div
            class="row sorting-container"
            id="clients-grid-1"
            data-layout="masonry"
          >
            <div
              class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-xs-12 sorting-item ecommerce natural"
              v-for="ver in versicles"
              v-bind:key="ver.id"
            >
              <div class="ui-block">
                <article class="hentry post">
                  <div class="post__author author vcard inline-items">
                    <div class="author-date">
                      <router-link
                        :to="{
                          name: 'Versicle',
                          query: get_query_params(
                            { book_id: ver.book.id },
                            false
                          )
                        }"
                        >{{ ver.book.name }}</router-link
                      >&nbsp;
                      <router-link
                        :to="{
                          name: 'Versicle',
                          query: get_query_params(
                            {
                              book_id: ver.book.id,
                              chapter: ver.chapter
                            },
                            false
                          )
                        }"
                        >{{ ver.chapter }}</router-link
                      >&nbsp;:&nbsp;
                      <router-link
                        :to="{
                          name: 'Versicle',
                          query: get_query_params(
                            {
                              book_id: ver.book.id,
                              chapter: ver.chapter,
                              versicle: ver.versicle
                            },
                            false
                          )
                        }"
                        >{{ ver.versicle }}</router-link
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
                          v-for="version in versions"
                          v-bind:key="version.id"
                        >
                          <router-link
                            :to="{
                              name: 'Versicle',
                              query: get_query_params(
                                { version_id: version.id },
                                false
                              )
                            }"
                            >{{ version.name }}</router-link
                          >
                        </li>
                      </ul>
                    </div>
                  </div>

                  <p>{{ ver.text }}</p>

                  <div class="post-additional-info inline-items">
                    <div class="names-people-likes">
                      {{ ver.version.name }}
                    </div>

                    <div class="comments-shared">
                        <a href="#" class="post-add-icon inline-items" data-toggle="modal" data-target="#dictionary_modal"
                          v-on:click="get_dictionary(ver.dictionary)">
                          <svg class="olymp-speech-balloon-icon"><use xlink:href="icons/icons.svg#olymp-speech-balloon-icon"></use></svg>
                          <span>{{ ver.dictionary.length }}</span>
                        </a>

                        <!-- <a href="#" class="post-add-icon inline-items">
                          <svg class="olymp-share-icon"><use xlink:href="icons/icons.svg#olymp-share-icon"></use></svg>
                          <span>24</span>
                        </a> -->
                    </div>
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

    <!-- Window-popup Edit Widget Profile -->
    <div class="modal fade" id="dictionary_modal">
      <div class="modal-dialog ui-block window-popup edit-widget edit-widget-profile">
        <a href="#" class="close icon-close" data-dismiss="modal" aria-label="Close">
          <svg class="olymp-close-icon"><use xlink:href="icons/icons.svg#olymp-close-icon"></use></svg>
        </a>

        <div class="ui-block-title">
          <h6 class="title">Dicionario</h6>
        </div>

        <div v-for="dic in dictionary" v-bind:key="dic.id">
          
          <div class="ui-block-title ui-block-title">
            <h6 class="title">{{ dic.palavra }}</h6>
          </div>

          
          <div class="ui-block-content">
            <p>{{ dic.significado }}</p>
          </div>

        </div>

      </div>
    </div>

    <!-- ... end Window-popup Edit Widget Profile -->

  </div>
</template>

<script>
export default {
  name: "Versicle",
  data() {
    return {
      versicles: {},
      versions: [],
      dictionary: [],
    };
  },
  components: {},
  mounted() {
    this.get_versions();
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
    get_dictionary(dict){
      this.$http.post("get_dictionary/", dict, {header: {'Content-Type': 'application/json'}}).then(
        response => {
          this.dictionary = response.body;
        },
        () => {
          // error callback
        }
      );
    },
    get_versions() {
      this.$http.get("get_versions").then(
        response => {
          // get body data
          this.versions = response.body;
        },
        () => {
          // error callback
        }
      );
    },
    get_versicles() {
      var params = {};

      // Deffault
      params["book_id"] = 1;
      params["version_id"] = 1;
      params["chapter"] = 1;
      // params['vesiculo'] = 1

      if (
        this.$route.query.id != undefined &&
        this.$route.query.id != null
      ) {
        params["book_id"] = this.$route.query.id;
      }

      if (
        this.$route.query.version_id != undefined &&
        this.$route.query.version_id != null
      ) {
        params["version_id"] = this.$route.query.version_id;
      }

      if (
        this.$route.query.versicle != undefined &&
        this.$route.query.versicle != null
      ) {
        params["versicle"] = this.$route.query.versicle;
      }

      if (
        this.$route.query.chapter != undefined &&
        this.$route.query.chapter != null
      ) {
        params["chapter"] = this.$route.query.chapter;
      }

      this.$http.get("versicles", { params: params }).then(
        response => {
          // get body data
          this.versicles = response.body.results;
        },
        () => {
          // error callback
        }
      );
    }
  }
};
</script>
