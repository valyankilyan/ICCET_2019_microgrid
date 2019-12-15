<template>
  <v-card
    class="mx-auto my-10"
    max-width="400"
  >
    <v-img
      src="https://nikatv.ru/public/upload/news/26565/images/3138.jpg"
      height="200px"
    ></v-img>

    <v-card-title>
      ВЫ: Колесо обозрения
    </v-card-title>

   
    <section>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Подача тока</h3>
            <span  @click="but = !but"><v-switch  v-model="WHswitch1" :label="``" class="ma-0 ml-3 pa-0" ></v-switch></span><span>{{but ? 'on' : 'off'}}</span>
              <span class="pl-4">Мощность{{}} Вт</span>
        </v-container>
        
          

        
        
    </section>


        <section>
              <v-expansion-panels
        
        multiple
      >
        <v-expansion-panel>
          <v-expansion-panel-header>Ваш тариф</v-expansion-panel-header>
          <v-expansion-panel-content >
              <section class="d-flex mb-0 pb-0">
              <span>Солненая Панель<br>3₽/кВт</span>
            <v-switch v-model="WHswitch2" :label="``" class="d-flex ma-0 ml-3 pa-0"></v-switch>
            <span>Аккумулятор<br>5₽/кВт</span>
              </section>
          </v-expansion-panel-content>
        </v-expansion-panel>
  
        <v-expansion-panel>
          <v-expansion-panel-header>Счет на оплату</v-expansion-panel-header>
          <v-expansion-panel-content>
             <section class="d-fle mb-0 pb-0">
              <p><strong>Вы работаете:</strong>  15:23:43 сек</p>
              <span><strong>Суммак к оплате:</strong> 4565₽</span>
              <v-btn color="cyan lighten-1 pl-5" text>оплатить</v-btn>
              
            
           
              </section>
          </v-expansion-panel-content>
        </v-expansion-panel>
  
        <v-expansion-panel>
          <v-expansion-panel-header>Квитанции на оплату</v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-simple-table height="250px">
                <template v-slot:default>
                <thead>
                    <tr>
                    <th class="text-left">Время работы</th>
                    <th class="text-left">Оплачено,₽</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="pay in pays" :key="pay.name">
                    <td>{{ pay.name }}</td>
                    <td>{{ pay.calories }}</td>
                    </tr>
                </tbody>
                </template>
            </v-simple-table>
                    </v-expansion-panel-content>
                    </v-expansion-panel>
                </v-expansion-panels>
                    
        </section>        
  </v-card>
</template>


<script>
 
  export default {
    data () {
      return {
        but:false,            // on/off кнопки включения   (true/false)
        WHswitch1: false,       // значение слайдера on/off (true/false)
        WHswitch2: false,       //значение слайдера акум/солнце  (true/false)
       
       
        pays: [
          {
            name: '1:45:67',
            calories: 157,
          },
          {
            name: '1:46:67',
            calories: 237,
          },
          {
            name: '1:47:67',
            calories: 518,
          },
        ],
      };
    },
    
    created() {
        this.$socket.addMessageHandler(this.messageHandle);
      //  this.$socket.send('scene');
      
      },
      destroyed() {
        this.$socket.removeMessageHandler(this.messageHandle);
      },
      watch: {
        WHswitch1: function() {
          this.sendData();
        },
         WHswitch2: function() {
          this.sendData();
        }
      },
      methods: {
        messageHandle(message) {
          console.log("обработано в Wheel " + message);
        },
        sendData() {
         // console.log(this.SCmusic);
       // store.commit('increment');

          let payload = {
             WHswitch1: this.WHswitch1,       // значение слайдера on/off (true/false)
              WHswitch2:  this.WHswitch2      //значение слайдера акум/солнце  (true/false)
            };

          this.$socket.send(JSON.stringify(payload));
        }
      }

  };
 /* const store = new Vuex.Store({
  state: {
        but:false,            // on/off кнопки включения   (true/false)
        WHswitch1: false,       // значение слайдера on/off (true/false)
        WHswitch2: false,
  },
  mutations: {
  increment(state) {
      // изменяем состояние
      state.WHswitch1;
  }
}});
*/
</script>
