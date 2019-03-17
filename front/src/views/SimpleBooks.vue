<template>
  <div>
    <div class="row">
        <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">
          <div class="clients-grid">

            <div class="row sorting-container" id="clients-grid-1" data-layout="masonry">

 

              <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12 col-xs-12 sorting-item ecommerce natural">
                <div class="ui-block">
                  <article class="hentry post">

                    <h4>Antigo Testamento</h4>
                    <hr>
                    
                    <div class="row">
                        <div class="col-sm-4">
                            <p v-for="book in organized_books.old_1">{{ book.liv_nome }}</p> 
                        </div>
                        <div class="col-sm-4">
                            <p v-for="book in organized_books.old_2">{{ book.liv_nome }}</p> 
                        </div>
                        <div class="col-sm-4">
                            <p v-for="book in organized_books.old_3">{{ book.liv_nome }}</p> 
                        </div>
                    </div>

                  </article>
                </div>
              </div>

              <div class="col-xl-6 col-lg-6 col-md-12 col-sm-12 col-xs-12 sorting-item ecommerce natural">
                <div class="ui-block">
                  <article class="hentry post">
                    
                    <h4>Novo Testamento</h4>
                    <hr>
                    <div class="row">
                        <div class="col-sm-6">
                          <p v-for="book in organized_books.new_1">{{ book.liv_nome }}</p> 
                        </div>
                        <div class="col-sm-6">
                          <p v-for="book in organized_books.new_2">{{ book.liv_nome }}</p> 
                        </div>
                    </div>

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
    name: "SimpleBooks",
    data(){
      return{
        books: [],
        organized_books: {
          "old_1": [],
          "old_2": [],
          "old_3": [],
          "new_1": [],
          "new_2": [],
        },
      }
    },
    mounted(){
      this.get_books();
    },
    components: {
        
    },
    methods: {
      get_books(){
        this.$http.get('books').then(response => {

          // get body data
          this.books = response.body;
          this.organize_books();

        }, response => {
          // error callback
        });
      },
      organize_books(){
        for(var i = 0; i < this.books.length; i++){
          if(this.books[i].liv_tes == 1){
            if(this.organized_books.old_1.length < 13){
              this.organized_books.old_1.push(this.books[i])
            }else if(this.organized_books.old_2.length < 13){
              this.organized_books.old_2.push(this.books[i])
            }else{
              this.organized_books.old_3.push(this.books[i])
            }
          }else{
            if(this.organized_books.new_1.length < 14){
              this.organized_books.new_1.push(this.books[i])
            }else{
              this.organized_books.new_2.push(this.books[i])
            }
          }
        }
      }
    }
}
</script>

