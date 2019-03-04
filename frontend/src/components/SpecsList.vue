<template>
    <div>
        <v-container>
            <v-layout row wrap>
                <v-flex md12>
                    <div v-for="spec in list">{{spec.kw}} - {{spec.rpm}} - {{spec.voltage}}</div>
                </v-flex>
            </v-layout>
        </v-container>
    </div>
</template>

<script>
    export default {
        data: () => ({
            list: [
                {'kw': 132, 'rpm': 1500, 'voltage': 380},
                {'kw': 18.5, 'rpm': 1000, 'voltage': 400},
                {'kw': 250, 'rpm': 1500, 'voltage': 380},
                {'kw': 450, 'rpm': 3000, 'voltage': 400},
            ]
        }),
        component: {},
        methods: {},
        watch: {},
        apollo: {}
    }
</script>

<style>

</style>
