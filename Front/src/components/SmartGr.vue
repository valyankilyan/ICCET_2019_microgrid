<template>
  <v-card class="mx-auto my-10" max-width="400">
    <v-img
      src="https://www.light-group.com.ua/userfiles/image/objects_gallery/photoimg_1445771990.jpg"
      height="200px"
    ></v-img>

    <v-card-title>ВЫ: Умная грядка</v-card-title>
    <section>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Подача тока</h3>
        <span>
          <v-switch v-model="currentSupply" :label="``" class="ma-0 ml-3 pa-0"></v-switch>
        </span>
        <span>{{currentSupply ? 'on' : 'off'}}</span>
        <span class="pl-4">Мощность {{power}} Вт</span>
      </v-container>

      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Температура в &#8451;:</h3>

        <v-slider
          :disabled="!currentSupply"
          v-model="temperature"
          thumb-label
          max="40"
          min="20"
          class="ma-0"
        ></v-slider>
      </v-container>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">
          Текущая температура:
          <span>{{currentTemperature}} &#8451;</span>
        </h3>
      </v-container>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Уровень яркости:</h3>

        <v-slider
          :disabled="!currentSupply"
          v-model="lightLevel"
          thumb-label
          class="ma-0"
          color="pink darken-1"
        ></v-slider>
      </v-container>

      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Уровень красного:</h3>

        <v-slider
          :disabled="!currentSupply"
          v-model="redLevel"
          thumb-label
          class="ma-0"
          color="red"
        ></v-slider>
      </v-container>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Уровень зеленого:</h3>

        <v-slider
          :disabled="!currentSupply"
          v-model="greenLevel"
          thumb-label
          class="ma-0"
          color="green"
        ></v-slider>
      </v-container>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Уровень голубого:</h3>

        <v-slider :disabled="!currentSupply" v-model="blueLevel" thumb-label class="ma-0"></v-slider>
      </v-container>
    </section>

    <section>
      <v-expansion-panels multiple>
        <v-expansion-panel>
          <v-expansion-panel-header>Ваш тариф</v-expansion-panel-header>
          <v-expansion-panel-content>
            <section class="d-flex mb-0 pb-0">
              <span>
                Аккумулятор
                <br />7₽/кВт
              </span>
              <v-switch v-model="tariff" :label="``" class="d-flex ma-0 ml-3 pa-0"></v-switch>
              <span>
                Водородные батарейки
                <br />5₽/кВт
              </span>
            </section>
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
              <span>
                <strong>Суммак к оплате:</strong>{{totalSum}}₽
              </span>
              <v-btn color="cyan lighten-1 pl-5" text @click="pay">оплатить</v-btn>
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
      akbTimer: new Timer(),
      hydrogenTimer: new Timer(),
      power: 0,
      lightLevel: "", //общий уровень освещения (щт 0 до 100%)
      redLevel: "", //уровень красного цвета (возвращает от 0 до 100)
      greenLevel: "", //уровень зеленого цвета (возвращает от 0 до 100)
      blueLevel: "", //уровень голубого цвета (возвращает от 0 до 100)
      temperature: "", // значение температуры (от 20 до 40)
      currentTemperature: 23, // значение текущей температуры в теплице
      currentSupply: false, // значение слайдера on/off (true/false)
      tariff: false, //значение слайдера акум/солнце  (true/false)

     pays: [
        {
          id: 1,
          workTime: "0:10:57",
          sum: 1678
        },
        {
          id: 2,
          workTime: "0:45:26",
          sum: 1200
        },
        {
          id: 3,
          workTime: "1:24:50",
          sum: 12296
        }
      ]
    };
  },
  created() {
    this.$socket.addMessageHandler(this.messageHandle);

    const smartGr = this.$store.getters.SMARTGR;
    if (smartGr) {
      this.currentSupply = smartGr.currentSupply;
      this.tariff = smartGr.tariff;
      this.lightLevel = smartGr.lightLevel;
      this.redLevel = smartGr.redLevel;
      this.greenLevel = smartGr.greenLevel;
      this.blueLevel = smartGr.blueLevel;
      this.temperature = smartGr.temperature;
     
    }
  },
  destroyed() {
    this.$socket.removeMessageHandler(this.messageHandle);
  },
  computed: {
    totalSum() {
      const akbSeconds = this.akbTimer.seconds;
      const hydrogenSeconds = this.hydrogenTimer.seconds;

      const pay = new Pay(akbSeconds, hydrogenSeconds);

      return pay.sum;
    }
  },
  watch: {
    lightLevel: function() {
      this.sendData();
    },
    redLevel: function() {
      this.sendData();
    },
    greenLevel: function() {
      this.sendData();
    },
    blueLevel: function() {
      this.sendData();
    },
    temperature: function() {
      this.sendData();
    },
    currentSupply: function() {
      this.sendData();

      if (this.currentSupply) {
        if (this.tariff) {
          this.hydrogenTimer.start();
        } else {
          this.akbTimer.start();
        }
      } else {
        this.hydrogenTimer.stop();
        this.akbTimer.stop();
      }
    },
     tariff: function() {
      this.sendData();
      if (this.tariff) {
        this.hydrogenTimer.start();
        this.akbTimer.stop();
      } else {
        this.akbTimer.start();
         this.hydrogenTimer.stop();
      }
    }
  },
  methods: {
    pay() {
      const akbSeconds = this.akbTimer.seconds;
      const hydrogenSeconds = this.hydrogenTimer.seconds;

      const pay = new Pay(akbSeconds, hydrogenSeconds);

      this.pays.unshift(pay);

      this.akbTimer.clear();
      this.hydrogenTimer.clear();
    },
    messageHandle(message) {
      console.log("обработано в SmartGr " + message);
    },
    sendData() {
      let payload = {
        type: "SmartGR",
        lightLevel: this.lightLevel, //общий уровень освещения (щт 0 до 100%)
        redLevel: this.redLevel, //уровень красного цвета (возвращает от 0 до 100)
        greenLevel: this.greenLevel, //уровень зеленого цвета (возвращает от 0 до 100)
        blueLevel: this.blueLevel, //уровень голубого цвета (возвращает от 0 до 100)
        temperature: this.temperature, // значение температуры (от 20 до 40)
        currentSupply: this.currentSupply, // значение слайдера on/off (true/false)
        tariff: this.tariff
      };

      this.$socket.send(JSON.stringify(payload));
       this.$store.commit("SET_SMARTGR", payload);
    }
  }
};
</script>
