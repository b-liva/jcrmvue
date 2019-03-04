<template>
    <v-app>
        <v-summary></v-summary>
        <ApolloQuery :query="customers_query">
            <template slot-scope="{ result: { loading, error, data } }">
                <span v-if="loading">Loading...</span>
                <span v-else-if="error">An error occured</span>

                <section v-if="data">
                    <ol>
                        <li v-for="customer in data.customers.edges">
                            {{customer.node.name}} <b>({{customer.node.orderCount}})</b> - <i>({{customer.node.customerPaymentAmount}})</i>
                            <ol>
                                <li style="margin-right: 20px;" v-for="req in customer.node.requestsSet.edges">{{req.node.number}}
                                    <ol>
                                        <li style="margin-right: 40px;" v-for="prof in req.node.xprefSet.edges">
                                            {{prof.node.number}}
                                        </li>
                                    </ol>
                                </li>
                            </ol>
                        </li>
                    </ol>
                </section>
            </template>
        </ApolloQuery>
    </v-app>
</template>

<script>
    import Summary from './components/Summary'
    import {GET_CUSTOMERS} from "./custom_queries";

    export default {
        name: 'App',
        components: {
            'v-summary': Summary,
        },
        data() {
            return {
                customers_query: GET_CUSTOMERS,
            }
        }
    }
</script>
