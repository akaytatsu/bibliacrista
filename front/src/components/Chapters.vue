<template>
    <div>
        <ul class="cat-list-bg-style align-center sorting-menu" v-if="livro_id > 0">
            <li class="cat-list__item active" v-for="cap in capitulos" v-bind:key="cap.ver_capitulo">
              <router-link
                :to="{
                  name: 'Versicle',
                  query: get_query_params({ capitulo: cap.ver_capitulo }, false, ['versiculo'])
                }">
                  {{ ("" + cap.ver_capitulo).padStart(2, "0") }}
                </router-link>
            </li>
          </ul>
    </div>
</template>

<script>
export default {
    name: "Chapters",
    data(){
        return{
            livro_id: 0,
            capitulos: [],
        }
    },
    mounted(){
        this.get_cap_from_book();
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
            var book_id = this.$route.query;

            params["versao_id"] = 5;

            if (
                this.$route.query.versao_id != undefined &&
                this.$route.query.versao_id != null
            ) {
                params["versao_id"] = this.$route.query.versao_id;
            }

            if (
                this.$route.query.livro_id != undefined &&
                this.$route.query.livro_id != null
            ) {
                this.livro_id = this.$route.query.livro_id;

                params["livro_id"] = this.livro_id;

                this.$http.get("capitulos_livro", { params: params }).then(
                    response => {
                    // get body data
                    this.capitulos = response.body;
                    },
                    () => {
                    // error callback
                    }
                );
            }            
        },
    }
}
</script>

