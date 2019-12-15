import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    but:false,            // on/off кнопки включения   (true/false)
    WHswitch1: false,       // значение слайдера on/off (true/false)
    WHswitch2: false,
  },
  getters : {},
  mutations: {
    increment(state) {
        // изменяем состояние
        state.WHswitch1;
  }
},
  actions : {}  
})