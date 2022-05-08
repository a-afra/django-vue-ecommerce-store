<template>
  <nav class="breadcrumb" aria-label="breadcrumbs">
    <ul>
      <li><router-link to="/">Boutique</router-link></li>
      <li class="is-active"><a href="#" aria-current="page">Sign up</a></li>
    </ul>
  </nav>

  <div class="page-sign-up">
    <div class="columns is-centered">
      <div class="column is-4">

        <form @submit.prevent="submitForm">
          <div class="box has-background-grey-dark has-text-centered">
            <h1 class="title has-text-light">Sign up</h1>

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
              <label class="label has-text-light has-text-left">Email</label>
              <div class="control has-icons-left">
                <input type="text" class="input is-rounded is-medium" v-model="email">
                <span class="icon is-small is-left">
                  <i class="fas fa-envelope"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <label class="label has-text-light has-text-left">Password</label>
              <div class="control has-icons-left">
                <input type="password" class="input is-rounded is-medium" v-model="password">
                <span class="icon is-small is-left">
                  <i class="fas fa-lock"></i>
                </span>
              </div>
            </div>

            <div class="field">
              <label class="label has-text-light has-text-left">Confirm password</label>
              <div class="control has-icons-left">
                <input type="password" class="input is-rounded is-medium mb-5" v-model="password2">
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
                <button class="button is-success mt-4 is-rounded is-medium is-fullwidth">Sign up</button>
              </div>
            </div>

            <hr>

            <div class="has-text-light">
            Or <router-link class="has-text-success" to="/log-in">click here</router-link> to Log in!
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
  name: 'SignUpView',
  data() {
    return {
      username: '',
      email: '',
      password: '',
      password2: '',
      errors: []
    }
  },
  mounted() {
    document.title = 'Sign up | Boutique'
  },
  methods: {
    submitForm() {
      this.errors = []

      if (this.username === '') {
        this.errors.push('The username field is empty')
      }

      if (this.email === '') {
        this.errors.push('The email field is empty')
      }

      if (this.password === '') {
        this.errors.push('The password field is empty')
      }

      if (this.password !== this.password2) {
        this.errors.push('The passwords doesn\'t match')
      }

      if (!this.errors.length) {
        const formData = {
          username: this.username,
          email: this.email,
          password: this.password
        }

        axios
            .post("/api/v1/users/", formData)
            .then(response => {
              toast({
                message: 'Account created, please log in!',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
              })

              this.$router.push('/log-in')
            })
            .catch(error => {
              if (error.response) {
                for (const property in error.response.data) {
                  this.errors.push(`${property}: ${error.response.data[property]}`)
                }

                console.log(JSON.stringify(error.response.data))
              } else if (error.message) {
                this.errors.push('Something went wrong. Please try again')

                console.log(JSON.stringify(error))
              }
            })
      }
    }
  }
}
</script>