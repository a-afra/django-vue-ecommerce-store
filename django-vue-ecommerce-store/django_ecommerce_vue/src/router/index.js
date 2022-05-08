import { createRouter, createWebHistory } from 'vue-router'

import store from "../store";
import HomeView from '../views/HomeView.vue'
import ProductView from "../views/ProductView";
import CategoryView from "../views/CategoryView";
import SearchView from "../views/SearchView";
import CartView from "../views/CartView";
import SignUpView from "../views/SignUpView";
import LogInView from "../views/LogInView";
import MyAccountView from "../views/MyAccountView";
import CheckoutView from "../views/CheckoutView";
import SuccessView from "../views/SuccessView";
import AboutMeView from "../views/AboutMeView";

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/:category_slug/:product_slug',
    name: 'Product',
    component: ProductView
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: CategoryView
  },
  {
    path: '/search',
    name: 'Search',
    component: SearchView
  },
  {
    path: '/cart',
    name: 'Cart',
    component: CartView
  },
  {
    path: '/cart/success',
    name: 'Success',
    component: SuccessView
  },
  {
    path: '/cart/checkout',
    name: 'Checkout',
    component: CheckoutView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUpView
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogInView
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccountView,
    meta: {
      requireLogin: true
    }
  },
  {
    path: '/about-me',
    name: 'AboutMe',
    component: AboutMeView,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
