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
    component: () => import('../views/ExperimenterView.vue'),
    children: [
      {
        path: '',
        name: 'experimenter-home',
        component: () => import('../views/UserView.vue')
      },
      {
        path: 'my-exp',
        name: 'my-experiment',
        component: () => import('../views/MyExpView.vue')
      }
    ]
  },
  {
    path: '/sup',
    component: () => import('../views/SupervisorView.vue'),
    children: [
      {
        path: '',
        name: 'supervisor-home',
        component: () => import('../views/UserView.vue')
      },
      {
        path: 'class',
        name: 'class-management',
        component: () => import('../views/ClassManagementView.vue')
      },
      {
        path: 'exp',
        name: 'experiment',
        component: () => import('../views/ExpView.vue'),
        // children: [
        //   {
        //     path: 'publish',
        //     name: 'publish-exp',
        //     component: () => import('../views/ExpPublishView.vue')
        //   },
        //   {
        //     path: 'watch',
        //     name: 'exp-watch',
        //     component: () => import('../views/ExpWatchView.vue')
        //   },
        //   {
        //     path: 'history',
        //     name: 'exp-history',
        //     component: () => import('../views/ExpHistoryView.vue')
        //   },
        // ]
      },
      {
        path: 'images',
        name: 'image-management',
        component: () => import('../views/ImageView.vue')
      },
      ],
  }
]

const router = new VueRouter({
  routes
})

export default router
