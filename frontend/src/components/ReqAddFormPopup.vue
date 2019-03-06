<template>
    <div>
        <v-container>
            <v-layout>
                <v-flex md6>
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
                                    <v-btn small color="primary" @click="submitReq" :disabled="requestItems.disabled">
                                        submit
                                    </v-btn>

                                </v-flex>

                            </v-layout>
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
    import {bus} from "../main"

    export default {
        name: "req-add-form",
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
            res: null,
            rs: null,
            requestItems: {
                id: "",
                number: "",
                customer: "",
                details: "",
                date: "",
                disabled: false,
                errors: "",
            },
            states: []
        }),
        component: {},
        methods: {
            customerList(itemm) {
                return itemm.node.name;
            },
            submitReq() {
                console.log(this.requestItems, this.customers, this.$apollo);
                this.$apollo.mutate({
                    mutation: CREATE_REQUEST,
                    variables: {
                        "customer": this.customers.edges[0].node.id,
                        "number": this.requestItems.number,
                        "date": this.requestItems.date,
                        "summary": this.requestItems.details
                    },
                }).then(
                    (result) => { /* handle a successful result */
                        this.requestItems.id = result.data.createRequest.requests.id;
                    },
                    (error) => { /* handle an error */
                        this.errors = error;
                    }
                );
                // this.requestItems.disabled = true;
                bus.$emit('reqIdGenerated', this.requestItems.id)
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
