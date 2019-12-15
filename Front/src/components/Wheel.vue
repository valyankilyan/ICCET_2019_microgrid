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
        <span class="pl-4">Мощность {{ power }} Вт</span>
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
                <strong>Сумма к оплате:</strong>
                {{totalSum}}₽
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
      akbTimer: new Timer(),
      hydrogenTimer: new Timer(),
      power: 0,
      currentSupply: false, // значение слайдера on/off (true/false)
      tariff: false, //значение слайдера акум/солнце  (true/false)
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
      this.tariff = wheel.tariff;
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
      console.log("обработано в Wheel " + message);
    },
    sendData() {
      let payload = {
        type: "Wheel",
        currentSupply: this.currentSupply, // значение слайдера on/off (true/false)
        tariff: this.tariff //значение слайдера акум/солнце  (true/false)
      };

      this.$socket.send(JSON.stringify(payload));

      this.$store.commit("SET_WHEEL", payload);
    }
  }
};
</script>
