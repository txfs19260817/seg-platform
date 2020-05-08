import Vue from 'vue'
import {
    Icon,
    Image,
    Dialog,
    Button,
    Container,
    Main,
    Header,
    Upload,
    Tooltip,
    Switch,
    Message,
    Loading
} from 'element-ui'

Vue.use(Icon);
Vue.use(Image);
Vue.use(Dialog);
Vue.use(Button);
Vue.use(Container);
Vue.use(Main);
Vue.use(Header);
Vue.use(Upload);
Vue.use(Tooltip);
Vue.use(Switch);
Vue.prototype.$message = Message;
Vue.prototype.$loading = Loading.service;
