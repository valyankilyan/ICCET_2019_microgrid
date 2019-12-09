<template>
  <v-card
    class="mx-auto my-10 mb-10"
    max-width="350"
  >
    <v-img
      src="https://i.ytimg.com/vi/J7BraQ9nX6E/maxresdefault.jpg"
      height="200px"
    ></v-img>

    <v-card-title>
     ВЫ: Супер Admin
    </v-card-title>
      
     <p class="ml-3">можно менять параметры<br> любых потребителей</p>           
         <div class="d-flex flex-column">  
           
           
            <router-link to="/wheel" style="text-decoration: none; color: white">
            <v-btn
                    color="cyan lighten-1"
                    text
                    rounded
                    class="my-2"
            >
                Whell
            </v-btn>
            </router-link>
            <router-link to="/scene" style="text-decoration: none; color: white">
                <v-btn
                        color="cyan lighten-1"
                        text
                        rounded
                        class="my-2"
                >
                    Scene
                </v-btn>
            </router-link> <router-link to="/radio" style="text-decoration: none; color: white">
                <v-btn
                        color="cyan lighten-1"
                        text
                        rounded
                        class="my-2"
                >
                    Radio
                </v-btn>
            </router-link>
             <router-link to="/light" style="text-decoration: none; color: white">
                <v-btn
                        color="cyan lighten-1"
                        text
                        rounded
                        class="my-2"
                >
                    Light
                </v-btn>
                </router-link>
                 <router-link to="/smartgr" style="text-decoration: none; color: white">
                <v-btn
                        color="cyan lighten-1"
                        text
                        rounded
                        class="my-2"
                >
                    SmartGr
                </v-btn>
            </router-link>
         </div>
  </v-card>
</template>









