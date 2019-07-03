<template>
  <v-expansion-panel>
    <v-expansion-panel-content>
      <template v-slot:header>
        <div>Cantrips</div>
      </template>
      <v-card>
        <v-card-text>{{ msg }}</v-card-text>
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
import axios from 'axios';

// @ is an alias to /src

export default {
  name: 'home',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:5000/ping';
      axios.get(path)
        .then((response) => {
          this.msg = response.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>
