import Vue from 'vue'
import {
    Icon,
    Image,
    Button,
    Container,
    Main,
    Header,
    Upload,
    Message,
    Loading
} from 'element-ui'

Vue.use(Icon);
Vue.use(Image);
Vue.use(Button);
Vue.use(Container);
Vue.use(Main);
Vue.use(Header);
Vue.use(Upload);
Vue.prototype.$message = Message;
Vue.prototype.$loading = Loading.service;
