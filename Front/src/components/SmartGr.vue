<template>
  <v-card
    class="mx-auto my-10"
    max-width="400"
  >
    <v-img
      src="https://www.light-group.com.ua/userfiles/image/objects_gallery/photoimg_1445771990.jpg"
      height="200px"
    ></v-img>

    <v-card-title>
      ВЫ: Умная грядка
    </v-card-title>

   
    <section>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Подача тока</h3>
            <span  @click="but = !but"><v-switch  v-model="SGswitch1" :label="``" class="ma-0 ml-3 pa-0" ></v-switch></span><span>{{but ? 'on' : 'off'}}</span>
            
        </v-container>
        
          

        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Температура в 	&#8451;:</h3>
             
               
                <v-slider
                :disabled="!but"
                v-model="SGsliderTemp"
                thumb-label
                 max="40"
              min="20"
                class="ma-0"
                ></v-slider>
              
        </v-container>
         <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Текущая температура:<span> {{SGtemp}}	&#8451;</span></h3>
             
               
                
              
        </v-container>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень яркости:</h3>
             
               
                <v-slider
                :disabled="!but"
                v-model="SGsliderAll"
                thumb-label
                class="ma-0"
                 color="pink darken-1"
                ></v-slider>
              
        </v-container>
        
          

        

        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень красного:</h3>
             
               
                <v-slider
                :disabled="!but"
                v-model="SGsliderRed"
                thumb-label
                class="ma-0"
                 color="red"
                ></v-slider>
              
        </v-container>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень зеленого:</h3>
             
               
                <v-slider
                :disabled="!but"
                v-model="SGsliderGreen"
                thumb-label
                
                class="ma-0"
                 color="green"
                ></v-slider>
              
        </v-container>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень голубого:</h3>
             
               
                <v-slider
                :disabled="!but"
                v-model="SGsliderBlue"
                thumb-label
                class="ma-0"
              
                ></v-slider>
              
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
            <v-switch v-model="SGswitch3" :label="``" class="d-flex ma-0 ml-3 pa-0"></v-switch>
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
//import axios from "axios";
  export default {
    data () {
      return {
        SGsliderAll:'',               //общий уровень освещения (щт 0 до 100%)
        SGsliderRed:'',               //уровень красного цвета (возвращает от 0 до 100)  
        SGsliderGreen:'',             //уровень зеленого цвета (возвращает от 0 до 100)
        SGsliderBlue:'',              //уровень голубого цвета (возвращает от 0 до 100)
        SGsliderTemp:'',        // значение температуры (от 20 до 40)
        SGtemp:23,              // значение текущей температуры в теплице
        but:false,            // on/off кнопки включения   (true/false)
        but2:false,           // on/off кнопки Свет в теплице (true/false) 
        SGswitch1: false,       // значение слайдера on/off (true/false)
        SGswitch2: false,       // значение слайдера Свет в теплице   (true/false)
        SGswitch3: false,       //значение слайдера акум/солнце  (true/false)
        
        pays: [
          {
            name: '1:45:67',
            calories: 157,
          },
          {
            name: '1:47:67',
            calories: 237,
          },
          {
            name: '1:48:67',
            calories: 518,
          },
        ],
      };
    },
    created() {
    this.$socket.addMessageHandler(this.messageHandle);
    this.$socket.send('scene');
  
  //this.$socket.send('Встречаются два новых русских, один у другого интересуется: - Слышь, Вован, а вот ты стометровку за сколько пробежишь? - Ну дык, Колян, за штуку баксов, ...');
  },
  destroyed() {
    this.$socket.removeMessageHandler(this.messageHandle);
  },
  watch: {
    SGsliderAll: function() {
      this.sendData();
    },
    SGsliderRed: function() {
      this.sendData();
    },
    SGsliderGreen: function() {
      this.sendData();
    },
    SGsliderBlue: function() {
      this.sendData();
    },
    SGsliderTemp: function() {
      this.sendData();
    },
    SGswitch1: function() {
      this.sendData();
    },
     SGswitch2: function() {
      this.sendData();
    },
     SGswitch3: function() {
      this.sendData();
    }
  },
  methods: {
    messageHandle(message) {
      console.log("обработано в Scene " + message);
    },
    sendData() {
      console.log(this.SCmusic);

      let payload = {
        SGsliderAll: this.SGsliderAll,               //общий уровень освещения (щт 0 до 100%)
        SGsliderRed: this.SGsliderRed,               //уровень красного цвета (возвращает от 0 до 100)  
        SGsliderGreen: this.SGsliderGreen,             //уровень зеленого цвета (возвращает от 0 до 100)
        SGsliderBlue: this.SGsliderBlue,              //уровень голубого цвета (возвращает от 0 до 100)
        SGsliderTemp: this.SGsliderTemp,        // значение температуры (от 20 до 40)
        SGswitch1: this.SGswitch1,       // значение слайдера on/off (true/false)
        SGswitch2: this.SGswitch2,       // значение слайдера Свет в теплице   (true/false)
        SGswitch3: this.SGswitch3,   
       
      };

      this.$socket.send(JSON.stringify(payload));
    }
  }
  };
</script>
