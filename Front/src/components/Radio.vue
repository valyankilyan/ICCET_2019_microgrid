<template>
  <v-card class="mx-auto my-10" max-width="400">
    <v-img
      src="https://craftboro.ru/wp-content/uploads/2019/07/16546/x5BYcUQtQfo.jpg"
      height="200px"
    ></v-img>

    <v-card-title>ВЫ: Радиостанция</v-card-title>

    <section>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Подача тока</h3>
        <span>
          <v-switch v-model="currentSupply" :label="``" class="ma-0 ml-3 pa-0"></v-switch>
        </span>
        <span>{{currentSupply ? 'on' : 'off'}}</span>
        <span class="pl-4">Мощность{{power}} Вт</span>
      </v-container>

      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Громкость:</h3>

        <v-slider
          :disabled="!currentSupply"
          v-model="volume"
          :thumb-size="27"
          thumb-label="always"
          class="ma-0"
        ></v-slider>
      </v-container>
    </section>

    <section>
      <v-expansion-panels multiple>
        <v-expansion-panel>
          <v-expansion-panel-header>Ваш тариф</v-expansion-panel-header>
          <v-expansion-panel-content>
            <section class="d-flex mb-0 pb-0">
              <span>
                Солненая Панель
                <br />3₽/кВт
              </span>
              <v-switch v-model="tariff" :label="``" class="d-flex ma-0 ml-3 pa-0"></v-switch>
              <span>
                Аккумулятор
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
                <strong>Вы работаете:</strong> 15:23:43 сек
              </p>
              <span>
                <strong>Сумма к оплате:</strong> 4565₽
              </span>
              <v-btn color="cyan lighten-1 pl-5" text>Оплатить</v-btn>
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
  data() {
    return {
      power: 0,
      volume: 0, //уровень громкости (возвращает от 0 до 100)
      currentSupply: false, // значение слайдера on/off (true/false)
      tariff: false, //значение слайдера акум/солнце  (true/false)
      pays: [
        {
          name: "1:45:67",
          calories: 157
        },
        {
          name: "1:56:67",
          calories: 237
        },
        {
          name: "1:32:67",
          calories: 518
        }
      ]
    };
  },
  created() {
    this.$socket.addMessageHandler(this.messageHandle);

    const radio = this.$store.getters.RADIO;
    if (radio) {
      this.currentSupply = radio.currentSupply;
      this.tariff = radio.tariff;
      this.volume = radio.volume;

    }
  },
  destroyed() {
    this.$socket.removeMessageHandler(this.messageHandle);
  },
  watch: {
    volume: function() {
      this.sendData();
    },
    currentSupply: function() {
      this.sendData();
    },
    tariff: function() {
      this.sendData();
    }
  },
  methods: {
    messageHandle(message) {
      console.log("обработано в Radio " + message);
    },
    sendData() {
      console.log(this.SCmusic);

      let payload = {
        type: 'Radio',
        volume: this.volume, //кнопка повтора трека  врзвращает =>(true)
        currentSupply: this.currentSupply, // значение слайдера on/off (true/false)
        tariff: this.tariff //значение слайдера акум/солнце  (true/false)
      };

      this.$socket.send(JSON.stringify(payload));
      this.$store.commit("SET_RADIO", payload);
    }
  }
};
</script>
