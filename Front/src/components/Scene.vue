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
            <span  @click="but = !but"><v-switch  v-model="switch1" :label="``" class="ma-0 ml-3 pa-0" ></v-switch></span><span>{{but ? 'on' : 'off'}}</span>
            
        </v-container>
        
          

        <v-col class="d-flex ma-0 pa-0 algin-center" cols="12" sm="8">
            <h3 class=" pl-6">Трек:</h3>
            <v-select
            :items="items"
            label="Выберети музыку"
            class="ma-0 pa-0 ml-3 "
            ></v-select>
        </v-col>

        <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Повтор трека:</h3>
             
            <span class="ma-0 pa-0 ml-2 mt-1">   
             <v-checkbox
             class="ma-0 pa-0 "
                v-model="ex4"
                label=""
                color="red"
                value="red"
                hide-details
              ></v-checkbox>
            </span>  
        </v-container>

         <v-container fluid class="d-flex mb-0 pb-0">
            <h3 class="pl-3">Bassboosted:</h3>
             
                        <span  @click="but2 = !but2"><v-switch  v-model="switch2" :label="``" class="ma-0 ml-3 pa-0" >
                          </v-switch></span><span>{{but2 ? 'on' : 'off'}}</span>

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
            <v-switch v-model="switch3" :label="``" class="d-flex ma-0 ml-3 pa-0"  color="red"></v-switch>
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
        but:false,
        but2:false, 
        switch1: false,
        switch2: false,
        switch3: false,
        items: ['Джон Сина', 'Шрек musik', 'Димон', 'Человеческая'],
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
