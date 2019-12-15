import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    wheel: null,
    scene: null,
    radio: null,
    light: null,
    smartGr: null
  },
  getters: {
    WHEEL: state => {
      return state.wheel;
    },
    RADIO: state => {
      return state.radio;
    },
    SCENE: state => {
      return state.scene;
    },
    SMARTGR: state => {
      return state.smartGr;
    },
    LIGHT: state => {
      return state.light;
    }
  },
  mutations: {
    SET_WHEEL: (state, payload) => {
      console.log(payload);
      state.wheel = payload;
    },
    SET_SCENE: (state, payload) => {
      state.scene = payload;
    },
    SET_RADIO: (state, payload) => {
      state.radio = payload;
    },
    SET_LIGHT: (state, payload) => {
      state.light = payload;
    },
    SET_SMARTGR: (state, payload) => {
      state.smartGr = payload;
    }
  },
  actions: {}
});