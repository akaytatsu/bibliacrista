<template>
  <div>
    <div class="row">
        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
          <div class="clients-grid">
            <ul class="cat-list-bg-style align-center sorting-menu">
              <li class="cat-list__item active" v-for="cap in capitulos" v-bind:key="cap">
                <router-link :to="{ name: 'Versicle', query: get_cap_params(cap) }">
                          {{(""+cap).padStart(2, '0')}}
                        </router-link>
              </li>
            </ul>

            <div class="row sorting-container" id="clients-grid-1" data-layout="masonry">


              <div class="col-xl-12 col-lg-12 col-md-12 col-sm-12 col-xs-12 sorting-item ecommerce natural"
                v-for="ver in versiculos" v-bind:key="ver.ver_id">
                <div class="ui-block">
                  <article class="hentry post">
                    <div class="post__author author vcard inline-items">
                      

                      <div class="author-date">
                        <router-link :to="{ name: 'Versicle', query: { livro_id: ver.ver_liv.liv_id } }">
                          {{ ver.ver_liv.liv_nome }}
                        </router-link>&nbsp;
                        <router-link :to="{ name: 'Versicle', query: { livro_id: ver.ver_liv.liv_id, capitulo: ver.ver_capitulo } }">
                          {{ ver.ver_capitulo }}
                        </router-link>&nbsp;:&nbsp;
                        <router-link :to="{ name: 'Versicle', query: { livro_id: ver.ver_liv.liv_id, capitulo: ver.ver_capitulo, versiculo: ver.ver_versiculo } }">
                          {{ ver.ver_versiculo }}
                        </router-link>
                      </div>

                      <!-- <div class="more">
                        <svg class="olymp-three-dots-icon">
                          <use xlink:href="icons/icons.svg#olymp-three-dots-icon"></use>
                        </svg>
                        <ul class="more-dropdown">
                          <li>
                            <a href="#">Edit Post</a>
                          </li>
                          <li>
                            <a href="#">Delete Post</a>
                          </li>
                          <li>
                            <a href="#">Turn Off Notifications</a>
                          </li>
                          <li>
                            <a href="#">Select as Featured</a>
                          </li>
                        </ul>
                      </div> -->
                    </div>

                    <p>
                      {{ ver.ver_texto }}
                    </p>

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
                    </div> -->
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
  data(){
    return {
      versiculos: {},
      capitulos: 0,
    }
  },
  components: {},
  mounted(){
    this.get_versicles();
  },
  methods: {
    get_cap_from_book(){

      var params = {}

      params['livro_id'] = 1
      params['versao_id'] = 1

      if(this.$route.query.livro_id != undefined && this.$route.query.livro_id != null){
        params['livro_id'] = this.$route.query.livro_id;
      }

      if(this.$route.query.versao_id != undefined && this.$route.query.versao_id != null){
        params['versao_id'] = this.$route.query.versao_id;
      }

      this.$http.get('capitulos_livro', { params: params}).then(response => {

        // get body data
        this.capitulos = response.body.total;

      }, response => {
        // error callback
      });
    },
    get_cap_params(capitulo){
      var params = {}

      // Deffault
      params['livro_id'] = 1
      params['versao_id'] = 1
      params['capitulo'] = capitulo

      if(this.$route.query.livro_id != undefined && this.$route.query.livro_id != null){
        params['livro_id'] = this.$route.query.livro_id;
      }

      if(this.$route.query.versao_id != undefined && this.$route.query.versao_id != null){
        params['versao_id'] = this.$route.query.versao_id;
      }

      return params;
    },
    get_versicles(){

      var params = {}

      // Deffault
      params['livro_id'] = 1
      params['versao_id'] = 1
      params['capitulo'] = 1
      // params['vesiculo'] = 1

      if(this.$route.query.livro_id != undefined && this.$route.query.livro_id != null){
        params['livro_id'] = this.$route.query.livro_id;
      }

      if(this.$route.query.versao_id != undefined && this.$route.query.versao_id != null){
        params['versao_id'] = this.$route.query.versao_id;
      }

      if(this.$route.query.versiculo != undefined && this.$route.query.versiculo != null){
        params['versiculo'] = this.$route.query.versiculo;
      }

      if(this.$route.query.capitulo != undefined && this.$route.query.capitulo != null){
        params['capitulo'] = this.$route.query.capitulo;
      }
      
      this.$http.get('versiculos', { params: params}).then(response => {

        // get body data
        this.get_cap_from_book();
        this.versiculos = response.body.results;

      }, response => {
        // error callback
      });
    }
  }
};
</script>

