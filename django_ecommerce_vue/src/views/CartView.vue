<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Boutique</router-link></li>
      <li class="is-active"><a href="#" aria-current="page">Cart</a></li>
    </ul>
  </nav>

  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Cart</h1>
      </div>

      <div class="column is-12 box">
        <table class="table is-fullwidth is-hoverable" v-if="cartTotalLength">
          <thead>
          <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Total</th>
            <th></th>
          </tr>
          </thead>

          <tbody>
          <CartItem
              v-for="item in cart.items"
              v-bind:key="item.product.id"
              v-bind:initialItem="item"
              v-on:removeFromCart="removeFromCart"/>
          </tbody>
        </table>

        <p v-else>You don't have any products in your cart...</p>
      </div>

      <div className="column is-12 box">
        <h2 className="subtitle">Summary</h2>

        <strong>${{ cartTotalPrice.toFixed(2) }}</strong>, {{ cartTotalLength }} items

        <hr>

        <router-link to="/cart/checkout" className="button is-info">Proceed to checkout</router-link>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'

export default {
  name: 'CartView',
  components: {
    CartItem
  },
  data() {
    return {
      cart: {
        items: []
      }
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
    document.title = 'Cart | Boutique'
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(i => i.product.id !== item.product.id)
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