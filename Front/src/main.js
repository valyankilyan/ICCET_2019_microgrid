import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify';
import router from "../router";
// import VueNativeSock from "vue-native-websocket";
import Socket from "./plugins/socket";

Vue.config.productionTip = false

Vue.use(Socket, { url:'ws://7709f4e2.ngrok.io' });

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
