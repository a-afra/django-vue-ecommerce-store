<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Boutique</router-link></li>
      <li class="is-active"><a href="#" aria-current="page">Log in</a></li>
    </ul>
  </nav>

  <div class="page-log-in">
    <div class="columns is-centered">
      <div class="column is-4">

        <form @submit.prevent="submitForm">
          <div class="box has-background-grey-dark has-text-centered">
            <h1 class="title has-text-light">Log In</h1>

            <div class="field">
              <label class="label has-text-light has-text-left">Username</label>
              <div class="control has-icons-left">
                <input type="text" class="input is-rounded is-medium" v-model="username">
                <span class="icon is-small is-left">
                  <i class="fas fa-user"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <label class="label has-text-light has-text-left">Password</label>
              <div class="control has-icons-left">
                <input type="password" class="input is-rounded is-medium mb-5" v-model="password">
                <span class="icon is-small is-left">
                  <i class="fas fa-lock"></i>
                </span>
              </div>
            </div>

            <div class="notification is-danger" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>

            <div class="field">
              <div class="control">
                <button class="button is-success mt-4 is-medium is-rounded is-fullwidth">Log In</button>
              </div>
            </div>

            <hr>

            <div class="has-text-light">
              Or <router-link class="has-text-success" to="/sign-up">click here</router-link> to Sign Up!
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
  name: 'LogInView',
  data() {
    return {
      username: '',
      password: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Log in | Boutique'
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = ""
      localStorage.removeItem("token")
      const formData = {
        username: this.username,
        password: this.password
      }
      await axios
          .post("/api/v1/token/login/", formData)
          .then(response => {
            const token = response.data.auth_token
            this.$store.commit('setToken', token)

            axios.defaults.headers.common["Authorization"] = "Token " + token
            localStorage.setItem("token", token)
            const toPath = this.$route.query.to || '/cart'
            this.$router.push(toPath)
          })
          .catch(error => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${property}: ${error.response.data[property]}`)
              }
            } else {
              this.errors.push('Something went wrong. Please try again')

              console.log(JSON.stringify(error))
            }
          })
    }
  }
}
</script>