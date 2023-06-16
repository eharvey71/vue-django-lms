import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'

require('@/assets/main.scss');

//dev
axios.defaults.baseURL = 'http://localhost:8000/api/v1/'
//prod/test
//axios.defaults.baseURL = 'http://207.154.213.45/api/v1/'

createApp(App).use(store).use(router, axios).mount('#app')