<template>
  <v-card class="mx-auto my-10 pb-3" max-width="400">
    <v-img
      src="http://rk.karelia.ru/wp-content/uploads/2019/11/p8tv0lom4xcsg808s0k-1280x720.jpg"
      height="200px"
    ></v-img>

    <v-card-title>Кванториада 2019</v-card-title>
    <v-card-subtitle class="pl-5">Карельские Энергетики</v-card-subtitle>

    <v-col class="d-flex ma-0 pa-0 algin-center" cols="12" sm="8">
      <h3 class="pl-6">Трек:</h3>
      <v-select
      
        :items="items"
        item-value="value"
        item-text="name"
        v-model="select"
        label=" Выберите Пользователя"
        class="ma-0 pa-0 ml-3"
      ></v-select>
    </v-col>

    <section class="d-flex">
      <v-col cols="12" sm="6" class="ma-0 pa-0 pl-6 d-flex">
        <v-text-field
          v-model="password"
          :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
          :rules="[rules.required, rules.min]"
          :type="show1 ? 'text' : 'password'"
          name="input-10-1"
          label="пароль"
          hint="At least 4 characters"
          counter
          class="ma-0 pa-0"
          @click:append="show1 = !show1"
        ></v-text-field>
      </v-col>
    </section>
    <span class="ma-0 pa-0 pl-5" id="elem">
      <router-link v-bind:to="select" style="text-decoration: none; color: white">
        <v-btn color="cyan lighten-1" text>войти</v-btn>
      </router-link>
    </span>
  <!--  <div v-for="itm in detail" :key="itm.name">
      <p>{{itm.image}}</p>
    </div>-->
  </v-card>
</template>


<style>
.v-application .mb-6 {
  margin-bottom: 26px !important;
}
</style>


<script>
import axios from "axios";

export default {
  data() {
    return {
      show1: false,
      linkk: '',
      select: "", // значение выбраного пользователя
      items: 
      [
        { name: 'Колесо обозрения', value: 'wheel' },
        { name: 'Сцена', value: 'scene' },
        { name: 'Радио', value: 'radio' },
        { name: 'Освещение', value: 'light' },
        { name: 'Умная грядка', value: 'smartgr' },
        { name: 'Admin', value: 'admin' }
      ],

      password: "", //от пароля
      rules: {
        required: value => !!value || "Required.",
        min: v => v.length >= 4 || "Min 4 characters",
        emailMatch: () => "The email and password you entered don't match"
      },
      detail: []
    };
  },
  created() {
    /* axios.get('https://my-json-server.typicode.com/AlexanderPanshin/dpv.school/user')
  .then(function (response) {
    // handle success
    console.log(response);
  })*/
    axios
      .get(
        `https://my-json-server.typicode.com/AlexanderPanshin/dpv.school/user`
      )
      .then(response => {
        this.detail = response.data;
      })
      .catch(error => {
        window.console.log(error);
        this.errored = true;
      });
  },
  methods: {
   /* xxx: function() {
     console.log(this.select);

       this.linkk = this.select.value;
      if(this.select == "Сцена")
        this.linkk = this.select;
        }*/
    
  }
};
</script>

