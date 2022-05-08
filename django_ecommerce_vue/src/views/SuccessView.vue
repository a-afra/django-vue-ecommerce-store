<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Boutique</router-link></li>
      <li><router-link to="/cart">Cart</router-link></li>
      <li><router-link to="/cart/checkout">Checkout</router-link></li>
      <li class="is-active"><a href="#" aria-current="page">Succes</a></li>
    </ul>
  </nav>

  <div class="page-success">
    <div class="columns is-multiline">
      <div class="column is-12 is-primary">
        <h1 class="title has-text-success">Your order has been completed!</h1>

        <h2 class="subtitle my-4">Thank you for shopping with us! Enjoy!</h2>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'SuccessView',
  mounted() {
    document.title = 'Success | Djackets'
  },
}
</script>