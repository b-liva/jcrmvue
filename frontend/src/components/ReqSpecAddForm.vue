<template>
    <div>
        <v-container>
            <v-layout row wrap>
                <v-flex md4>
                    <v-text-field
                            v-model="reqSpecItems.kw"
                            label="kw"
                    ></v-text-field>
                </v-flex>
                <v-flex md4>
                    <v-text-field
                            v-model="reqSpecItems.rpm"
                            label="rpm"
                    ></v-text-field>
                </v-flex>
                <v-flex md4>
                    <v-text-field
                            v-model="reqSpecItems.voltage"
                            label="voltage"
                    ></v-text-field>
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
        </v-container>
        <div>{{reqSpecItems}}</div>
    </div>
</template>

<script>


    export default {
        data: () => ({
            reqSpecItems: {
                kw: "",
                rpm: "",
                voltage: "",
                ip: "",
                ic: "",
                details: "",
            },
        }),
        component: {},
        methods: {
            submitSpec(){
                console.log(this.reqSpecItems)
            }
        },
        watch: {},

        apollo: {}
    }
</script>

<style>

</style>
