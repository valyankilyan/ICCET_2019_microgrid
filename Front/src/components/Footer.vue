<template>
    <v-footer
            dense fixed app
            padless
    >
        <v-row
                justify="center"
                no-gutters
        >
            <v-btn
                    v-for="link in links"
                    :key="link"
                    color="white"
                    text
                    rounded
                    class="my-2"
            >
                {{ link }}
            </v-btn>
           
            <router-link to="/admin" style="text-decoration: none; color: white">
            <v-btn
                    color="white"
                    text
                    rounded
                    class="my-2"
            >
                Admin
            </v-btn>
            </router-link>
            <router-link to="/wheel" style="text-decoration: none; color: white">
            <v-btn
                    color="white"
                    text
                    rounded
                    class="my-2"
            >
                Whell
            </v-btn>
            </router-link>
            <router-link to="/scene" style="text-decoration: none; color: white">
                <v-btn
                        color="white"
                        text
                        rounded
                        class="my-2"
                >
                    Scene
                </v-btn>
            </router-link> <router-link to="/radio" style="text-decoration: none; color: white">
                <v-btn
                        color="white"
                        text
                        rounded
                        class="my-2"
                >
                    Radio
                </v-btn>
            </router-link>
             <router-link to="/light" style="text-decoration: none; color: white">
                <v-btn
                        color="white"
                        text
                        rounded
                        class="my-2"
                >
                    Light
                </v-btn>
                 <router-link to="/smartgr" style="text-decoration: none; color: white">
                <v-btn
                        color="white"
                        text
                        rounded
                        class="my-2"
                >
                    SmartGr
                </v-btn>
            </router-link>
            </router-link>
            <v-col
                    class="py-4 text-center white--text"
                    cols="12"
            >
                {{ new Date().getFullYear() }} — <strong>Карельские энергетики</strong>
            </v-col>
        </v-row>
    </v-footer>
</template>

<script>
    export default {
        data: () => ({
            links:''
        }),
    }
</script>




 