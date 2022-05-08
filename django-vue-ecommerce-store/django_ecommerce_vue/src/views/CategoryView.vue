<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Boutique</router-link></li>
      <li><a href="#">Categories</a></li>
      <li class="is-active"><a href="#" aria-current="page">{{ category.name }}</a></li>
    </ul>
  </nav>

  <div class="page-category">
    <div class="column is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ category.name }}</h2>
      </div>

      <div class="columns is-multiline">
        <ProductBox
        v-for="product in category.products"
        v-bind:key="product.id"
        v-bind:product="product" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

import ProductBox from "@/components/ProductBox";

export default {
  name: "CategoryView",
  components: {
    ProductBox
  },
  data() {
    return {
      category: {
        products: []
      }
    }
  },
  watch: {
    $route(to, from) {
      if (to.name === 'Category') {
        this.getCategory()
      }
    }
  },
  mounted() {
        this.getCategory()
  },
  methods: {
    async getCategory() {
      const categorySlug = this.$route.params.category_slug

      this.$store.commit('setIsLoading', true)

      axios
          .get(`/api/v1/products/${categorySlug}/`)
          .then(response => {
            this.category = response.data

            document.title = this.category.name + ' | Boutique'
          })
          .catch(error => {
            console.log(error)

            toast({
              message: 'Something went wrong. Please try again.',
              type: 'is-danger',
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: 'bottom-right',
            })
          })

      this.$store.commit('setIsLoading', false)
    }
  },
}
</script>

<style scoped>

</style>