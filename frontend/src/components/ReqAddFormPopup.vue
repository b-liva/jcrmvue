<template>
    <div>
        <v-container>
            <v-layout row wrap>
                <v-flex md5>
                    <v-text-field
                            v-model="requestItems.number"
                            label="req no"
                            prepend-icon="numeric"
                    ></v-text-field>
                </v-flex>
                <v-flex md7>
                    <v-autocomplete
                            :loading="loading"
                            :items="states"
                            :search-input.sync="search"
                            cache-items
                            class="mx-3"
                            flat
                            hide-no-data
                            hide-details
                            label="select a customer"
                            solo-inverted
                    ></v-autocomplete>
                </v-flex>
                <v-flex md12>
                    <v-textarea
                            v-model="requestItems.details"
                            name="input-7-1"
                            box
                            label="Details"
                            auto-grow
                            value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
                    ></v-textarea>

                </v-flex>
                <v-flex md12>
                    <v-layout wrap>
                        <v-flex md5>
                            <PDatePicker v-model="requestItems.date" md2></PDatePicker>

                        </v-flex>
                        <v-flex md5>
                            <v-btn small color="primary" @click="submitReq">submit</v-btn>

                        </v-flex>

                    </v-layout>
                </v-flex>
            </v-layout>


        </v-container>
        <div>{{requestItems}}</div>

        <div v-if="customers.edges">
            customer name : {{customers.edges[0].node.name}}<br>
            customer code : {{customers.edges[0].node.code}}
        </div>
    </div>
</template>

<script>

    import {FIND_CUSTOMER_BY_NAME, CREATE_REQUEST} from "../custom_queries";
    import {GET_SALES_EXP} from "../queries/user_queries";
    import PDatePicker from "vue2-persian-datepicker/src/components/PDatePicker";

    export default {
        components: {
            PDatePicker,
        },
        data: () => ({
            visible: true,
            loading: false,
            sales_exp: "",
            customers: [],
            items: [],
            select: null,
            search: null,
            requestItems: {
                number: "",
                customer: "",
                details: "",
                date: "",
            },
            states: []
        }),
        component: {},
        methods: {
            customerList(itemm) {
                return itemm.node.name;
            },
            submitReq() {
                console.log(this.requestItems, this.customers);
                this.$apollo.mutate({
                    mutation: CREATE_REQUEST,
                    variables: {
                        "customer": this.customers.edges[0].node.id,
                        "number": this.requestItems.number,
                        "date": this.requestItems.date,
                        "summary": this.requestItems.details
                    }
                })
            }
        },
        watch: {
            search(val) {
                // console.log(val)
                this.loading = true;
                this.requestItems.customer = val;
                this.items = this.customers.edges;
                if (this.items) {
                    this.states = this.items.map(this.customerList);
                }
                this.loading = false
            }
        },

        apollo: {
            sales_exp: {
                query: GET_SALES_EXP,
            },
            customers: {
                query: FIND_CUSTOMER_BY_NAME,
                variables() {
                    return {
                        "name": this.requestItems.customer
                    }
                }
                ,
                skip() {
                    return !this.requestItems.customer
                }
            }
        }
    }
</script>

<style>

</style>
