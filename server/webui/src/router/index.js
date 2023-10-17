import Vue from 'vue'
import VueRouter from 'vue-router'
// import HomeView from '../views/HomeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'login',
    component: () => import('../views/LoginView.vue')
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // },
  {
    path: '/exp',
    name: 'experimenter',
    component: () => import('../views/ExperimenterView.vue')
  },
  {
    path: '/sup',
    name: 'supervisor',
    component: () => import('../views/SupervisorView.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
