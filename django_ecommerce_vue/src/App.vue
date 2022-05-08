<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item">
          <img src="../public/boutique-logo.png" type="image" alt="logo">
          <strong style="padding-left: 5px">  BOUTIQUE</strong>
        </router-link>

        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">


          <div class="navbar-item">
            <form method="get" action="/search">
              <div class="field has-addons">
                <div class="control has-icons-left">
                  <input type="text" class="input" placeholder="Search products..." name="query">
                  <span class="icon is-left">
                    <i class="fas fa-search"></i>
                  </span>
                </div>

              </div>
            </form>
          </div>

          <div class="navbar-item has-dropdown is-hoverable">
            <a class="navbar-link">
              Categories
            </a>
            <div class="navbar-dropdown">
              <router-link to="/men" class="navbar-item">Men</router-link>
              <router-link to="/women" class="navbar-item">Women</router-link>
              <hr class="navbar-divider">
              <router-link to="/about-me" class="navbar-item">About me</router-link>
            </div>
          </div>

        </div>

        <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">

            <div class="navbar-item">
              <router-link to="/cart" class="button is-info">
                <span>Cart ({{ cartTotalLength }})</span>
                <span class="icon"><i class="fas fa-shopping-cart"></i></span>
              </router-link>
            </div>

            <template v-if="$store.state.isAuthenticated">
              <router-link to="/my-account" class="button is-light">My account</router-link>
            </template>

            <template v-else>
              <router-link to="/log-in" class="button is-primary">SignUp / LogIn</router-link>
            </template>

          </div>
        </div>
      </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading}">
      <div class="lds-dual-ring"></div>
    </div>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered has-text-grey">Designed for practice purpose</p>
      <p class="has-text-centered has-text-grey">Afra © 2022</p>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export  default {
  data() {
    return {
      showMobileMenu: false,
      cart: {
        items: []
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')

    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed: {
    cartTotalLength() {
      let totalLength = 0

      for (let i = 0; i < this.cart.items.length; i++) {
        totalLength += this.cart.items[i].quantity
      }

      return totalLength
    }
  }
}
</script>

<style lang="scss">
@import '../node_modules/bulma';

.lds-dual-ring {
  display: inline-block;
  width: 80px;
  height: 80px;
}
.lds-dual-ring:after {
  content: " ";
  display: block;
  width: 64px;
  height: 64px;
  margin: 8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}
@keyframes lds-dual-ring {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.is-loading-bar {
  height: 0;
  overflow: hidden;
  -webkit-transition: all 0.3s;
  transition: all 0.3s;
  &.is-loading {
    height: 80px;
  }
}
</style>
