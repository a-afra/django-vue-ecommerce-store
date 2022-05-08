<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Boutique</router-link></li>
      <li><router-link to="/cart">Cart</router-link></li>
      <li class="is-active"><a href="#" aria-current="page">Checkout</a></li>
    </ul>
  </nav>

  <div class="page-checkout">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title mb-4">Checkout</h1>
      </div>
    </div>
  </div>

  <div class="column is-12 box">
    <table class="table is-fullwidth">
      <thead>
      <tr>
        <th>Product</th>
        <th>Price</th>
        <th>Quantity</th>
        <th>Total</th>
      </tr>
      </thead>

      <tbody>
      <tr
          v-for="item in cart.items"
          v-bind:key="item.product.id"
      >
        <td>{{ item.product.name }}</td>
        <td>${{ item.product.price }}</td>
        <td>{{ item.quantity }}</td>
        <td>${{ getItemTotal(item).toFixed(2) }}</td>
      </tr>
      </tbody>

      <tfoot>
      <tr>
        <td colspan="2">Total</td>
        <td>{{ cartTotalLength }}</td>
        <td>${{ cartTotalPrice.toFixed(2)}}</td>
      </tr>
      </tfoot>
    </table>
  </div>

  <div class="column is-12 box">
    <h2 class="subtitle">Shipping details</h2>

    <p class="has-text-grey mb-4">* All fields are required.</p>

    <div class="columns is-multiline">
      <div class="column">
        <div class="field">
          <label>First name*</label>
            <input type="text" class="input mt-2" v-model="first_name">
        </div>

        <div class="field">
          <label>Last name*</label>
          <div class="control">
            <input type="text" class="input mt-2" v-model="last_name">
          </div>
        </div>

        <div class="field">
          <label>E-mail*</label>
          <div class="control">
            <input type="email" class="input mt-2" v-model="email">
          </div>
        </div>
      </div>

      <div class="column">
        <div class="field">
          <label>Address*</label>
          <div class="control">
            <input type="text" class="input mt-2" v-model="address">
          </div>
        </div>

        <div class="field">
          <label>Zip code*</label>
          <div class="control">
            <input type="text" class="input mt-2" v-model="zipcode">
          </div>
        </div>

        <div class="field">
          <label>Phone*</label>
          <div class="control">
            <input type="number" class="input mt-2" v-model="phone">
          </div>
        </div>
      </div>
    </div>

    <div class="notification is-danger mt-4" v-if="errors.length">
        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
      </div>

      <div class="mb-4"></div>
      <template v-if="cartTotalLength">
        <button class="button is-info" @click="submitForm">Proceed to payment</button>
      </template>
  </div>

</template>

<script>
import axios from "axios";

export default {
  name: "CheckoutView",
  data() {
    return {
      cart: {
        items: []
      },
      card: {},
      first_name: '',
      last_name: '',
      email:'',
      phone: '',
      address: '',
      zipcode: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Checkout | Boutique'

    this.cart = this.$store.state.cart
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.product.price
    },
    submitForm() {
      this.errors = []
      if (this.first_name === '') {
        this.errors.push('The first name field is empty!')
      }
      if (this.last_name === '') {
        this.errors.push('The last name field is empty!')
      }
      if (this.email === '') {
        this.errors.push('The email field is empty!')
      }
      if (this.phone === '') {
        this.errors.push('The phone field is empty!')
      }
      if (this.address === '') {
        this.errors.push('The address field is empty!')
      }
      if (this.zipcode === '') {
        this.errors.push('The zip code field is empty!')
      }

      this.$store.commit('setIsLoading', true)

      const items = []

        for (let i = 0; i < this.cart.items.length; i++) {
          const item = this.cart.items[i]
          const obj = {
            product: item.product.id,
            quantity: item.quantity,
            price: item.product.price * item.quantity
          }

          items.push(obj)
        }

        const data = {
          'first_name': this.first_name,
          'last_name': this.last_name,
          'email': this.email,
          'address': this.address,
          'zipcode': this.zipcode,
          'phone': this.phone,
          'items': items,
        }

        axios
            .post('/api/v1/checkout/', data)
            .then(response => {
              this.$store.commit('clearCart')
              this.$router.push('/cart/success')
            })
            .catch(error => {
              this.errors.push('Something went wrong.')

              console.log(error)
            })

        this.$store.commit('setIsLoading', false)
    }
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.quantity
      }, 0)
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, curVal) => {
        return acc += curVal.product.price * curVal.quantity
      }, 0)
    },
  }
}
</script>

<style scoped>

</style>