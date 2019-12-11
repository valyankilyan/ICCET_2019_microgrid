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
            <h3 class="pl-3">Подача тока{{retry}}</h3>
            <span  @click="but = !but"><v-switch  v-model="switch1" :label="``" class="ma-0 ml-3 pa-0" ></v-switch></span><span>{{but ? 'on' : 'off'}}</span>
            
        </v-container>
        
          

        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Температура в 	&#8451;:</h3>
             
               
                <v-slider
                v-model="sliderTemp"
                thumb-label
                 max="40"
              min="20"
                class="ma-0"
                ></v-slider>
              
        </v-container>
         <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Текущая температура:<span> {{temp}}	&#8451;</span></h3>
             
               
                
              
        </v-container>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень яркости:</h3>
             
               
                <v-slider
                v-model="sliderAll"
                thumb-label
                class="ma-0"
                 color="pink darken-1"
                ></v-slider>
              
        </v-container>
        
          

        

        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень красного:</h3>
             
               
                <v-slider
                v-model="sliderRed"
                thumb-label
                class="ma-0"
                 color="red"
                ></v-slider>
              
        </v-container>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень зеленого:</h3>
             
               
                <v-slider
                v-model="sliderGreen"
                thumb-label
                
                class="ma-0"
                 color="green"
                ></v-slider>
              
        </v-container>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Уровень голубого:</h3>
             
               
                <v-slider
                v-model="sliderBlue"
                thumb-label
                class="ma-0"
              
                ></v-slider>
              
        </v-container>
        
        
    </section>


        <section>
              <v-expansion-panels
        v-model="panel"
        :disabled="disabled"
        multiple
      >
        <v-expansion-panel>
          <v-expansion-panel-header>Ваш тариф</v-expansion-panel-header>
          <v-expansion-panel-content >
              <section class="d-flex mb-0 pb-0">
              <span>Солненая Панель<br>3₽/кВт</span>
            <v-switch v-model="switch3" :label="``" class="d-flex ma-0 ml-3 pa-0"></v-switch>
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
        sliderAll:'',               //общий уровень освещения (щт 0 до 100%)
        sliderRed:'',               //уровень красного цвета (возвращает от 0 до 100)  
        sliderGreen:'',             //уровень зеленого цвета (возвращает от 0 до 100)
        sliderBlue:'',              //уровень голубого цвета (возвращает от 0 до 100)
        sliderTemp:'',        // значение температуры (от 20 до 40)
        temp:23,              // значение текущей температуры в теплице
        but:false,            // on/off кнопки включения   (true/false)
        but2:false,           // on/off кнопки Свет в теплице (true/false) 
        switch1: false,       // значение слайдера on/off (true/false)
        switch2: false,       // значение слайдера Свет в теплице   (true/false)
        switch3: false,       //значение слайдера акум/солнце  (true/false)
        
        pays: [
          {
            name: '1:45:67',
            calories: 157,
          },
          {
            name: '1:45:67',
            calories: 237,
          },
          {
            name: '1:45:67',
            calories: 518,
          },
        ],
      }
    },
  }
</script>
