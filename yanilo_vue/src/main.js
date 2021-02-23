// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import settings from "./settings";
// elementUI 导入
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';  // 需要import引入一下css文件，和我们的link标签引入是一个效果，而import .. from ..是配合export default来使用的
import '../static/css/style.css';
import '../utils/js/jquery.min';
import header from '@/components/common/Header';
import axios from 'axios';
import store from "./store";


require('video.js/dist/video-js.css');
require('vue-video-player/src/custom-theme.css');
import VideoPlayer from 'vue-video-player'
import he from "element-ui/src/locale/lang/he";
Vue.use(VideoPlayer);

// 调用插件
Vue.use(ElementUI);
Vue.config.productionTip = false;
Vue.prototype.$settings = settings;
axios.defaults.withCredentials = false;
Vue.prototype.Header = header;








Vue.prototype.$axios = axios
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
