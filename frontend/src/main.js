import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import ApolloClient from "apollo-boost";
import VueApollo from "vue-apollo";
import 'material-design-icons-iconfont/dist/material-design-icons.css'
export const bus = new Vue();

const client = new ApolloClient({
    // uri: "https://api.graph.cool/simple/v1/cjexem1he3let0153tpc5ftu1"
    uri: "http://localhost:8000/graphql"
});

const apolloProvider = new VueApollo({
    defaultClient: client
});

Vue.use(VueApollo);

Vue.config.productionTip = false;

new Vue({
    apolloProvider,
    render: h => h(App),
}).$mount('#app');
