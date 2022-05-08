<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Boutique</router-link></li>
      <li class="is-active"><a href="#" aria-current="page">My account</a></li>
    </ul>
  </nav>

  <div class="my-account-page columns is-multiline is-centered">
    <div class="column is-three-quarters">
      <div class="my-account card ">
        <header class="card-header">
          <p class="card-header-title">My Account</p>
          <button @click="logout()" class="card-header-icon button is-danger mt-1 mr-1">Log out</button>
        </header>

        <div class="card-content columns is-multiline">
          <div class="column">
            <h2 class="subtitle">My information</h2>
            <div class="columns is is-multiline box">
              <div class="column">
                <h3 class="has-text-grey">Username</h3>
                <h3><strong>{{ user.username }}</strong></h3>
              </div>

              <div class="column">
                <h3 class="has-text-grey">Email</h3>
                <h3><strong>{{ user.email }}</strong></h3>
              </div>
            </div>
          </div>
        </div>

        <hr>

        <div class="card-content columns is-multiline">
          <div class="column">
            <h2 class="subtitle">My orders</h2>

            <OrderSummary
              v-for="order in orders"
              v-bind:key="order.id"
              v-bind:order="order" />

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import OrderSummary from '@/components/OrderSummary.vue'

export default {
  name: 'MyAccountView',
  components: {
    OrderSummary
  },
  data() {
    return {
      orders: [],
      user: {}
    }
  },
  mounted() {
    document.title = 'My account | Boutique'

    this.getMyOrders()
    this.getUserInfo()
  },
  methods: {
    logout() {
      axios.defaults.headers.common["Authorization"] = ""

      localStorage.removeItem("token")
      localStorage.removeItem("username")
      localStorage.removeItem("userid")

      this.$store.commit('removeToken')

      this.$router.push('/')
    },
    async getMyOrders() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get('/api/v1/orders/')
          .then(response => {
            this.orders = response.data
          })
          .catch(error => {
            console.log(error)
          })

      this.$store.commit('setIsLoading', false)
    },
    async getUserInfo() {
      this.$store.commit('setIsLoading', true)

      await axios
          .get('/api/v1/get-user')
          .then(response => {
            this.user = response.data
          })
          .catch(error => {
            console.log(error)
          })

      this.$store.commit('setIsLoading', false)
    }
  }
}
</script>