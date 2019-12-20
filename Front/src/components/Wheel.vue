<template>
  <v-card class="mx-auto my-10" max-width="400">
    <v-img src="https://nikatv.ru/public/upload/news/26565/images/3138.jpg" height="200px"></v-img>

    <v-card-title>ВЫ: Колесо обозрения</v-card-title>

    <section>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Подача тока</h3>
        <span>
          <v-switch v-model="currentSupply" :label="``" class="ma-0 ml-3 pa-0"></v-switch>
        </span>
        <span>{{currentSupply ? 'on' : 'off'}}</span>
        <span class="pl-4" >Мощность {{sum }} Втc</span>
      </v-container>
    </section>

    <section>
      <v-expansion-panels multiple>
        <v-expansion-panel>
          <v-expansion-panel-header>Ваш тариф</v-expansion-panel-header>
          <v-expansion-panel-content>
            <v-col class="d-flex ma-0 pa-0 algin-center" cols="12" sm="8">
              <h3 class="pl-6">Тариф:</h3>
              <v-select
                 :disabled="!currentSupply"
                :items="items"
                item-value="value"
                item-text="name"
                v-model="selectTariff"
                label=" Выбрать"
                class="ma-0 pa-0 ml-3"
              ></v-select>
            </v-col>
            <section>
              <v-container fluid class="d-flex mb-0 pb-0">
                <h3 class="pl-3">Подача тока</h3>
                <span>
                  <v-switch v-model="akbTariff" :label="``" class="ma-0 ml-3 pa-0"></v-switch>
                </span>
                <span>{{akbTariff ? 'on' : 'off'}}</span>
               
              </v-container>
            </section>
           <!-- <section class="d-flex mb-0 pb-0">
              <span>
                Аккумулятор
                <br />7₽/кВт
              </span>
              <v-switch v-model="selectTariff" :label="``" class="d-flex ma-0 ml-3 pa-0"></v-switch>
              <span>
                Водородные батарейки
                <br />5₽/кВт
              </span>
            </section>-->
          </v-expansion-panel-content>
        </v-expansion-panel>

        <v-expansion-panel>
          <v-expansion-panel-header>Счет на оплату</v-expansion-panel-header>
          <v-expansion-panel-content>
            <section class="d-fle mb-0 pb-0">
              <p>
                <strong>Вы работаете на акб:</strong>
                {{this.akbTimer}} сек
              </p>
              <p>
                <strong>Вы работаете на водороде:</strong>
                {{this.hydrogenTimer}} сек
              </p>
               <p>
                <strong>Вы работаете на HEAVY водороде:</strong>
                {{this.hydro2Timer}} сек
              </p>
              <span>
                <strong>Сумма к оплате:</strong>
                {{total}}₽
              </span>
              <v-btn color="cyan lighten-1 pl-5" text @click="pay">Оплатить</v-btn>
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
                    <th class="text-left">Сумма,₽</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="pay in pays" :key="pay.id">
                    <td>{{ pay.workTime }}</td>
                    <td>{{ pay.sum }}</td>
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
import Timer from "@/plugins/timer.js";
import Pay from "@/plugins/pay.js";

export default {
  data() {
    return {
      total:0,
       sum:0,
      obj:0,
      akbTimer: new Timer(),
      hydrogenTimer: new Timer(),
      hydro2Timer: new Timer(),
      power: 0,
      currentSupply: false, // значение слайдера on/off (true/false)
      selectTariff: 1,
      items: [
        { name: 'АКБ 5₽/Втс ', value: 1 },
        { name: 'Водородные батарейки 7₽/Втс', value: 2 },
        { name: 'HEAVY Водородные батарейки 8₽/Втс', value: 3 },
      
      ], //значение слайдера акум/солнце  (true/false)
      pays: [
        {
          id: 1,
          workTime: "1:45:67",
          sum: 100
        },
        {
          id: 2,
          workTime: "1:45:67",
          sum: 100
        },
        {
          id: 3,
          workTime: "1:45:67",
          sum: 100
        }
      ]
    };
  },
  created() {
    this.$socket.addMessageHandler(this.messageHandle);

    const wheel = this.$store.getters.WHEEL;
    if (wheel) {
      this.currentSupply = wheel.currentSupply;
      this.selectTariff = wheel.selectTariff;
    }
  },
  destroyed() {
    this.$socket.removeMessageHandler(this.messageHandle);
  },
  computed: {
    totalSum() {
      const akbSeconds = this.akbTimer.seconds;
      const hydrogenSeconds = this.hydrogenTimer.seconds;
      const hydro2Seconds = this.hydro2Timer.seconds;

      const pay = new Pay(akbSeconds, hydrogenSeconds, hydro2Seconds);

      return pay.sum;
    }
  },
  watch: {
    currentSupply: function() {
      this.sendData();
      this.fun();
    

      if (this.currentSupply) {
        if (this.selectTariff == 1) {
          this.akbTimer.start();
        } else {
            if (this.selectTariff == 2) {
            this.hydrogenTimer.start();
            }  else {
               if (this.selectTariff == 3) {
            this.hydro2Timer.start();
            }
          }

        
        }
        
      } else {
        this.hydrogenTimer.stop();
        this.hydro2Timer.stop();
        this.akbTimer.stop();
      }
    },
    selectTariff: function() {
      this.sendData();
      this.selectTariff = this.selectTariff;
     // this.currentSupply = false;

      if (this.selectTariff == 1) {
        
        this.akbTimer.start();
        this.hydrogenTimer.stop();
         this.hydro2Timer.stop();
      } else {
          
          if (this.selectTariff == 2) {
            
            this.akbTimer.stop();
            this.hydrogenTimer.start();
            this.hydro2Timer.stop();
          } else {
            if (this.selectTariff == 3) {
        
        this.akbTimer.stop();
        this.hydrogenTimer.stop();
         this.hydro2Timer.start();
      } 
          }
      }
    }
  },
  methods: {
     fun(){
  console.log('timed out function');
   setTimeout(this.func, 2500);
  },
    func(){
      let payload = {
        type: "wheel",
        ask: 1
        
     
      };
        console.log('timevsegerghergion');
      this.$socket.send(JSON.stringify(payload));

      this.$store.commit("SET_WHEEL", payload);
      if(this.currentSupply){
     setTimeout(this.fun, 2500);
      }
  },
   

    pay() {
      const akbSeconds = this.akbTimer.seconds;
      const hydrogenSeconds = this.hydrogenTimer.seconds;

      const pay = new Pay(akbSeconds, hydrogenSeconds);

      this.pays.unshift(pay);

      this.akbTimer.clear();
      this.hydrogenTimer.clear();
    },
    messageHandle(message) {
      console.log("обработано в Wheel " + message);
      //  this.obj = JSON.parse(message)
        this.obj = Number(message);
       this.sum = this.sum + this.obj;
      
        
        
        if (this.selectTariff == 1) {
        this.total = this.total + this.obj*5; 
       
      } else {
          
          if (this.selectTariff == 2) {
            this.total = this.total + this.obj*7; 
          } else {
            if (this.selectTariff == 3) {
        this.total = this.total + this.obj*8; 
      } 
          }
      }
    },
    sendData() {
      let payload = {
        type: "Wheel",
        currentSupply: this.currentSupply, // значение слайдера on/off (true/false)
        selectTariff: this.selectTariff //значение слайдера акум/солнце  (true/false)
      };

      this.$socket.send(JSON.stringify(payload));

      this.$store.commit("SET_WHEEL", payload);
    }
  }
};
</script>