<template>
    <div>
        <v-container>
            <v-layout row wrap>
                <v-flex md12>
                    <div v-for="spec in specs.reqspecSet.edges">{{spec.node.kw}} - {{spec.node.rpm}} - {{spec.node.voltage}}</div>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    import {GET_SPEC_SET} from "../custom_queries";

    export default {
        data: () => ({
            specs: [],
            list: [
                {'kw': 132, 'rpm': 1500, 'voltage': 380},
                {'kw': 18.5, 'rpm': 1000, 'voltage': 400},
                {'kw': 250, 'rpm': 1500, 'voltage': 380},
                {'kw': 450, 'rpm': 3000, 'voltage': 400},
            ]
        }),
        props: {
            reqId: String,
        },
        component: {},
        methods: {},
        watch: {},
        apollo: {
            specs: {
                query: GET_SPEC_SET,
                variables: {
                    "id": "UmVxdWVzdE5vZGU6NTk2"
                }
            }
        }
    }
</script>

<style>

</style>
