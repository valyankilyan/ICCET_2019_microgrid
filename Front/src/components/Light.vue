<template>
  <v-card
    class="mx-auto my-10"
    max-width="400"
  >
    <v-img
      src="https://img1.akspic.ru/image/87835-bashnya-noch-neboskreb-stolica-muzykant-1280x800.jpg"
      height="200px"
    ></v-img>

    <v-card-title>
      ВЫ: Освещение
    </v-card-title>

   
    <section>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Подача тока</h3>
            <span  @click="but = !but"><v-switch  v-model="LIswitch1" :label="``" class="ma-0 ml-3 pa-0" ></v-switch></span><span>{{but ? 'on' : 'off'}}</span>
            <span class="pl-4">Мощность{{}} Вт</span>
        </v-container>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень яркости:</h3>
             
               
                <v-slider
                :disabled="!but"
                v-model="LIsliderAll"
                :thumb-size="27"
            thumb-label="always"
                class="ma-0"
                 color="pink darken-1"
                ></v-slider>
              
        </v-container>
        
          

        

        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень красного:</h3>
             
               
                <v-slider
                :disabled="!but"
                v-model="LIsliderRed"
                :thumb-size="27"
            thumb-label="always"
                class="ma-0"
                 color="red"
                ></v-slider>
              
        </v-container>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень зеленого:</h3>
             
               
                <v-slider
                :disabled="!but"
                v-model="LIsliderGreen"
                :thumb-size="27"
            thumb-label="always"
                
                class="ma-0"
                 color="green"
                ></v-slider>
              
        </v-container>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень голубого:</h3>
             
               
                <v-slider
                :disabled="!but"
                v-model="LIsliderBlue"
                :thumb-size="27"
            thumb-label="always"
                class="ma-0"
              
                ></v-slider>
              
        </v-container>
        
        
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Лампа на горе:</h3>
            <span  @click="but2 = !but2"><v-switch :disabled="!but" v-model="LIswitch2" :label="``" class="ma-0 ml-3 pa-0" ></v-switch></span><span>{{but2 ? 'on' : 'off'}}</span>
            
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
            <v-switch v-model="LIswitch3" :label="``" class="d-flex ma-0 ml-3 pa-0"></v-switch>
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
        LIsliderAll: 0,               //общий уровень освещения (щт 0 до 100%)
        LIsliderRed: 0,               //уровень красного цвета (возвращает от 0 до 100)  
        LIsliderGreen: 0,             //уровень зеленого цвета (возвращает от 0 до 100)
        LIsliderBlue: 0,              //уровень голубого цвета (возвращает от 0 до 100)
        but:false,                  // on/off кнопки включения   (true/false)
        but2:false,                 // on/off кнопки ласпа на горе   (true/false) 
        LIswitch1: false,             // значение слайдера on/off (true/false)
        LIswitch2: false,             // значение слайдера лампа на горе   (true/false)
        LIswitch3: false,             //значение слайдера акум/солнце  (true/false)
       
        pays: [
          {
            name: '1:45:67',
            calories: 157,
          },
          {
            name: '1:48:67',
            calories: 237,
          },
          {
            name: '1:55:67',
            calories: 518,
          },
        ],
      };
    },
    created() {
    this.$socket.addMessageHandler(this.messageHandle);
    
  
  //this.$socket.send('Встречаются два новых русских, один у другого интересуется: - Слышь, Вован, а вот ты стометровку за сколько пробежишь? - Ну дык, Колян, за штуку баксов, ...');
  },
  destroyed() {
    this.$socket.removeMessageHandler(this.messageHandle);
  },
  watch: {
    LIsliderAll: function() {
      this.sendData();
    },
    LIsliderRed: function() {
      this.sendData();
    },
    LIsliderGreen: function() {
      this.sendData();
    },
    LIsliderBlue: function() {
      this.sendData();
    },
    LIswitch1: function() {
      this.sendData();
    },
    LIswitch2: function() {
      this.sendData();
    },
    LIswitch3: function() {
      this.sendData();
    }
  },
  methods: {
    messageHandle(message) {
      console.log("обработано в Light " + message);
    },
    sendData() {
      console.log(this.SCmusic);

      let payload = {
        LIsliderAll: this.LIsliderAll,               //общий уровень освещения (щт 0 до 100%)
        LIsliderRed: this.LIsliderRed,               //уровень красного цвета (возвращает от 0 до 100)  
        LIsliderGreen: this.LIsliderGreen,             //уровень зеленого цвета (возвращает от 0 до 100)
        LIsliderBlue: this.LIsliderBlue,              //уровень голубого цвета (возвращает от 0 до 100)
        LIswitch1: this.LIswitch1,             // значение слайдера on/off (true/false)
        LIswitch2: this.LIswitch2,             // значение слайдера лампа на горе   (true/false)
        LIswitch3: this.LIswitch3             //значение слайдера акум/солнце  (true/false)
      };

      this.$socket.send(JSON.stringify(payload));
    }
  }
  };
</script>
