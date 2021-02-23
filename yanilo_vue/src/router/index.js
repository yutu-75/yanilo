import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/Login'
import Register from "@/components/Register";
import Course from "@/components/Course"
import Detail from "@/components/Detail";
import Cart from "@/components/Cart";
import Order from "@/components/Order";
import Player from "@/components/Player";
import Myorder from "@/components/Myorder";
import Book from "@/components/Book";
Vue.use(Router)

export default new Router({
  mode:'history',
  routes: [
    {
      path: '/',
      //name: 'heme',
      component: Home
    },
        {
      path: '/home',
      //name: 'heme',
      component: Home
    },
        {
      path: '/user/login',
      //name: 'heme',
      component: Login
    },
        {
      path: '/register',
      //name: 'heme',
      component: Register
    },
        {
      path: '/courses',
      //name: 'heme',
      component: Course

    },
    {
      path: '/courses/detail/:id',//courses/detail/1/
      //name: 'heme',
      component: Detail
    },
    {
      path: '/cart',//courses/detail/1/
      //name: 'heme',
      component: Cart
    },
    {
      path: '/order',//courses/detail/1/
      //name: 'heme',
      component: Order
    },
    {
      path: '/myorder',//courses/detail/1/
      //name: 'heme',
      component: Myorder
    },
    {
      path: '/polyv/player/:vid',//courses/detail/1/
      //path: '/polyv/player/:vid',//courses/detail/1/
      //name: 'heme',
      component: Player
    },
        {
      path: '/book',
      component: Book
    },

  ]
})
