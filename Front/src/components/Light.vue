<template>
  <v-card class="mx-auto my-10" max-width="400">
    <v-img
      src="https://img1.akspic.ru/image/87835-bashnya-noch-neboskreb-stolica-muzykant-1280x800.jpg"
      height="200px"
    ></v-img>

    <v-card-title>ВЫ: Освещение</v-card-title>

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
        <h3 class="pl-3">Уровень яркости:</h3>

        <v-slider
          :disabled="!currentSupply"
          v-model="lightLevel"
          :thumb-size="27"
          thumb-label="always"
          class="ma-0"
          color="pink darken-1"
        ></v-slider>
      </v-container>

      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Уровень красного:</h3>

        <v-slider
          :disabled="!currentSupply"
          v-model="redLevel"
          :thumb-size="27"
          thumb-label="always"
          class="ma-0"
          color="red"
        ></v-slider>
      </v-container>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Уровень зеленого:</h3>

        <v-slider
          :disabled="!currentSupply"
          v-model="greenLevel"
          :thumb-size="27"
          thumb-label="always"
          class="ma-0"
          color="green"
        ></v-slider>
      </v-container>
      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Уровень голубого:</h3>

        <v-slider
          :disabled="!currentSupply"
          v-model="blueLevel"
          :thumb-size="27"
          thumb-label="always"
          class="ma-0"
        ></v-slider>
      </v-container>

      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Лампа на горе:</h3>
        <span>
          <v-switch
            :disabled="!currentSupply"
            v-model="projector"
            :label="``"
            class="ma-0 ml-3 pa-0"
          ></v-switch>
        </span>
        <span>{{projector ? 'on' : 'off'}}</span>
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
                <strong>Суммак к оплате:</strong> 4565₽
              </span>
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
  data() {
    return {
      power: 0,
      lightLevel: 0, //общий уровень освещения (щт 0 до 100%)
      redLevel: 0, //уровень красного цвета (возвращает от 0 до 100)
      greenLevel: 0, //уровень зеленого цвета (возвращает от 0 до 100)
      blueLevel: 0, //уровень голубого цвета (возвращает от 0 до 100)
      currentSupply: false, // on/off кнопки включения   (true/false)
      projector: false, // on/off кнопки ласпа на горе   (true/false)
      tariff: false, //значение слайдера акум/солнце  (true/false)

      pays: [
        {
          name: "1:45:67",
          calories: 157
        },
        {
          name: "1:48:67",
          calories: 237
        },
        {
          name: "1:55:67",
          calories: 518
        }
      ]
    };
  },
  created() {
   this.$socket.addMessageHandler(this.messageHandle);

    const light = this.$store.getters.LIGHT;
    if (light) {
      this.currentSupply = light.currentSupply;
      this.tariff = light.tariff;
      this.lightLevel = light.lightLevel;
      this.redLevel = light.redLevel;
      this.greenLevel = light.greenLevel;
      this.blueLevel = light.blueLevel;
      this.projector = light.projector;
     
      
    }
  },
  destroyed() {
    this.$socket.removeMessageHandler(this.messageHandle);
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
    currentSupply: function() {
      this.sendData();
    },
    projector: function() {
      this.sendData();
    },
    tariff: function() {
      this.sendData();
    }
  },
  methods: {
    messageHandle(message) {
      console.log("обработано в Light " + message);
    },
    sendData() {
      let payload = {
        type: 'Light',
        lightLevel: this.lightLevel, //общий уровень освещения (щт 0 до 100%)
        redLevel: this.redLevel, //уровень красного цвета (возвращает от 0 до 100)
        greenLevel: this.greenLevel, //уровень зеленого цвета (возвращает от 0 до 100)
        blueLevel: this.blueLevel, //уровень голубого цвета (возвращает от 0 до 100)
        currentSupply: this.currentSupply, // значение слайдера on/off (true/false)
        projector: this.projector, // значение слайдера лампа на горе   (true/false)
        tariff: this.tariff //значение слайдера акум/солнце  (true/false)
      };

      this.$socket.send(JSON.stringify(payload));
      this.$store.commit("SET_LIGHT", payload);
    }
  }
};
</script>
