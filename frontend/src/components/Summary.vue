<template>
    <div>
        <ApolloQuery :query="summary">
            <template slot-scope="{ result: { loading, error, data } }">
                <span v-if="loading">Loading...</span>
                <span v-else-if="error">An error occured</span>
                <v-container>
                    <v-layout>
                        <v-card flat class="pa-3">
                            <v-flex xs6 md4>تعداد روتین: {{data.routineCount}}</v-flex>
                        </v-card>
                        <v-card flat class="pa-3">
                            <v-flex xs6 md4>تعداد تعمیرات: {{data.servicesCount}}</v-flex>
                        </v-card>
                        <v-card flat class="pa-3">
                            <v-flex xs6 md4>تعداد پروژه: {{data.projectCount}}</v-flex>
                        </v-card>
                        <v-card flat class="pa-3">
                            <v-flex xs6 md4>تعداد ضد انفجار: {{data.exCount}}</v-flex>
                        </v-card>
                        <v-card flat class="pa-3">
                            <v-flex xs6 md4>تعداد کل درخواست ها: {{data.ordersCount}}</v-flex>
                        </v-card>
                    </v-layout>
                </v-container>
            </template>
        </ApolloQuery>
        <v-container>
            <v-layout>
                <v-flex v-if="showForm" xs12 md6>
                        <req-add-form></req-add-form>
                </v-flex>
                <v-flex v-if="!showForm" xs12 md6>
                        <req-spec-add-form></req-spec-add-form>
                </v-flex>
                <v-flex v-if="!showForm" xs12 md6>
                        <spec-list></spec-list>
                </v-flex>
            </v-layout>
        </v-container>
        <v-btn @click="showForm = !showForm">toggle</v-btn>
    </div>
</template>
<script>

    import 'material-design-icons-iconfont/dist/material-design-icons.css'
    import {GET_SUMMARY} from "../custom_queries";
    import ReqAddFormPopup from "./ReqAddFormPopup"
    import ReqSpecAddForm from "./ReqSpecAddForm"
    import SpecsList from "./SpecsList"

    export default {
        components: {
            "req-add-form": ReqAddFormPopup,
            "req-spec-add-form": ReqSpecAddForm,
            "spec-list": SpecsList,
        },
        data: () => ({
            summary: GET_SUMMARY,
            visible: true,
            showForm: true,
            loading: false,
            sales_exp: "",
        }),
        methods: {},
        watch: {},

        apollo: {}
    }
</script>


<style>

</style>
