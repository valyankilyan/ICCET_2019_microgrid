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
        <span @click="but = !but">
          <v-switch v-model="RAswitch1" :label="``" class="ma-0 ml-3 pa-0"></v-switch>
        </span>
        <span>{{but ? 'on' : 'off'}}</span>
          <span class="pl-4">Мощность{{}} Вт</span>
      </v-container>

      <v-container fluid class="d-flex mb-0 pb-0">
        <h3 class="pl-3">Громкость:</h3>

        <v-slider :disabled="!but" v-model="RAsliderMax" :thumb-size="27" thumb-label="always" class="ma-0"></v-slider>
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
              <v-switch v-model="RAswitch2" :label="``" class="d-flex ma-0 ml-3 pa-0"></v-switch>
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
      RAsliderMax: 0, //уровень громкости (возвращает от 0 до 100)
      but: false, // on/off кнопки включения   (true/false)
      RAswitch1: false, // значение слайдера on/off (true/false)
      RAswitch2: false, //значение слайдера акум/солнце  (true/false)
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
    
  
  //this.$socket.send('Встречаются два новых русских, один у другого интересуется: - Слышь, Вован, а вот ты стометровку за сколько пробежишь? - Ну дык, Колян, за штуку баксов, ...');
  },
  destroyed() {
    this.$socket.removeMessageHandler(this.messageHandle);
  },
  watch: {
    RAsliderMax: function() {
      this.sendData();
    },
    RAswitch1: function() {
      this.sendData();
    },
    RAswitch2: function() {
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
        RAsliderMax: this.RAsliderMax,  //кнопка повтора трека  врзвращает =>(true)
        RAswitch1: this.RAswitch1,  // значение слайдера on/off (true/false)
        RAswitch2: this.RAswitch2  //значение слайдера акум/солнце  (true/false)
      };

      this.$socket.send(JSON.stringify(payload));
    }
  }
};
</script>
