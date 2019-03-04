<template>
    <v-app>
        <v-summary></v-summary>
        <!--<v-req-add></v-req-add>-->
    </v-app>
</template>

<script>
    import Summary from './components/Summary'
    import ReqAddFormPopup from './components/ReqAddFormPopup'
    import {GET_CUSTOMERS} from "./custom_queries";

    export default {
        name: 'App',
        components: {
            'v-summary': Summary,
            'v-req-add': ReqAddFormPopup,
        },
        data() {
            return {
                customers_query: GET_CUSTOMERS,
            }
        },
    }
</script>
