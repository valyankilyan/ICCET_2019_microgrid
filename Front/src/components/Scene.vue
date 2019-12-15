<template>
  <v-card class="mx-auto my-10" max-width="400">
    <v-img
      src="https://cdn.pixabay.com/photo/2015/04/23/17/18/disney-736374__480.jpg"
      height="200px"
    ></v-img>

    <v-card-title>ВЫ: Сцена</v-card-title>

    <section>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Подача тока:</h3>
        <span>
          <v-switch v-model="currentSupply" :label="``" class="ma-0 ml-3 pa-0"></v-switch>
        </span>
        <span>{{currentSupply ? 'on' : 'off'}}</span>
        <span class="pl-4">Мощность {{power}} Вт</span>
      </v-container>

      <v-col class="d-flex ma-0 pa-0 algin-center" cols="12" sm="8">
        <h3 class="pl-6">Трек:</h3>
        <v-select
          :disabled="!currentSupply"
          item-value="valueS"
          item-text="name"
          :items="SCitems"
          v-model="track"
          label="Выберите музыку"
          class="ma-0 pa-0 ml-3"
        ></v-select>
      </v-col>

      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Повтор трека:</h3>

        <span class="ma-0 pa-0 ml-2 mt-1">
          <v-checkbox
            class="ma-0 pa-0"
            :disabled="!currentSupply"
            v-model="retryTrack"
            label
            color="red"
            value="true"
            hide-details
          ></v-checkbox>
        </span>
      </v-container>

      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Bassboosted:</h3>

        <span>
          <v-switch
            :disabled="!currentSupply"
            v-model="bassboosted"
            :label="``"
            class="ma-0 ml-3 pa-0"
          ></v-switch>
        </span>
        <span>{{bassboosted ? 'on' : 'off'}}</span>
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
      retryTrack: false, //кнопка повтора трека  врзвращает =>(true)
      track: 1, //какой трек сейчас играет   (цифра от 1 до 6)
      currentSupply: false, //on/off кнопки включения   (true/false)
      bassboosted: false, //значение слайдера бастбуст   (true/false)
      tariff: false, //значение слайдера акум/солнце  (true/false)
      SCitems: [
        { name: "Шрек music", valueS: 1 },
        { name: "Атвинта", valueS: 2 },
        { name: "Soccer physics", valueS: 3 },
        { name: "Димон", valueS: 4 },
        { name: "Джон Сина", valueS: 5 },
        { name: "SILENCE", valueS: 6 }
      ],
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

    const scene = this.$store.getters.SCENE;
    if (scene) {
      this.currentSupply = scene.currentSupply;
      this.tariff = scene.tariff;
      this.retryTrack = scene.retryTrack;
      this.bassboosted = scene.bassboosted;
      this.tariff = scene.tariff;
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
    retryTrack: function() {
      this.sendData();
    },
    track: function() {
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
    bassboosted: function() {
      this.sendData();
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
      console.log("обработано в Scene " + message);
    },
    sendData() {
      console.log(this.track);

      let payload = {
        type: "Scene",
        retryTrack: this.retryTrack, //кнопка повтора трека  врзвращает =>(true)
        track: this.track, //какой трек сейчас играет   (цифра от 1 до 6)
        currentSupply: this.currentSupply, // значение слайдера on/off (true/false)
        bassboosted: this.bassboosted, //значение слайдера бастбуст   (true/false)
        tariff: this.tariff //значение слайдера акум/солнце  (true/false)
      };

      this.$socket.send(JSON.stringify(payload));
      this.$store.commit("SET_SCENE", payload);
    }
  }
};
</script>
