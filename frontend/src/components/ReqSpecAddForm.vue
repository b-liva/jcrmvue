<template>
    <div>
        <v-container>
            <v-layout row wrap xs6>
                <v-flex xs6>
                    <v-layout wrap>
                        <v-flex md3>
                            <v-text-field
                                    v-model="reqSpecItems.qty"
                                    label="qty"
                            ></v-text-field>
                        </v-flex>
                        <v-flex md3>
                            <v-text-field
                                    v-model="reqSpecItems.kw"
                                    label="kw"
                            ></v-text-field>
                        </v-flex>
                        <v-flex md3>
                            <v-text-field
                                    v-model="reqSpecItems.rpm"
                                    label="rpm"
                            ></v-text-field>
                        </v-flex>
                        <v-flex md3>
                            <v-text-field
                                    v-model="reqSpecItems.voltage"
                                    label="voltage"
                            ></v-text-field>
                        </v-flex>
                        <v-flex>
                            <v-checkbox v-model="reqSpecItems.tech" label="Tech"></v-checkbox>
                            <v-checkbox v-model="reqSpecItems.price" label="Price"></v-checkbox>
                            <v-checkbox v-model="reqSpecItems.permission" label="Permission"></v-checkbox>
                            <v-checkbox v-model="reqSpecItems.sent" label="Sent"></v-checkbox>
                        </v-flex>
                        <v-flex md12>
                            <v-textarea
                                    v-model="reqSpecItems.details"
                                    name="input-7-1"
                                    box
                                    label="Details"
                                    auto-grow
                                    value="The Woodman set to work at once, and so sharp was his axe that the tree was soon chopped nearly through."
                            ></v-textarea>
                        </v-flex>
                        <v-flex md12>
                            <v-btn small color="primary" @click="submitSpec">submit</v-btn>
                        </v-flex>
                    </v-layout>
                </v-flex>
                <v-flex xs6>
                    <v-layout>
                        <v-flex>
                            <spec-list :req-id="reqSpecItems.reqId"></spec-list>
                        </v-flex>
                    </v-layout>
                </v-flex>
            </v-layout>
        </v-container>
        <div>{{reqSpecItems}}</div>
    </div>
</template>

<script>
    import SpecsList from "./SpecsList"
    import {CREATE_SPEC} from "../custom_queries";
    import {bus} from "../main"

    export default {
        components: {
            'spec-list': SpecsList
        },
        data: () => ({
            reqSpecItems: {
                id: null,
                reqId: null,
                qty: null,
                kw: null,
                rpm: null,
                voltage: null,
                ip: null,
                ic: null,
                details: "",
                tech: false,
                price: false,
                permission: false,
                sent: false,
                cancelled: false,
            },
        }),
        methods: {
            submitSpec() {
                this.$apollo.mutate({
                    mutation: CREATE_SPEC,
                    variables: {
                        "reqId": "UmVxdWVzdE5vZGU6NTk2",
                        "qty": this.reqSpecItems.qty,
                        "type": 1,
                        "kw": this.reqSpecItems.kw,
                        "rpm": this.reqSpecItems.rpm,
                        "voltage": this.reqSpecItems.voltage,
                        "permission": this.reqSpecItems.permission,
                        "price": this.reqSpecItems.price,
                        "sent": this.reqSpecItems.sent,
                        "tech": this.reqSpecItems.tech,
                        "cancelled": this.reqSpecItems.cancelled,
                    }
                }).then(
                    (result) => {
                        console.log(result)
                    },
                    (errors) => {
                        console.log(errors)
                    });
                console.log(this.reqSpecItems)
            }

        },
        created(){
            bus.$on('reqIdGenerated', (data) => {
                console.log('now passed.');
                console.log(data);
                this.reqSpecItems.reqId = data
            })
        },
        watch: {},

        apollo: {}
    }
</script>

<style>

</style>
