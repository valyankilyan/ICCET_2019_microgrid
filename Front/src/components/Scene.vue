<template>
  <v-card
    class="mx-auto my-10"
    max-width="400"
  >
    <v-img
      src="https://cdn.pixabay.com/photo/2015/04/23/17/18/disney-736374__480.jpg"
      height="200px"
    ></v-img>

    <v-card-title>
      ВЫ: Сцена
    </v-card-title>

   
    <section>
        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Подача тока:</h3>
            <span @click="but = !but"><v-switch  v-model="SCswitch1" :label="``" class="ma-0 ml-3 pa-0" ></v-switch></span><span>{{but ? 'on' : 'off'}}</span>
            
        </v-container>
        
          

        <v-col class="d-flex ma-0 pa-0 algin-center" cols="12" sm="8">
            <h3 class=" pl-6">Трек:</h3>
            <v-select
            :disabled = !but
            item-value="valueS"
            item-text="name"
            :items="SCitems"
             v-model="SCmusic"
            label="Выберети музыку"
            class="ma-0 pa-0 ml-3 "
            
            ></v-select>
        </v-col>

        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Повтор трека:</h3>
             
            <span class="ma-0 pa-0 ml-2 mt-1">   
             <v-checkbox
             class="ma-0 pa-0 "
             :disabled = !but
                v-model="SCretry"
                label=""
                color="red"
                value="true"
                hide-details
              ></v-checkbox>
            </span>  
        </v-container>

         <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Bassboosted:</h3>
             
                        <span  @click="but2 = !but2"><v-switch  :disabled = !but v-model="SCswitch2" :label="``" class="ma-0 ml-3 pa-0" >
                          </v-switch></span><span>{{but2 ? 'on' : 'off'}}</span>

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
            <v-switch v-model="SCswitch3" :label="``" class="d-flex ma-0 ml-3 pa-0"  color="red"></v-switch>
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
        SCretry:'',           //кнопка повтора трека  врзвращает =>(true)
        SCmusic:'',           //какой трек сейчас играет   (цифра от 1 до 6)
        but:false,          //on/off кнопки включения   (true/false)
        but2:false,         //on/off кнопки бастбуста   (true/false) 
        SCswitch1: false,     // значение слайдера on/off (true/false)
        SCswitch2: false,     //значение слайдера бастбуст   (true/false)
        SCswitch3: false,     //значение слайдера акум/солнце  (true/false)
         SCitems: 
      [
        { name: 'Шрек music', valueS: 1 },
        { name: 'Атвинта', valueS: 2 },
        { name: 'Soccer physics', valueS: 3 },
        { name: 'Димон', valueS: 4 },
        { name: 'Джон Сина', valueS: 5 },
        { name: 'SILENCE', valueS: 6 }
      ],

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
      }
    },
  }
</script>
