<template>
    <div>
        <ul class="cat-list-bg-style align-center sorting-menu" v-if="book_id > 0">
            <li class="cat-list__item active" v-for="cap in chapters" v-bind:key="cap.chapter">
              <router-link
                :to="{
                  name: 'Versicle',
                  query: get_query_params({ chapter: cap.chapter }, false, ['versicle'])
                }">
                  {{ ("" + cap.chapter).padStart(2, "0") }}
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
            book_id: 0,
            chapters: [],
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

            params["version_id"] = 1;

            if (this.$route.query.version_id != undefined && this.$route.query.version_id != null ) {
                params["version_id"] = this.$route.query.version_id;
            }

            if (this.$route.query.book_id != undefined && this.$route.query.book_id != null) {
                this.book_id = this.$route.query.book_id;

                params["book_id"] = this.book_id;

                this.$http.get("book_chapters", { params: params }).then(
                    response => {
                    // get body data
                    this.chapters = response.body;
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

