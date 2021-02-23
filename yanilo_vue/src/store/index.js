import Vue from 'vue'
import Vuex from 'vuex'


Vue.use(Vuex)

  export default new Vuex.Store({
  state: {
    cart_length: 0,
    gwc: 0,
  },
  mutations: {
    add_cart (state, cart_length) {
      state.cart_length = cart_length;

    }
  }
})



