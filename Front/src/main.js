import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from "../router";
// import VueNativeSock from "vue-native-websocket";
import Socket from "./plugins/socket";
import { store } from "./plugins/store"; //добавил сторе

Vue.config.productionTip = false

//Vue.use(Socket, { url:'ws://40f3e784.ngrok.io' });
Vue.use(Socket, { url:'ws://7e21a1bc.ngrok.io' });

new Vue({
  vuetify,
  store, //добавил сторе
  router,
  render: h => h(App)
}).$mount('#app')


