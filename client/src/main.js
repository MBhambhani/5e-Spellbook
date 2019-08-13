import Vue from 'vue';
import Vuetify from 'vuetify';
import App from './App.vue';
import router from './router';
import 'vuetify/dist/vuetify.min.css';
import 'material-design-icons-iconfont/dist/material-design-icons.css';

Vue.use(Vuetify, {
  iconfont: 'md',
  theme: {
    primary: '#342e37',
    secondary: '#9fd356',
    accent: '#fa824c',
    error: '#a4243b',
    info: '#3c91e6',
    success: '#9fd356',
    warning: '#fa824c',
  },
});
Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
